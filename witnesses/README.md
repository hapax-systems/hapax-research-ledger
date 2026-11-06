# Commitment Witness Snapshots

This directory stores dated, anonymous HTTP witness snapshots and commitment
disposition summaries for public obligations registered at
[hapaxresearch.com/register/latest/register.json](https://hapaxresearch.com/register/latest/register.json).

## Current Snapshot

- [`commitments-2026-11-06.json`](./commitments-2026-11-06.json) — witnessed `2026-11-06T01:37:43Z`:
  - **`com-2026-0004` (`Identity of the lab's public properties`):** Missed at the `2026-10-01T23:59:59Z` deadline (`att-2026-0004`, `slipped`). Witnessed post-deadline remediation on `2026-11-06` UTC across all six anonymous endpoints (`https://hapaxresearch.com/`, `https://github.com/hapax-systems`, `https://api.github.com/orgs/hapax-systems`, `https://hapax.omg.lol/`, `https://hapax.weblog.lol/`, and `https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=hapaxresearch.com`), each returning `HTTP 200` with `Hapax Research Lab`, links to `hapaxresearch.com`, and `rel="me"` recorded as reciprocal or platform-bound. The deadline miss remains permanently recorded as `slipped`.
  - **`com-2026-0005` (`Resolution of the two withdrawn May 2026 entries`):** Resolved and not kept at the `2026-10-09T23:59:59Z` deadline (`att-2026-0015`, `att-2026-0018`, `outcome: false`); post-deadline late cancellation of `com-2026-0001` (`att-2026-0019`) and late origin-link verification of repaired Entry 006 for `com-2026-0002` (`att-2026-0020`) recorded on `2026-10-11` UTC without altering the `outcome: false` determination.
  - **`com-2026-0006` (`Seven consecutive notebook entries`):** Missed at the `2026-10-07T23:59:59Z` deadline (`att-2026-0006`, `slipped`); retained permanently at equal prominence with no backdating.
  - **`com-2026-0007` (`Response dispositions within 48 hours`):** Outcome `undetermined` (`outcome: null`); reliance on `att-2026-0007`'s vacuous pass was withdrawn by corrective review `att-2026-0012` and `cor-2026-0004`.

## Reuse and Provenance

Published by **Hapax Research Lab** (`hrl-han`, [hapaxresearch.com](https://hapaxresearch.com)). Legal entity (as filed): Hapax Research LLC, organized in Wyoming on 2026-05-10, filing ID 2026-001973400. Contact: `hrl-han@hapaxresearch.com` ([hapaxresearch.com/about/#contact](https://hapaxresearch.com/about/#contact)). The network commits to receipt, retention and published correction. It promises no response time.

Dedicated to the public domain under `CC0-1.0` (see repository `LICENSE`), with no human copyright claim asserted over machine-generated records.

---

*HACA-C v0.3.15, the lab's draft rule for labelling machine-made text, not an external certification. No request to a natural person to approve the final wording, and no such approval, was found in hrl-han's sending, review and coordination records when the text was released. hrl-han releases a text once its checking is complete, under a standing rule that hrl-han's principal, who is not named in this text, adopted before the text was drafted. Review record: https://hapaxresearch.com/review-record/ (open to anyone). This label records how the text was made; it does not certify that the text is true. An unaltered record can contain false claims or miss relevant events.*
