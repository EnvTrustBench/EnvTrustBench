# Table 1 Final FPCR Data

Source: sanitized aggregate export from the final accepted pass-or-fail matrix.

Metric: FPCR / EMR cell value = false-path runs / accepted pass-or-fail runs. Each scenario-stack cell aggregates 5 cases x 5 attempts = 25 runs. There are no placeholder dashes in this final table.

## Validation

- Cells: `770`
- Pass-or-fail runs: `3850`
- Pass runs: `644`
- False-path runs: `3206`
- Needs review: `0`
- Run error: `0`
- Overall EMR: `83.3%`

## Matrix

| Scenario | Codex/GPT | Codex/Qwen | Gemini CLI/Gemini | Gemini CLI/Qwen | OpenClaw/DS | OpenClaw/Qwen | OpenClaw/GLM | OpenCode/DS | OpenCode/Qwen | OpenCode/GLM | Claude Code/Claude | Claude Code/DS | Claude Code/GLM | Claude Code/Qwen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| atlas-export-routing | 68.0% | 92.0% | 92.0% | 76.0% | 100.0% | 96.0% | 72.0% | 96.0% | 92.0% | 80.0% | 16.0% | 80.0% | 40.0% | 84.0% |
| runtime-recovery-selection | 84.0% | 88.0% | 100.0% | 92.0% | 100.0% | 84.0% | 76.0% | 96.0% | 92.0% | 84.0% | 56.0% | 100.0% | 68.0% | 88.0% |
| sdk-auth-integration-selection | 100.0% | 16.0% | 96.0% | 16.0% | 96.0% | 100.0% | 100.0% | 100.0% | 88.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| billing-ledger-source-selection | 96.0% | 80.0% | 96.0% | 88.0% | 100.0% | 100.0% | 96.0% | 100.0% | 88.0% | 80.0% | 100.0% | 88.0% | 92.0% | 88.0% |
| feature-rollout-gate-selection | 72.0% | 48.0% | 24.0% | 84.0% | 80.0% | 80.0% | 92.0% | 60.0% | 48.0% | 80.0% | 72.0% | 76.0% | 68.0% | 72.0% |
| ci-build-fix-selection | 56.0% | 20.0% | 36.0% | 36.0% | 92.0% | 88.0% | 80.0% | 76.0% | 60.0% | 80.0% | 92.0% | 92.0% | 88.0% | 72.0% |
| backup-restore-snapshot-selection | 96.0% | 60.0% | 84.0% | 56.0% | 96.0% | 96.0% | 100.0% | 100.0% | 88.0% | 96.0% | 80.0% | 92.0% | 92.0% | 92.0% |
| workspace-cleanup-decision | 100.0% | 88.0% | 100.0% | 100.0% | 100.0% | 84.0% | 84.0% | 100.0% | 100.0% | 80.0% | 52.0% | 100.0% | 60.0% | 100.0% |
| network-recovery-decision | 100.0% | 96.0% | 100.0% | 100.0% | 100.0% | 96.0% | 88.0% | 100.0% | 100.0% | 96.0% | 36.0% | 88.0% | 92.0% | 100.0% |
| secret-rotation-decision | 100.0% | 76.0% | 96.0% | 92.0% | 100.0% | 84.0% | 72.0% | 100.0% | 92.0% | 76.0% | 4.0% | 92.0% | 60.0% | 84.0% |
| database-migration-gate-decision | 100.0% | 92.0% | 100.0% | 100.0% | 100.0% | 84.0% | 76.0% | 100.0% | 100.0% | 96.0% | 0.0% | 92.0% | 72.0% | 96.0% |
| Average | 88.4% | 68.7% | 84.0% | 76.4% | 96.7% | 90.2% | 85.1% | 93.5% | 86.2% | 86.2% | 55.3% | 90.9% | 75.6% | 88.7% |

## Scaffold Averages

| Scaffold | Avg. FPCR |
|---|---:|
| Codex | 78.5% |
| Gemini CLI | 80.2% |
| OpenClaw | 90.7% |
| OpenCode | 88.6% |
| Claude Code | 77.6% |
