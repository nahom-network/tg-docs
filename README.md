# Telegram API & Serverless · LLM docs

Independent, static mirrors of the Telegram Bot API and Telegram Serverless
documentation for humans and AI assistants. Each set includes a landing page,
searchable section catalog, `llms.txt`, individual linked Markdown files, and
`llms-full.txt`. This project is not affiliated with Telegram.

- Bot API: `/`
- Serverless: `/serverless/`

## Deploy on GitHub Pages

1. Push this repository to GitHub. The workflow runs on push to `main` or
   `master` and always checks out the ref that triggered it, so it also works
   after the default branch is renamed.
2. In **Settings → Pages → Build and deployment**, select **GitHub Actions**.
3. In **Settings → Actions → General → Workflow permissions**, allow read/write
   access if your organization permits it. The refresh job needs to push commits.
4. Run **Actions → Update docs and deploy Pages → Run workflow**. Leave
   **refresh** enabled to fetch the latest documentation immediately.

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
http://localhost:8000/serverless/ for Serverless. Serve `_site`, not the
repository root. The site needs HTTP to load its search catalog; opening
`index.html` directly won't load search.

## Refresh and test

```sh
python update_docs.py
python -m unittest discover -s tests -v
python build_llms.py tg-docs.md --output llms-docs --force
python build_llms.py serverless-docs.md --output llms-docs/serverless --force
python build_site.py
```

`tg-docs.md` and `serverless-docs.md` are the source snapshots.
`llms-docs/` holds the generated Bot API Markdown, with the Serverless set under
`llms-docs/serverless/`. `_site/` is the ignored deployment artifact. Snapshot
dates and the Bot API version come from the sources, not hardcoded UI values.
Network or conversion validation failures stop publication instead of replacing
a snapshot.

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

The mirrored snapshots are generated into `llms-docs/external/` and listed under
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
