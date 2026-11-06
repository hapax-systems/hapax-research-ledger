# hapax-research-ledger Agent Instructions

This repository is published by **Hapax Research Lab** under the `hapax-systems`
GitHub organization. Do not create, move, or point repository automation at any
personal user namespace or outside `hapax-systems`.

## Review Guidelines

External GitHub App reviewers such as CodeRabbit, Claude, and Codex are
advisory. Their comments can be useful input, but they are not authoritative
merge or release gates unless a governed Hapax Research Lab task explicitly
routes them into the review process.

- Keep Codecov and Semgrep advisory signal sources unless a governed task
  promotes a specific stable aggregate context.
- Preserve the `all-green` aggregate for branch protection and release tooling.
- Do not print or persist plaintext secrets; use the deployment secret store or
  GitHub Secrets.
- Treat `dv-ledger.ndjson` as append-only unless a governed task explicitly
  authorizes a correction.
- Validate `latest.json`, `dv-ledger.ndjson`, and `schema/` before marking a PR
  ready.
