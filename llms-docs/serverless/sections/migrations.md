# Migrations

Source: https://core.telegram.org/bots/serverless#migrations

[Documentation index](../llms.txt)

Your database changes as your bot grows. The platform keeps that safe by separating **deploying code** from **changing data**, and by classifying every schema change by how risky it is.

**Deploying never touches the database.** When you `npx tgcloud push` a changed `schema.js`, the platform records the new schema and tells you what the database *would* change — but applies nothing:

```bash
npx tgcloud push       # deploy schema.js; reports pending DB changes
npx tgcloud migrate    # review and apply them
```

`npx tgcloud migrate` computes the difference between your schema and the live database and walks you through it. You are always asked before anything is applied. This means a routine code deploy can never trigger a data migration by accident.

Each pending change carries a status that determines how `migrate` treats it:

| Status | Meaning | In `migrate` |
|---|---|---|
| **safe** | Additive and non‑blocking — a new table, column, or index | Applied together in one step, on confirmation |
| **warning** | Potentially destructive or slow — dropping something, or an index on a huge table | Presented one at a time, each confirmed separately |
| **manual** | Can't be done automatically — e.g. changing a column's type | Shown with guidance; you perform it by hand |
| **undocumented** | Exists in the database but not in your schema | Shown for awareness; not applied |

Safe changes are quick and reversible in spirit, so they go through together. Each warning is a deliberate, individual confirmation — there is no "apply all" for destructive changes. 

Manual changes come with a reason and a suggested action. `migrate` ends with a summary: how many changes were applied, skipped, awaiting a manual fix, or not in your schema. 

> See [`migrate`](migrate.md) for the flags (`--dry-run`, `--safe`, `--yes`, `--local`).

##### Removing things

Deleting a table or column from `schema.js` does **not** drop it — that would make an accidental deletion catastrophic. To remove something, mark it deprecated:

```js
// drop a column
text('email').deprecated('replaced by login')

// drop a whole table
export const oldSessions = table('old_sessions', { /* … */ }).deprecated('unused');
```

On the next `migrate`, the deprecated object shows up as a **warning**‑status drop that you confirm individually. Once it's gone, remove the declaration.

##### Changing a column's type

Type changes are **manual** — SQLite can't always do them in place, and coercing existing values is a judgment call. `migrate` will show the change and its reasoning; perform it yourself with raw SQL (`db.run(...)`), typically by creating a new column or table, copying data, and swapping.
