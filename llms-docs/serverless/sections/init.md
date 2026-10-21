# `init`

Source: https://core.telegram.org/bots/serverless#init

[Documentation index](../llms.txt)

```bash
npx tgcloud init
```

Scaffolds a new project in the current directory: the `tgcloud/` folder with `schema.js`, `lib/`, `handlers/` and a starter handler, plus `tgcloud.jsonc`, `AGENTS.md`, `docs/`, and the `.tgcloud/` state folder. Run it in the root of an existing front‑end project too — it adds the `tgcloud/` folder and the docs, and never overwrites your files. If it recognizes the front‑end, it also points `tgcloud.jsonc` at the build folder and adds a `deploy` script (build, then push) to your `package.json` — only if you don't have a `deploy` script already. See [Mini App front‑end](mini-app-front-end.md).

`init` refuses to create a project **inside another project**. Re‑running it in a project's own root is fine and just adds anything missing.
