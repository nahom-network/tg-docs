# Command-line interface

Source: https://core.telegram.org/bots/serverless#command-line-interface

[Documentation index](../llms.txt)

`tgcloud` is the bridge between your project folder and the cloud. It scaffolds projects, shows you what changed, deploys, runs modules, and applies database migrations. It needs [Node.js](https://nodejs.org) 18 or newer. Two ways to get it:

```bash
# Recommended — create a project with the CLI installed into it:
npm create @tgcloud/bot example_bot

# Or install the CLI globally and init an empty folder:
npm install -g @tgcloud/cli
tgcloud init
```

The npm package is `@tgcloud/cli`, and the command it installs is `tgcloud`. Every command works from any subfolder of your project.

| Command | Purpose |
|---|---|
| [`init`](init.md) | Scaffold a new project in the current folder |
| [`add`](add.md) | Scaffold a new module (a handler, an endpoint or a lib module) |
| [`login`](login.md) | Link the project to a bot (saves the token) |
| [`status`](status.md) | Show what changed locally vs. the cloud |
| [`diff`](diff.md) | Show the line‑by‑line changes |
| [`push`](push.md) | Deploy changed modules and the Mini App's build to the cloud |
| [`migrate`](migrate.md) | Apply schema changes to the database |
| [`run`](run.md) | Execute a module on the platform without deploying |
| [`fetch`](fetch.md) | Check what is deployed, without changing local files |
| [`pull`](pull.md) | Bring local files in line with the cloud |
| [`reset`](reset.md) | Discard local changes; restore from the cloud state |
| [`webhook`](webhook.md) | Inspect and re‑sync the platform‑managed webhook |
| [`completion`](completion.md) | Print a shell completion script (bash/zsh/fish) |
| [`upgrade`](upgrade.md) | Move a pre‑0.2.0 project layout into `tgcloud/` |

## In this section

- [Authentication](authentication.md)
- [`init`](init.md)
- [`add`](add.md)
- [`login`](login.md)
- [`status`](status.md)
- [`diff`](diff.md)
- [`push`](push.md)
- [`migrate`](migrate.md)
- [`run`](run.md)
- [`fetch`](fetch.md)
- [`pull`](pull.md)
- [`reset`](reset.md)
- [`webhook`](webhook.md)
- [`completion`](completion.md)
- [`upgrade`](upgrade.md)
- [Staying in sync](staying-in-sync.md)
