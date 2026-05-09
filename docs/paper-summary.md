# Paper Summary

Working title:

`When Agents Overtrust Environmental Evidence: An Extensible Agentic Framework for Benchmarking Evidence-Grounding Defects in LLM Agents`

## Short Description

EnvTrustBench evaluates whether LLM agents keep actions grounded in the true environment state when plausible files, logs, APIs, command outputs, web pages, or memory-like observations are stale, wrong, or adversarial.

## Core Claim

The benchmark targets evidence-grounding defects, not only prompt injection or harmful user requests. A run fails when the agent reaches a task-incorrect false path because it overtrusts environment-facing evidence.

## Current Evaluation

The current local evaluation instantiates 55 cases from 11 task scenarios and 5 evidence-grounding patterns. It evaluates 14 model-scaffold stacks over 3,850 accepted pass-or-fail runs. Agents avoided the false path in 644 runs and completed it in 3,206 runs.

## Public Wording To Prefer

- "environment-facing evidence"
- "evidence-grounding defect"
- "false-path completion rate"
- "machine-scoreable cases"
- "validation oracle under the true environment state"

## Public Wording To Avoid For Now

- Do not claim full reproducibility until raw traces and runner scripts are sanitized.
- Do not call hard variants official results unless they have clean model-behavior runs.
- Do not publish or link the submitted PDF until the advisor confirms it is allowed.

