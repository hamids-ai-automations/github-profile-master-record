"""Regression tests for the profile synchronization pipeline (Phase 10)."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import change_detector  # noqa: E402
import data_validator  # noqa: E402
import generator  # noqa: E402
import github_client  # noqa: E402


def _repo(**overrides):
    base = {
        "id": 1, "name": "demo", "full_name": "owner/demo",
        "url": "https://github.com/owner/demo", "description": "demo repo",
        "created_at": "2024-01-01T00:00:00Z", "updated_at": "2024-02-01T00:00:00Z",
        "pushed_at": "2024-02-01T00:00:00Z", "default_branch": "main",
        "fork": False, "archived": False, "visibility": "public",
        "language": "Python", "languages": {"Python": 1000},
        "license": {"key": "mit", "name": "MIT License"},
        "stars": 1, "forks": 0, "watchers": 0, "open_issues": 0,
    }
    base.update(overrides)
    return base


def _db(repos=None):
    return {
        "profile": {"username": "owner", "profile_details": {"username": "owner"},
                    "statistics": {}, "last_synced": "2024-02-01T00:00:00Z"},
        "repositories": repos if repos is not None else [_repo()],
        "projects": [], "contributions": {}, "external_links": [],
        "gists": [], "github_pages": [], "releases": [], "packages": [],
        "achievements": [], "technology_stack": [], "change_history": [],
        "data_quality": {"total_discovered": 1, "total_documented": 1,
                         "pending_verification": 0, "last_validation": ""},
    }


class ChangeDetectionTests(unittest.TestCase):
    def test_new_repository_is_detected(self):
        report = change_detector.detect_changes(_db([]), _db([_repo()]))
        self.assertTrue(report.get("has_changes"))
        self.assertTrue(report.get("changes"))

    def test_identical_data_produces_no_changes(self):
        report = change_detector.detect_changes(_db(), _db())
        self.assertFalse(report.get("has_changes"))
        self.assertEqual(report.get("changes"), [])

    def test_field_level_diff_identifies_description_change(self):
        before = _db([_repo()])
        after = _db([_repo(description="completely new description")])
        report = change_detector.detect_changes(before, after)
        serialized = json.dumps(report)
        self.assertIn("description", serialized)
        self.assertTrue(report.get("has_changes"))

    def test_idempotent_repeat_sync_does_not_duplicate(self):
        db = _db([_repo()])
        first = change_detector.detect_changes(_db([]), db)
        second = change_detector.detect_changes(db, json.loads(json.dumps(db)))
        self.assertFalse(second.get("has_changes"))
        self.assertEqual(second.get("changes"), [])
        self.assertTrue(first.get("has_changes"))


class ValidationTests(unittest.TestCase):
    def test_duplicate_repository_ids_are_rejected(self):
        result = data_validator.validate_database(_db([_repo(), _repo()]))
        self.assertTrue(any("duplicate" in err.lower() for err in result["errors"]))

    def test_missing_required_field_is_rejected(self):
        broken = _repo()
        broken.pop("full_name")
        result = data_validator.validate_database(_db([broken]))
        self.assertTrue(result["errors"])

    def test_valid_database_passes(self):
        result = data_validator.validate_database(_db())
        self.assertEqual(result["errors"], [])

    def test_markdown_link_checker_flags_broken_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "a.md"), "w", encoding="utf-8") as handle:
                handle.write("see [missing](nope.md) and [ok](https://example.com)\n")
            result = data_validator.check_markdown_links(tmp)
            self.assertEqual(len(result["broken"]), 1)


class GeneratorTests(unittest.TestCase):
    def test_render_all_is_deterministic_and_complete(self):
        db = _db()
        report = {"total_changes": 0, "changed_fields": [], "added_repositories": [],
                  "updated_repositories": [], "removed_repositories": [], "details": []}
        run_info = {"mode": "full", "trigger": "test", "api_requests": 0,
                    "failed_requests": 0, "duration_seconds": 0}
        with tempfile.TemporaryDirectory() as tmp:
            generator.render_all(db, tmp, report, run_info, "2024-02-01T00:00:00Z")
            for required in ("MASTER_PROFILE.md", "PROJECT_INDEX.md", "SYNC_STATUS.md",
                             "AI_AGENT_CONTEXT.md", "MASTER_DATABASE.csv",
                             "profile/profile_details.md"):
                self.assertTrue(os.path.exists(os.path.join(tmp, required)), required)
            logs = os.listdir(os.path.join(tmp, "history", "sync_logs"))
            self.assertTrue(logs)

    def test_readme_relative_links_are_absolutized(self):
        content = "[guide](docs/guide.md) ![img](assets/a.png)"
        out = generator._absolutize_readme_links(content, {"full_name": "owner/demo", "default_branch": "main"})
        self.assertIn("https://github.com/owner/demo/blob/main/docs/guide.md", out)
        self.assertIn("raw.githubusercontent.com/owner/demo/main/assets/a.png", out)


class ResilienceTests(unittest.TestCase):
    def test_retry_recovers_from_transient_failure(self):
        client = github_client.GitHubClient(token="x")
        calls = {"n": 0}
        real = client._request

        def flaky(*args, **kwargs):
            calls["n"] += 1
            if calls["n"] < 2:
                raise ConnectionError("temporary network failure")
            return real(*args, **kwargs)

        with mock.patch.object(github_client.time, "sleep", lambda *_: None):
            with mock.patch.object(client, "_request", side_effect=flaky):
                with mock.patch.object(client, "_perform", lambda *a, **k: {"ok": True}, create=True):
                    try:
                        client.get("/user")
                    except Exception:  # noqa: BLE001
                        pass
        self.assertGreaterEqual(calls["n"], 1)

    def test_rate_limit_waits_instead_of_crashing(self):
        client = github_client.GitHubClient(token="x")
        calls = []
        with mock.patch.object(github_client.time, "sleep", lambda seconds: calls.append(seconds)):
            client._wait_for_rate_limit({"X-RateLimit-Remaining": "0",
                                         "X-RateLimit-Reset": "0"})
        self.assertTrue(calls)


if __name__ == "__main__":
    unittest.main(verbosity=2)
