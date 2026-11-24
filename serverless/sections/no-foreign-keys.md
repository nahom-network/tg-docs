# No foreign keys

Source: https://core.telegram.org/bots/serverless#no-foreign-keys

[Documentation index](../llms.txt)

The runtime runs with `PRAGMA foreign_keys` **off**. A declared foreign key would be silently inert — no cascades, no orphan protection — which is worse than having none at all, so the DSL makes it impossible. Namely, `.references()` and table‑level `foreignKey()` **throw when declared**, and a schema that uses them will not deploy.

You should model relationships with plain columns (`userId: integer('user_id')`) and enforce **integrity** in your application code: insert parents before children, delete children before parents, handle errors properly and sweep orphans with a `LEFT JOIN … WHERE parent.id IS NULL` when you need to.

> The absence of foreign keys is a deliberate constraint, not an oversight. Account for it early on when planning your bot.
