# Anatomy of a project

Source: https://core.telegram.org/bots/serverless#anatomy-of-a-project

[Documentation index](../llms.txt)

```bash
example_bot/
├─ tgcloud/             # the deployed part — nothing else is
│  ├─ handlers/         # update handlers — flat, one level only
│  │  ├─ message.js
│  │  └─ callback_query.js
│  ├─ endpoints/        # functions your Mini App calls — flat, one level only
│  │  └─ getProfile.js
│  ├─ lib/              # shared modules; subdirectories allowed
│  │  ├─ reply.js
│  │  └─ internal/util.js
│  └─ schema.js         # database schema — one file
└─ .tgcloud/            # CLI state, git‑ignored
```

Only `.js` files inside `tgcloud/` — `schema.js`, `lib/`, `handlers/`, `endpoints/` — are **deployed**. Everything else — Markdown, config files, the `.tgcloud/` folder, anything outside `tgcloud/` — stays on your machine. Module names are relative to `tgcloud/`. The file `tgcloud/handlers/message.js` is the module `handlers/message`, and that is the name `npx tgcloud run` takes.

> **Upgrading from an older project?** Projects created before CLI 0.2.0 kept `schema.js`, `lib/` and `handlers/` at the project root. Run [`npx tgcloud upgrade`](upgrade.md) once to move them into `tgcloud/`.

**`schema.js`** — your database. It declares tables as named exports using the schema DSL and lives in `tgcloud/` as a single file. It is deployed like any other module, but deploying it never changes the database — schema changes are applied separately with `npx tgcloud migrate`. See [The database](the-database.md).

**`lib/`** — shared code, anything you want to reuse across handlers: pure helpers, database access layers, formatting, integrations with outside services. `lib/` is the only directory that may contain **subdirectories** (`lib/internal/util.js`, `lib/payments/stripe.js`), so you can organize a larger codebase however you like. Modules in `lib/` are never invoked directly by the platform; they exist to be imported by handlers and by each other.

**`handlers/`** — the entry points of your bot. Each file corresponds to one **Telegram update type**, and the platform routes each incoming update to the matching handler:

| File | Handles |
|---|---|
| `handlers/message.js` | New incoming messages |
| `handlers/inline_query.js` | New incoming [inline](https://core.telegram.org/bots/api.md#inline-mode) queries |
| `handlers/callback_query.js` | New incoming callback queries |
| … | _any other Bot API update type_ |

`handlers/` is **flat** — no subdirectories. A handler's `export default` is the function the platform calls (see [Handlers](handlers.md)).

An update type is handled **only if its handler file exists and is non‑empty**. If there is no `handlers/<type>.js` — or the file is empty — updates of that type are ignored, and the platform runs nothing for them. So keep only the handlers you actually need: each one you add is another update type your bot wakes up to process, and leaving out the rest means Telegram doesn't spin up your code for updates you'd only discard anyway. 

> To scaffold a new handler, run [`npx tgcloud add handlers/<type>`](add.md).

**`endpoints/`** — the server side of your Mini App. Each file is a function the Mini App calls by name, so `endpoints/getProfile.js` answers `POST /api/getProfile`. The platform checks that the call comes from a Telegram user inside your Mini App before your code runs, and hands you that user. `endpoints/` is **flat**, like `handlers/`. See [Endpoints](endpoints.md).

**`.tgcloud/`** — machine‑local state managed entirely by the CLI, including your saved credentials. It is git‑ignored, and you should never read from or write to it by hand — use the CLI commands instead.
