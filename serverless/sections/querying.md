# Querying

Source: https://core.telegram.org/bots/serverless#querying

[Documentation index](../llms.txt)

`db` is a fluent query builder. **Every query is asynchronous** — the terminal methods (`.all()`, `.get()`, `.values()`, `.run()`) return Promises, so **always** `await`.

```js
import { db } from 'sdk';
import { eq, and, desc, asc, count, sql } from 'sdk/db';
import { users, todos } from '../schema.js';

await db.select().from(todos).all();                          // all rows
await db.select().from(todos).where(eq(todos.id, 1)).get();   // first row or null
await db.select().from(todos).values();                       // rows as value arrays

await db.select().from(todos)
  .where(and(eq(todos.userId, uid), eq(todos.done, false)))
  .orderBy(desc(todos.priority), asc(todos.id))
  .limit(10).offset(20)
  .all();

// custom projection: { alias: columnRef | sqlExpr | aggregate }
await db.select({ id: todos.id, title: todos.text, n: count() })
  .from(todos).groupBy(todos.userId).having(sql`count(*) > ${1}`).all();

// row count — a helper, not a builder terminal:
await db.$count(todos);                        // all rows
await db.$count(todos, eq(todos.done, false)); // with a filter
```

- Chainable: `.where()`, `.orderBy()`, `.limit()`, `.offset()`, `.groupBy()`, `.having()`, `.distinct()`. 
- Terminals: `.all()`, `.get()`, `.values()`. 
- Count rows with `db.$count(table, where?)` (or `count()` in a projection).

**Insert, update, delete:**

```js
await db.insert(todos).values({ userId: 1, text: 'Buy milk' }).run();
await db.insert(todos).values([{ text: 'A' }, { text: 'B' }]).run();   // batch
await db.insert(todos).values({ text: 'X' }).returning().run();        // RETURNING *

await db.insert(users).values({ tgId: 42, name: 'Ann' })
  .onConflictDoUpdate({ target: users.tgId, set: { name: 'Ann' } }).run();

await db.update(todos).set({ done: true }).where(eq(todos.id, 1)).run();
await db.delete(todos).where(eq(todos.id, 1)).run();
```

> Note that a batch insert is one statement, so it's capped by SQLite's variable limit (`rows × columns`); if you go over it, the insert errors out — chunk it yourself.

**Operators** are imported from `sdk/db`:

```js
import {
  eq, ne, gt, gte, lt, lte,
  like, notLike,
  isNull, isNotNull, and, or, not,
  between, notBetween, inArray, notInArray,
  count, sum, avg, min, max,
  asc, desc,
} from 'sdk/db';
```

`.where(a, b)` with multiple arguments is the same as `and(a, b)`. A comparison's second argument is a value by default, but may be another column or `` sql`…` `` — e.g. `eq(a.x, b.y)`. Aggregates (`count/sum/avg/min/max`) are sql fragments for a `.select({ … })` projection.

**Raw SQL** — when the builder isn't enough, drop to raw SQL. The mode is chosen by method: `db.run` for writes, `db.all` for many rows, `db.get` for one row, `db.values` for rows as positional arrays.

```js
await db.run('UPDATE todos SET done = 1 WHERE id = :id', { ':id': 5 });
// → { rowsAffected: 3, lastInsertRowid: 0, rows: [] }

await db.all(sql`SELECT * FROM todos WHERE done = ${false}`);
await db.get(sql`SELECT count(*) AS c FROM todos`);
await db.values(sql`SELECT id, text FROM todos`);   // → [[1, 'buy milk']]
```

A write resolves to a **run result** — `rowsAffected`, `lastInsertRowid`, and `rows`, which carry a `RETURNING` clause if the SQL had one. Reach for `db.values` when a query projects two columns of the same name (a join like `SELECT u.id, o.id`): `db.all` keys rows by column name, so the second `id` would overwrite the first.

The `` sql`…` `` tag turns `${value}` into a bound parameter and `${table.column}` into an identifier, and splices nested `sql` fragments. Use `sql.raw('…')` for a literal with no parameters.

> Raw queries are **not bound to a table**, so their rows come back without mode conversion — a boolean is `0`/`1`, a JSON column is a string, a timestamp is a number. Only the table‑bound builder converts values.
