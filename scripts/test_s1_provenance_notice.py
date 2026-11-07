"""Offline checks of the correction's scope and custody, not scientific validation."""

import hashlib
import json
import re
import subprocess
from functools import lru_cache
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
BASE = "fbef61945b7acb0c14a4635243e80e89b7a28feb"  # pragma: allowlist secret (public commit)
URL = "https://github.com/hapax-systems/hapax-research-ledger/blob/" + BASE + "/"
TREE_URL = URL.replace("/blob/", "/tree/")
NOTICE = "review-records/ERRATUM-20261106.md"
MANUSCRIPTS = [
    f"examinations/hieh-2026-000{i}/HIEH-2026-000{i}.md" for i in range(1, 5)
] + ["publications/pub-2026-0001/PUB-2026-0001.md"]
SIDECARS = [p.removesuffix(".md") + ".u12.json" for p in MANUSCRIPTS]
INDEXES = ["README.md", "review-records/README.md"]
HISTORY_START = "<!-- historical-review-narrative:start -->"
HISTORY_END = "<!-- historical-review-narrative:end -->"


@lru_cache
def original(path):
    return subprocess.check_output(
        ["git", "show", f"{BASE}:{path}"], cwd=ROOT, timeout=10
    )


def text(path):
    return (ROOT / path).read_text()


@pytest.mark.parametrize("path", MANUSCRIPTS)
def test_each_manuscript_has_visible_dated_qualification(path):
    opening = text(path).split("**Record ID:**", 1)[0]
    assert "2026-11-06" in opening and "UNVERIFIED" in opening
    assert "../../" + NOTICE in opening
    assert URL + path in opening


@pytest.mark.parametrize("path", MANUSCRIPTS)
def test_current_assurances_are_qualified(path):
    lines = text(path).splitlines()
    release = next(line for line in lines if line.startswith("**Release State:**"))
    review = next(line for line in lines if line.startswith("| **Review Provenance**"))
    assert "UNVERIFIED" in release and "under revision/review" in release
    assert "UNVERIFIED" in review and "retained labels" in review
    assert not re.search(r"(?:verification|review) complete", text(path), re.I)
    assert "**Independent Multi-Lineage Review**" not in text(path)


@pytest.mark.parametrize("path", SIDECARS)
def test_sidecar_assurance_fields_are_qualified(path):
    data = json.loads(text(path))
    assert "UNVERIFIED" in data["release_state"]
    assert "UNVERIFIED" in data["drbst_strip"]["R_orthogonal_review"]
    assert "UNVERIFIED" in data["drbst_strip"]["T_temporal_state"]
    assert data["dh3_privacy_receipt"]["status"] == "HISTORICAL_PASS_NOT_REVALIDATED"
    assert "../../" + NOTICE in data["drbst_strip"]["R_orthogonal_review"]
    if "subject_vendor_family_excluded" in data:
        assert data["subject_vendor_family_excluded"].startswith(
            "Historical policy assertion:"
        )


@pytest.mark.parametrize("path", SIDECARS)
def test_unrelated_sidecar_content_is_preserved(path):
    before, after = json.loads(original(path)), json.loads(text(path))
    for data in (before, after):
        del data["release_state"]
        del data["dh3_privacy_receipt"]["status"]
        del data["drbst_strip"]["R_orthogonal_review"]
        del data["drbst_strip"]["T_temporal_state"]
        data.pop("subject_vendor_family_excluded", None)
    assert before == after


@pytest.mark.parametrize("path", INDEXES)
def test_indexes_expose_current_notice_and_bound_history(path):
    current = text(path).split(HISTORY_START)[0]
    assert "ERRATUM-20261106.md" in current and "UNVERIFIED" in current
    if path == "review-records/README.md":
        history = text(path).split(HISTORY_START + "\n", 1)[1].split(HISTORY_END, 1)[0]
        assert history == original(path).decode()
        assert "Historical narrative" in current and "not current acceptance" in current


def test_erratum_distinguishes_labels_from_attestation_and_science():
    notice = text(NOTICE)
    for phrase in (
        "requested_model",
        "served_lineage",
        "UNVERIFIED",
        "endpoint-reported",
        "fallback",
        "does not establish substitution",
        "under revision/review",
        "No new review",
        "experiment",
        "exact-byte",
        "13 JSON",
        "54 unique response hashes",
    ):
        assert phrase in notice
    for path in MANUSCRIPTS + SIDECARS + ["review-records/README.md", "SHA256SUMS.txt"]:
        assert URL + path in notice


@pytest.mark.parametrize("path", MANUSCRIPTS + INDEXES + [NOTICE])
def test_correction_and_preimage_links_resolve_offline(path):
    links = re.findall(r"\]\(([^)]+)\)", text(path).split(HISTORY_START)[0])
    assert links, path
    for link in links:
        if link.startswith(URL):
            assert original(link.removeprefix(URL)), link
        elif link.startswith(TREE_URL):
            kind = subprocess.check_output(
                ["git", "cat-file", "-t", f"{BASE}:{link.removeprefix(TREE_URL)}"],
                cwd=ROOT,
                text=True,
                timeout=10,
            )
            assert kind.strip() == "tree", link
        elif not re.match(r"[a-z]+:", link):
            destination, _, fragment = link.partition("#")
            target = (ROOT / path).parent / destination
            assert target.is_file(), link
            if fragment:
                headings = re.findall(r"^#+ (.+)$", target.read_text(), re.M)
                assert fragment in {h.lower().replace(" ", "-") for h in headings}, link
        elif ("/blob/" in link or "/tree/" in link) and "hapax-research-ledger" in link:
            pytest.fail(f"Unpinned or wrong preimage link: {link}")


def test_retained_review_json_bytes_and_inventory_are_frozen():
    paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", BASE, "review-records/"],
        cwd=ROOT,
        text=True,
        timeout=10,
    ).splitlines()
    expected = {p for p in paths if p.endswith(".json")}
    assert len(expected) == 13
    assert {
        str(p.relative_to(ROOT)) for p in (ROOT / "review-records").glob("*.json")
    } == expected
    for path in sorted(expected):
        assert (ROOT / path).read_bytes() == original(path), path


def test_manifest_preserves_unrelated_entries_and_covers_changed_public_artifacts():
    def entries(value):
        return dict(line.split("  ", 1)[::-1] for line in value.splitlines())

    before = entries(original("SHA256SUMS.txt").decode())
    after = entries(text("SHA256SUMS.txt"))
    changed = set(MANUSCRIPTS + SIDECARS + INDEXES + [NOTICE])
    assert set(before) <= set(after)
    assert changed <= set(after)
    assert set(after) - set(before) <= changed
    for path, digest in after.items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
        if path not in changed:
            assert digest == before[path], path
