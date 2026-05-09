# Release Boundary

This draft is intended for a public GitHub project page, not a complete reproducibility archive.

## Include Now

- Public-facing project README.
- Aggregate benchmark counts and final Table 1 matrix.
- High-level benchmark construction explanation.
- Sanitized docs derived from manuscript text.

## Hold Back Until Review

- Submitted manuscript PDF, because the local PDF says "Submitted to 40th Conference on Neural Information Processing Systems (NeurIPS 2026). Do not distribute."
- Raw run directories, result packages, `.zip` archives, SQLite coordinator state, stdout/stderr logs, remote worker records, and upload-center pulls.
- Provider configuration, OAuth material, API keys, upload keys, machine inventory, and cloud runner details.
- Experimental hard variants or failed reruns that are not part of the official denominator.

## Recommended Public Repo Name

Use `EnvTrustBench/EnvTrustBench` for the primary project repository. It gives the clean URL:

`https://github.com/EnvTrustBench/EnvTrustBench`

If the team wants package-style naming later, create a second repository named `envtrustbench`.

