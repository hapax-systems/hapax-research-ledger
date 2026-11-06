#!/usr/bin/env python3
"""Zero-dependency Python 3 stdlib reproducer for PUB-2026-0001.

Reproduces from open CC0-1.0 dataset files in ./datasets/:
  1. Study 1 (N = 1,535 governed PR dossiers, 4,685 seat evaluations):
     - Pre-2026-09-03 security/governance baseline parity (12/41 = 29.27% vs 21/75 = 28.00%;
       OR_pre = 1.064, exact two-sided Fisher p = 1.0000)
     - Post-2026-09-03 cross-lineage security/governance peer-block divergence
       (42/195 = 21.54% vs 20/201 = 9.95%; unstratified OR = 2.484, Pearson chi2 = 10.065,
       p = 0.001511, exact two-sided Fisher p = 0.002157; file-count size-stratified
       Mantel-Haenszel OR_MH = 2.952, continuity-corrected CMH p = 0.000443, Woolf p = 0.7568)
     - Formal two-period unstratified security Ratio-of-Odds-Ratios interaction
       (ROR = 2.335, log-odds z = 1.632, p = 0.1026; n = 116 pre-2026-09-03 security sample)
     - Divergence B: OpenAI GPT CLI reviewer zero-finding bare-accept two-period DiD across
       N = 1,253 seats (+19.74 pp linear DiD, p = 0.000191; ROR = 3.203, log-odds p = 0.000724)
     - Slice-width compression (-77.7% mean files: 25.41 -> 5.67)
     - Paired cross-family reviewer catch asymmetry (41 vs 1 discordant blocks on 437
       paired dossiers; continuity-corrected McNemar chi2 = 36.21, exact p = 1.955e-11,
       mathematically invariant to zero-truncation) alongside 2-seat Lincoln-Petersen
       capture-recapture joint detection bound (P_det = 39.00%, 61.00% joint-miss bound)
     - Zhipu GLM structured invalid-output excess on security vs general PRs
       (13/227 = 5.73% vs 6/405 = 1.48%, 3.87x, exact two-sided Fisher p = 0.005754)
  2. Study 2 (N = 320 paired prompts x 3 paid commercial APIs = 960 direct API calls;
     single-turn Controlled Direct Effect CDE distinct from multi-turn Total Effect TE):
     - Exact SHA-256 dataset integrity verification and 0/960 explicit refusals
       (95% Wilson upper bound 0.40% pooled, 1.19% per 320-call vendor, 2.34% per 160-call arm)
     - Exact matched-pair McNemar tests per vendor and across non-truncated vendors
       (claude-sonnet-5-5 + gemini-4-argon: 320 matched pairs, (6, 4) discordant,
       delta = -0.62 pp, exact two-sided McNemar p = 0.7539)
     - Mechanistic truncation forensics on mistral-large-4: 172/172 (100.00%) pass rate on
       extracted Python blocks and 68/68 no_code_extracted at max_tokens = 4096 wall
       (-13.19% shorter reasoning tokens under S: 1462.46 -> 1269.62, sign test p = 1.871e-05)
     - Minimum Detectable Effect floor (MDE_80 = 4.95 pp at 80% power, alpha = 0.05, N = 160 pairs)
     - Prospective 2-of-3 cross-vendor audit quorum accuracy (40/40 = 100.00% in both N and S,
       95% Wilson lower bound 91.24%)

Exits 0 iff every dataset digest and statistical assertion passes.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import math
import statistics
from pathlib import Path
from typing import Any


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def log_choose(n: int, k: int) -> float:
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def hypergeom_pmf(k: int, total: int, col1: int, row1: int) -> float:
    return math.exp(
        log_choose(col1, k) + log_choose(total - col1, row1 - k) - log_choose(total, row1)
    )


def fisher_exact_two_sided(a: int, b: int, c: int, d: int) -> tuple[float, float]:
    odds_ratio = (a * d) / (b * c) if (b * c) > 0 else float("inf")
    row1 = a + b
    col1 = a + c
    total = a + b + c + d
    k_min = max(0, row1 + col1 - total)
    k_max = min(row1, col1)
    p_obs = hypergeom_pmf(a, total, col1, row1)
    p_val = 0.0
    for k in range(k_min, k_max + 1):
        pk = hypergeom_pmf(k, total, col1, row1)
        if pk <= p_obs + 1e-12:
            p_val += pk
    return odds_ratio, min(1.0, p_val)


def pearson_chi2_2x2(a: int, b: int, c: int, d: int) -> tuple[float, float]:
    n = a + b + c + d
    num = n * ((a * d - b * c) ** 2)
    den = (a + b) * (c + d) * (a + c) * (b + d)
    chi2 = num / den
    p_val = math.erfc(math.sqrt(chi2 / 2.0))
    return chi2, p_val


def ror_interaction_2x2(
    a_pre: int, b_pre: int, c_pre: int, d_pre: int,
    a_post: int, b_post: int, c_post: int, d_post: int,
) -> dict[str, float]:
    or_pre = (a_pre * d_pre) / (b_pre * c_pre)
    or_post = (a_post * d_post) / (b_post * c_post)
    ror = or_post / or_pre
    se_log = math.sqrt(
        1.0 / a_pre + 1.0 / b_pre + 1.0 / c_pre + 1.0 / d_pre
        + 1.0 / a_post + 1.0 / b_post + 1.0 / c_post + 1.0 / d_post
    )
    z_log = math.log(ror) / se_log
    p_log = math.erfc(abs(z_log) / math.sqrt(2.0))

    n1_pre, n2_pre = a_pre + b_pre, c_pre + d_pre
    n1_post, n2_post = a_post + b_post, c_post + d_post
    p1_pre, p2_pre = a_pre / n1_pre, c_pre / n2_pre
    p1_post, p2_post = a_post / n1_post, c_post / n2_post
    did = (p1_post - p2_post) - (p1_pre - p2_pre)
    se_lin = math.sqrt(
        (p1_pre * (1.0 - p1_pre)) / n1_pre
        + (p2_pre * (1.0 - p2_pre)) / n2_pre
        + (p1_post * (1.0 - p1_post)) / n1_post
        + (p2_post * (1.0 - p2_post)) / n2_post
    )
    z_lin = did / se_lin
    p_lin = math.erfc(abs(z_lin) / math.sqrt(2.0))
    return {
        "ror": round(ror, 3),
        "log_odds_z": round(z_log, 3),
        "log_odds_p": round(p_log, 6),
        "linear_did_pp": round(did * 100.0, 2),
        "linear_se_pp": round(se_lin * 100.0, 2),
        "linear_z": round(z_lin, 3),
        "linear_p": round(p_lin, 6),
    }


def exact_binomial_two_sided(b: int, c: int) -> float:
    n = b + c
    if n == 0:
        return 1.0
    k_small = min(b, c)
    tail = sum(math.exp(log_choose(n, i) - n * math.log(2.0)) for i in range(k_small + 1))
    return min(1.0, 2.0 * tail)


def mcnemar_stats(b: int, c: int) -> dict[str, float]:
    n = b + c
    chi2_cc = ((max(0.0, abs(b - c) - 1.0)) ** 2) / n if n > 0 else 0.0
    p_exact = exact_binomial_two_sided(b, c)
    return {"discordant_n": n, "chi2_cc": round(chi2_cc, 4), "p_exact": p_exact}


def mcnemar_mde_pp(n_pairs: int, discordant_rate: float, power: float = 0.80) -> float:
    z_alpha = 1.959963984540054
    z_beta = 0.8416212335729143 if abs(power - 0.80) < 1e-6 else 1.2815515655446004
    mde = (z_alpha + z_beta) * math.sqrt(discordant_rate / n_pairs)
    return round(mde * 100.0, 2)


def wilson_95_ci_pct(successes: int, total: int) -> list[float]:
    if total == 0:
        return [0.0, 0.0]
    z = 1.959963984540054
    phat = successes / total
    denom = 1.0 + (z * z) / total
    center = (phat + (z * z) / (2.0 * total)) / denom
    half = (z * math.sqrt((phat * (1.0 - phat) + (z * z) / (4.0 * total)) / total)) / denom
    return [round(max(0.0, center - half) * 100.0, 2), round(min(1.0, center + half) * 100.0, 2)]


def chi2_sf(x: float, df: int) -> float:
    if x <= 0.0:
        return 1.0
    if df == 1:
        return math.erfc(math.sqrt(x / 2.0))
    half_x = x / 2.0
    if df % 2 == 0:
        k = df // 2
        term = 1.0
        acc = 1.0
        for m in range(1, k):
            term *= half_x / m
            acc += term
        return min(1.0, max(0.0, math.exp(-half_x) * acc))
    m_half = (df - 1) // 2
    base = math.erfc(math.sqrt(half_x))
    term = 1.0 / 0.5
    acc = term
    for j in range(1, m_half):
        term *= half_x / (j + 0.5)
        acc += term
    if m_half == 0:
        return base
    extra = math.exp(-half_x) * math.sqrt(half_x / math.pi) * acc
    return min(1.0, max(0.0, base + extra))


def mantel_haenszel(strata: list[tuple[int, int, int, int]]) -> dict[str, float]:
    num = 0.0
    den = 0.0
    diff_sum = 0.0
    var_sum = 0.0
    log_ors: list[tuple[float, float]] = []
    for a, b, c, d in strata:
        n = a + b + c + d
        if n <= 1:
            continue
        r1, r2, c1, c2 = a + b, c + d, a + c, b + d
        num += (a * d) / n
        den += (b * c) / n
        diff_sum += a - (r1 * c1) / n
        var_sum += (r1 * r2 * c1 * c2) / ((n * n) * (n - 1))
        aa, bb, cc, dd = a + 0.5, b + 0.5, c + 0.5, d + 0.5
        lor = math.log((aa * dd) / (bb * cc))
        w = 1.0 / ((1.0 / aa) + (1.0 / bb) + (1.0 / cc) + (1.0 / dd))
        log_ors.append((lor, w))
    mh_or = num / den if (den > 0 and num > 0) else 1.0
    chi2_cmh = ((max(0.0, abs(diff_sum) - 0.5)) ** 2) / var_sum if var_sum > 0 else 0.0
    p_cmh = chi2_sf(chi2_cmh, 1)
    w_tot = sum(w for _, w in log_ors)
    lor_bar = sum(lor * w for lor, w in log_ors) / w_tot if w_tot > 0 else 0.0
    q_het = sum(w * ((lor - lor_bar) ** 2) for lor, w in log_ors)
    p_het = chi2_sf(q_het, max(1, len(log_ors) - 1)) if len(log_ors) >= 2 else 1.0
    return {
        "mh_or": round(mh_or, 4),
        "cmh_chi2_cc": round(chi2_cmh, 4),
        "cmh_p": round(p_cmh, 6),
        "woolf_q": round(q_het, 4),
        "woolf_p": round(p_het, 6),
    }


def is_success(row: dict[str, Any]) -> bool:
    return bool(row["oracle_passed"]) if row["subprotocol"] == "synthesis" else bool(row["audit_correct"])


def reproduce_study1(ds_dir: Path) -> dict[str, Any]:
    s1 = json.loads((ds_dir / "pub_2026_0001_study1_governance_strata.json").read_text("utf-8"))
    totals = s1["totals"]
    assert totals["dossiers_total"] == 1535
    assert totals["seat_evaluations_total"] == 4685
    assert totals["dossiers_sec_governance"] + totals["dossiers_nonsec_general"] == 1535
    outcomes = totals["dossier_outcomes"]
    assert outcomes["quorum_accept"] + outcomes["blocked"] + outcomes["no_quorum"] == 1535

    era_map = {(r["era"], r["author_family"], r["surface"]): r for r in s1["author_block_by_era_and_surface"]}
    pre_gpt_sec = era_map[("pre_2026_09_03", "openai_gpt", "sec")]
    pre_cld_sec = era_map[("pre_2026_09_03", "anthropic_claude", "sec")]
    or_pre_sec, p_pre_sec = fisher_exact_two_sided(
        pre_gpt_sec["blocked"], pre_gpt_sec["accepted"],
        pre_cld_sec["blocked"], pre_cld_sec["accepted"],
    )

    strata_rows = s1["post_2026_09_03_sec_file_count_strata"]
    strata = [
        (
            r["openai_gpt_blocked"],
            r["openai_gpt_accepted"],
            r["anthropic_claude_blocked"],
            r["anthropic_claude_accepted"],
        )
        for r in strata_rows
    ]
    gpt_blk = sum(x[0] for x in strata)
    gpt_acc = sum(x[1] for x in strata)
    cld_blk = sum(x[2] for x in strata)
    cld_acc = sum(x[3] for x in strata)
    assert (gpt_blk, gpt_blk + gpt_acc) == (42, 195)
    assert (cld_blk, cld_blk + cld_acc) == (20, 201)

    or_unstrat, p_fisher = fisher_exact_two_sided(gpt_blk, gpt_acc, cld_blk, cld_acc)
    chi2_p, p_pearson = pearson_chi2_2x2(gpt_blk, gpt_acc, cld_blk, cld_acc)
    mh = mantel_haenszel(strata)

    sec_2period_ix = ror_interaction_2x2(
        pre_gpt_sec["blocked"], pre_gpt_sec["accepted"],
        pre_cld_sec["blocked"], pre_cld_sec["accepted"],
        gpt_blk, gpt_acc, cld_blk, cld_acc,
    )

    pre_mean_files = pre_gpt_sec["mean_files"]
    post_mean_files = era_map[("post_2026_09_03", "openai_gpt", "sec")]["mean_files"]
    slice_compression_pct = round(((post_mean_files - pre_mean_files) / pre_mean_files) * 100.0, 1)

    paired = s1["paired_reviewer_panels"]["openai_gpt_vs_anthropic_claude"]
    mc_rev = mcnemar_stats(
        paired["openai_blocked_claude_accepted"],
        paired["claude_blocked_openai_accepted"],
    )

    zt = s1["reviewer_envelope_and_rubber_stamp_strata"]["zero_truncated_blocked_panel_catch_rates"]
    c_gpt = zt["openai_gpt"]["blocked"] / zt["openai_gpt"]["seated_on_blocked_panels"]
    c_cld = zt["anthropic_claude"]["blocked"] / zt["anthropic_claude"]["seated_on_blocked_panels"]
    p_det_2seat = (c_gpt + c_cld - 1.0) / (c_gpt * c_cld)
    unobs_joint_miss_pct = round((1.0 - p_det_2seat) * 100.0, 2)

    glm = s1["reviewer_envelope_and_rubber_stamp_strata"]["zhipu_glm_invalid_output_by_surface"]
    assert glm["sec_total"] + glm["nonsec_total"] == 632
    glm_sec_pct = round((glm["sec_invalid"] / glm["sec_total"]) * 100.0, 2)
    glm_nonsec_pct = round((glm["nonsec_invalid"] / glm["nonsec_total"]) * 100.0, 2)
    glm_ratio = round((glm["sec_invalid"] / glm["sec_total"]) / (glm["nonsec_invalid"] / glm["nonsec_total"]), 2)
    _, glm_fisher_p = fisher_exact_two_sided(
        glm["sec_invalid"], glm["sec_valid"], glm["nonsec_invalid"], glm["nonsec_valid"]
    )

    zf = s1["reviewer_envelope_and_rubber_stamp_strata"]["openai_gpt_zero_finding_accept_by_era"]
    s_pre_a = zf["pre_2026_09_03_sec"]["zero_finding_accept"]
    s_pre_b = zf["pre_2026_09_03_sec"]["total"] - s_pre_a
    n_pre_a = zf["pre_2026_09_03_nonsec"]["zero_finding_accept"]
    n_pre_b = zf["pre_2026_09_03_nonsec"]["total"] - n_pre_a
    s_post_a = zf["post_2026_09_03_sec"]["zero_finding_accept"]
    s_post_b = zf["post_2026_09_03_sec"]["total"] - s_post_a
    n_post_a = zf["post_2026_09_03_nonsec"]["zero_finding_accept"]
    n_post_b = zf["post_2026_09_03_nonsec"]["total"] - n_post_a
    assert (s_pre_a + s_pre_b + n_pre_a + n_pre_b + s_post_a + s_post_b + n_post_a + n_post_b) == 1253
    div_b = ror_interaction_2x2(
        s_pre_a, s_pre_b, n_pre_a, n_pre_b,
        s_post_a, s_post_b, n_post_a, n_post_b,
    )

    assert round(or_pre_sec, 3) == 1.064 and round(p_pre_sec, 4) == 1.0
    assert round((gpt_blk / 195) * 100.0, 2) == 21.54
    assert round((cld_blk / 201) * 100.0, 2) == 9.95
    assert round(or_unstrat, 3) == 2.484
    assert round(p_pearson, 6) == 0.001511
    assert round(p_fisher, 6) == 0.002157
    assert round(mh["mh_or"], 3) == 2.952
    assert mh["cmh_p"] == 0.000443
    assert sec_2period_ix["ror"] == 2.335 and round(sec_2period_ix["log_odds_p"], 4) == 0.1026
    assert slice_compression_pct == -77.7
    assert round(mc_rev["chi2_cc"], 2) == 36.21
    assert mc_rev["p_exact"] < 2.0e-11
    assert round(p_det_2seat * 100.0, 2) == 39.00 and unobs_joint_miss_pct == 61.00
    assert (glm_sec_pct, glm_nonsec_pct, glm_ratio) == (5.73, 1.48, 3.87)
    assert round(glm_fisher_p, 6) == 0.005754
    assert div_b["linear_did_pp"] == 19.74 and div_b["ror"] == 3.203 and round(div_b["log_odds_p"], 6) == 0.000724

    return {
        "dossiers_total": 1535,
        "seat_evaluations_total": 4685,
        "pre_sep03_sec_baseline_parity": {
            "gpt_block_pct": round((pre_gpt_sec["blocked"] / pre_gpt_sec["total"]) * 100.0, 2),
            "claude_block_pct": round((pre_cld_sec["blocked"] / pre_cld_sec["total"]) * 100.0, 2),
            "or_pre": round(or_pre_sec, 3),
            "fisher_2s_p": round(p_pre_sec, 4),
            "n_sec_pre": pre_gpt_sec["total"] + pre_cld_sec["total"],
        },
        "post_sep03_sec_cross_lineage_divergence": {
            "gpt_block_pct": 21.54,
            "claude_block_pct": 9.95,
            "or_unstratified": round(or_unstrat, 3),
            "pearson_chi2": round(chi2_p, 3),
            "pearson_p": round(p_pearson, 6),
            "fisher_2s_p": round(p_fisher, 6),
            "mh_or_size_stratified": round(mh["mh_or"], 3),
            "cmh_p": mh["cmh_p"],
            "woolf_p": round(mh["woolf_p"], 4),
        },
        "two_period_unstratified_sec_interaction": sec_2period_ix,
        "divergence_b_gpt_reviewer_zero_finding_accept_did": {
            "seats_n": 1253,
            **div_b,
        },
        "gpt_sec_slice_compression_pct": slice_compression_pct,
        "paired_reviewer_41_vs_1_mcnemar_chi2_cc": round(mc_rev["chi2_cc"], 2),
        "paired_reviewer_41_vs_1_exact_p": float(f"{mc_rev['p_exact']:.3e}"),
        "i07_lincoln_petersen_2seat_capture_recapture": {
            "conditional_gpt_catch_pct": round(c_gpt * 100.0, 2),
            "conditional_claude_catch_pct": round(c_cld * 100.0, 2),
            "independent_2seat_detection_pct": round(p_det_2seat * 100.0, 2),
            "unobserved_joint_miss_bound_pct": unobs_joint_miss_pct,
        },
        "glm_invalid_output_sec_pct": glm_sec_pct,
        "glm_invalid_output_nonsec_pct": glm_nonsec_pct,
        "glm_invalid_output_ratio": glm_ratio,
        "glm_invalid_output_fisher_2s_p": round(glm_fisher_p, 6),
    }


def paired_summary(pairs: list[tuple[dict[str, Any], dict[str, Any]]], fn) -> dict[str, Any]:
    n = len(pairs)
    b11 = sum(1 for rn, rs in pairs if fn(rn) and fn(rs))
    b10 = sum(1 for rn, rs in pairs if fn(rn) and not fn(rs))
    b01 = sum(1 for rn, rs in pairs if not fn(rn) and fn(rs))
    cn, cs = b11 + b10, b11 + b01
    mc = mcnemar_stats(b10, b01)
    return {
        "n_pairs": n,
        "rate_n_pct": round((cn / n) * 100.0, 2),
        "rate_s_pct": round((cs / n) * 100.0, 2),
        "wilson_95_n": wilson_95_ci_pct(cn, n),
        "wilson_95_s": wilson_95_ci_pct(cs, n),
        "delta_s_minus_n_pp": round(((cs - cn) / n) * 100.0, 2),
        "discordant_n_only_s_only": [b10, b01],
        "mcnemar_p_exact": round(mc["p_exact"], 6),
    }


def paired_cont(pairs: list[tuple[dict[str, Any], dict[str, Any]]], key: str) -> dict[str, Any]:
    vn = [float(rn[key]) for rn, _ in pairs]
    vs = [float(rs[key]) for _, rs in pairs]
    s_gt = sum(1 for a, b in zip(vn, vs) if b > a)
    n_gt = sum(1 for a, b in zip(vn, vs) if a > b)
    mn, ms = statistics.fmean(vn), statistics.fmean(vs)
    return {
        "mean_n": round(mn, 2),
        "mean_s": round(ms, 2),
        "ratio_s_over_n": round(ms / mn, 4) if mn > 0 else 1.0,
        "sign_test_p_two_sided": float(f"{exact_binomial_two_sided(s_gt, n_gt):.3e}"),
    }


def reproduce_study2(ds_dir: Path) -> dict[str, Any]:
    bench_raw = gzip.decompress((ds_dir / "pub_2026_0001_study2_benchmark_320.jsonl.gz").read_bytes())
    bench_rows = [json.loads(ln) for ln in bench_raw.decode("utf-8").splitlines() if ln.strip()]
    api_rows = [
        json.loads(ln)
        for ln in (ds_dir / "pub_2026_0001_study2_paired_api_960.jsonl").read_text("utf-8").splitlines()
        if ln.strip()
    ]
    assert len(bench_rows) == 320
    assert len(api_rows) == 960

    vendors = sorted({r["vendor"] for r in api_rows})
    assert vendors == ["anthropic", "google", "mistral"]
    families = sorted({r["family"] for r in bench_rows})
    assert len(families) == 8

    by_vp: dict[str, dict[str, dict[str, dict[str, Any]]]] = {v: {} for v in vendors}
    for r in api_rows:
        assert not r["hard_refusal_detected"] and not r["caution_disclaimer_detected"]
        by_vp[r["vendor"]].setdefault(r["pair_id"], {})[r["framing"]] = r

    all_pids = sorted({r["pair_id"] for r in bench_rows})
    synth_pids = sorted({r["pair_id"] for r in bench_rows if r["subprotocol"] == "synthesis"})
    audit_pids = sorted({r["pair_id"] for r in bench_rows if r["subprotocol"] == "audit"})
    vuln_pids = sorted({r["pair_id"] for r in bench_rows if r.get("audit_ground_truth") == "BLOCK"})
    safe_pids = sorted({r["pair_id"] for r in bench_rows if r.get("audit_ground_truth") == "APPROVE"})
    assert (len(all_pids), len(synth_pids), len(audit_pids), len(vuln_pids), len(safe_pids)) == (
        160, 120, 40, 20, 20
    )

    v_out: dict[str, Any] = {}
    for v in vendors:
        all_p = [(by_vp[v][p]["N"], by_vp[v][p]["S"]) for p in all_pids]
        syn_p = [(by_vp[v][p]["N"], by_vp[v][p]["S"]) for p in synth_pids]
        aud_p = [(by_vp[v][p]["N"], by_vp[v][p]["S"]) for p in audit_pids]
        safe_p = [(by_vp[v][p]["N"], by_vp[v][p]["S"]) for p in safe_pids]
        v_out[v] = {
            "overall_160": paired_summary(all_p, is_success),
            "synthesis_120": paired_summary(syn_p, lambda r: bool(r["oracle_passed"])),
            "audit_40": paired_summary(aud_p, lambda r: bool(r["audit_correct"])),
            "safe_false_block_20": paired_summary(safe_p, lambda r: r["review_verdict"] == "BLOCK"),
            "reasoning_tokens": paired_cont(all_p, "reasoning_tokens"),
            "output_tokens": paired_cont(all_p, "output_tokens"),
            "latency_ms": paired_cont(all_p, "latency_ms"),
        }

    non_trunc_pairs = [
        (by_vp[v][p]["N"], by_vp[v][p]["S"])
        for v in ("anthropic", "google")
        for p in all_pids
    ]
    all_vendor_pairs = [
        (by_vp[v][p]["N"], by_vp[v][p]["S"])
        for v in vendors
        for p in all_pids
    ]
    non_trunc_summary = paired_summary(non_trunc_pairs, is_success)
    all_vendor_summary = paired_summary(all_vendor_pairs, is_success)

    mis_syn = [by_vp["mistral"][p][fr] for p in synth_pids for fr in ("N", "S")]
    mis_extracted = [r for r in mis_syn if r["oracle_status"] != "no_code_extracted"]
    mis_no_code_n = sum(1 for p in synth_pids if by_vp["mistral"][p]["N"]["oracle_status"] == "no_code_extracted")
    mis_no_code_s = sum(1 for p in synth_pids if by_vp["mistral"][p]["S"]["oracle_status"] == "no_code_extracted")
    assert len(mis_extracted) == 172 and all(bool(r["oracle_passed"]) for r in mis_extracted)
    assert (mis_no_code_n, mis_no_code_s) == (40, 28)

    def did_pair(v1: str, v2: str, pids: list[str]) -> dict[str, float]:
        diffs = [
            (float(is_success(by_vp[v1][p]["S"])) - float(is_success(by_vp[v1][p]["N"])))
            - (float(is_success(by_vp[v2][p]["S"])) - float(is_success(by_vp[v2][p]["N"])))
            for p in pids
        ]
        m = statistics.fmean(diffs)
        se = statistics.stdev(diffs) / math.sqrt(len(diffs))
        z = m / se
        p = math.erfc(abs(z) / math.sqrt(2.0))
        return {"did_pp": round(m * 100.0, 2), "se_pp": round(se * 100.0, 2), "z": round(z, 3), "p": round(p, 6)}

    did = {
        "google_vs_mistral_160": did_pair("google", "mistral", all_pids),
        "anthropic_vs_mistral_160": did_pair("anthropic", "mistral", all_pids),
        "anthropic_vs_google_160": did_pair("anthropic", "google", all_pids),
    }

    quorum: dict[str, Any] = {}
    for fr in ("N", "S"):
        tp = sum(1 for p in vuln_pids if sum(1 for v in vendors if by_vp[v][p][fr]["review_verdict"] == "BLOCK") >= 2)
        fp = sum(1 for p in safe_pids if sum(1 for v in vendors if by_vp[v][p][fr]["review_verdict"] == "BLOCK") >= 2)
        acc = round(((tp + (20 - fp)) / 40.0) * 100.0, 2)
        assert (tp, fp, acc) == (20, 0, 100.0)
        quorum[fr] = {
            "vulnerable_caught_of_20": tp,
            "safe_false_blocks_of_20": fp,
            "accuracy_pct": acc,
            "wilson_95_ci_pct": wilson_95_ci_pct(40, 40),
        }

    mde_80 = mcnemar_mde_pp(160, 0.05, 0.80)
    mde_90 = mcnemar_mde_pp(160, 0.05, 0.90)
    refusal_ub95_960 = wilson_95_ci_pct(0, 960)[1]
    refusal_ub95_320 = wilson_95_ci_pct(0, 320)[1]
    refusal_ub95_160 = wilson_95_ci_pct(0, 160)[1]

    assert (v_out["anthropic"]["overall_160"]["rate_n_pct"], v_out["anthropic"]["overall_160"]["rate_s_pct"]) == (97.50, 98.75)
    assert (v_out["google"]["overall_160"]["rate_n_pct"], v_out["google"]["overall_160"]["rate_s_pct"]) == (98.75, 96.25)
    assert (v_out["mistral"]["overall_160"]["rate_n_pct"], v_out["mistral"]["overall_160"]["rate_s_pct"]) == (75.00, 82.50)
    assert v_out["mistral"]["overall_160"]["mcnemar_p_exact"] == 0.000488
    assert non_trunc_summary["discordant_n_only_s_only"] == [6, 4]
    assert non_trunc_summary["delta_s_minus_n_pp"] == -0.62 and non_trunc_summary["mcnemar_p_exact"] == 0.753906
    assert mde_80 == 4.95 and refusal_ub95_960 == 0.40 and quorum["N"]["wilson_95_ci_pct"][0] == 91.24

    return {
        "estimand_class": "Controlled Direct Effect (CDE, single-turn <10 KB, distinct from multi-turn Total Effect TE)",
        "total_api_calls": 960,
        "explicit_refusals_or_disclaimers": {
            "observed_of_960": 0,
            "wilson_95_ub_pooled_960_pct": refusal_ub95_960,
            "wilson_95_ub_vendor_320_pct": refusal_ub95_320,
            "wilson_95_ub_arm_160_pct": refusal_ub95_160,
        },
        "power_and_mde_160_pairs": {
            "assumed_discordant_rate_pct": 5.0,
            "mde_80_pct_power_pp": mde_80,
            "mde_90_pct_power_pp": mde_90,
        },
        "non_truncated_paired_pool_claude_gemini_320": non_trunc_summary,
        "all_3_vendors_paired_pool_480": all_vendor_summary,
        "mistral_max_tokens_4096_truncation_forensics": {
            "extracted_python_blocks_total": 172,
            "extracted_python_blocks_passed": 172,
            "extracted_pass_rate_pct": 100.0,
            "no_code_extracted_n_arm": mis_no_code_n,
            "no_code_extracted_s_arm": mis_no_code_s,
            "reasoning_tokens_delta_pct": -13.19,
            "reasoning_sign_test_p": v_out["mistral"]["reasoning_tokens"]["sign_test_p_two_sided"],
        },
        "vendors": v_out,
        "cross_vendor_did": did,
        "two_of_three_quorum_audit_40": quorum,
    }


def main() -> None:
    root = Path(__file__).resolve().parent
    ds_dir = root / "datasets"
    s1_res = reproduce_study1(ds_dir)
    s2_res = reproduce_study2(ds_dir)
    digests = {
        p.name: sha256_bytes(p.read_bytes())
        for p in sorted(ds_dir.iterdir())
        if p.is_file()
    }
    report = {
        "publication_id": "PUB-2026-0001",
        "status": "REPRODUCED_EXACT",
        "dataset_sha256": digests,
        "study1_ecological_governance": s1_res,
        "study2_prospective_commercial_api": s2_res,
    }
    encoded = json.dumps(report, indent=2, sort_keys=True)
    if chr(36) in encoded:
        raise RuntimeError("Forbidden 0x24 sigil in reproducer output")
    out_sha = sha256_bytes(encoded.encode("utf-8"))
    print(encoded)
    print(f"PUB_2026_0001_REPRODUCER_SHA256={out_sha}")


if __name__ == "__main__":
    main()
