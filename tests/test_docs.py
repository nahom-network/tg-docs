import json
from pathlib import Path
import re
import tempfile
import unittest

import build_llms
import build_site
import update_docs


def sample_html(extra=""):
    entries = "".join(f"<h4>Type{i}</h4><p>A type.</p>" for i in range(100))
    return ('<nav>Not documentation</nav><div id="dev_page_content">'
            '<h3><a class="anchor" name="recent-changes"></a>Recent changes</h3>'
            '<h4>October 1, 2026</h4><p><strong>Bot API 10.3</strong></p>'
            '<h3>Available methods</h3><h4>sendMessage</h4>'
            '<p>Returns <a href="#user">User</a>.</p>'
            '<table><thead><tr><th>Field</th><th>Type</th></tr></thead>'
            '<tbody><tr><td>text</td><td>String</td></tr></tbody></table>'
            '<h4>User</h4><p>A user.</p><h4>getUpdates</h4><p>Updates.</p>'
            + entries + extra + '<h3>Games</h3><p>Games API.</p></div><footer>Footer</footer>')


class ConversionTests(unittest.TestCase):
    def test_conversion_preserves_tables_links_and_fences(self):
        html = sample_html('<h4>Formatting</h4><pre><code class="language-markdown">'
                           '```python\nprint(1)\n```\n# Example heading\n'
                           '[User](#user)</code></pre>')
        body = update_docs.convert_html(html)
        files = build_llms.build(body)
        self.assertNotIn('Not documentation', body)
        self.assertNotIn('Footer', body)
        self.assertIn('| Field | Type |', files['sections/sendmessage.md'])
        self.assertIn('[User](user.md)', files['sections/sendmessage.md'])
        self.assertIn('````markdown', files['sections/formatting.md'])
        self.assertIn('# Example heading', files['sections/formatting.md'])
        self.assertNotIn('sections/example-heading.md', files)

    def test_invalid_html_does_not_replace_source(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'source.md'
            source.write_text('keep me', encoding='utf-8')
            for html in ('<h1>Error</h1>', '<div id="dev_page_content"><h3>Recent changes</h3></div>'):
                with self.assertRaises(ValueError):
                    update_docs.update(source, Path(directory) / 'out', html)
                self.assertEqual(source.read_text(encoding='utf-8'), 'keep me')

    def test_unchanged_fetch_does_not_change_date(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'source.md'
            output = Path(directory) / 'docs'
            update_docs.update(source, output, sample_html())
            first = source.read_bytes()
            update_docs.update(source, output, sample_html())
            self.assertEqual(first, source.read_bytes())

    def test_snapshot_links_and_deterministic_build(self):
        source = Path('tg-docs.md').read_text(encoding='utf-8-sig')
        files = build_llms.build(source)
        self.assertEqual(files, build_llms.build(source))
        self.assertGreater(len(files), 100)
        full = files['llms-full.txt']
        self.assertIn('[Message](sections/message.md)', full)
        self.assertNotIn('[Message](https://core.telegram.org/bots/api#message)', full)
        self.assertIn('sections/formatting-options.md#markdownv2-style', full)
        for name, content in files.items():
            if not name.startswith('sections/') and name != 'llms-full.txt':
                continue
            for line, outside in build_llms.outside_fences(content.splitlines()):
                if not outside:
                    continue
                for target in re.findall(r'\]\(([^\s)]+)', line):
                    path = target.split('#')[0]
                    if path.endswith('.md') and '://' not in path:
                        resolved = 'sections/' + path if name.startswith('sections/') else path
                        self.assertIn(resolved, files, (name, target))

    def test_full_reference_keeps_example_links_unchanged(self):
        text = ('### Recent changes\n\n#### User\n\nA user.\n\n'
                '#### Example\n\n[User](#user)\n\n'
                '`[User](#user)`\n\n````\n[User](#user)\n````\n')
        full = build_llms.build(text)['llms-full.txt']
        self.assertIn('[User](sections/user.md)', full)
        self.assertIn('`[User](#user)`', full)
        self.assertIn('````\n[User](#user)\n````', full)

    def test_site_manifest_matches_files(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            build_site.build_site(Path('tg-docs.md'), output)
            catalog = json.loads((output / 'docs.json').read_text(encoding='utf-8'))
            self.assertEqual(catalog['page_count'], len(catalog['sections']))
            self.assertTrue((output / 'index.html').is_file())
            self.assertTrue((output / 'assets/site.js').is_file())
            for section in catalog['sections']:
                self.assertTrue((output / section['path']).is_file())

    def test_rebuild_retires_only_generated_files(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'site'
            source = Path(directory) / 'source.md'
            source.write_text('### Recent changes\n\n#### Retired\n\nOld docs.\n', encoding='utf-8')
            build_site.build_site(source, output)
            unrelated = output / 'keep.txt'
            unrelated.write_text('user file')
            source.write_text('### Recent changes\n\n#### Current\n\nNew docs.\n', encoding='utf-8')
            build_site.build_site(source, output)
            self.assertFalse((output / 'sections/retired.md').exists())
            self.assertTrue((output / 'sections/current.md').exists())
            self.assertEqual(unrelated.read_text(), 'user file')


if __name__ == '__main__':
    unittest.main()
