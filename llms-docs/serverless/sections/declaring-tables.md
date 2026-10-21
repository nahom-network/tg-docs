# Declaring tables

Source: https://core.telegram.org/bots/serverless#declaring-tables

[Documentation index](../llms.txt)

Tables are **named exports** in `schema.js`. Calling `table()` builds a description at load time (it does not touch the database); the platform discovers the exported tables when you deploy `schema.js` and migrates the database to match.

```js
import { table, integer, text, boolean, json, index, sql } from 'sdk/db';

export const users = table('users', {
  id:      integer('id').primaryKey({ autoIncrement: true }),
  tgId:    integer('tg_id').unique(),
  name:    text('name').notNull(),
  lang:    text('lang').default('en'),
  isAdmin: boolean('is_admin').default(false),
  prefs:   json('prefs'),
  created: integer('created_at', { mode: 'timestamp' }).default(sql`(unixepoch())`),
}, (t) => ({
  createdIdx: index('idx_users_created').on(t.created),
}));
```

`table(name, columns, extras?)`: 

- **`name`** is the SQL table name; 
- **`columns`** is a map of JS property → column definition; 
- **`extras`** is an optional callback `(t) => ({ … })` where `t` exposes the columns (`t.created` is a reference to that column) — declare indexes and table‑level constraints here.

##### Column types

| Factory | SQLite type | Notes |
|---|---|---|
| `text()` | TEXT | |
| `integer()` | INTEGER | |
| `real()` | REAL | alias `float()` |
| `numeric()` | NUMERIC | |
| `blob()` | BLOB | reads/writes `Uint8Array` |
| `boolean()` | INTEGER | stored as 0/1, read as `true`/`false` |
| `json()` | TEXT | auto `JSON.stringify` / `JSON.parse` |

> The column name argument is optional — omit it and the JS key is used. The `mode` option controls how values convert between SQLite and JavaScript.

| `mode` | Stored as | JS value |
|---|---|---|
| `boolean` | INTEGER 0/1 | `boolean` |
| `json` | TEXT (JSON) | any object/array |
| `timestamp` | INTEGER (unix seconds) | `Date` |
| `timestamp_ms` | INTEGER (unix ms) | `Date` |
| `bytes` | BLOB | `Uint8Array` |

`boolean()` and `json()` are shorthands for `integer(name, { mode: 'boolean' })` and `text(name, { mode: 'json' })`.

A `blob()` reads and writes a `Uint8Array` — the runtime has no Node `Buffer` (and a `Buffer` is a `Uint8Array` subclass, so this is the portable base type). The `mode` above governs only how a value is **encoded**, independent of the column's storage type: so `blob('col', { mode: 'json' })` is the BLOB counterpart of `json()` — the same JSON encoding, kept in a BLOB column rather than TEXT.

> **TLDR:** `blob()` uses `Uint8Array`. `mode` controls encoding, not storage, so `blob(..., { mode: 'json' })` stores JSON as a BLOB, while `json()` stores it as TEXT.

##### Column modifiers

Column modifiers chain onto a column.

```js
integer('id').primaryKey({ autoIncrement: true })
text('name').notNull()
text('tg').unique()
text('lang').default('en')
integer('created_at', { mode: 'timestamp' }).default(sql`(unixepoch())`)
text('slug').generatedAlwaysAs(sql`lower(name)`, { mode: 'stored' })  // or 'virtual'
text('email').deprecated('replaced by login')   // marks the column for removal
```

> `.default()` on a `json()` column encodes the value for you; a `` sql`…` `` default is passed through verbatim. `.deprecated()` is terminal — see [Migrations](migrations.md).

##### Indexes and constraints
Indexes and constraints are declared in the `extras` callback, where the columns are in scope.

```js
table('t', { /* … */ }, (t) => ({
  uq:     unique('uq_email').on(t.email),
  chk:    check('chk_done', sql`${t.done} in (0, 1)`),
  idx:    index('idx_name').on(t.col),
  uidx:   uniqueIndex('uidx_email').on(t.email),
  lower:  index('idx_lower').on(sql`lower(${t.email})`),          // expression index
  active: index('idx_active').on(t.userId).where(sql`done = 0`),  // partial index
}));
```

Table‑level modifiers chain after `table(...)`: `.strict()`, `.withoutRowid()`, `.deprecated('reason')`.
