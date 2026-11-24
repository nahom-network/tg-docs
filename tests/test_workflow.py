from pathlib import Path
import re
import unittest


WORKFLOW = Path(".github/workflows/docs.yml")


class WorkflowTests(unittest.TestCase):
    def test_checkout_uses_triggering_ref_instead_of_a_pinned_branch(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("- uses: actions/checkout@v4", text)
        self.assertNotIn("ref: ${{ github.event.repository.default_branch }}", text)
        self.assertNotRegex(text, re.compile(r"^\s*ref:\s*(main|master)\s*$", re.MULTILINE))

    def test_commit_pushes_to_the_branch_that_triggered_the_run(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn('git push origin "HEAD:${GITHUB_REF_NAME}"', text)
        self.assertNotIn("HEAD:${{ github.event.repository.default_branch }}", text)

    def test_push_trigger_covers_both_common_default_branches(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("branches: [main, master]", text)

    def test_workflow_publishes_site_to_the_branch_root(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("python update_docs.py", text)
        self.assertIn("python build_site.py --output .", text)
        self.assertIn("python build_site.py --output _site", text)
        self.assertIn("sections external serverless llms.txt llms-full.txt", text)
        self.assertIn("git push origin \"HEAD:${GITHUB_REF_NAME}\"", text)

    def test_workflow_skips_its_own_generated_commit(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn(
            "github.event.head_commit.author.username != 'github-actions[bot]'", text)


if __name__ == "__main__":
    unittest.main()
