import json
from pathlib import Path
import posixpath
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
                    update_docs.update_api(source, Path(directory) / 'out', html,
                                           externals=None)
                self.assertEqual(source.read_text(encoding='utf-8'), 'keep me')

    def test_unchanged_fetch_does_not_change_date(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'source.md'
            output = Path(directory) / 'docs'
            update_docs.update_api(source, output, sample_html(), externals=None)
            first = source.read_bytes()
            update_docs.update_api(source, output, sample_html(), externals=None)
            self.assertEqual(first, source.read_bytes())

    def test_serverless_update_is_stable_and_rejects_incomplete_markdown(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'serverless.md'
            output = Path(directory) / 'docs'
            text = Path('serverless-docs.md').read_text(encoding='utf-8-sig')
            body = re.sub(r'\A---\n.*?\n---\n', '', text, count=1, flags=re.S)
            update_docs.update_serverless(source, output, body, externals=None)
            first = source.read_bytes()
            self.assertTrue((output / 'sections/handlers.md').is_file())
            update_docs.update_serverless(source, output, body, externals=None)
            self.assertEqual(first, source.read_bytes())
            with self.assertRaises(ValueError):
                update_docs.update_serverless(source, output, '# Not the docs\n',
                                              externals=None)

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

    def test_linked_telegram_pages_become_local_markdown(self):
        text = ('### Recent changes\n\n#### ReplyKeyboardMarkup\n\n'
                'See [keyboards](https://core.telegram.org/bots/features#keyboards) and '
                '[missing](https://core.telegram.org/bots/url#x).\n')
        externals = {'https://core.telegram.org/bots/features':
                     '# Telegram Bot Features\n\n### Inputs\n\n'
                     'See [FAQ](/bots/faq.md) and [dice](/bots/api/types/dice.md).\n'}
        files = build_llms.build(text, externals)
        self.assertIn('[keyboards](../external/bots/features.md#keyboards)',
                      files['sections/replykeyboardmarkup.md'])
        self.assertIn('[keyboards](external/bots/features.md#keyboards)',
                      files['llms-full.txt'])
        self.assertIn('[missing](https://core.telegram.org/bots/url#x)',
                      files['sections/replykeyboardmarkup.md'])
        page = files['external/bots/features.md']
        self.assertIn('# Telegram Bot Features', page)
        self.assertIn('Source: https://core.telegram.org/bots/features', page)
        self.assertIn('[Documentation index](../../llms.txt)', page)
        self.assertIn('[FAQ](https://core.telegram.org/bots/faq.md)', page)
        self.assertIn('- [Telegram Bot Features](external/bots/features.md)',
                      files['llms.txt'])
        # Without snapshots the previous output is preserved.
        self.assertIn('[keyboards](https://core.telegram.org/bots/features#keyboards)',
                      build_llms.build(text)['sections/replykeyboardmarkup.md'])

    def test_generated_links_to_mirrored_pages_resolve(self):
        externals = build_llms.load_externals(Path('external-docs'))
        for snapshot in ('tg-docs.md', 'serverless-docs.md'):
            text = Path(snapshot).read_text(encoding='utf-8-sig')
            files = build_llms.build(text, externals)
            for name, content in files.items():
                if not (name.startswith(('sections/', 'external/'))
                        or name == 'llms-full.txt'):
                    continue
                start = posixpath.dirname(name)
                for line, outside in build_llms.outside_fences(content.splitlines()):
                    if not outside:
                        continue
                    for target in re.findall(r'\]\(([^\s)]+)', line):
                        path = target.split('#')[0]
                        if path.endswith('.md') and '://' not in path:
                            resolved = posixpath.normpath(posixpath.join(start, path))
                            self.assertIn(resolved, files, (snapshot, name, target))

    def test_external_pages_are_downloaded_and_missing_markdown_is_skipped(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source = directory / 'source.md'
            source.write_text(
                '### Recent changes\n\n#### Item\n\n'
                '[features](https://core.telegram.org/bots/features#keyboards)\n'
                '[url](https://core.telegram.org/bots/url)\n', encoding='utf-8')
            calls = []

            def fake_fetch(url, accept):
                calls.append(url)
                if url.endswith('/bots/url.md'):
                    raise update_docs.HTTPError(url, 404, 'Not Found', None, None)
                return '# Telegram Bot Features\n\nText.\n'

            original = update_docs.fetch
            update_docs.fetch = fake_fetch
            try:
                update_docs.update_external_pages(source, directory / 'external-docs')
            finally:
                update_docs.fetch = original
            self.assertEqual(calls, ['https://core.telegram.org/bots/features.md',
                                     'https://core.telegram.org/bots/url.md'])
            self.assertTrue((directory / 'external-docs/bots/features.md').is_file())
            self.assertFalse((directory / 'external-docs/bots/url.md').exists())
            self.assertIn('https://core.telegram.org/bots/features',
                          build_llms.load_externals(directory / 'external-docs'))

    def test_site_publishes_linked_pages(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source = directory / 'api.md'
            source.write_text('### Recent changes\n\n#### Section\n\n'
                              '[features](https://core.telegram.org/bots/features#x)\n',
                              encoding='utf-8')
            serverless = directory / 'serverless.md'
            serverless.write_text('### Recent changes\n\n#### Handlers\n\nText.\n',
                                  encoding='utf-8')
            build_site.build_site(
                source, directory / 'site', serverless_source=serverless,
                externals={'https://core.telegram.org/bots/features':
                           '# Telegram Bot Features\n\nText.\n'})
            page = directory / 'site/external/bots/features.md'
            self.assertTrue(page.is_file())
            self.assertIn('(../external/bots/features.md#x)',
                          (directory / 'site/sections/section.md').read_text(encoding='utf-8'))

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

            serverless = json.loads((output / 'serverless/docs.json').read_text(encoding='utf-8'))
            self.assertEqual(serverless['page_count'], len(serverless['sections']))
            self.assertTrue((output / 'serverless/index.html').is_file())
            self.assertTrue((output / 'serverless/llms.txt').is_file())
            self.assertIn('sections/handlers.md',
                          (output / 'serverless/index.html').read_text(encoding='utf-8'))
            for section in serverless['sections']:
                self.assertTrue((output / 'serverless' / section['path']).is_file())

    def test_published_site_serves_indexes_from_the_root(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            build_site.build_site(Path('tg-docs.md'), output)
            for name in ('index.html', 'serverless/index.html', 'serverless.html',
                         'docs.json', 'llms.txt', 'llms-full.txt',
                         'serverless/llms.txt', 'serverless/llms-full.txt',
                         'assets/site.js'):
                self.assertTrue((output / name).is_file(), name)
                self.assertNotIn('/llms-docs/', (output / name).read_text(encoding='utf-8'), name)
            self.assertIn('url=serverless/',
                          (output / 'serverless.html').read_text(encoding='utf-8'))
            self.assertEqual((output / 'CNAME').read_text(encoding='utf-8').strip(),
                             Path('CNAME').read_text(encoding='utf-8').strip())

    def test_serverless_snapshot_builds_linked_pages(self):
        text = Path('serverless-docs.md').read_text(encoding='utf-8-sig')
        files = build_llms.build(text)
        for name in ('sections/handlers.md', 'sections/endpoints.md',
                     'sections/the-database.md', 'sections/command-line-interface.md'):
            self.assertIn(name, files)
        self.assertIn('[Handlers](handlers.md)',
                      files['sections/projects-and-modules.md'])
        self.assertIn('[endpoints](sections/endpoints.md)', files['llms-full.txt'])
        self.assertIn('Telegram Serverless', files['llms.txt'])

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
