# Telegram Bot API · LLM docs

An independent, static Telegram Bot API mirror for humans and AI assistants.
Includes a landing page, searchable section catalog, `llms.txt`, individual linked
Markdown files, and `llms-full.txt`. This project is not affiliated with Telegram.

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
`https://nahom-d54.github.io/tg-docs/` work without configuring a base URL. The deployed
LLM index lives at `https://nahom-d54.github.io/tg-docs/llms.txt` (not the account's
domain root). Custom domains work too.

The workflow fetches `https://core.telegram.org/bots/api` every Monday at 06:23 UTC,
converts only `#dev_page_content` to Markdown, validates it, runs `build_llms.py`,
commits changed snapshots, and deploys the website in the same run. Pushes to
the default branch rebuild/deploy the checked-in snapshot without a network refresh.
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

Open http://localhost:8000. Serve `_site`, not the repository root. The site needs
HTTP to load its search catalog; opening `index.html` directly won't load search.

## Refresh and test

```sh
python update_docs.py
python -m unittest discover -s tests -v
python build_site.py
```

`tg-docs.md` is the source snapshot; `llms-docs/` holds generated Markdown.
`_site/` is the ignored deployment artifact. The page's snapshot date and API
version come from the source, not hardcoded UI values. Network or conversion
validation failures stop publication instead of replacing the snapshot.

The converter requires the official page's current heading structure. If
Telegram changes it, validation intentionally fails until the parser is updated.
Markdown links are served as raw files for LLM consumption, not rendered HTML
documentation pages. Tables and code examples are preserved without AI rewriting.

## Search engine discovery

The deployment build renders the full section catalog into HTML (no JavaScript
needed for crawling) and adds robots directives, social metadata, structured
WebPage data, an absolute canonical URL, and a homepage `sitemap.xml`.
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
if you manage it. The sitemap lists the HTML homepage, not the raw Markdown files.
