# The database

Source: https://core.telegram.org/bots/serverless#the-database

[Documentation index](../llms.txt)

Every bot gets its own database — an SQLite‑backed store that persists between invocations and is available to every module through `db`. You describe your tables in `schema.js` with a small, typed DSL; you read and write them with a fluent query builder; and you evolve them with reviewed migrations.

> **Know [Drizzle ORM](https://orm.drizzle.team)?** Then you already know how to talk to the database here. The schema DSL and query builder follow Drizzle — the column builders, `select().from().where()`, the operators, `onConflictDoUpdate`, `.returning()`, and the `sql` tag all behave the way you'd expect, so reading and writing data is the familiar API you already use. You just import it from `sdk/db`, and a couple of platform specifics (most notably [no foreign keys](no-foreign-keys.md)) are pointed out where they come up.

## In this section

- [Declaring tables](declaring-tables.md)
- [No foreign keys](no-foreign-keys.md)
- [Querying](querying.md)
- [Migrations](migrations.md)
