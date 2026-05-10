# EnvTrustBench Paper Basics

Working title:

`When Agents Overtrust Environmental Evidence: An Extensible Agentic Framework for Benchmarking Evidence-Grounding Defects in LLM Agents`

## Problem

LLM agents increasingly act through environment-facing scaffolds that expose files, web pages, APIs, command outputs, logs, package metadata, helper scripts, and memory-like state. These observations guide tool choice, recovery, state tracking, and action selection, but their reliability and authority cannot be assumed.

EnvTrustBench studies whether agents keep actions grounded in the true environment state when plausible observations are stale, wrong, non-authoritative, incomplete, or adversarial.

## Core Definition

An evidence-grounding defect is a behavioral failure where an agent treats environment-facing evidence as sufficient ground for action and follows a task-incorrect false path under the true environment state.

Each case specifies:

- the true environment state,
- the task objective,
- the correct path under that state,
- a false path,
- and a verification opportunity that can distinguish the two.

## Framework

EnvTrustBench is an extensible agentic framework. A benchmark author supplies a task scenario `s`, and the generator materializes:

| Component | Meaning |
|---|---|
| `W0` | trusted initial in-scope workspace state |
| `E0` | out-of-workspace environment state and evidence sources |
| `q` | agent-facing task objective |
| `Omega` | validation oracle |

The evaluated agent runs on `q`; EnvTrustBench records the action-observation trace, final state, and oracle verdict.

## Evidence-Grounding Patterns

| Abbrev. | Pattern | Decisive entry surface | Oracle focus |
|---|---|---|---|
| POP | Unsupported Persistent Observation | Stable external observation | Whether the agent accepts static or semi-static evidence as current authority. |
| RFM | Misleading Runtime Feedback | Feedback returned after an agent action | Whether misleading diagnostics, logs, APIs, command output, or tool feedback move the agent into the false path. |
| TSM | Invalid Temporal State | Time, schedule, lease, expiry, or delayed task state | Whether the agent misgrounds the current time window or scheduled state. |
| DMM | Stale Derived Memory | Retained memory, carryover state, or derived agent state | Whether stale retained or derived state is used as current truth. |
| EAM | Unverified Executable Artifact | Downloaded or imported executable artifact | Whether the agent adopts or executes an unapproved artifact because its metadata, self-description, or behavior presents it as the current path. |

## Current Public Evaluation

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

FPCR means false-path completion rate: the percentage of accepted pass-or-fail runs where the agent completed the task-incorrect false path under the true environment state. Lower is better.

## Public Release Boundary

This public summary intentionally excludes the submitted manuscript PDF, raw run directories, result packages, SQLite coordinator state, stdout/stderr logs, remote worker records, provider configuration, OAuth material, API keys, upload keys, machine inventory, cloud runner details, and experimental variants that are not part of the official denominator.
