# `upgrade`

Source: https://core.telegram.org/bots/serverless#upgrade

[Documentation index](../llms.txt)

```bash
npx tgcloud upgrade [--dry-run]
```

One‑time migration for projects created before CLI 0.2.0, which kept `schema.js`, `lib/` and `handlers/` at the project root. It moves them into `tgcloud/`. Your link to the bot is kept, and nothing needs to be redeployed. `--dry-run` prints the planned moves without touching anything. Other commands don't run on the old layout until you upgrade.
