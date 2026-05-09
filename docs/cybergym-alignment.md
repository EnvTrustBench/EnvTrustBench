# CyberGym Alignment Notes

Reference: `https://www.cybergym.io/`.

CyberGym uses two public surfaces:

- A project page with a hero statement, resource buttons, leaderboard, overview, impact/key findings, example trace, and citation.
- A GitHub repository with install, dataset download, evaluation, server, firewall, example agents, citation, and license sections.

## EnvTrustBench Equivalent

| CyberGym Section | EnvTrustBench Public Draft |
|---|---|
| Hero and tagline | `README.md` title, tagline, and first paragraph |
| Paper / Code / Dataset / Blog buttons | Project page, paper placeholder, results, release boundary |
| Leaderboard | `README.md` leaderboard snapshot and `data/leaderboard-snapshot.csv` |
| Overview | `README.md` overview and case tuple |
| Real-world impact | Use "Key Findings" for now; avoid overclaiming deployment impact |
| Example trace | Use an example case shape until raw traces are sanitized |
| Citation | Placeholder until paper metadata is approved |
| Installation / evaluation | Defer until code and runner release boundary is approved |

## What Not To Copy Yet

- Do not publish raw traces as an "example trace" until redaction is complete.
- Do not publish the submitted PDF while the local copy says "Do not distribute".
- Do not expose provider, OAuth, remote runner, upload-center, or cloud execution details.

## Recommended Site Sections

1. Hero: benchmark name, tagline, one-paragraph summary, links.
2. Leaderboard: ranked stack table, metric definition, denominator.
3. Overview: case generation workflow and oracle.
4. Evidence-grounding patterns: five-pattern taxonomy.
5. Key findings: aggregate FPCR, stack spread, evidence-channel spread.
6. Example case: sanitized database migration gate or Atlas export routing.
7. Citation and contact: add after advisor approval.
