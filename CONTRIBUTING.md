# Contributing to Awesome Hackbots

Thanks for helping build the best curated list of **hackbots** — AI agents and LLM-powered tools for offensive security.

## What belongs here

In scope:

- Autonomous / semi-autonomous **pentest, red-team, bug-bounty, recon, exploit, CTF** agents
- **Code-auditing / SAST** agents and neurosymbolic vuln hunters
- **LLM-guided fuzzing** and cyber reasoning systems (CRS), including AIxCC-related work
- **Security MCP servers** that expose offensive tooling (Burp, Kali, nmap, Nuclei, RE tools, …)
- **Benchmarks & datasets** for measuring cyber agents (Cybench, CVE-Bench, BountyBench, …)
- **Commercial hackbots** and closely related AppSec AI products
- Foundational **papers**, high-signal **blogs/talks**, **competitions**, and sibling **awesome lists**

Out of scope (open a discussion if unsure):

- Purely **defensive** LLM-security / prompt-injection guardrail tools (point people at `awesome-llm-security` instead)
- Generic LLM frameworks with no security focus
- Broken, 404, or unverifiable links
- Duplicate entries of the same project under a different mirror without a clear reason

## Entry format

Add the project to `data/projects.json` (preferred) **or** open a PR that edits the README and we will sync JSON.

Required fields:

```json
{
  "name": "ProjectName",
  "url": "https://github.com/org/repo",
  "category": "Autonomous Pentest Agents",
  "type": "open-source",
  "stars": null,
  "last_commit": null,
  "archived": false,
  "rating": 0,
  "note": "One short sentence: what it does and why it matters."
}
```

- `type`: `open-source` | `commercial` | `event` | `paper` (`event` = competition, conference, or community site; rated like commercial, base 3.2)
- `note`: original wording; do **not** copy descriptions wholesale from other awesome lists
- After adding GitHub entries, run:

  ```bash
  python3 scripts/update_stats.py
  ```

  (Set `GITHUB_TOKEN` or `GH_TOKEN` to avoid the 60 req/hr unauthenticated limit.)

## Quality bar

- **Working URL** (HTTP 200). GitHub repos must resolve via the API.
- Prefer **actively maintained** or historically important (USENIX, AIxCC, Project Zero, …).
- One line of description, no marketing fluff, consistent punctuation.
- Mark archived projects; do not delete historically important ones without discussion.

## Rating & stars

Ratings (1.0–5.0) are computed by `scripts/update_stats.py` from stars (capped), last push, and a small prestige boost table. Do not hand-edit ratings unless you are updating the rubric in that script. Live Shields.io badges in the README always hit GitHub; numeric stars/ratings come from the last script run.

## Pull request process

1. Fork and create a branch.
2. Add/update `data/projects.json`.
3. Run `python3 scripts/update_stats.py` (or `--offline` if you only changed non-GitHub fields).
4. Ensure README tables still look sane.
5. Open a PR with a short rationale and the verified URL.

## Code of conduct

Be respectful. This is an offensive-security resource — discuss capabilities without sharing illegal targeting advice. Authorized testing only.

## License

Contributions are dedicated to the public domain under [CC0 1.0](LICENSE).
