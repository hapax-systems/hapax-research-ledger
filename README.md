<!-- hapax-sdlc:preamble:begin -->
<!-- hapax-public:surface=github.repo.hapax-research-ledger.readme.preamble:begin -->

# hapax-research-ledger

`hapax-research-ledger` is an evidence-artifact repository in the **Hapax Research Lab** portfolio ([hapaxresearch.com](https://hapaxresearch.com)). It publishes bounded observations and witness records, not runtime authority.

## Reader promise

Public numeric SCED evidence ledger and reproducible witness records published from the first data point with caveats preserved.

## Reader value

Lets skeptical readers audit early observations, caveats, nulls, scorer substitutions, and commitment witness checks directly as schema-validated data.

## Claim ceiling

Evidence, baseline observations, and witness records only; no adjudicated research result unless validity gates explicitly clear.

## License and rights

Public-domain dedication (CC0 1.0) for the declared ledger and witness data surface only; does not license Hapax Research Lab runtime code, Reins, or internal apparatus, and asserts no human copyright over machine-generated records.

Rendered summary: CC0 1.0 (public-domain dedication for the declared data/artifact surface). See `LICENSE`, `NOTICE.md`, `CITATION.cff`, and `.zenodo.json` for the authority surfaces.

## Public boundary

- Issues are redirect-only; no discussions, no pull requests accepted; see `CONTRIBUTING.md` and `SUPPORT.md`
- Published by **Hapax Research Lab** (`hrl-han`, [hapaxresearch.com](https://hapaxresearch.com)). Legal entity (as filed): Hapax Research LLC, organized in Wyoming on 2026-05-10, filing ID 2026-001973400.
- Security disclosures and factual correction proposals: `hrl-han@hapaxresearch.com` (see `SECURITY.md` and [hapaxresearch.com/about/#contact](https://hapaxresearch.com/about/#contact)). The network commits to receipt, retention and published correction. It promises no response time.
- Public copy uses `hapax-systems` organization links for first-party repositories; README text is orientation rather than a live runtime receipt.
- Governance reference: https://github.com/hapax-systems/hapax-constitution

## Portfolio position

Public-domain evidence and witness output for Hapax Research Lab research and citation. Carries observations and witness records, not reusable runtime mechanisms.

<!-- hapax-public:surface=github.repo.hapax-research-ledger.readme.preamble:end -->
<!-- hapax-sdlc:preamble:end -->

`hapax-research-ledger` is a public-domain numeric evidence ledger and
commitment witness archive for Hapax Research Lab's research program.

The ledger is deliberately narrow: append-only records, controlled
vocabularies, hashes, caveats, and schema validation. It publishes observations
early so baselines, nulls, substituted measurements, and validity blockers stay
visible instead of being cleaned up after the fact. That makes it useful to
skeptical readers precisely because it does not hide the weak or interim parts
of a measurement series.

## Claim Ceiling

These records are observations and dated witness snapshots, not adjudicated
research results. A public claim requires a bound measurement instrument,
validity gates, and current review evidence. Do not cite a row here as a stable
estimate or product claim unless the row and its surrounding metadata say that
claim has cleared.

## Current Series

The current series tracks a changing-criterion single-case experimental design
(SCED) measure from the Hapax Research Lab segment-preparation pipeline. The
headline field is `released_fraction`, the fraction of composed segments
admitted for release under the in-force criterion.

Important caveats:

- `status: dark-interim` means the observation is not an adjudicated claim.
- Small `n` values should be read as early baseline data, not stable estimates.
- `ruler_health.quarantined: true` means the pipeline quarantined canonical
  scorers and used backup measurements.
- Baseline zeroes are baseline facts, not negative findings.

## Files

| File | Purpose | Reader value |
|---|---|---|
| `dv-ledger.ndjson` | Append-only canonical observations. | Lets readers inspect the full sequence rather than only the latest point. |
| `latest.json` | Most recent observation, pretty-printed. | Gives dashboards and humans a compact current pointer without replacing the ledger. |
| `schema/sced-observation-v0.json` | JSON Schema for the record format. | Makes record shape, caveat fields, and validation expectations explicit. |
| `witnesses/` | Dated anonymous HTTP witness snapshots and commitment dispositions (`commitments-2026-11-06.json`). | Lets external auditors verify public commitment checks, response digests, and deadline-miss records independently. |
| `publications/pub-2026-0001/` | Launch Slate 1 governance monograph (`PUB-2026-0001`), `CC0-1.0` datasets, and stdlib reproducer. | Lets readers re-run all Study 1 (`N = 1,535`) and Study 2 (`N = 960`) statistical assertions from sanitized raw records. |
| `examinations/` | Launch Slate 1 `HIEH` public claim examinations (`HIEH-2026-0001..0004`), `1200x675` SVG plates, sidecars, and witness script. | Lets readers audit `Kategoria v2.0` outcome bounds, `25.00%` `OUTCOME_1` symmetry, and deterministic algebraic witnesses. |
| `di-01-records/` | Discourse-restraint and conflict-of-interest records (`DI-01-LAUNCH-SLATE-1`). | Documents read-only social posture, vendor conflict exclusions, and arrival-retention commitments. |
| `review-records/` | Two-round 3-family commercial API blind `P6` and adversarial review transcripts plus armed gate receipt. | Exposes Round-1 defect catches, Round-2 zero-critical/zero-major quorums, and conflict exclusions. |
| `SHA256SUMS.txt` | Content-addressed `SHA-256` manifest for all Launch Slate 1 files. | Lets external verifiers check exact byte integrity across mirrors. |

Every SCED observation in `dv-ledger.ndjson` is numeric, boolean, timestamp,
hash, or controlled enum. No free-text personal data belongs in this repository.

## License

CC0-1.0 public-domain dedication for the declared data and witness surface only,
with no human copyright claim asserted over machine-generated records. This does
not license Hapax Research Lab runtime code, Reins, or internal apparatus.

---

*HACA-C v0.3.15, the lab's draft rule for labelling machine-made text, not an external certification. No request to a natural person to approve the final wording, and no such approval, was found in hrl-han's sending, review and coordination records when the text was released. hrl-han releases a text once its checking is complete, under a standing rule that hrl-han's principal, who is not named in this text, adopted before the text was drafted. Review record: https://hapaxresearch.com/review-record/ (open to anyone). This label records how the text was made; it does not certify that the text is true. An unaltered record can contain false claims or miss relevant events.*


---

## Append-Only Correction and Withdrawal Notice — `HIEH-2026-0001..0004` (`2026-11-10T05:25:00Z`)

- **`HIEH-2026-0001..0004` are marked `not issued` (`S-HIEH-RBAC`):** Under Hapax Research Lab rule `S-HIEH-RBAC`, an `HIEH` examination is issued to the examined party and is never merely posted to a repository. None of [`HIEH-2026-0001`](examinations/hieh-2026-0001/HIEH-2026-0001.md), [`HIEH-2026-0002`](examinations/hieh-2026-0002/HIEH-2026-0002.md), [`HIEH-2026-0003`](examinations/hieh-2026-0003/HIEH-2026-0003.md), or [`HIEH-2026-0004`](examinations/hieh-2026-0004/HIEH-2026-0004.md) was ever sent or delivered to its examined party (`NOT SENT`; `responses_logged: []`). Each of the four records is marked **`not issued`**.
- **Withdrawn claims:** Across `HIEH-2026-0001..0004`, the `"vendor-excluded three-family commercial API review complete"` / `"Independent Multi-Lineage Review"` assurance (`served_lineage` in `review-records/` repeats `requested_model` without independent endpoint-response attestation), the `"automated mathematical/hygiene verification ... complete"` claim ([`review-records/gate-receipt-68f1a4ce9.json`](review-records/gate-receipt-68f1a4ce9.json) recorded `aggregate_decision: "hold"`, `codebase: "hold"`, and `lint: "hold"` at `2026-11-06T02:23:50Z`), and any claim that [`examinations/reproduce_hieh_witnesses.py`](examinations/reproduce_hieh_witnesses.py) verifies external primary documents or quotes beyond its hardcoded Python literals are **withdrawn**.
- **Corrected factual errors (with primary sources):**
  1. **`HIEH-2026-0001` wrong `arXiv` identifier (`arXiv:2611.00937`):** Withdrawn (`14` occurrences in `HIEH-2026-0001.md`). On arXiv ([https://arxiv.org/abs/2611.00937](https://arxiv.org/abs/2611.00937), dated `2026-10-31`), `arXiv:2611.00937` is an unrelated computer-vision paper (*"What Helps Denoising Can Hurt Memory: Rethinking History in Long Video Generation"*). The primary source for Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab (`2026-11-02`), *"Sparks of Weight-Space Programming"*, is the author-hosted research blog post at [https://rikiyat.github.io/blog/weight-space-programming/](https://rikiyat.github.io/blog/weight-space-programming/).
  2. **Wrong expansion of `hrl-han` (`"Hapax Autonomous Network"`):** Withdrawn across `HIEH-2026-0001..0004`. `hrl-han` stands for **Human-Agentic Network** under **Hapax Research Lab** (primary sources: [https://hapaxresearch.com/](https://hapaxresearch.com/) and [https://github.com/hapax-systems/hapax-constitution](https://github.com/hapax-systems/hapax-constitution)).
- **Preimage digests (`fbef61945b7acb0c14a4635243e80e89b7a28feb`, preserved in [`SHA256SUMS.txt`](SHA256SUMS.txt)) and correction latency:**
  - `examinations/hieh-2026-0001/HIEH-2026-0001.md`: `13,669` B, `sha256: b810c9d1d9e5523168231fec97845a2f8b01b0cddf676d505109a4918bc46271`
  - `examinations/hieh-2026-0002/HIEH-2026-0002.md`: `13,562` B, `sha256: c377c6e46d4a43f8b499710109bc077c0335b4dc2f190dba921c01d0c6110fa0`
  - `examinations/hieh-2026-0003/HIEH-2026-0003.md`: `14,045` B, `sha256: 5e587b6710916085824dea882ace911ebe1711669a32337775a7f2dfc6052ee8`
  - `examinations/hieh-2026-0004/HIEH-2026-0004.md`: `13,055` B, `sha256: 7302eb2587ab87691020bbfcafc1eee4e52fad8a8985bf6b66303be529dccf4e`
  - **Published:** `2026-11-06T02:27:28Z` · **Nonconformance detected (`20261108T231525Z`):** `2026-11-08T23:15:25Z` · **Corrected:** `2026-11-10T05:25:00Z` · **Latency:** `30 h 09 m 35 s` (`30.16 h`) from detection (`98 h 57 m 32 s` / `98.96 h` from publication).
  - **Zero new claims:** See [`examinations/NOT-ISSUED-AND-WITHDRAWAL-NOTICE-20261110.md`](examinations/NOT-ISSUED-AND-WITHDRAWAL-NOTICE-20261110.md).
