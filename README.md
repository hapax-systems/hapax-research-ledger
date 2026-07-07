<!-- hapax-sdlc:preamble:begin -->

# hapax-research-ledger

`hapax-research-ledger` is an evidence-artifact repository in the Hapax Systems portfolio. It publishes bounded observations or metadata, not runtime authority.

## Reader promise

Public numeric-only SCED evidence ledger published from the first data point with caveats preserved.

## Claim ceiling

Evidence/baseline data only; no adjudicated research result unless validity gates explicitly clear.

## License and rights

Public-domain data posture for the ledger only; does not license Hapax runtime code, Reins, or council internals.

Rendered summary: CC0 1.0 (public-domain dedication for the declared data/artifact surface). See `LICENSE` for the authority surfaces.

## Public boundary

- Issues are redirect-only; no discussions, no pull requests accepted; see `CONTRIBUTING.md` and `SUPPORT.md`
- Public copy must use `hapax-systems` organization links for first-party Hapax repositories.
- Publication, weblog, RSS, social, DOI/archive, and other public fanout paths must route through the governed publication bus or a documented guarded legacy surface.
- Governance reference: https://github.com/hapax-systems/hapax-constitution

## Portfolio position

Evidence/artifact output for public research and citation. Carries observations, not reusable runtime mechanisms.

<!-- hapax-sdlc:preamble:end -->

# hapax-research-ledger

`hapax-research-ledger` is a public-domain numeric evidence ledger for the
Hapax research program.

The ledger is deliberately narrow: append-only records, controlled
vocabularies, hashes, caveats, and schema validation. It publishes observations
early so baselines, nulls, substituted measurements, and validity blockers stay
visible instead of being cleaned up after the fact.

## Claim Ceiling

These records are observations, not adjudicated research results. A public
claim requires a bound measurement instrument, validity gates, and current
review evidence. Do not cite a row here as a stable estimate or product claim
unless the row and its surrounding metadata say that claim has cleared.

## Current Series

The current series tracks a changing-criterion single-case experimental design
(SCED) measure from the Hapax segment-preparation pipeline. The headline field
is `released_fraction`, the fraction of composed segments admitted for release
under the in-force criterion.

Important caveats:

- `status: dark-interim` means the observation is not an adjudicated claim.
- Small `n` values should be read as early baseline data, not stable estimates.
- `ruler_health.quarantined: true` means the pipeline quarantined canonical
  scorers and used backup measurements.
- Baseline zeroes are baseline facts, not negative findings.

## Files

| File | Purpose |
|---|---|
| `dv-ledger.ndjson` | Append-only canonical observations. |
| `latest.json` | Most recent observation, pretty-printed. |
| `schema/sced-observation-v0.json` | JSON Schema for the record format. |

Every public record is numeric, boolean, timestamp, hash, or controlled enum.
No free-text personal data belongs in this ledger.

## License

CC0-1.0 public-domain dedication for the declared data surface only. This does
not license Hapax runtime code, Reins, or council internals.
