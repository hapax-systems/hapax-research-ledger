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

## Corrections

**2026-11-06 — Launch Slate 1:** Named-model review assurance is **UNVERIFIED**; the five substantive findings remain under revision/review. Read the [canonical provenance erratum](review-records/ERRATUM-20261106.md) before relying on the historical review or release-state claims. No new review or scientific validation is claimed.

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
| `review-records/` | Historical review transcripts, gate receipt, and dated provenance erratum. | Preserves reported findings; named-model assurance is UNVERIFIED and old quorum labels are not current acceptance. |
| `SHA256SUMS.txt` | Content-addressed `SHA-256` manifest for all Launch Slate 1 files. | Lets external verifiers check exact byte integrity across mirrors. |

Every SCED observation in `dv-ledger.ndjson` is numeric, boolean, timestamp,
hash, or controlled enum. No free-text personal data belongs in this repository.

## License

CC0-1.0 public-domain dedication for the declared data and witness surface only,
with no human copyright claim asserted over machine-generated records. This does
not license Hapax Research Lab runtime code, Reins, or internal apparatus.

---

*HACA-C v0.3.15, the lab's draft rule for labelling machine-made text, not an external certification. No request to a natural person to approve the final wording, and no such approval, was found in hrl-han's sending, review and coordination records when the text was released. hrl-han releases a text once its checking is complete, under a standing rule that hrl-han's principal, who is not named in this text, adopted before the text was drafted. Review record: https://hapaxresearch.com/review-record/ (open to anyone). This label records how the text was made; it does not certify that the text is true. An unaltered record can contain false claims or miss relevant events.*
