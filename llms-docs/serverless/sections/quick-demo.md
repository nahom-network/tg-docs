# Quick demo

Source: https://core.telegram.org/bots/serverless#quick-demo

[Documentation index](../llms.txt)

Here is a complete, working demo bot. It replies to every message and remembers how many it has seen from each chat.

`tgcloud/schema.js`

```js
import { table, integer } from 'sdk/db';

export const counters = table('counters', {
  chatId: integer('chat_id').primaryKey(),
  seen:   integer('seen').notNull().default(0),
});
```

`tgcloud/handlers/message.js`

```js
import { api, db } from 'sdk';
import { sql } from 'sdk/db';
import { counters } from '../schema.js';

export default async function (message) {
  const chatId = message.chat.id;

  // Insert the counter, or bump it if this chat already has one — and get the
  // resulting row back in the same statement via .returning().
  const [row] = await db.insert(counters)
    .values({ chatId, seen: 1 })
    .onConflictDoUpdate({
      target: counters.chatId,
      set: { seen: sql`${counters.seen} + 1` },
    })
    .returning()
    .run();

  await api.sendMessage({
    chat_id: chatId,
    text: `Hello! I've seen ${row.seen} message(s) from you.`,
  });
}
```

Deploy it:

```bash
npx tgcloud push       # upload the modules
npx tgcloud migrate    # create the `counters` table
```

That's a live bot with persistent state and no server. Everything in it — `api`, `db`, the `table()` DSL — is described in the sections below.

Serverless is a general backend for Telegram bots and Mini Apps, not a template for one kind of app. It is ideal for:

- **Conversational AI Bots** that need to store per‑user state in a database.
- **Mini App Backends** that store user data and serve dynamic content.
- **Games and Tools** — including leaderboards, quizzes and more.
- **Automations and Integrations** that call third‑party HTTP APIs and push results into chats.
