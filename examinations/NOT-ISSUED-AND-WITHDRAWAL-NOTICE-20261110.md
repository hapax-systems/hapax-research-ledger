# Append-Only Correction and Withdrawal Notice: `HIEH-2026-0001..0004` (`2026-11-10T05:25:00Z`)

- **Repository:** `hapax-systems/hapax-research-ledger`
- **Governed Correction Row:** `hieh-0001-0004-append-only-withdrawal-and-not-issued-notice-20261109`
- **Preimage Commit:** `fbef61945b7acb0c14a4635243e80e89b7a28feb` (`2026-11-06T02:27:28Z`)
- **Nonconformance Detection Timestamp:** `2026-11-08T23:15:25Z` (`20261108T231525Z` determination record)
- **Correction Timestamp:** `2026-11-10T05:25:00Z`
- **Correction Latency:** `30 h 09 m 35 s` (`30.16 h`) from the `2026-11-08T23:15:25Z` nonconformance determination (`98 h 57 m 32 s` / `98.96 h` from the `2026-11-06T02:27:28Z` commit `fbef61945b7acb0c14a4635243e80e89b7a28feb`)

---

## 1. `HIEH-2026-0001..0004` Marked `not issued` (`S-HIEH-RBAC`)

Under Hapax Research Lab rule `S-HIEH-RBAC`, an `HIEH` examination is an addressed communication issued to the examined party and is never merely posted to a repository. None of `HIEH-2026-0001`, `HIEH-2026-0002`, `HIEH-2026-0003`, or `HIEH-2026-0004` was ever sent or delivered to its examined party (`NOT SENT`; `responses_logged: []`).

Each of the four records is therefore marked **`not issued`**:

| Record ID | Path | Preimage Bytes | Preimage `SHA-256` (`fbef61945b7a…`) | Disposition |
|---|---|---:|---|---|
| `HIEH-2026-0001` | [`examinations/hieh-2026-0001/HIEH-2026-0001.md`](hieh-2026-0001/HIEH-2026-0001.md) | `13,669` | `b810c9d1d9e5523168231fec97845a2f8b01b0cddf676d505109a4918bc46271` | **`not issued`** (append-only notice added; prior lines unedited) |
| `HIEH-2026-0002` | [`examinations/hieh-2026-0002/HIEH-2026-0002.md`](hieh-2026-0002/HIEH-2026-0002.md) | `13,562` | `c377c6e46d4a43f8b499710109bc077c0335b4dc2f190dba921c01d0c6110fa0` | **`not issued`** (append-only notice added; prior lines unedited) |
| `HIEH-2026-0003` | [`examinations/hieh-2026-0003/HIEH-2026-0003.md`](hieh-2026-0003/HIEH-2026-0003.md) | `14,045` | `5e587b6710916085824dea882ace911ebe1711669a32337775a7f2dfc6052ee8` | **`not issued`** (append-only notice added; prior lines unedited) |
| `HIEH-2026-0004` | [`examinations/hieh-2026-0004/HIEH-2026-0004.md`](hieh-2026-0004/HIEH-2026-0004.md) | `13,055` | `7302eb2587ab87691020bbfcafc1eee4e52fad8a8985bf6b66303be529dccf4e` | **`not issued`** (append-only notice added; prior lines unedited) |

---

## 2. Withdrawn Unverified Claims

1. **Three-family commercial API review completion (`HIEH-2026-0001..0004`):** The claim that `"vendor-excluded three-family commercial API review complete"` / `"Independent Multi-Lineage Review"` was verified is **withdrawn**. The retained review records in [`review-records/`](../review-records/) (`hieh-2026-0001-review-round1.json` through `hieh-2026-0004-review-round2.json`) record requested model strings (`anthropic/claude-sonnet-5-5`, `google/gemini-4-argon`, `mistral/mistral-large-4`) where `served_lineage` repeats `requested_model` without independent endpoint-response attestation.
2. **Automated mathematical/hygiene gate completion (`HIEH-2026-0001..0004`):** The claim that `"automated mathematical/hygiene verification ... complete"` cleared release gates is **withdrawn**. The committed gate receipt [`review-records/gate-receipt-68f1a4ce9.json`](../review-records/gate-receipt-68f1a4ce9.json) (`sha256: acb20b5330e7f7644b174e1c2389767a8c63bcf9f0011392d53609f04086c391`) recorded `aggregate_decision: "hold"`, `codebase: "hold"`, and `lint: "hold"` on all five Launch Slate 1 records at `2026-11-06T02:23:50Z`.
3. **Witness script verification scope (`HIEH-2026-0001..0004`):** [`examinations/reproduce_hieh_witnesses.py`](reproduce_hieh_witnesses.py) evaluates arithmetic and `SHA-256` digests over hardcoded Python constants within the script itself and reads no external primary documents; any claim that it verifies external primary files or external verbatim quotes is **withdrawn**.
4. **Additional record-specific withdrawals:**
   - On `HIEH-2026-0001`: the `1,572.5x` cross-architecture scale ratio comparison, the `25,600` forward-pass token evaluation count (the source states a budget of `50` passes and batches of up to `512` problems, which is a ceiling rather than an observed count), and the `Exp 8b` unpaired `34/500` vs `35/500` comparison as a matched control are **withdrawn**.
   - On `HIEH-2026-0002` and `HIEH-2026-0004`: no primary source URL or archived capture is linked in the record, and the `15`-word quote `SHA-256` in `HIEH-2026-0004` (`52f5578f4d2a29ebdbd2443284fcb44ccde3e1c1bb3be2f83968976f2602ba65`) is computed from a hardcoded string literal in `reproduce_hieh_witnesses.py`.

---

## 3. Factual Corrections and Primary-Source Citations

1. **Wrong `arXiv` identifier in `HIEH-2026-0001` (`arXiv:2611.00937`):**
   - **Withdrawn error:** `HIEH-2026-0001.md` (`14` occurrences), `HIEH-2026-0001.u12.json`, and `reproduce_hieh_witnesses.py` cite `Takehi et al., arXiv:2611.00937`.
   - **Primary source for `arXiv:2611.00937`:** On arXiv ([https://arxiv.org/abs/2611.00937](https://arxiv.org/abs/2611.00937), dated `2026-10-31`), `arXiv:2611.00937` is an unrelated computer-vision paper titled *"What Helps Denoising Can Hurt Memory: Rethinking History in Long Video Generation"*.
   - **Primary source for Takehi et al. (`2026-11-02`):** Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab, *"Sparks of Weight-Space Programming"* (`2026-11-02`), was published as an author-hosted research blog post at [https://rikiyat.github.io/blog/weight-space-programming/](https://rikiyat.github.io/blog/weight-space-programming/).
2. **Wrong expansion of `hrl-han` (`"Hapax Autonomous Network"`):**
   - **Withdrawn error:** `HIEH-2026-0001..0004` expand `hrl-han` as `"Hapax Autonomous Network"` (and `"autonomous research network"` in `HIEH-2026-0004`).
   - **Primary source for `hrl-han`:** `hrl-han` stands for **Human-Agentic Network** under **Hapax Research Lab** (primary sources: [https://hapaxresearch.com/](https://hapaxresearch.com/) and [https://github.com/hapax-systems/hapax-constitution](https://github.com/hapax-systems/hapax-constitution)).

---

## 4. Zero New Claims

This notice is strictly a withdrawal and factual correction record. It edits no prior line in any existing file and asserts no new scientific, empirical, or capability claims.
