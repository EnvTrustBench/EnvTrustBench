# Project Page Outline

This is the CyberGym-style landing-page outline for `envtrustbench.org` or GitHub Pages.

## Hero

Title:

`EnvTrustBench`

Subtitle:

`Evaluating LLM agents' evidence-grounding robustness against misleading environmental observations.`

Summary:

`EnvTrustBench evaluates whether LLM agents keep actions grounded in the true environment state when files, logs, APIs, command outputs, web pages, memory-like state, or executable artifacts are stale, wrong, or adversarial.`

Buttons:

- Paper: pending approval
- Code: `https://github.com/EnvTrustBench/EnvTrustBench`
- Dataset: `https://huggingface.co/datasets/Str1ck/envtrustbench-results`
- Results: `data/table1-final-fpcr.md`
- Release boundary: `docs/release-boundary.md`

## Leaderboard

Columns:

- Rank
- Agent Scaffold
- Model
- Runs
- FPCR

Metric note:

`FPCR = false-path runs / accepted pass-or-fail runs. Lower is better.`

## Overview Figure

Suggested flow:

`Task Scenario -> Workspace + Environment -> Agent Objective -> Agent Execution -> Trace + Final State -> Oracle Verdict`

## Key Findings

- 3,206 of 3,850 accepted runs completed the false path.
- Stack-average FPCR ranges from 55.3% to 96.7%.
- Failures occur across multiple evidence channels, not only explicit prompt injection.

## Example Case

Use a sanitized database migration gate decision example first. It is compact and easy to explain without releasing raw traces.

## Citation

Leave as `Coming soon` until the public paper metadata is approved.
