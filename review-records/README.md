# Launch Slate 1 — Independent Multi-Lineage Review & Gate Records (`2026-11-06`)

**Publisher:** `Hapax Research Lab` · `hrl-han` · `e-FORM` · `CC BY 4.0`  
**Legal Entity:** Legal entity (as filed): Hapax Research LLC, organized in Wyoming on 2026-05-10, filing ID 2026-001973400  
**Release State:** `◇ provisional`

## 1. Vendor-Excluded Commercial API Quorum Architecture

Every manuscript in Launch Slate 1 (`PUB-2026-0001`, `HIEH-2026-0001`, `HIEH-2026-0002`, `HIEH-2026-0003`, and `HIEH-2026-0004`) underwent two rounds of adversarial verification across **three independent commercial API model families**:

1. **`anthropic`:** `claude-sonnet-5-5`
2. **`google`:** `gemini-4-argon`
3. **`mistral`:** `mistral-large-4`

**Subject-Lineage Conflict Exclusion (`OpenAI` Excluded):** Because `PUB-2026-0001`, `HIEH-2026-0001`, and `HIEH-2026-0002` evaluate `OpenAI` model behavior or `OpenAI`-calibrated instruments and `HIEH-2026-0004` examines a corporate disclosure within the `Microsoft` / `OpenAI` corporate group, `OpenAI` models were strictly excluded (`0` adjudication calls across all rounds).

Each round executed `27` live paid commercial API calls (`54` total calls across Round 1 and Round 2):
- **Pass A (`12` calls per round: `4` `HIEH` records x `3` families):** Blind `P6` masked-outcome classification, where all `OUTCOME_1..OUTCOME_5` labels, verdict strings, and sidecar references were stripped from the manuscript before asking each independent family to classify the primary `Kategoria v2.0` outcome from the quantitative witnesses and scope bounds alone.
- **Pass B (`15` calls per round: `5` manuscripts x `3` families):** Full-manuscript biostatistical, algebraic, and privacy-hygiene adversarial audit (`reject` / `revise` / `accept-with-findings` / `accept`).

---

## 2. Two-Round Audit Trajectory & Substantive Remediations

### Round 1 (`2026-11-06T02:04:56Z` — `p6-hostile-review-summary-round1.json`)
- **Pass A Blind `P6` Convergence:** **`12 / 12` (`100%`, `3 / 3` independent families on all `4` `HIEH` examinations)** converged on the exact published `Kategoria v2.0` outcome sets on the first blind pass.
- **Pass B Adversarial Findings Caught & Remediated Before Publication:**
  1. **`HIEH-2026-0004` Scenario C Arithmetic Fix:** Corrected Scenario C rounded classified-share change for `0.0495 -> 0.0334` from `-30.91%` to **`-32.53%`** (alongside exact `-40.00%` witness at `TPR_1 = 33.83%`) in `HIEH-2026-0004.md`, `reproduce_hieh_witnesses.py`, and `plates/HIEH-2026-0004.svg`, and raised the positive-stratum oversampling target to `n_pos >= 400` (`95%` Wilson half-width `<= +-5.0 pp` across `[0, 1]`).
  2. **`PUB-2026-0001` Subprotocol Accounting & Paired-Delta Reconciliation:** Explicitly partitioned Study 2's `160` matched prompt pairs (`320` prompts per family) into `120` code-synthesis pairs (`240` calls; `172` passed + `68` `no_code_extracted` on `mistral-large-4` at `max_tokens = 4096`) and `40` diff-audit pairs (`80` calls: `20` `F7` subtle-bug + `20` `F8` clean-refactor pairs; `80 / 80` passed on `mistral-large-4`, totaling `172 + 80 = 252 / 320`), and distinguished OpenAI's overall `-5.90 pp` paired delta from the `10.3%` vs. `15.8%` task-subset rates.
  3. **`HIEH-2026-0002` False-Alarm Ratio Precision:** Corrected the `p = 0.25%`, `TPR = 80%`, `FPR = 8%` false-alarm-per-true-catch ratio from `39.98` to exact **`39.90`** (`0.0798 / 0.0020`).
  4. **Zero Unexpanded House Codes:** Expanded or replaced internal taxonomy shorthands (`U12`, `P6`, `D-H3`, `C9`, `DRBST`) on first use across all five outward manuscripts so external readers need zero internal documentation.

### Round 2 (`2026-11-06T02:22:10Z` — `p6-hostile-review-summary-round2.json`)
- **Pass A Blind `P6` Convergence:** **`12 / 12` (`100%`, `3 / 3` families on all `4` `HIEH` records)**.
- **Pass B Manuscript Quorums:** **`5 / 5` `quorum-accept` (`15 / 15` seats returning `accept` or `accept-with-findings`, `0` `critical` findings, `0` `major` findings across all five manuscripts)**.

| Manuscript | Artifact `SHA-256` | `anthropic` (`claude-sonnet-5-5`) | `google` (`gemini-4-argon`) | `mistral` (`mistral-large-4`) | Critical / Major | Quorum Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `PUB-2026-0001.md` | `af83c03dda62b643...` | `accept-with-findings` | `accept` | `accept` | `0 / 0` | **`quorum-accept`** |
| `HIEH-2026-0001.md` | `b810c9d1d9e55231...` | `accept-with-findings` | `accept` | `accept` | `0 / 0` | **`quorum-accept`** |
| `HIEH-2026-0002.md` | `c377c6e46d4a43f8...` | `accept-with-findings` | `accept` | `accept` | `0 / 0` | **`quorum-accept`** |
| `HIEH-2026-0003.md` | `5e587b6710916085...` | `accept-with-findings` | `accept` | `accept` | `0 / 0` | **`quorum-accept`** |
| `HIEH-2026-0004.md` | `7302eb2587ab8769...` | `accept` | `accept` | `accept` | `0 / 0` | **`quorum-accept`** |

---

## 3. Armed `PublicationHardeningGate` Receipt (`gate-receipt-68f1a4ce9.json`)

All five final manuscripts were evaluated through `PublicationHardeningGate` (`68f1a4ce9`) with `operator_name_guard_armed: true`, `signed_review_evidence` bound to Round-2 `quorum-accept`, and `hieh_bundle` readiness checks enabled:
- `zero_reject_children_all_documents: true`
- `zero_lint_errors_all_documents: true`
- `artifact_envelope: pass`, `known_entities: pass`, `legal_name: pass`, `review: pass` across all records (remaining `hold` flags on `lint` and `codebase` reflect advisory prose style warnings and external non-repository code identifiers, with `0` `error`-severity lint findings and `0` `reject` children).

---

## 4. Directory Contents

- `gate-receipt-68f1a4ce9.json` — Armed `PublicationHardeningGate` receipt over exact final manuscript `SHA-256` digests.
- `p6-hostile-review-summary-round1.json` & `*-review-round1.json` — Complete Round-1 `P6` + adversarial seat transcripts (`27` calls).
- `p6-hostile-review-summary-round2.json` & `*-review-round2.json` — Complete Round-2 `P6` + adversarial seat transcripts (`27` calls, `0` critical / `0` major).
