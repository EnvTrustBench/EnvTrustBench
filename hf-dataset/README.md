---
license: cc-by-nc-nd-4.0
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

This Hugging Face dataset contains the public paper-facing basics and aggregate results for EnvTrustBench. It is intended as the lightweight public dataset entry for the project page and paper-facing release workflow.

## Paper Basics

Working title:

`When Agents Overtrust Environmental Evidence: An Extensible Agentic Framework for Benchmarking Evidence-Grounding Defects in LLM Agents`

LLM agents increasingly act through environment-facing scaffolds that expose files, web pages, APIs, command outputs, logs, package metadata, helper scripts, and memory-like state. These observations guide tool choice, recovery, state tracking, and action selection, but their reliability and authority cannot be assumed.

EnvTrustBench studies evidence-grounding defects: behavioral failures where an agent treats environment-facing evidence as sufficient ground for action and follows a task-incorrect false path under the true environment state.

Given a task scenario `s`, EnvTrustBench materializes the generated benchmark case:

`Gen(s) = (W0, E0, q, Omega)`

| Component | Meaning |
|---|---|
| `W0` | trusted initial in-scope workspace state |
| `E0` | out-of-workspace environment state and evidence sources |
| `q` | agent-facing task objective |
| `Omega` | validation oracle |

The evaluated agent runs on `q`; EnvTrustBench records the action-observation trace, final state, and oracle verdict.

## Contents

| File | Description |
|---|---|
| `paper-basics.md` | Public summary of the paper problem, definition, framework, patterns, and release boundary. |
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

## Evidence-Grounding Patterns

| Abbrev. | Pattern | Decisive entry surface |
|---|---|---|
| POP | Unsupported Persistent Observation | Stable external observation |
| RFM | Misleading Runtime Feedback | Feedback returned after an agent action |
| TSM | Invalid Temporal State | Time, schedule, lease, expiry, or delayed task state |
| DMM | Stale Derived Memory | Retained memory, carryover state, or derived agent state |
| EAM | Unverified Executable Artifact | Downloaded or imported executable artifact |

## Release Boundary

This dataset intentionally excludes raw run directories, result packages, SQLite coordinator state, stdout/stderr logs, remote worker records, provider configuration, OAuth material, API keys, upload keys, machine inventory, cloud runner details, and the submitted manuscript PDF.

Project page: <https://envtrustbench.github.io/EnvTrustBench/>

Code and public docs: <https://github.com/EnvTrustBench/EnvTrustBench>
