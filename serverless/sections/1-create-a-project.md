# 1. Create a project

Source: https://core.telegram.org/bots/serverless#1-create-a-project

[Documentation index](../llms.txt)

The fastest way to start is the project creator, which scaffolds a project and installs the CLI into it:

```bash
npm create @tgcloud/bot example_bot
cd example_bot
```

The argument is the target folder: pass `.` to scaffold into the current folder, or any path. It works in an existing folder too and never overwrites files you already have.

This gives you a ready‑to‑edit project:

```bash
example_bot/
├─ tgcloud/             # everything the platform runs
│  ├─ handlers/
│  │  └─ message.js     # a starter message handler (echoes text back)
│  ├─ lib/              # your shared modules go here (empty to start)
│  └─ schema.js         # your database tables
├─ docs/
│  └─ tgcloud-sdk.md    # SDK reference (for you and your AI tools)
├─ AGENTS.md            # orientation for AI coding assistants
├─ package.json
└─ tgcloud.jsonc        # project config
```

The scaffolded files are self‑documenting — each one contains commented examples of what you can do next.

The CLI installs into the project as a local dev‑dependency, so you run it with `npx tgcloud <command>` (npx finds the copy in your project's `node_modules`), or through the `npm run` shortcuts the scaffold adds to `package.json` (`npm run deploy`, `npm run status`). By default there is no global `tgcloud` on your `PATH`.

You can also install it globally — `npm install -g @tgcloud/cli` — if you'd rather type a bare `tgcloud` from anywhere. That's handy for running `tgcloud init` in any empty folder, and it's what shell tab‑completion needs. Either way you get the same project.

> **Building a Mini App?** Start from its front‑end instead. Create it with your usual tool, then run the project creator in that folder. See [Mini App front‑end](mini-app-front-end.md).
