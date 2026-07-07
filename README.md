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
- `ruler_health.quarantined: true` means canonical scorers were quarantined and
  backup measurements were substituted.
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
