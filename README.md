# Hapax Research Ledger

An open, append-only ledger of **changing-criterion single-case experimental design (SCED)**
observations from the Hapax research program — published the moment data exists ("garage door up").

This ledger is machine-generated and governed: each line is emitted under the program's
Research Development LifeCycle (RDLC) and published through its publication bus. It is
**numeric-only by construction** — no free-text, no personal data.

## What is being measured

The current series is the **producer-side dependent variable** of `hapax-segment-prep`:
does the system compose broadcast segments that clear a *moving* coherence/composability
criterion `C_k`. The headline measure is `released_fraction` — the fraction of composed
segments admitted for release at the in-force criterion.

## Read this honestly

These are **early baseline observations, not results, and not claims.**

- `status: dark-interim` — no observation here is an adjudicated claim. Under the RDLC,
  a public *claim* requires a bound measurement instrument and validity gates that these
  observations do not yet have (`psi1_construct_validity: dark`, `not_assertable`).
- `n` is tiny (currently 2). Do not read any figure as a stable estimate.
- `mean_pre_gate` is a **substituted-ruler value**: on these observations the canonical
  scorers were quarantined and backups were substituted (`ruler_health.quarantined: true`).
  Treat the score accordingly — it is not a canonical-ruler measurement.
- `released_fraction = 0.0` at `criterion = 3.0` is an **A-phase baseline** (where the
  system cannot yet clear the bar), *not* a negative finding.
- `s2_composability` is a **separate, earlier** population (pre-coherence gate);
  S2-accepted is not the same as released.

The point of publishing this from the first data point is exactly to make the baseline,
the caveats, and the moving criterion visible as the work happens — including the nulls.

## Files

- `dv-ledger.ndjson` — append-only, one canonical observation per line.
- `latest.json` — the most recent observation, pretty-printed.
- `schema/sced-observation-v0.json` — JSON Schema for the record format (`sced-observation/v0`).

## Schema (`sced-observation/v0`)

A flat JSON object: `schema_version`, `observation_id`, `generated_at`, the measures
(`phases`, `s2_composability`, `axis_observations`), `ruler_health`, controlled-vocabulary
`caveats`, and a `provenance` block (method, RDLC stage, integrity `record_sha256`).
Every field is a number, boolean, or controlled enum — by design.

## License

Data released under **CC0-1.0** (public domain dedication). Reuse freely; a citation back
to this ledger is appreciated but not required.
