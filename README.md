# Awesome Hackbots [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of **hackbots** — AI agents and LLM-powered tools that autonomously or semi-autonomously perform offensive security: pentesting, bug bounty, recon, vulnerability discovery, exploitation, CTF solving, code auditing, LLM-guided fuzzing, and red-team operations — plus the surrounding ecosystem of benchmarks, MCP servers, papers, competitions, and writing.

Curated by [Rafael Gacek](https://bersec.me)

[![entries](https://img.shields.io/badge/entries-215-blue?style=flat-square)](#contents) [![license](https://img.shields.io/badge/license-CC0-lightgrey?style=flat-square)](LICENSE) [![maintainer](https://img.shields.io/badge/maintainer-BerSec-red?style=flat-square)](https://github.com/BerSecHub)

## What is a hackbot?

A **hackbot** is an automated system that uses AI (typically LLMs, often with tools, sandboxes, fuzzers, and traditional scanners) in a meaningful way to find and/or exploit vulnerabilities in real targets — bug-bounty programs, production apps, CTF challenges, or source code.

This list prioritizes **verified, notable, actively maintained** projects. Every GitHub entry was checked via the GitHub API; dead/404 links are dropped. Star counts and ratings are refreshed by `scripts/update_stats.py` (data in `data/projects.json`).

## Legend

| Mark | Meaning |
|------|---------|
| 🟢 | Open-source project / tool |
| 🟠 | Commercial product / company |
| 🔵 | Research paper, blog post, or long-form writing |
| ⚠️ | Archived or unmaintained (still historically important) |
| ★ rating | Transparent 1–5 score — see [Rating rubric](#rating-rubric) |

_Stats snapshot: **2026-10-27** (UTC). Re-run `python3 scripts/update_stats.py` to refresh._

## Contents

- [Top hackbots leaderboard](#top-hackbots-leaderboard)
- [Rating rubric](#rating-rubric)
- [Autonomous Pentest Agents](#autonomous-pentest-agents) (39)
- [Commercial Hackbots](#commercial-hackbots) (14)
- [Frameworks, Skills & Harnesses](#frameworks-skills-harnesses) (18)
- [Code Auditing & SAST Agents](#code-auditing-sast-agents) (18)
- [LLM Fuzzing & Cyber Reasoning Systems](#llm-fuzzing-cyber-reasoning-systems) (13)
- [Security MCP Servers](#security-mcp-servers) (12)
- [Reverse Engineering Agents](#reverse-engineering-agents) (14)
- [CTF Solvers & Agents](#ctf-solvers-agents) (7)
- [Bug Bounty & Recon](#bug-bounty-recon) (10)
- [Benchmarks & Datasets](#benchmarks-datasets) (17)
- [Research Papers](#research-papers) (15)
- [Talks, Blogs & Writing](#talks-blogs-writing) (12)
- [Competitions](#competitions) (7)
- [People & Communities](#people-communities) (7)
- [Related Awesome Lists](#related-awesome-lists) (12)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

## Top hackbots leaderboard

Highest-rated **open-source** agents and CRS/SAST systems (excludes pure lists, blogs, and commercial SaaS). Ratings combine stars (capped), maintenance recency, and prestige boosts — not stars alone.

| # | Name | ★ Stars | Rating | Category |
|--:|------|--------:|:------:|----------|
| 1 | [Strix](https://github.com/usestrix/strix) | 72.1k | **5.0** ★★★★★ | Autonomous Pentest Agents |
| 2 | [Shannon](https://github.com/KeygraphHQ/shannon) | 49.4k | **4.8** ★★★★½ | Autonomous Pentest Agents |
| 3 | [SWE-agent (EnIGMA)](https://github.com/SWE-agent/SWE-agent) | 20.6k | **4.8** ★★★★½ | CTF Solvers & Agents |
| 4 | [PentAGI](https://github.com/vxcontrol/pentagi) | 32.5k | **4.7** ★★★★½ | Autonomous Pentest Agents |
| 5 | [Buttercup](https://github.com/trailofbits/buttercup) | 1.7k | **4.6** ★★★★½ | LLM Fuzzing & Cyber Reasoning Systems |
| 6 | [PentestGPT](https://github.com/GreyDGL/PentestGPT) | 16.1k | **4.3** ★★★★☆ | Autonomous Pentest Agents |
| 7 | [OSS-Fuzz-Gen](https://github.com/google/oss-fuzz-gen) | 1.4k | **4.3** ★★★★☆ | LLM Fuzzing & Cyber Reasoning Systems |
| 8 | [hackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT) | 1.3k | **4.1** ★★★★☆ | Autonomous Pentest Agents |
| 9 | [Semgrep](https://github.com/semgrep/semgrep) | 17.3k | **3.8** ★★★½☆ | Code Auditing & SAST Agents |
| 10 | [Codex Security](https://github.com/openai/codex-security) | 11.2k | **3.7** ★★★½☆ | Code Auditing & SAST Agents |
| 11 | [deepsec](https://github.com/vercel-labs/deepsec) | 8.3k | **3.7** ★★★½☆ | Code Auditing & SAST Agents |
| 12 | [CyberStrikeAI](https://github.com/AIPentest/CyberStrikeAI) | 8.1k | **3.7** ★★★½☆ | Autonomous Pentest Agents |
| 13 | [FuzzingBrain](https://github.com/fuzzingbrain/afc-crs-all-you-need-is-a-fuzzing-brain) | 146 | **3.7** ★★★½☆ | LLM Fuzzing & Cyber Reasoning Systems |
| 14 | [Decepticon](https://github.com/BitterSecurity/Decepticon) | 6.4k | **3.6** ★★★½☆ | Autonomous Pentest Agents |
| 15 | [Atlantis](https://github.com/Team-Atlanta/aixcc-afc-atlantis) | 653 | **3.6** ★★★½☆ | LLM Fuzzing & Cyber Reasoning Systems |

## Rating rubric

Each entry gets a **1.0–5.0** rating stored in `data/projects.json`:

| Signal | How it scores |
|--------|---------------|
| **Stars** (open-source) | `log10(min(stars, 50000))` scaled to **0–2.0**. Cap fights star inflation. Counts above 100k are anomalous: they score **0**, display as n/a, and cannot lead the leaderboard on stars. |
| **Maintenance** | Last push ≤30d → 1.5; ≤90d → 1.2; ≤180d → 0.8; ≤365d → 0.4; older → 0.1. **Archived → 0** (and overall cap 2.5). |
| **Prestige boost** | Manual +0.4–1.5 for AIxCC placements, USENIX/ICML/NDSS papers, Project Zero, XBOW, Cybench/CVE-Bench, etc. |
| **Open-source base** | +0.5 |
| **Commercial** | Base **3.2** + prestige (no GitHub stars required). |
| **Paper / writing** | Base **3.0** + prestige. |

Shields.io star badges in category tables always reflect **live** GitHub data; the numeric star column and rating come from the last `update_stats.py` run.

## Autonomous Pentest Agents

End-to-end or multi-agent systems that plan and execute offensive assessments with LLMs.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [Strix](https://github.com/usestrix/strix) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/usestrix/strix?style=flat-square)<br>72.1k | 2026-10-26 | **5.0** | Autonomous AI hackers with dynamic PoC validation |
| [Shannon](https://github.com/KeygraphHQ/shannon) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/KeygraphHQ/shannon?style=flat-square)<br>49.4k | 2026-10-15 | **4.8** | White-box autonomous AI pentester; strong XBOW-bench results |
| [PentAGI](https://github.com/vxcontrol/pentagi) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/vxcontrol/pentagi?style=flat-square)<br>32.5k | 2026-10-22 | **4.7** | Fully autonomous multi-agent pentest with Docker sandbox + Neo4j |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/GreyDGL/PentestGPT?style=flat-square)<br>16.1k | 2026-07-14 | **4.3** | USENIX Security 2024 LLM pentest agent; widely cited |
| [hackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/ipa-lab/hackingBuddyGPT?style=flat-square)<br>1.3k | 2026-10-24 | **4.1** | Minimal research framework for LLM Linux priv-esc (~50 LOC) |
| [CyberStrikeAI](https://github.com/AIPentest/CyberStrikeAI) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/AIPentest/CyberStrikeAI?style=flat-square)<br>8.1k | 2026-10-23 | **3.7** | Go platform with Eino agents, MCP tools, RAG, human oversight |
| [Decepticon](https://github.com/BitterSecurity/Decepticon) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/BitterSecurity/Decepticon?style=flat-square)<br>6.4k | 2026-10-26 | **3.6** | LangGraph multi-agent red-team hacking agent + MCP |
| [RedAmon](https://github.com/samugit83/redamon) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/samugit83/redamon?style=flat-square)<br>3.2k | 2026-10-22 | **3.5** | Attack-surface graph + Kali sandbox with human approval gates |
| [PentestAgent](https://github.com/GH05TCREW/pentestagent) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/GH05TCREW/pentestagent?style=flat-square)<br>3.2k | 2026-10-26 | **3.5** | Black-box AI pentest with playbooks for bounty/red-team |
| [Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Armur-Ai/Pentest-Swarm-AI?style=flat-square)<br>3.1k | 2026-10-26 | **3.5** | Swarm of recon/exploit/reporting specialist agents |
| [Deep Eye](https://github.com/zakirkun/deep-eye) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/zakirkun/deep-eye?style=flat-square)<br>2.4k | 2026-10-06 | **3.4** | AI-assisted pentest scanner with multi-LLM payload generation |
| [Pentest-AI](https://github.com/0xSteph/pentest-ai) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/0xSteph/pentest-ai?style=flat-square)<br>1.8k | 2026-10-09 | **3.4** | AI pentester via MCP/CLI/CI with machine-oracle exploit verification |
| [T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/elder-plinius/T3MP3ST?style=flat-square)<br>6.6k | 2026-09-08 | **3.3** | Meta-harness wrapping coding agents into recon-to-report hunters |
| [Cairn](https://github.com/oritera/Cairn) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/oritera/Cairn?style=flat-square)<br>4.5k | 2026-09-07 | **3.3** | State-space search engine for autonomous pentest/CTF |
| [NeuroSploit](https://github.com/JoasASantos/NeuroSploit) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/JoasASantos/NeuroSploit?style=flat-square)<br>1.5k | 2026-10-19 | **3.3** | Rust CLI harness with second-model adjudication of findings |
| [Xalgorix](https://github.com/xalgorix/xalgorix) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/xalgorix/xalgorix?style=flat-square)<br>1.3k | 2026-10-26 | **3.3** | Self-hosted autonomous pentest agents with local dashboard |
| [DarkMoon](https://github.com/ASCIT31/Dark-Moon) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/ASCIT31/Dark-Moon?style=flat-square)<br>1.1k | 2026-10-26 | **3.3** | Autonomous platform orchestrating 80+ tools via Markdown playbooks |
| [Nebula](https://github.com/berylliumsec/nebula) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/berylliumsec/nebula?style=flat-square)<br>1.1k | 2026-10-26 | **3.3** | AI pentesting CLI assistant with local-LLM support |
| [Clearwing](https://github.com/Lazarus-AI/clearwing) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Lazarus-AI/clearwing?style=flat-square)<br>1.1k | 2026-10-18 | **3.3** | ReAct network pentest agent + parallel source hunter |
| [AIRecon](https://github.com/pikpikcu/airecon) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/pikpikcu/airecon?style=flat-square)<br>1.1k | 2026-10-12 | **3.3** | Kali Docker sandbox + Caido proxy recon→exploit→report TUI |
| [PentestCode](https://github.com/s0ld13rr/pentestcode) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/s0ld13rr/pentestcode?style=flat-square)<br>886 | 2026-10-23 | **3.3** | Multi-agent terminal pentesting with persistent engagement state |
| [AIDA](https://github.com/Vasco0x4/AIDA) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Vasco0x4/AIDA?style=flat-square)<br>506 | 2026-10-21 | **3.2** | Connects AI to 400+ tools via MCP in Exegol container |
| [Pentest Copilot](https://github.com/bugbasesecurity/pentest-copilot) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/bugbasesecurity/pentest-copilot?style=flat-square)<br>1.5k | 2026-08-14 | **3.1** | Browser-based ethical hacking assistant with agentic command runner |
| [BugTraceAI](https://github.com/BugTraceAI/BugTraceAI) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/BugTraceAI/BugTraceAI?style=flat-square)<br>357 | 2026-10-19 | **3.1** | Multi-agent authorized web app security testing platform |
| [REDCELL](https://github.com/martian56/redcell) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/martian56/redcell?style=flat-square)<br>348 | 2026-10-06 | **3.1** | Orchestrator+executor LLM agents in Kali container |
| [cyber-harness](https://github.com/chainreactors/cyber-harness) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/chainreactors/cyber-harness?style=flat-square)<br>347 | 2026-10-26 | **3.1** | Single-binary agent runtime for pentest/red-team/bounty |
| [LazyOwn](https://github.com/grisuno/LazyOwn) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/grisuno/LazyOwn?style=flat-square)<br>300 | 2026-10-26 | **3.1** | Red-team C2 with LLM operator + 153 MCP tools |
| [LuaN1aoAgent](https://github.com/SanMuzZzZz/LuaN1aoAgent) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/SanMuzZzZz/LuaN1aoAgent?style=flat-square)<br>1.4k | 2026-09-15 | **3.0** | Dual-graph (causal + attack) plan-execute-reflect pentest agent |
| [HackGPT](https://github.com/NoDataFound/hackGPT) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/NoDataFound/hackGPT?style=flat-square)<br>1.2k | 2026-08-12 | **3.0** | Early (2023) GPT-driven toolkit of offensive prompts/scripts; mostly historical |
| [VulnBot](https://github.com/KHenryAegis/VulnBot) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/KHenryAegis/VulnBot?style=flat-square)<br>203 | 2026-10-13 | **3.0** | Multi-agent collaborative pentest framework with RAG |
| [ShiftGrid](https://github.com/BuFuuu/shiftgrid) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/BuFuuu/shiftgrid?style=flat-square)<br>42 | 2026-10-07 | **2.7** | Prompt engine turning Claude Code into human-in-the-loop pentester |
| [CAI](https://github.com/aliasrobotics/cai) ⚠️ | 🟢 open-source | ![stars](https://img.shields.io/github/stars/aliasrobotics/cai?style=flat-square)<br>9.8k | 2026-08-22 | **2.5** | Alias Robotics agent framework; top AI team in HTB AI vs Humans CTF (19/20); archived Aug 2026 [ARCHIVED] |
| [numasec](https://github.com/FrancescoStabile/numasec) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/FrancescoStabile/numasec?style=flat-square)<br>822 | 2026-05-08 | **2.5** | Terminal AI security agent with runbooks and evidence tracking |
| [HunterX](https://github.com/nullc0d30/HunterX) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/nullc0d30/HunterX?style=flat-square)<br>13 | 2026-10-26 | **2.5** | AI-assisted offensive engine for recon and vuln orchestration |
| [ARTEMIS](https://github.com/Stanford-Trinity/ARTEMIS) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Stanford-Trinity/ARTEMIS?style=flat-square)<br>548 | 2026-04-14 | **2.1** | Stanford Trinity autonomous vuln discovery with Codex subagents |
| [Ankou](https://github.com/Red-Hex-Consulting/Ankou) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Red-Hex-Consulting/Ankou?style=flat-square)<br>239 | 2026-04-24 | **1.9** | AI-powered C2 with built-in AI companion for target analysis [URL corrected] |
| [AutoPentest-DRL](https://github.com/crond-jaist/AutoPentest-DRL) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/crond-jaist/AutoPentest-DRL?style=flat-square)<br>448 | 2022-02-15 | **1.7** | Automated pentesting with deep reinforcement learning [URL corrected] |
| [HackSynth](https://github.com/aielte-research/HackSynth) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/aielte-research/HackSynth?style=flat-square)<br>319 | 2025-06-24 | **1.7** | Planner/summarizer LLM agent for autonomous pentest benchmarks |
| [hero](https://github.com/jthack/hero) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/jthack/hero?style=flat-square)<br>43 | 2024-02-24 | **1.3** | Joseph Thacker hackbot PoC: request in → AI payload + validate |

## Commercial Hackbots

Vendors shipping autonomous or AI-assisted offensive testing / AppSec products.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [XBOW](https://xbow.com/) | 🟠 commercial | — | — | **4.7** | Autonomous offensive platform; #1 HackerOne automated findings; exploit-validated |
| [Horizon3 NodeZero](https://www.horizon3.ai/) | 🟠 commercial | — | — | **4.0** | Autonomous pentest platform (NodeZero) for continuous validation |
| [Pentera](https://www.pentera.io/) | 🟠 commercial | — | — | **3.8** | Automated security validation / continuous automated red teaming platform |
| [AttackIQ](https://www.attackiq.com/) | 🟠 commercial | — | — | **3.2** | Adversary emulation / BAS platform with AI-assisted testing |
| [Bugcrowd AI](https://www.bugcrowd.com/) | 🟠 commercial | — | — | **3.2** | Crowdsourced + AI-assisted bug bounty / pentest programs |
| [Checkmarx AI](https://checkmarx.com/) | 🟠 commercial | — | — | **3.2** | Enterprise AppSec with AI-assisted SAST/DAST |
| [DryRun Security](https://www.dryrun.security/) | 🟠 commercial | — | — | **3.2** | AI code security review focused on intent and risk |
| [Escape](https://escape.tech/) | 🟠 commercial | — | — | **3.2** | API security testing with AI-driven discovery and scanning |
| [HackerOne Hai](https://www.hackerone.com/ai) | 🟠 commercial | — | — | **3.2** | HackerOne AI assistant (Hai) for triage and research workflows |
| [Hadrian](https://hadrian.io/) | 🟠 commercial | — | — | **3.2** | Autonomous external attack-surface management and testing |
| [ProjectDiscovery Neo](https://projectdiscovery.io/blog/neo-v1) | 🟠 commercial | — | — | **3.2** | Nuclei makers' autonomous platform: parallel agents pentest apps/APIs, red-team, re-prove fixes |
| [Snyk DeepCode AI](https://snyk.io/) | 🟠 commercial | — | — | **3.2** | AI-assisted code security and fix suggestions |
| [Strix Cloud](https://strix.ai/) | 🟠 commercial | — | — | **3.2** | Commercial offering around the open-source Strix AI hackers |
| [ZeroPath](https://zeropath.com/) | 🟠 commercial | — | — | **3.2** | AI-powered application security / SAST-style code hunting |

## Frameworks, Skills & Harnesses

Agent skills, harnesses, and scaffolding that turn coding agents into security operators.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [Mantis](https://github.com/google/mantis) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/google/mantis?style=flat-square)<br>2.5k | 2026-10-25 | **4.4** | Google security-review skills + ADK harness for vuln discovery |
| [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/0x4m4/hexstrike-ai?style=flat-square)<br>13.1k | 2026-08-03 | **4.3** | MCP server exposing 150+ security tools to AI agents |
| [Cloudflare Security Audit Skill](https://github.com/cloudflare/security-audit-skill) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/cloudflare/security-audit-skill?style=flat-square)<br>48.3k | 2026-09-14 | **3.7** | Coding-agent skill for multi-phase source security audits |
| [Claude-Red](https://github.com/SnailSploit/Claude-Red) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/SnailSploit/Claude-Red?style=flat-square)<br>9.4k | 2026-10-12 | **3.7** | Offensive security SKILL.md library for Claude red-team ops |
| [Agentic Bug Hunter](https://github.com/awarexone/Agentic-Bug-Hunter) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/awarexone/Agentic-Bug-Hunter?style=flat-square)<br>5.4k | 2026-10-23 | **3.6** | Claude Code plugin/CLI for bounty recon→validate→report |
| [Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/elementalsouls/Claude-BugHunter?style=flat-square)<br>5.3k | 2026-10-26 | **3.6** | 80+ Claude Code skills + slash commands for bug hunting |
| [defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/anthropics/defending-code-reference-harness?style=flat-square)<br>7.7k | 2026-08-06 | **3.4** | Anthropic reference Claude Code skills for vuln discovery |
| [pentest-ai-agents](https://github.com/0xSteph/pentest-ai-agents) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/0xSteph/pentest-ai-agents?style=flat-square)<br>2.4k | 2026-10-06 | **3.4** | 50 Claude Code subagents for authorized pentesting |
| [offensive-ai-compilation](https://github.com/jiep/offensive-ai-compilation) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/jiep/offensive-ai-compilation?style=flat-square)<br>1.4k | 2026-10-03 | **3.3** | Curated Offensive AI tools, techniques, and papers |
| [sast-skills](https://github.com/utkusen/sast-skills) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/utkusen/sast-skills?style=flat-square)<br>1.3k | 2026-10-23 | **3.3** | Agent skills turning coding assistants into SAST scanners |
| [VulnHunter](https://github.com/capitalone/VulnHunter) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/capitalone/VulnHunter?style=flat-square)<br>1.1k | 2026-10-07 | **3.3** | Capital One Claude Code skills: attacker-oriented source review |
| [OPFOR](https://github.com/KeyValueSoftwareSystems/agent-opfor) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/KeyValueSoftwareSystems/agent-opfor?style=flat-square)<br>584 | 2026-10-21 | **3.2** | Adversary emulation for AI agents and MCP servers |
| [AgentHound](https://github.com/adithyan-ak/AgentHound) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/adithyan-ak/AgentHound?style=flat-square)<br>453 | 2026-10-25 | **3.1** | Offensive framework for agentic infra: MCP/A2A recon & looting |
| [Transilience Community Tools](https://github.com/transilienceai/communitytools) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/transilienceai/communitytools?style=flat-square)<br>595 | 2026-07-29 | **2.9** | Claude Code skills/agents/slash commands for pentest & bounty |
| [Forefy .context](https://github.com/forefy/.context) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/forefy/.context?style=flat-square)<br>153 | 2026-10-26 | **2.9** | Skills, Goals, Dynamic Workflows for security auditing |
| [claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/anthropics/claude-code-security-review?style=flat-square)<br>6.6k | 2026-02-11 | **2.5** | Official Claude semantic SAST GitHub Action for PR diffs |
| [Bug-Bounty-Agents](https://github.com/matty69v/Bug-Bounty-Agents) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/matty69v/Bug-Bounty-Agents?style=flat-square)<br>453 | 2026-04-30 | **2.4** | 43 AI agent personas across the bug-bounty lifecycle |
| [cyber-security-llm-agents](https://github.com/NVISOsecurity/cyber-security-llm-agents) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/NVISOsecurity/cyber-security-llm-agents?style=flat-square)<br>397 | 2024-05-07 | **1.7** | NVISO AutoGen agents for cybersecurity (RSAC 2024) |

## Code Auditing & SAST Agents

LLM agents and neurosymbolic tools that hunt vulnerabilities in source code.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [Semgrep](https://github.com/semgrep/semgrep) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/semgrep/semgrep?style=flat-square)<br>17.3k | 2026-10-26 | **3.8** | Lightweight SAST with built-in MCP server for AI coding agents |
| [Codex Security](https://github.com/openai/codex-security) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/openai/codex-security?style=flat-square)<br>11.2k | 2026-10-26 | **3.7** | OpenAI CLI/SDK for find/validate/fix vulnerabilities |
| [deepsec](https://github.com/vercel-labs/deepsec) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/vercel-labs/deepsec?style=flat-square)<br>8.3k | 2026-09-29 | **3.7** | Vercel Labs agent-powered scanner for large repos |
| [snyk/agent-scan](https://github.com/snyk/agent-scan) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/snyk/agent-scan?style=flat-square)<br>3.2k | 2026-10-26 | **3.5** | Snyk agent-oriented scanning for AI coding agents |
| [Visa Vulnerability Agentic Harness](https://github.com/visa/visa-vulnerability-agentic-harness) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/visa/visa-vulnerability-agentic-harness?style=flat-square)<br>3k | 2026-10-22 | **3.5** | Agentic SAST for discovery + exploitability verification |
| [open-kritt](https://github.com/Kritt-ai/open-kritt) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Kritt-ai/open-kritt?style=flat-square)<br>2.3k | 2026-10-26 | **3.4** | Self-hosted platform orchestrating AI agents for code vuln research |
| [AutoCVE](https://github.com/larlarua/AutoCVE) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/larlarua/AutoCVE?style=flat-square)<br>1.2k | 2026-10-01 | **3.3** | Agent-driven CVE discovery pipeline with verification |
| [Metis](https://github.com/arm/metis) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/arm/metis?style=flat-square)<br>888 | 2026-10-26 | **3.3** | Arm agentic framework for deep semantic security code review |
| [OpenAnt](https://github.com/knostic/OpenAnt) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/knostic/OpenAnt?style=flat-square)<br>785 | 2026-10-26 | **3.2** | Detect-then-attack harness; only surviving findings reported |
| [0](https://github.com/0sec-labs/0) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/0sec-labs/0?style=flat-square)<br>521 | 2026-10-26 | **3.2** | Local browser console harness for code review and vuln research |
| [agentgg](https://github.com/agentgg-dev/agentgg) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/agentgg-dev/agentgg?style=flat-square)<br>442 | 2026-10-20 | **3.1** | Agentic white-box SAST following imports/call graphs |
| [OpenHack](https://github.com/openhackai/OpenHack) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/openhackai/OpenHack?style=flat-square)<br>430 | 2026-10-17 | **3.1** | Agentic security scanner using exclusively open-source models |
| [Vulnhuntr](https://github.com/protectai/vulnhuntr) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/protectai/vulnhuntr?style=flat-square)<br>2.8k | 2025-02-06 | **2.9** | Zero-shot LLM call-chain vuln discovery; found 0-days in production Python |
| [llm-sast-scanner](https://github.com/SunWeb3Sec/llm-sast-scanner) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/SunWeb3Sec/llm-sast-scanner?style=flat-square)<br>289 | 2026-08-22 | **2.7** | SAST skill with structured source-to-sink analysis |
| [rust-in-peace](https://github.com/scadastrangelove/rust-in-peace) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/scadastrangelove/rust-in-peace?style=flat-square)<br>25 | 2026-10-14 | **2.6** | Agent-assisted Rust vuln discovery with adversarial triage |
| [IRIS](https://github.com/iris-sast/iris) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/iris-sast/iris?style=flat-square)<br>444 | 2026-07-02 | **2.4** | Neurosymbolic SAST combining LLMs with CodeQL for Java |
| [Reproof](https://github.com/scadastrangelove/reproof) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/scadastrangelove/reproof?style=flat-square)<br>4 | 2026-10-12 | **2.3** | Multi-language agentic vuln discovery with PoC replay |
| [burpgpt](https://github.com/aress31/burpgpt) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/aress31/burpgpt?style=flat-square)<br>2.4k | 2024-06-09 | **2.0** | Burp Suite extension integrating GPT for passive scanning |

## LLM Fuzzing & Cyber Reasoning Systems

LLM-guided fuzzers and DARPA AIxCC-style cyber reasoning systems (find + prove + patch).

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [Buttercup](https://github.com/trailofbits/buttercup) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/trailofbits/buttercup?style=flat-square)<br>1.7k | 2026-10-19 | **4.6** | Trail of Bits AIxCC CRS (2nd place); fuzz + LLM patch |
| [OSS-Fuzz-Gen](https://github.com/google/oss-fuzz-gen) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/google/oss-fuzz-gen?style=flat-square)<br>1.4k | 2026-10-26 | **4.3** | Google LLM-powered fuzz target generation via OSS-Fuzz |
| [FuzzingBrain](https://github.com/fuzzingbrain/afc-crs-all-you-need-is-a-fuzzing-brain) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/fuzzingbrain/afc-crs-all-you-need-is-a-fuzzing-brain?style=flat-square)<br>146 | 2026-10-12 | **3.7** | AIxCC finalist CRS with diverse LLM strategies [URL corrected] |
| [Atlantis](https://github.com/Team-Atlanta/aixcc-afc-atlantis) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Team-Atlanta/aixcc-afc-atlantis?style=flat-square)<br>653 | 2025-11-25 | **3.6** | Team Atlanta AIxCC Final winner CRS ($4M) |
| [EvoMaster](https://github.com/WebFuzzing/EvoMaster) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/WebFuzzing/EvoMaster?style=flat-square)<br>797 | 2026-10-26 | **3.2** | AI-driven system-level test generation for REST/GraphQL/RPC |
| [OSS-CRS](https://github.com/ossf/oss-crs) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/ossf/oss-crs?style=flat-square)<br>174 | 2026-10-26 | **3.0** | OpenSSF framework for LLM-based autonomous bug-finding/fixing |
| [ChatAFL](https://github.com/ChatAFLndss/ChatAFL) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/ChatAFLndss/ChatAFL?style=flat-square)<br>400 | 2025-06-30 | **2.5** | LLM-guided protocol fuzzing extending AFLNet (NDSS'24) |
| [Theori RoboDuck (AIxCC archive)](https://github.com/theori-io/aixcc-afc-archive) ⚠️ | 🟢 open-source | ![stars](https://img.shields.io/github/stars/theori-io/aixcc-afc-archive?style=flat-square)<br>274 | 2025-08-05 | **2.5** | Theori AIxCC 3rd-place CRS (archived public release) [ARCHIVED] |
| [FuzzyAI](https://github.com/cyberark/FuzzyAI) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/cyberark/FuzzyAI?style=flat-square)<br>1.6k | 2026-02-06 | **2.3** | CyberArk automated LLM fuzzing for jailbreaks / LLM API vulns |
| [Artiphishell](https://github.com/shellphish/artiphishell) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/shellphish/artiphishell?style=flat-square)<br>144 | 2025-08-27 | **2.2** | Shellphish AIxCC CRS / Artiphishell |
| [TitanFuzz](https://github.com/ise-uiuc/TitanFuzz) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/ise-uiuc/TitanFuzz?style=flat-square)<br>95 | 2023-09-10 | **1.4** | First LLM-based fuzzer for DL frameworks (ISSTA'23) |
| [42-b3yond-6ug CRS](https://github.com/42-b3yond-6ug/42-b3yond-6ug-crs) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/42-b3yond-6ug/42-b3yond-6ug-crs?style=flat-square)<br>31 | 2025-08-19 | **1.2** | 42-b3yond-6ug AIxCC Cyber Reasoning System |
| [42-b3yond-6ug ASC](https://github.com/42-b3yond-6ug/42-b3yond-6ug-asc) ⚠️ | 🟢 open-source | ![stars](https://img.shields.io/github/stars/42-b3yond-6ug/42-b3yond-6ug-asc?style=flat-square)<br>6 | 2025-08-19 | **1.0** | 42-b3yond-6ug CRS from the AIxCC Semifinal Competition (ASC) [ARCHIVED] |

## Security MCP Servers

Model Context Protocol servers that expose offensive security tools to AI clients.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [Burp Suite MCP Server](https://github.com/PortSwigger/mcp-server) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/PortSwigger/mcp-server?style=flat-square)<br>1.3k | 2026-10-16 | **4.1** | Official PortSwigger Burp ↔ AI clients via MCP |
| [cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/cisco-ai-defense/mcp-scanner?style=flat-square)<br>1.1k | 2026-10-23 | **3.3** | Cisco AI Defense scanner for MCP server threats |
| [Google Security MCP](https://github.com/google/mcp-security) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/google/mcp-security?style=flat-square)<br>535 | 2026-10-16 | **3.2** | MCP for Google SecOps (Chronicle), TI, and security products |
| [pentestMCP](https://github.com/ramkansal/pentestMCP) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/ramkansal/pentestMCP?style=flat-square)<br>111 | 2026-09-25 | **2.6** | 20+ assessment tools (Nmap, Nuclei, ZAP, SQLMap) via MCP |
| [mcp-vanguard](https://github.com/skyvanguard/mcp-vanguard) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/skyvanguard/mcp-vanguard?style=flat-square)<br>4 | 2026-10-20 | **2.3** | 89 pentest MCP tools; Windows/WSL Kali bridge |
| [MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Wh0am123/MCP-Kali-Server?style=flat-square)<br>864 | 2026-03-17 | **2.2** | MCP exposing Kali Linux tooling to AI agents [URL corrected] |
| [pwno-mcp](https://github.com/pwno-io/pwno-mcp) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/pwno-io/pwno-mcp?style=flat-square)<br>282 | 2026-03-12 | **1.9** | Stateful GDB/pwndbg MCP for binary exploitation: sessions, context snapshots, exploit I/O |
| [mcp-for-security](https://github.com/cyproxio/mcp-for-security) ⚠️ | 🟢 open-source | ![stars](https://img.shields.io/github/stars/cyproxio/mcp-for-security?style=flat-square)<br>628 | 2026-03-30 | **1.7** | Collection of security-tool MCP servers [URL corrected] [ARCHIVED] |
| [Bolt](https://github.com/CyberStrikeus/bolt) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/CyberStrikeus/bolt?style=flat-square)<br>74 | 2026-04-03 | **1.7** | Docker MCP exposing 100+ Kali tools as plugins |
| [DomScan MCP](https://github.com/estevecastells/domscan-mcp) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/estevecastells/domscan-mcp?style=flat-square)<br>1 | 2026-07-22 | **1.4** | Hosted domain-intel MCP (DNS, WHOIS/RDAP, TLS, subdomains, reputation) |
| [nuclei-mcp](https://github.com/addcontent/nuclei-mcp) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/addcontent/nuclei-mcp?style=flat-square)<br>49 | 2025-08-04 | **1.3** | MCP wrapper for ProjectDiscovery Nuclei scanner |
| [PentestThinkingMCP](https://github.com/ibrahimsaleem/PentestThinkingMCP) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/ibrahimsaleem/PentestThinkingMCP?style=flat-square)<br>38 | 2025-08-30 | **1.3** | Beam Search/MCTS attack-path planning MCP for CTF/pentest |

## Reverse Engineering Agents

LLM assistants and MCP bridges for IDA, Ghidra, Binary Ninja, JADX, and friends.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/mrexodia/ida-pro-mcp?style=flat-square)<br>13.2k | 2026-09-26 | **4.4** | MCP bridge for IDA Pro → LLM decompile/xref/debug workflows |
| [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/LaurieWired/GhidraMCP?style=flat-square)<br>11.6k | 2026-10-10 | **4.3** | MCP server exposing Ghidra RE ops to any MCP-capable LLM |
| [ghidra-mcp](https://github.com/bethington/ghidra-mcp) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/bethington/ghidra-mcp?style=flat-square)<br>5.9k | 2026-10-26 | **3.6** | Ghidra MCP with 200+ tools; GUI plugin or headless |
| [ReVa](https://github.com/cyberkaida/reverse-engineering-assistant) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/cyberkaida/reverse-engineering-assistant?style=flat-square)<br>882 | 2026-10-26 | **3.3** | Ghidra-focused RE assistant with MCP + Claude Skills |
| [Gepetto](https://github.com/JusticeRage/Gepetto) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/JusticeRage/Gepetto?style=flat-square)<br>3.5k | 2026-08-15 | **3.2** | IDA Pro plugin: GPT comments and variable renaming |
| [JADX MCP Server](https://github.com/zinja-coder/jadx-mcp-server) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/zinja-coder/jadx-mcp-server?style=flat-square)<br>810 | 2026-10-19 | **3.2** | MCP for JADX-AI Android APK reverse engineering |
| [GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/symgraph/GhidrAssistMCP?style=flat-square)<br>790 | 2026-10-09 | **3.2** | Native Ghidra MCP extension with security-sensitive tool gating |
| [IDAssist](https://github.com/symgraph/IDAssist) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/symgraph/IDAssist?style=flat-square)<br>890 | 2026-09-20 | **3.0** | IDA Pro LLM plugin: explanations, rename, RAG, knowledge graph |
| [LLM4Decompile](https://github.com/albertan017/LLM4Decompile) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/albertan017/LLM4Decompile?style=flat-square)<br>7.2k | 2026-02-12 | **2.5** | Research binary-to-C decompilation with LLMs |
| [APKTool MCP Server](https://github.com/zinja-coder/apktool-mcp-server) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/zinja-coder/apktool-mcp-server?style=flat-square)<br>677 | 2026-07-02 | **2.5** | MCP for Apktool decompile/inspect Android APKs |
| [x64dbg_mcp](https://github.com/bromoket/x64dbg_mcp) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/bromoket/x64dbg_mcp?style=flat-square)<br>136 | 2026-06-08 | **2.2** | MCP server exposing x64dbg debugging to AI clients |
| [REA](https://github.com/morluto/rea) | 🟢 open-source | n/a | 2026-10-27 | **2.0** | Local CLI/MCP for agent-assisted RE of native/.NET/JS. Star count looks anomalously high (created 2026-04-14) and is excluded from rating. |
| [GhidrOllama](https://github.com/lr-m/GhidrOllama) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/lr-m/GhidrOllama?style=flat-square)<br>156 | 2024-11-29 | **1.5** | Ghidra script using Ollama for function analysis/renaming |
| [binaryninja-mcp](https://github.com/MCPPhalanx/binaryninja-mcp) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/MCPPhalanx/binaryninja-mcp?style=flat-square)<br>51 | 2025-05-13 | **1.3** | MCP server for Binary Ninja-assisted reverse engineering |

## CTF Solvers & Agents

Agents that autonomously solve CTF challenges and interactive exploit tasks.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [SWE-agent (EnIGMA)](https://github.com/SWE-agent/SWE-agent) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=flat-square)<br>20.6k | 2026-10-19 | **4.8** | SWE-agent with EnIGMA CTF mode (ICML'25): interactive tools for debugger/netcat-style CTF solving |
| [Project Muteki](https://github.com/FishCodeTech/muteki) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/FishCodeTech/muteki?style=flat-square)<br>617 | 2026-10-26 | **3.2** | Multi-agent CTF-solving swarm with CLI agent engines |
| [D-CIPHER (NYU CTF Agents)](https://github.com/NYU-LLM-CTF/nyuctf_agents) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/NYU-LLM-CTF/nyuctf_agents?style=flat-square)<br>174 | 2026-07-17 | **3.1** | NYU planner/executor/auto-prompter multi-agent CTF solver; SOTA on NYU CTF Bench, Cybench, HTB |
| [BoxPwnr](https://github.com/0ca/BoxPwnr) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/0ca/BoxPwnr?style=flat-square)<br>467 | 2026-07-24 | **2.4** | Benchmark LLMs on HTB, PortSwigger, picoCTF, TryHackMe… |
| [ChatGPT on CTF](https://github.com/LiuYuancheng/ChatGPT_on_CTF) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/LiuYuancheng/ChatGPT_on_CTF?style=flat-square)<br>53 | 2026-08-18 | **2.4** | Research: can LLMs solve CTFs by running commands? |
| [Veria Labs CTF Agent](https://github.com/verialabs/ctf-agent) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/verialabs/ctf-agent?style=flat-square)<br>889 | 2026-03-29 | **2.2** | Coordinator LLM races model swarms; BSidesSF 2026 winner |
| [Palisade ReAct&Plan (Hacking CTFs with Plain Agents)](https://github.com/PalisadeResearch/intercode) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/PalisadeResearch/intercode?style=flat-square)<br>71 | 2024-12-05 | **2.0** | Simple ReAct&Plan agent that saturated InterCode-CTF (95%) with plain prompting + Kali tools |

## Bug Bounty & Recon

AI-assisted recon, scanning, reporting, and bounty workflows.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [Nuclei](https://github.com/projectdiscovery/nuclei) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/projectdiscovery/nuclei?style=flat-square)<br>32.3k | 2026-10-26 | **3.9** | Fast vuln scanner; AI template generation via -ai flag |
| [PwnDoc](https://github.com/pwndoc/pwndoc) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/pwndoc/pwndoc?style=flat-square)<br>2.9k | 2026-10-26 | **3.5** | Pentest report generator with AI-assisted finding generation |
| [SysReptor](https://github.com/Syslifters/sysreptor) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Syslifters/sysreptor?style=flat-square)<br>2.6k | 2026-10-25 | **3.5** | Pentest reporting platform with AI agent drafting findings |
| [OpenOSINT](https://github.com/OpenOSINT/OpenOSINT) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/OpenOSINT/OpenOSINT?style=flat-square)<br>1.8k | 2026-10-22 | **3.4** | AI OSINT agent (REPL, MCP, CLI, web) with 20 tools |
| [VoidAccess](https://github.com/KatrielMoses/voidaccess) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/KatrielMoses/voidaccess?style=flat-square)<br>936 | 2026-10-21 | **3.3** | Dark-web OSINT: Tor fan-out + LLM entity graph + IOC export |
| [OSINTGPT](https://github.com/estebanpdl/osintgpt) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/estebanpdl/osintgpt?style=flat-square)<br>532 | 2026-10-25 | **3.2** | OSINT analysis with GPT embeddings + vector search |
| [HackBot](https://github.com/morpheuslord/HackBot) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/morpheuslord/HackBot?style=flat-square)<br>365 | 2026-09-19 | **2.8** | LLaMA-based cybersecurity chatbot for scan/code analysis |
| [BruteForceAI](https://github.com/MorDavid/BruteForceAI) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/MorDavid/BruteForceAI?style=flat-square)<br>1.9k | 2026-07-17 | **2.7** | LLM-powered brute-force combining AI reasoning with login attacks |
| [pentest-agents](https://github.com/H-mmer/pentest-agents) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/H-mmer/pentest-agents?style=flat-square)<br>1k | 2026-06-12 | **2.6** | Bug-bounty agent suite (~50 agents, 2 MCP servers) for Claude Code/Codex/Gemini/Cursor with hunt loops |
| [ReconAIzer](https://github.com/hisxo/ReconAIzer) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/hisxo/ReconAIzer?style=flat-square)<br>905 | 2023-05-03 | **1.9** | Burp extension using GPT to discover endpoints/params during recon |

## Benchmarks & Datasets

Evaluation suites for measuring hackbot / cyber-agent capability.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [Cybench](https://github.com/andyzorigin/cybench) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/andyzorigin/cybench?style=flat-square)<br>346 | 2026-10-17 | **4.1** | 40 professional CTF tasks from 4 competitions for LLM agents |
| [CVE-Bench](https://github.com/uiuc-kang-lab/cve-bench) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/uiuc-kang-lab/cve-bench?style=flat-square)<br>303 | 2026-09-24 | **3.8** | ICML 2025: AI agents vs real critical web CVEs in Docker |
| [ExploitGym](https://github.com/sunblaze-ucb/exploitgym) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/sunblaze-ucb/exploitgym?style=flat-square)<br>1.2k | 2026-10-08 | **3.3** | Real-world userspace/V8/kernel exploit benchmark for agents |
| [CyberGym](https://github.com/sunblaze-ucb/cybergym) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/sunblaze-ucb/cybergym?style=flat-square)<br>975 | 2026-08-28 | **3.0** | Large-scale AI-agent vulnerability analysis evaluation |
| [AIRTBench-Code](https://github.com/dreadnode/AIRTBench-Code) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/dreadnode/AIRTBench-Code?style=flat-square)<br>111 | 2026-10-15 | **2.9** | Harness/dataset for autonomous AI red-team CTF evaluation |
| [XBOW Validation Suite](https://github.com/xbow-engineering/validation-benchmarks) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/xbow-engineering/validation-benchmarks?style=flat-square)<br>739 | 2026-07-07 | **2.5** | XBOW public validation benchmarks for offensive agents |
| [ExploitBench](https://github.com/exploitbench/exploitbench) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/exploitbench/exploitbench?style=flat-square)<br>437 | 2026-07-04 | **2.4** | AI-agent progress on V8/Chromium exploit ladders |
| [BountyBench](https://github.com/bountybench/bountybench) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/bountybench/bountybench?style=flat-square)<br>112 | 2025-07-24 | **2.3** | 25 real systems / 40 bug bounties; Detect-Exploit-Patch |
| [CTFusion](https://github.com/kaist-hacking/CTFusion) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/kaist-hacking/CTFusion?style=flat-square)<br>4 | 2026-07-11 | **2.1** | KAIST live-CTF streaming benchmark: CTFd MCP + proxy so agents compete without contamination |
| [Inspect Cyber](https://github.com/UKGovernmentBEIS/inspect_cyber) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/UKGovernmentBEIS/inspect_cyber?style=flat-square)<br>44 | 2026-06-18 | **2.0** | UK AISI Inspect extension for agentic cyber evaluations |
| [Damn Vulnerable LLM Agent](https://github.com/ReversecLabs/damn-vulnerable-llm-agent) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/ReversecLabs/damn-vulnerable-llm-agent?style=flat-square)<br>536 | 2025-06-25 | **1.8** | Vulnerable LangChain ReAct agent for prompt-injection practice |
| [SEC-bench](https://github.com/SEC-bench/SEC-bench) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/SEC-bench/SEC-bench?style=flat-square)<br>104 | 2026-01-27 | **1.8** | Reproducible real-world vuln instances from CVE/OSV |
| [AI Goat](https://github.com/dhammon/ai-goat) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/dhammon/ai-goat?style=flat-square)<br>373 | 2024-08-22 | **1.7** | Vulnerable-by-design local LLM CTF for AI security learning |
| [InterCode](https://github.com/princeton-nlp/intercode) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/princeton-nlp/intercode?style=flat-square)<br>257 | 2024-05-05 | **1.6** | Interactive coding benchmark incl. CTF tasks |
| [NYU CTF Bench](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/NYU-LLM-CTF/NYU_CTF_Bench?style=flat-square)<br>182 | 2025-09-22 | **1.6** | Dockerized CSAW CTF challenges for LLM-agent evaluation |
| [CTFTiny](https://github.com/NYU-LLM-CTF/CTFTiny) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/NYU-LLM-CTF/CTFTiny?style=flat-square)<br>21 | 2026-03-10 | **1.5** | Lightweight CTF benchmark from NYU LLM CTF group |
| [Cyber-Zero](https://github.com/amazon-science/Cyber-Zero) ⚠️ | 🟢 open-source | ![stars](https://img.shields.io/github/stars/amazon-science/Cyber-Zero?style=flat-square)<br>100 | 2026-02-13 | **1.4** | Amazon Science: train cyber agents without runtime; EnIGMA scaffold [ARCHIVED] |

## Research Papers

Foundational and recent papers on autonomous hacking, CTF agents, and CRS.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [PentestGPT (USENIX'24)](https://arxiv.org/abs/2308.02167) | 🔵 paper / writing | — | — | **4.2** | PentestGPT: An LLM-empowered Automatic Penetration Testing Tool |
| [CVE-Bench (ICML'25)](https://arxiv.org/abs/2503.17332) | 🔵 paper / writing | — | — | **4.0** | Benchmarking AI Agents Ability to Exploit Real-World CVEs |
| [Cybench](https://arxiv.org/abs/2408.08926) | 🔵 paper / writing | — | — | **4.0** | Framework for Evaluating Cybersecurity Capabilities of LLMs |
| [EnIGMA (ICML'25)](https://arxiv.org/abs/2409.16165) | 🔵 paper / writing | — | — | **4.0** | Enhanced Interactive Generative Model Agent; SOTA CTF |
| [LLM Agents can Autonomously Hack Websites](https://arxiv.org/abs/2402.06664) | 🔵 paper / writing | — | — | **4.0** | Foundational claim that LLM agents can hack websites autonomously |
| [SoK: DARPA AIxCC](https://arxiv.org/abs/2602.07666) | 🔵 paper / writing | — | — | **4.0** | SoK of AIxCC competition design, architectures, lessons |
| [BountyBench](https://arxiv.org/abs/2505.14534) | 🔵 paper / writing | — | — | **3.8** | Detect-Exploit-Patch evaluation on real bug bounties |
| [ATLANTIS CRS](https://arxiv.org/abs/2509.14589) | 🔵 paper / writing | — | — | **3.0** | ATLANTIS: AI-driven Threat Localization, Analysis, and Triage |
| [AutoAttacker](https://arxiv.org/abs/2403.02691) | 🔵 paper / writing | — | — | **3.0** | A Large Language Model Guided System to Automate Attacks |
| [ChatAFL (NDSS'24)](https://arxiv.org/abs/2306.12445) | 🔵 paper / writing | — | — | **3.0** | Large Language Model guided Protocol Fuzzing |
| [HackingBuddyGPT / Getting pwn'd by AI](https://arxiv.org/abs/2308.00121) | 🔵 paper / writing | — | — | **3.0** | LLM agents for privilege escalation (FSE'23 industrial) |
| [HackSynth](https://arxiv.org/abs/2412.01777) | 🔵 paper / writing | — | — | **3.0** | LLM agent framework for autonomous pentesting + benchmarks |
| [NYU CTF Bench](https://arxiv.org/abs/2406.05590) | 🔵 paper / writing | — | — | **3.0** | A Scalable LLM-driven CTF Benchmark for Cybersecurity |
| [PENTEST-AI Framework Survey](https://arxiv.org/abs/2502.16725) | 🔵 paper / writing | — | — | **3.0** | Survey / framing of AI-driven penetration testing |
| [Teams of LLM Agents can Exploit Zero-Day Vulnerabilities](https://arxiv.org/abs/2406.01637) | 🔵 paper / writing | — | — | **3.0** | Multi-agent LLM systems exploiting real zero-days |

## Talks, Blogs & Writing

Essays, vendor write-ups, and research blogs that define the space.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [From Naptime to Big Sleep (Project Zero)](https://projectzero.google/2024/10/from-naptime-to-big-sleep.html) | 🔵 paper / writing | — | — | **4.5** | Big Sleep finds real SQLite 0-day; Naptime→DeepMind collab |
| [Introducing XBOW](https://xbow.com/blog/introducing-xbow) | 🔵 paper / writing | — | — | **4.5** | XBOW launch: autonomous offensive AI platform |
| [Project Naptime (Project Zero)](https://projectzero.google/2024/06/project-naptime.html) | 🔵 paper / writing | — | — | **4.5** | P0 framework evaluating offensive LLM capabilities |
| [XBOW Blog](https://xbow.com/blog) | 🔵 paper / writing | — | — | **4.5** | XBOW write-ups: HackerOne #1 run, exploit case studies, benchmark methodology |
| [All About Hackbots (Joseph Thacker)](https://josephthacker.com/ai/2024/02/21/hackbots.html) | 🔵 paper / writing | — | — | **4.0** | Defines 'hackbot'; Hero PoC; foundational essay |
| [DARPA AIxCC Results](https://www.darpa.mil/news/2025/aixcc-results) | 🔵 paper / writing | — | — | **4.0** | Official DARPA AIxCC Final results announcement |
| [The Bug Bounty Singularity (Joseph Thacker)](https://josephthacker.com/hacking/2026/07/01/we-built-a-hackbot.html) | 🔵 paper / writing | — | — | **4.0** | Building a hackbot that found 126 bugs in 5 months |
| [AIxCC Final and Team Atlanta](https://team-atlanta.github.io/blog/post-afc/) | 🔵 paper / writing | — | — | **3.0** | Winning Atlantis CRS technical retrospective |
| [Build your own vulnerability harness (Cloudflare)](https://blog.cloudflare.com/build-your-own-vulnerability-harness/) | 🔵 paper / writing | — | — | **3.0** | Cloudflare on agentic vuln harnesses and their audit skill |
| [Buttercup wins 2nd at AIxCC (Trail of Bits)](https://blog.trailofbits.com/2025/08/09/trail-of-bits-buttercup-wins-2nd-place-in-aixcc-challenge/) | 🔵 paper / writing | — | — | **3.0** | ToB Buttercup AIxCC write-up |
| [Getting started with Mantis (Google)](https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs) | 🔵 paper / writing | — | — | **3.0** | Google Mantis harness for find-and-fix workflows |
| [Rise of Autonomous Hackbots (HackerOne)](https://www.hackerone.com/blog/rise-autonomous-hackbots-cybersecurity) | 🔵 paper / writing | — | — | **3.0** | Joseph Thacker on HackerOne: state of autonomous hackbots |

## Competitions

AI-for-offense competitions and challenge series.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [DARPA AI Cyber Challenge (AIxCC)](https://aicyberchallenge.com/) | 🟠 commercial | — | — | **4.7** | Two-year DARPA+ARPA-H competition for autonomous CRS |
| [AgentCTF × AgentXploit (Berkeley RDI)](https://ctf.secure-agent.com/) | 🟠 commercial | — | — | **3.7** | Berkeley RDI competition: build A2A exploit agents vs real CVEs in 20+ AI/web frameworks |
| [Neurogrid CTF (Hack The Box)](https://ctf.hackthebox.com/event/details/neurogrid-ctf-the-ultimate-ai-security-showdown-2712) | 🟠 commercial | — | — | **3.7** | HTB AI-first, MCP-only CTF (Nov 2025) benchmarking AI security agents; 156 AI teams vs humans |
| [AI vs Humans CTF (Palisade × Hack The Box)](https://github.com/PalisadeResearch/ai-vs-humans-ctf-report) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/PalisadeResearch/ai-vs-humans-ctf-report?style=flat-square)<br>7 | 2026-10-01 | **3.4** | First public AI-agent vs human CTF (Mar 2025, 403 teams); full data, agent designs and standings |
| [CSAW](https://www.csaw.io/) | 🟠 commercial | — | — | **3.2** | NYU student cybersecurity games and conference; parent of the separate LLM CTF Attack Competition |
| [CSAW LLM CTF Attack Competition](https://csaw.io/competition/llm-ctf-attack-competition) | 🟠 commercial | — | — | **3.2** | CSAW competition: generative AI solving CTF challenges |
| [DEF CON AI Village](https://aivillage.org/) | 🟠 commercial | — | — | **3.2** | DEF CON village for AI security research, talks, and challenges |

## People & Communities

Researchers, labs, and orgs shaping the hackbot ecosystem.

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [Brendan Dolan-Gavitt (@moyix)](https://xbow.com/authors/brendan-dolan-gavitt) | 🔵 paper / writing | — | — | **4.5** | XBOW AI researcher, ex-NYU prof; co-author of NYU CTF Bench and D-CIPHER, LLM-for-security pioneer |
| [Project Zero / Big Sleep](https://projectzero.google/) | 🔵 paper / writing | — | — | **4.5** | Google P0 + DeepMind offensive LLM research program |
| [Joseph Thacker (@rezz0)](https://josephthacker.com/) | 🔵 paper / writing | — | — | **4.0** | Coined popular 'hackbots' framing; HackerOne AI lead / researcher |
| [Alias Robotics (CAI)](https://aliasrobotics.com/) | 🟠 commercial | — | — | **3.2** | Creators of CAI Cybersecurity AI framework |
| [Trail of Bits](https://www.trailofbits.com/) | 🟠 commercial | — | — | **3.2** | Buttercup CRS; MCP security; offensive AI research shop |
| [hackingBuddy.ai](https://hackingbuddy.ai/) | 🔵 paper / writing | — | — | **3.0** | Academic community/site around hackingBuddyGPT priv-esc research |
| [Palisade Research](https://palisaderesearch.org/) | 🔵 paper / writing | — | — | **3.0** | AI-risk lab running AI-vs-human CTF tracks and offensive-capability elicitation studies |

## Related Awesome Lists

Sibling curated lists and closely related resources (we write our own descriptions).

| Name | Type | Stars | Last push | Rating | Description |
|------|:----:|------:|:---------:|:------:|-------------|
| [awesome-ai-security-tools](https://github.com/scadastrangelove/awesome-ai-security-tools) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/scadastrangelove/awesome-ai-security-tools?style=flat-square)<br>1.7k | 2026-10-25 | **3.4** | Broad AI security tools with caveats and star tracking |
| [Awesome-AI-Hacking-Agents](https://github.com/EvanThomasLuke/Awesome-AI-Hacking-Agents) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/EvanThomasLuke/Awesome-AI-Hacking-Agents?style=flat-square)<br>722 | 2026-10-25 | **3.2** | List of AI hacking agents with paper links |
| [awesome-cybersecurity-agentic-ai](https://github.com/raphabot/awesome-cybersecurity-agentic-ai) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/raphabot/awesome-cybersecurity-agentic-ai?style=flat-square)<br>606 | 2026-10-26 | **3.2** | Autonomous security agents, frameworks, research |
| [Awesome-LLM4Cybersecurity](https://github.com/tmylla/Awesome-LLM4Cybersecurity) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/tmylla/Awesome-LLM4Cybersecurity?style=flat-square)<br>1.8k | 2026-08-20 | **3.1** | LLMs for cybersecurity: pentest, exploit gen, vuln detect |
| [awesome-ai-cybersecurity](https://github.com/ElNiak/awesome-ai-cybersecurity) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/ElNiak/awesome-ai-cybersecurity?style=flat-square)<br>162 | 2026-10-07 | **2.9** | Mixed offensive/defensive AI-for-security list (tools, papers, datasets) |
| [Awesome-Offensive-AI-Agentic-Landscape](https://github.com/Yeti-791/Awesome-Offensive-AI-Agentic-Landscape) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Yeti-791/Awesome-Offensive-AI-Agentic-Landscape?style=flat-square)<br>400 | 2026-09-10 | **2.8** | Offensive agentic AI: projects, papers, commercial |
| [awesome-ai-pentesting](https://github.com/skyvanguard/awesome-ai-pentesting) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/skyvanguard/awesome-ai-pentesting?style=flat-square)<br>95 | 2026-10-25 | **2.8** | Curated autonomous AI pentesting agents and MCP tools |
| [awesome-ai-offensive-security](https://github.com/yeyintminthuhtut/awesome-ai-offensive-security) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/yeyintminthuhtut/awesome-ai-offensive-security?style=flat-square)<br>33 | 2026-07-30 | **2.4** | Large catalogue of offensive AI / pentest agents |
| [Awesome-GPT-Agents](https://github.com/fr0gger/Awesome-GPT-Agents) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/fr0gger/Awesome-GPT-Agents?style=flat-square)<br>6.6k | 2024-07-21 | **2.2** | GPT agents for cyber (offensive/defensive/analytical) |
| [awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/Puliczek/awesome-mcp-security?style=flat-square)<br>743 | 2026-03-03 | **2.1** | MCP security resources: tools, papers, vulns |
| [ai-exploits](https://github.com/protectai/ai-exploits) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/protectai/ai-exploits?style=flat-square)<br>1.8k | 2024-10-23 | **2.0** | Exploit collection targeting AI/ML infra (MLflow, Ray, H2O); not an AI-powered tool |
| [awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) | 🟢 open-source | ![stars](https://img.shields.io/github/stars/corca-ai/awesome-llm-security?style=flat-square)<br>1.7k | 2025-08-20 | **2.0** | Tools and docs about LLM security (defense-leaning) |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome — especially new verified agents, benchmarks, and MCP servers. Please do not submit unverified, low-effort, or purely defensive-only tools (those belong in LLM-security lists).

Refresh stats after merging GitHub entries:

```bash
python3 scripts/update_stats.py          # needs network; set GITHUB_TOKEN for higher rate limits
python3 scripts/update_stats.py --offline  # regenerate README from existing data/projects.json
```

## Disclaimer

This list is for **authorized** security testing, research, and education only. Many tools can cause damage if misused. Always obtain explicit permission before testing systems you do not own. Maintainers are not responsible for misuse. Inclusion ≠ endorsement of legality, safety, or quality.

## License

[CC0 1.0 Universal](LICENSE) — public domain dedication.

---

<sub>Maintained by [Rafał Gacek (BerSec)](https://github.com/BerSecHub) · Polish pentester (OSCP / BSCP / AIRTP+) · Stats generated 2026-10-27 UTC · 215 entries</sub>
