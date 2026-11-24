# 5. Add a database table

Source: https://core.telegram.org/bots/serverless#5-add-a-database-table

[Documentation index](../llms.txt)

Let's make the bot remember something. Open `tgcloud/schema.js` and declare a table:

```js
import { table, integer, text, sql } from 'sdk/db';

export const messages = table('messages', {
  id:      integer('id').primaryKey({ autoIncrement: true }),
  chatId:  integer('chat_id').notNull(),
  text:    text('text'),
  created: integer('created_at', { mode: 'timestamp' }).default(sql`(unixepoch())`),
});
```

Deploy the schema, then apply it to the database:

```bash
npx tgcloud push       # uploads the new schema
npx tgcloud migrate    # creates the `messages` table
```

`push` reports that the schema is out of sync and shows you the pending change, but applies nothing. `migrate` walks you through the change and, on your confirmation, creates the table. This two‑step model — and what happens with riskier changes like drops — is covered in [Migrations](migrations.md).
