# Telegram API & Serverless · LLM docs

Independent, static mirrors of the Telegram Bot API and Telegram Serverless
documentation for humans and AI assistants. Each set includes a landing page,
searchable section catalog, `llms.txt`, individual linked Markdown files, and
`llms-full.txt`. This project is not affiliated with Telegram.

- Bot API: `/`
- Serverless: `/serverless/`

## Deploy on GitHub Pages

The workflow runs on push to `main` or `master`, always checks out the ref that
triggered it, and builds two outputs:

- the site **in the branch root**, which is what Pages serves when the source is
  **Deploy from a branch → main → / (root)**; and
- the same site in `_site`, uploaded as a Pages artifact for the **GitHub
  Actions** source.

The branch root is the current live source, so `llms.txt`, `llms-full.txt`,
`docs.json`, `sections/`, and `serverless/` live in the root. The workflow
rebuilds and commits those generated files after each run. Switching Pages to
**GitHub Actions** later needs no further change because `_site` is already
produced.

Generated commits are skipped by the workflow itself to avoid loops, but Pages
still rebuilds the branch. **Settings → Actions → General → Workflow
permissions** must allow read/write access so the job can push. Run **Actions →
Update docs and deploy Pages → Run workflow** to refresh immediately.

No hosting service, API key, or custom token is required. Project sites such as
`https://nahom-d54.github.io/tg-docs/` work without configuring a base URL. The
deployed LLM indexes live at `https://nahom-d54.github.io/tg-docs/llms.txt` and
`https://nahom-d54.github.io/tg-docs/serverless/llms.txt` (not the account's
domain root). Custom domains work too.

Every Monday at 06:23 UTC the workflow fetches both official pages, converts the
Bot API's `#dev_page_content` to Markdown and the Serverless Markdown endpoint
directly, validates both, runs `build_llms.py` for each set, commits changed
snapshots, and deploys the website in the same run. Pushes to the default branch
rebuild/deploy the checked-in snapshots without a network refresh.
GitHub schedules may be delayed and can be disabled after 60 days of inactivity
in public repositories; re-enable the workflow if necessary.

If branch protection prevents bot pushes, allow the Actions bot to update the
branch or adapt the commit step to your pull-request approval process. No force
push or branch-protection bypass is configured.

## Local preview

Requires Python 3.10+ (CI uses 3.13).

```sh
python -m pip install -r requirements.txt
python build_site.py
python -m http.server 8000 --directory _site
```

Open http://localhost:8000 for the Bot API set or
http://localhost:8000/serverless/ for Serverless. `build_site.py` writes to
`_site/` by default; pass `--output .` to write the branch-published layout into
the repository root. The site needs HTTP to load its search catalog; opening
`index.html` directly won't load search.

## Refresh and test

```sh
python update_docs.py
python -m unittest discover -s tests -v
python build_site.py --output .
python build_site.py --output _site
```

`tg-docs.md` and `serverless-docs.md` are the source snapshots. The generated
Bot API Markdown lives in `sections/`, `external/`, `llms.txt`, and
`llms-full.txt`; the Serverless set lives in `serverless/`. `_site/` is the
ignored artifact for an Actions deployment. Snapshot dates and the Bot API
version come from the sources, not hardcoded UI values. Network or conversion
validation failures stop publication instead of replacing a snapshot.

The Bot API converter requires the official page's current heading structure.
The Serverless set uses Telegram's official `/bots/serverless.md` endpoint, so it
does not depend on the HTML layout. If either source changes shape, validation
intentionally fails until the parser is updated. Markdown links are served as raw
files for LLM consumption, not rendered HTML documentation pages. Tables and code
examples are preserved without AI rewriting.

### Linked Telegram pages

Sections such as `sections/sendrichmessage.md` link to other Telegram pages,
for example `https://core.telegram.org/bots/features#keyboards`. When a page has
an official Markdown endpoint (`/bots/features.md`), `update_docs.py` mirrors it
under `external-docs/` and link rewriting points the section at the local copy
(`../external/bots/features.md#keyboards`) instead of the live website. Links
without a Markdown endpoint keep their original URL.

The mirrored snapshots are generated into `external/` and listed under
**Referenced Telegram pages** in `llms.txt`. Passing `--externals` to
`build_llms.py` or `build_site.py` selects a different snapshot directory; the
default is `external-docs`.

## Search engine discovery

The deployment build renders both section catalogs into HTML (no JavaScript
needed for crawling) and adds robots directives, social metadata, structured
WebPage data, absolute canonical URLs, and a `sitemap.xml` listing both homepages.
The workflow reads the actual public URL from GitHub Pages configuration.
For a custom domain, set the repository Actions variable **SITE_URL** to the full
homepage URL, including its trailing slash. Configure the domain in Pages too.

To preview production SEO metadata locally:

```sh
python build_site.py --site-url https://nahom-d54.github.io/tg-docs/
```

Submit the deployed `sitemap.xml` URL in Google Search Console or Bing Webmaster
Tools and request indexing of the homepage. Indexing is not guaranteed. A
project site's `/tg-docs/robots.txt` is not the domain-level crawler policy: crawlers
consult `/robots.txt` at the domain root. Ensure that root policy allows crawling
if you manage it. The sitemap lists the HTML homepages, not the raw Markdown files.
