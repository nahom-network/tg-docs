# Mini App front-end

Source: https://core.telegram.org/bots/serverless#mini-app-front-end

[Documentation index](../llms.txt)

The project root is yours, and it is the natural place for your Mini App's front‑end — built with React, Vue, Svelte or plain HTML, by Vite or any other bundler. Serverless hosts its **build output** next to your bot. One `push` deploys the code and the static files together, and the app is served at `https://app<app_id>.tgcloud.ai/` (`push` prints the exact address — use it as your Mini App's URL in [@BotFather](https://t.me/BotFather)).

> **Reporting abuse.** Mini Apps on tgcloud.ai are published by independent developers. To report illegal content or abuse on an `app<app_id>.tgcloud.ai` subdomain, email [abuse@telegram.org](mailto:abuse@telegram.org).

To start, create the front‑end first, with whatever tool you like, then add Serverless on top of it:

```bash
npm create vite@latest example_app   # or create-vue, …
cd example_app
npm create @tgcloud/bot .
```

The project creator never overwrites your files. It adds the `tgcloud/` folder next to the front‑end, recognizes the build folder, and adds an `npm run deploy` script that builds the app and deploys it together with the bot.

What gets hosted is set in **`tgcloud.jsonc`**, the project's config file at the project root:

```jsonc
{
  "$schema": "./node_modules/@tgcloud/cli/schema/tgcloud.json",
  "static": {
    "source": "dist",
    "spa": true,
    "immutable": ["/assets/*"],
    "headers":   [{ "path": "/*", "set": { "Referrer-Policy": "no-referrer" } }],
    "redirects": [{ "from": "/old", "to": "/new", "status": 301 }]
  }
}
```

Only `"source"` is required. It is the build folder, relative to the project root. The other keys of `"static"` configure how it is served (below). `init` creates `tgcloud.jsonc` for you. When it recognizes the front‑end, it also fills in `"source"`:

| Front‑end | `init` sets `"source"` to |
|---|---|
| Vite — React, Vue, Svelte, Solid, … | `dist` |
| Next.js, Nuxt, SvelteKit, React Router, TanStack Start, Angular | nothing — configure a static export first, then set `"source"` to its folder yourself |

With any other setup, set `"source"` to your build folder yourself.

The `$schema` line gives your editor autocomplete and validation for every key. The file is JSON with comments and trailing commas allowed. If another tool of yours has to read it as plain JSON, name it `tgcloud.json` instead — then it must be strict JSON.

**Build before you push.** `push` uploads the folder exactly as it is on disk — except files and folders whose name starts with a dot, which are skipped — and never runs your build, so a plain `npx tgcloud push` after editing the front‑end would deploy the previous build. Use `npm run deploy` (it runs your `build` script, then `tgcloud push`), or build yourself first.

The serving options:

- **`spa`** — serve `index.html` for paths that don't exist and have no file extension, so a client‑side router works on reload. Paths with an extension still get `404`.
- **`immutable`** — patterns for content‑hashed files (Vite's `/assets/*`) that browsers may cache for a year. Use it only for content‑hashed files. Any other file matched here would stay stale in browsers for a year, and there is no way to recall it.
- **`headers`** — response headers for the paths a rule matches (an exact path, or a prefix ending in `/*`). A `null` value removes a header.
- **`redirects`** — redirect rules, where the first match wins. An existing file always beats a rule. `status` is `301` unless you set it.
- **`"static": "dist"`** — a shorthand for `{ "source": "dist" }` when you need nothing else.
- **`"static": false`** — remove the deployed site on the next push. Deleting the key instead just stops this project from managing static files, and whatever is deployed stays.

The site is served from the root of its own host, so your bundler's default `base` (`/`) is correct. Telegram Web opens Mini Apps in an iframe, so don't add `X-Frame-Options` or a restrictive `frame-ancestors` policy.

The same host answers your [endpoints](endpoints.md) under `/api/` — that's where `Telegram.WebApp.Serverless.call('getProfile', …)` goes. Don't put files of your own under `/api/` in the build folder.
