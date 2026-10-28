#!/usr/bin/env python3
"""Refresh GitHub stars / last_commit / archived for awesome-hackbots and regenerate README.md.

Usage:
  python3 scripts/update_stats.py              # fetch + rate + write README
  python3 scripts/update_stats.py --offline     # rate + README only (no API)
  python3 scripts/update_stats.py --fetch-only  # update projects.json stats only

Requires network for --fetch (default). Uses unauthenticated GitHub REST API
(60 req/hr) or GITHUB_TOKEN / GH_TOKEN for higher limits.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "projects.json"
README = ROOT / "README.md"
GH_PAT = re.compile(r"^https?://github\.com/([^/]+)/([^/#?]+)", re.I)

# Prestige boosts keyed by lowercase URL substring
BOOSTS = {
    "usestrix/strix": 1.0,
    "greydgl/pentestgpt": 1.2,
    "vxcontrol/pentagi": 0.8,
    "keygraphhq/shannon": 0.8,
    "aliasrobotics/cai": 0.4,
    "trailofbits/buttercup": 1.2,
    "team-atlanta/aixcc-afc-atlantis": 1.5,
    "theori-io/aixcc-afc-archive": 1.0,
    "fuzzingbrain/afc-crs-all-you-need-is-a-fuzzing-brain": 0.8,
    "shellphish/artiphishell": 0.7,
    "andyzorigin/cybench": 1.0,
    "uiuc-kang-lab/cve-bench": 1.0,
    "bountybench/bountybench": 0.8,
    "google/oss-fuzz-gen": 1.0,
    "google/mantis": 1.0,
    "protectai/vulnhuntr": 0.8,
    "ipa-lab/hackingbuddygpt": 0.8,
    "swe-agent/swe-agent": 1.0,
    "chataflndss/chatafl": 0.8,
    "projectzero.google": 1.5,
    "xbow.com": 1.5,
    "josephthacker.com": 1.0,
    "aicyberchallenge.com": 1.5,
    "arxiv.org/abs/2308.02167": 1.2,
    "arxiv.org/abs/2402.06664": 1.0,
    "arxiv.org/abs/2409.16165": 1.0,
    "arxiv.org/abs/2408.08926": 1.0,
    "arxiv.org/abs/2503.17332": 1.0,
    "arxiv.org/abs/2505.14534": 0.8,
    "arxiv.org/abs/2602.07666": 1.0,
    "portswigger/mcp-server": 0.8,
    "0x4m4/hexstrike-ai": 0.8,
    "mrexodia/ida-pro-mcp": 0.6,
    "lauriewired/ghidramcp": 0.6,
    "horizon3.ai": 0.8,
    "pentera.io": 0.6,
    "darpa.mil/news/2025/aixcc-results": 1.0,
    # 2026-10-27 verified additions (modest; same 0.4–1.5 rubric)
    "nyu-llm-ctf/nyuctf_agents": 0.8,
    "palisaderesearch/intercode": 0.6,
    "palisaderesearch/ai-vs-humans-ctf-report": 1.0,
    "ctf.secure-agent.com": 0.5,
    "neurogrid-ctf": 0.5,
    "kaist-hacking/ctfusion": 0.5,
    # 2026-10-28 verified additions (modest; same 0.4–1.5 rubric).
    # nyuctf_agents_craken is longer than nyuctf_agents so the specific key wins.
    "nyu-llm-ctf/nyuctf_agents_craken": 0.6,
    "aivillage.org/blog/halctf": 0.5,
    "cloud.tencent.com/developer/article/2661083": 0.5,
    "sean.heelan.io": 0.8,
    "seanheelan/anamnesis-release": 0.6,
}

# Above this, a star total is not credible adoption for this list (REA: ~393k
# on a repo created 2026-04-14). Those counts score 0, display as n/a, and
# cannot place an entry on the leaderboard. The 50k cap still applies below it.
ANOMALOUS_STARS = 100_000

CATEGORY_ORDER = [
    "Autonomous Pentest Agents",
    "Commercial Hackbots",
    "Frameworks, Skills & Harnesses",
    "Code Auditing & SAST Agents",
    "LLM Fuzzing & Cyber Reasoning Systems",
    "Security MCP Servers",
    "Reverse Engineering Agents",
    "CTF Solvers & Agents",
    "Bug Bounty & Recon",
    "Benchmarks & Datasets",
    "Research Papers",
    "Talks, Blogs & Writing",
    "Competitions",
    "People & Communities",
    "Related Awesome Lists",
]

LEADERBOARD_CATEGORIES = {
    "Autonomous Pentest Agents",
    "LLM Fuzzing & Cyber Reasoning Systems",
    "Code Auditing & SAST Agents",
    "CTF Solvers & Agents",
}

TYPE_LEGEND = {
    "open-source": "🟢 open-source",
    "commercial": "🟠 commercial",
    "event": "🟣 event / community",
    "paper": "🔵 paper / writing",
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def gh_headers() -> dict:
    h = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-hackbots-update-stats",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def fetch_repo(owner: str, repo: str) -> dict:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url, headers=gh_headers())
    with urllib.request.urlopen(req, timeout=30) as r:
        item = json.load(r)
    return {
        "stars": item["stargazers_count"],
        "last_commit": item["pushed_at"],
        "archived": bool(item["archived"]),
        "html_url": item["html_url"],
        "found": True,
    }


def stars_anomalous(stars: int | None) -> bool:
    return bool(stars and int(stars) > ANOMALOUS_STARS)


def star_component(stars: int | None) -> float:
    if not stars or stars <= 0 or stars_anomalous(stars):
        return 0.0
    # Cap dampens ordinary star-farming below the anomalous cutoff
    s = min(int(stars), 50_000)
    # log10(1)=0 … log10(50001)≈4.7 → map to 0…2.0
    return min(2.0, math.log10(s + 1) / math.log10(50_001) * 2.0)


def maint_component(last_commit: str | None, archived: bool, now: datetime) -> float:
    if archived:
        return 0.0
    if not last_commit:
        return 0.4
    dt = datetime.fromisoformat(last_commit.replace("Z", "+00:00"))
    days = (now - dt).days
    if days <= 30:
        return 1.5
    if days <= 90:
        return 1.2
    if days <= 180:
        return 0.8
    if days <= 365:
        return 0.4
    return 0.1


def boost_for(url: str) -> float:
    """Longest matching key wins so a repo name that extends another keeps its own boost.

    Example: nyuctf_agents (0.8) is a substring of nyuctf_agents_craken (0.6).
    Equal-length ties still take the higher value.
    """
    u = url.lower()
    best_len = -1
    best = 0.0
    for k, v in BOOSTS.items():
        if k not in u:
            continue
        if len(k) > best_len or (len(k) == best_len and v > best):
            best_len = len(k)
            best = v
    return best


def compute_rating(p: dict, now: datetime) -> float:
    typ = p.get("type", "open-source")
    # event shares the commercial base. Without this, competitions would
    # fall through to the open-source formula and collapse to ~1.0.
    if typ in ("commercial", "event"):
        return round(min(5.0, max(1.0, 3.2 + boost_for(p["url"]))), 1)
    if typ == "paper":
        return round(min(5.0, max(1.0, 3.0 + boost_for(p["url"]))), 1)
    # open-source
    sc = star_component(p.get("stars"))
    mc = maint_component(p.get("last_commit"), p.get("archived", False), now)
    bc = boost_for(p["url"])
    total = 0.5 + sc + mc + bc
    if p.get("archived"):
        total = min(total, 2.5)
    return round(min(5.0, max(1.0, total)), 1)


def stars_badge(p: dict) -> str:
    m = GH_PAT.match(p["url"])
    if not m:
        return "—"
    owner, repo = m.group(1), m.group(2)
    return f"![stars](https://img.shields.io/github/stars/{owner}/{repo}?style=flat-square)"


def fmt_stars(n: int | None) -> str:
    if n is None:
        return "—"
    if stars_anomalous(n):
        return "n/a"
    if n >= 1000:
        return f"{n/1000:.1f}k".replace(".0k", "k")
    return str(n)


def fmt_date(iso: str | None) -> str:
    if not iso:
        return "—"
    return iso[:10]


def rating_stars(r: float) -> str:
    full = int(r)
    half = 1 if (r - full) >= 0.5 else 0
    return "★" * full + ("½" if half else "") + "☆" * (5 - full - half)


def load() -> dict:
    return json.loads(DATA.read_text())


def save(doc: dict) -> None:
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(doc, indent=2) + "\n")


def refresh_github(doc: dict, sleep_s: float = 0.85) -> tuple[int, int]:
    now = now_utc()
    ok = fail = 0
    projects = doc["projects"]
    for i, p in enumerate(projects):
        m = GH_PAT.match(p["url"])
        if not m:
            continue
        owner, repo = m.group(1), m.group(2)
        try:
            info = fetch_repo(owner, repo)
            p["stars"] = info["stars"]
            p["last_commit"] = info["last_commit"]
            p["archived"] = info["archived"]
            # keep canonical html url if redirected
            if info.get("html_url"):
                p["url"] = info["html_url"]
            ok += 1
            print(f"[{ok+fail}] {owner}/{repo}: ★{info['stars']} archived={info['archived']}")
        except urllib.error.HTTPError as e:
            fail += 1
            print(f"[{ok+fail}] {owner}/{repo}: HTTP {e.code}", file=sys.stderr)
            if e.code in (403, 429):
                print("Rate limited; sleeping 70s…", file=sys.stderr)
                time.sleep(70)
        except Exception as e:
            fail += 1
            print(f"[{ok+fail}] {owner}/{repo}: {e}", file=sys.stderr)
        time.sleep(sleep_s)
    doc.setdefault("meta", {})["generated_at"] = now.isoformat()
    doc["meta"]["last_fetch_ok"] = ok
    doc["meta"]["last_fetch_fail"] = fail
    return ok, fail


_OLD_ANOMALY_FLAGS = (
    "[star count looks anomalously high — rating uses capped stars]",
    "[star count looks anomalously high - rating uses capped stars]",
)


def _sort_key(p: dict) -> tuple:
    # Anomalous totals must not win ties the way a real star count would.
    stars = 0 if stars_anomalous(p.get("stars")) else (p.get("stars") or 0)
    return (-p["rating"], -stars, p["name"].lower())


def apply_ratings(doc: dict) -> None:
    now = now_utc()
    for p in doc["projects"]:
        p["rating"] = compute_rating(p, now)
        note = p.get("note") or ""
        for flag in _OLD_ANOMALY_FLAGS:
            note = note.replace(flag, "")
        note = re.sub(r"\s{2,}", " ", note).strip()
        if p.get("archived") and "[ARCHIVED]" not in note:
            note = f"{note} [ARCHIVED]".strip()
        if stars_anomalous(p.get("stars")) and "excluded from rating" not in note.lower():
            note = f"{note} Star count excluded from rating (looks anomalously high).".strip()
        p["note"] = note
    doc["projects"].sort(key=_sort_key)
    doc.setdefault("meta", {})["entry_count"] = len(doc["projects"])
    doc["meta"]["generated_at"] = now.isoformat()
    doc["meta"]["rating_rubric"] = {
        "scale": "1.0–5.0",
        "open_source": (
            "0.5 base + star_component(≤2.0 using log10 of min(stars,50000); "
            "stars above 100000 score 0 and display as n/a) "
            "+ maintenance(≤1.5) + prestige boost(≤1.5); archived capped at 2.5"
        ),
        "maintenance": "≤30d=1.5, ≤90d=1.2, ≤180d=0.8, ≤365d=0.4, older=0.1; archived=0",
        "commercial": "base 3.2 + prestige boost",
        "event": "base 3.2 + prestige boost (competitions and community events; same formula as commercial)",
        "paper": "base 3.0 + prestige boost",
        "prestige_examples": "AIxCC placements, USENIX/ICML/NDSS, Project Zero, XBOW, major benchmarks",
    }


def render_readme(doc: dict) -> str:
    projects = doc["projects"]
    meta = doc.get("meta", {})
    by_cat: dict[str, list] = defaultdict(list)
    for p in projects:
        by_cat[p["category"]].append(p)

    gen = meta.get("generated_at", now_utc().isoformat())
    gen_day = gen[:10]

    lines: list[str] = []
    lines += [
        "# Awesome Hackbots [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> A curated list of **hackbots** — AI agents and LLM-powered tools that autonomously or "
        "semi-autonomously perform offensive security: pentesting, bug bounty, recon, vulnerability "
        "discovery, exploitation, CTF solving, code auditing, LLM-guided fuzzing, and red-team operations — "
        "plus the surrounding ecosystem of benchmarks, MCP servers, papers, competitions, and writing.",
        "",
        "Curated by [Rafael Gacek](https://bersec.me)",
        "",
        f"[![entries](https://img.shields.io/badge/entries-{len(projects)}-blue?style=flat-square)](#contents) "
        "[![license](https://img.shields.io/badge/license-CC0-lightgrey?style=flat-square)](LICENSE) "
        "[![maintainer](https://img.shields.io/badge/maintainer-BerSec-red?style=flat-square)](https://github.com/BerSecHub)",
        "",
        "## What is a hackbot?",
        "",
        "A **hackbot** is an automated system that uses AI (typically LLMs, often with tools, sandboxes, "
        "fuzzers, and traditional scanners) in a meaningful way to find and/or exploit vulnerabilities in "
        "real targets — bug-bounty programs, production apps, CTF challenges, or source code.",
        "",
        "This list prioritizes **verified, notable, actively maintained** projects. Every GitHub entry was "
        "checked via the GitHub API; dead/404 links are dropped. Star counts and ratings are refreshed by "
        "`scripts/update_stats.py` (data in `data/projects.json`).",
        "",
        "## Legend",
        "",
        "| Mark | Meaning |",
        "|------|---------|",
        "| 🟢 | Open-source project / tool |",
        "| 🟠 | Commercial product / company |",
        "| 🟣 | Competition, event or community |",
        "| 🔵 | Research paper, blog post, or long-form writing |",
        "| ⚠️ | Archived or unmaintained (still historically important) |",
        "| ★ rating | Transparent 1–5 score — see [Rating rubric](#rating-rubric) |",
        "",
        f"_Stats snapshot: **{gen_day}** (UTC). Re-run `python3 scripts/update_stats.py` to refresh._",
        "",
        "## Contents",
        "",
        "- [Top hackbots leaderboard](#top-hackbots-leaderboard)",
        "- [Rating rubric](#rating-rubric)",
    ]
    for cat in CATEGORY_ORDER:
        if cat in by_cat:
            anchor = re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")
            lines.append(f"- [{cat}](#{anchor}) ({len(by_cat[cat])})")
    lines += [
        "- [Contributing](#contributing)",
        "- [Disclaimer](#disclaimer)",
        "",
        "## Top hackbots leaderboard",
        "",
        "Highest-rated **open-source** agents and CRS/SAST systems (excludes pure lists, blogs, and commercial SaaS). "
        "Ratings combine stars (capped), maintenance recency, and prestige boosts — not stars alone.",
        "",
        "| # | Name | ★ Stars | Rating | Category |",
        "|--:|------|--------:|:------:|----------|",
    ]
    lb = [
        p
        for p in projects
        if p["type"] == "open-source"
        and p["category"] in LEADERBOARD_CATEGORIES
        and not p.get("archived")
        and not stars_anomalous(p.get("stars"))
    ][:15]
    for i, p in enumerate(lb, 1):
        lines.append(
            f"| {i} | [{p['name']}]({p['url']}) | {fmt_stars(p.get('stars'))} | "
            f"**{p['rating']}** {rating_stars(p['rating'])} | {p['category']} |"
        )

    lines += [
        "",
        "## Rating rubric",
        "",
        "Each entry gets a **1.0–5.0** rating stored in `data/projects.json`:",
        "",
        "| Signal | How it scores |",
        "|--------|---------------|",
        "| **Stars** (open-source) | `log10(min(stars, 50000))` scaled to **0–2.0**. Cap fights star inflation. Counts above 100k are anomalous: they score **0**, display as n/a, and cannot lead the leaderboard on stars. |",
        "| **Maintenance** | Last push ≤30d → 1.5; ≤90d → 1.2; ≤180d → 0.8; ≤365d → 0.4; older → 0.1. **Archived → 0** (and overall cap 2.5). |",
        "| **Prestige boost** | Manual +0.4–1.5 for AIxCC placements, USENIX/ICML/NDSS papers, Project Zero, XBOW, Cybench/CVE-Bench, etc. |",
        "| **Open-source base** | +0.5 |",
        "| **Commercial** | Base **3.2** + prestige (no GitHub stars required). |",
        "| **Event / community** | Same base as commercial (**3.2**) + prestige. Competitions and community sites use this so they are not scored like GitHub repos. |",
        "| **Paper / writing** | Base **3.0** + prestige. |",
        "",
        "Shields.io star badges in category tables always reflect **live** GitHub data; the numeric star column "
        "and rating come from the last `update_stats.py` run.",
        "",
    ]

    for cat in CATEGORY_ORDER:
        items = by_cat.get(cat)
        if not items:
            continue
        # sort: rating desc, stars desc, name
        items = sorted(items, key=_sort_key)
        lines += [f"## {cat}", ""]
        # short blurb per category
        blurbs = {
            "Autonomous Pentest Agents": "End-to-end or multi-agent systems that plan and execute offensive assessments with LLMs.",
            "Commercial Hackbots": "Vendors shipping autonomous or AI-assisted offensive testing / AppSec products.",
            "Frameworks, Skills & Harnesses": "Agent skills, harnesses, and scaffolding that turn coding agents into security operators.",
            "Code Auditing & SAST Agents": "LLM agents and neurosymbolic tools that hunt vulnerabilities in source code.",
            "LLM Fuzzing & Cyber Reasoning Systems": "LLM-guided fuzzers and DARPA AIxCC-style cyber reasoning systems (find + prove + patch).",
            "Security MCP Servers": "Model Context Protocol servers that expose offensive security tools to AI clients.",
            "Reverse Engineering Agents": "LLM assistants and MCP bridges for IDA, Ghidra, Binary Ninja, JADX, and friends.",
            "CTF Solvers & Agents": "Agents that autonomously solve CTF challenges and interactive exploit tasks.",
            "Bug Bounty & Recon": "AI-assisted recon, scanning, reporting, and bounty workflows.",
            "Benchmarks & Datasets": "Evaluation suites for measuring hackbot / cyber-agent capability.",
            "Research Papers": "Foundational and recent papers on autonomous hacking, CTF agents, and CRS.",
            "Talks, Blogs & Writing": "Essays, vendor write-ups, and research blogs that define the space.",
            "Competitions": "AI-for-offense competitions and challenge series.",
            "People & Communities": "Researchers, labs, and orgs shaping the hackbot ecosystem.",
            "Related Awesome Lists": "Sibling curated lists and closely related resources (we write our own descriptions).",
        }
        if cat in blurbs:
            lines += [blurbs[cat], ""]
        lines += [
            "| Name | Type | Stars | Last push | Rating | Description |",
            "|------|:----:|------:|:---------:|:------:|-------------|",
        ]
        for p in items:
            typ = TYPE_LEGEND.get(p["type"], p["type"])
            arch = " ⚠️" if p.get("archived") else ""
            if stars_anomalous(p.get("stars")):
                # Live Shields badge would republish the untrusted total.
                star_cell = "n/a"
            else:
                badge = stars_badge(p) if p["type"] == "open-source" and GH_PAT.match(p["url"]) else "—"
                star_n = fmt_stars(p.get("stars")) if p.get("stars") is not None else "—"
                # Prefer badge for GH; show count in same cell
                star_cell = f"{badge}<br>{star_n}" if badge != "—" else star_n
            desc = (p.get("note") or "").replace("|", "\\|")
            # strip internal flags from display slightly
            lines.append(
                f"| [{p['name']}]({p['url']}){arch} | {typ} | {star_cell} | {fmt_date(p.get('last_commit'))} | "
                f"**{p['rating']}** | {desc} |"
            )
        lines.append("")

    lines += [
        "## Contributing",
        "",
        "See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome — especially new verified agents, benchmarks, "
        "and MCP servers. Please do not submit unverified, low-effort, or purely defensive-only tools "
        "(those belong in LLM-security lists).",
        "",
        "Refresh stats after merging GitHub entries:",
        "",
        "```bash",
        "python3 scripts/update_stats.py          # needs network; set GITHUB_TOKEN for higher rate limits",
        "python3 scripts/update_stats.py --offline  # regenerate README from existing data/projects.json",
        "```",
        "",
        "## Disclaimer",
        "",
        "This list is for **authorized** security testing, research, and education only. "
        "Many tools can cause damage if misused. Always obtain explicit permission before testing systems you do not own. "
        "Maintainers are not responsible for misuse. Inclusion ≠ endorsement of legality, safety, or quality.",
        "",
        "## License",
        "",
        "[CC0 1.0 Universal](LICENSE) — public domain dedication.",
        "",
        "---",
        "",
        f"<sub>Maintained by [Rafał Gacek (BerSec)](https://github.com/BerSecHub) · Polish pentester (OSCP / BSCP / AIRTP+) · "
        f"Stats generated {gen_day} UTC · {len(projects)} entries</sub>",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--offline", action="store_true", help="Skip GitHub API; just re-rate and render README")
    ap.add_argument("--fetch-only", action="store_true", help="Fetch stats only; do not write README")
    ap.add_argument("--sleep", type=float, default=0.85, help="Delay between GitHub API calls")
    args = ap.parse_args()

    if not DATA.exists():
        print(f"Missing {DATA}", file=sys.stderr)
        return 1
    doc = load()

    if not args.offline:
        print("Fetching GitHub repository stats…")
        refresh_github(doc, sleep_s=args.sleep)
        apply_ratings(doc)
        save(doc)
        print(f"Wrote {DATA}")
    else:
        apply_ratings(doc)
        save(doc)
        print(f"Re-rated offline → {DATA}")

    if not args.fetch_only:
        README.write_text(render_readme(doc))
        print(f"Wrote {README}")
        # category counts
        c = Counter(p["category"] for p in doc["projects"])
        for cat in CATEGORY_ORDER:
            if cat in c:
                print(f"  {c[cat]:3d}  {cat}")
        print(f"Total: {len(doc['projects'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
