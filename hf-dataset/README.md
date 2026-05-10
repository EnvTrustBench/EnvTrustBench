---
license: mit
language:
  - en
pretty_name: EnvTrustBench Aggregate Results
tags:
  - benchmark
  - llm-agents
  - agent-evaluation
  - robustness
  - evidence-grounding
  - tool-use
size_categories:
  - n<1K
configs:
  - config_name: table1_fpcr
    data_files:
      - split: table1_fpcr
        path: table1-final-fpcr.csv
  - config_name: leaderboard
    data_files:
      - split: leaderboard
        path: leaderboard-snapshot.csv
---

# EnvTrustBench Aggregate Results

EnvTrustBench evaluates whether LLM agents keep actions grounded in the true environment state when files, logs, APIs, command outputs, web pages, memory-like state, or executable artifacts are stale, wrong, or adversarial.

This Hugging Face dataset contains the public aggregate results for EnvTrustBench. It is intended as a lightweight public dataset entry for the project page and paper-facing release workflow.

## Contents

| File | Description |
|---|---|
| `table1-final-fpcr.csv` | Final aggregate FPCR matrix by scenario and model-scaffold stack. |
| `table1-final-fpcr.md` | Human-readable version of the final Table 1 aggregate data and validation counts. |
| `leaderboard-snapshot.csv` | Stack-level leaderboard snapshot ranked by false-path completion rate. |

## Benchmark Snapshot

| Item | Count |
|---|---:|
| Task scenarios | 11 |
| Evidence-grounding patterns | 5 |
| Machine-scoreable cases | 55 |
| Model-scaffold stacks | 14 |
| Accepted pass-or-fail runs | 3,850 |
| Pass runs | 644 |
| False-path runs | 3,206 |
| Aggregate FPCR / EMR | 83.3% |

## Metric

FPCR means false-path completion rate: the percentage of accepted pass-or-fail runs where the agent completed the task-incorrect false path under the true environment state. Lower is better.

## Release Boundary

This dataset intentionally excludes raw run directories, result packages, SQLite coordinator state, stdout/stderr logs, remote worker records, provider configuration, OAuth material, API keys, upload keys, machine inventory, cloud runner details, and the submitted manuscript PDF.

Project page: <https://envtrustbench.github.io/EnvTrustBench/>

Code and public docs: <https://github.com/EnvTrustBench/EnvTrustBench>
