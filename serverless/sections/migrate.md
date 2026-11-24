# `migrate`

Source: https://core.telegram.org/bots/serverless#migrate

[Documentation index](../llms.txt)

```bash
npx tgcloud migrate
```

Applies your schema changes to the database. It computes the difference between `schema.js` and the live database, then walks you through it one step at a time with a running `[N/M]` counter:

- A brief summary of all pending changes.
- **Safe changes**, applied together in a single step on your confirmation.
- **Warnings** (drops, slow operations), one at a time, each confirmed separately.
- **Manual changes**, shown with a reason and suggested action, not applied automatically.
- **Undocumented objects** (in the database but not your schema), shown for awareness. 

It ends with a summary: applied, skipped, awaiting manual fix, not in schema.

> See [Migrations](migrations.md) for the model.

Options: `--dry-run` (print everything, apply nothing), `--safe` (auto‑apply safe changes, skip warnings), `--yes` (auto‑apply safe changes and every warning, skip manual — use with care), `--local` (diff against your local `schema.js` instead of the deployed one). Without a flag, `migrate` requires a terminal and errors in a non‑interactive environment rather than guessing.
