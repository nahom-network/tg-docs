# 6. Store and read data

Source: https://core.telegram.org/bots/serverless#6-store-and-read-data

[Documentation index](../llms.txt)

Now use the table from your handler. Edit `tgcloud/handlers/message.js`:

```js
import { api, db } from 'sdk';
import { eq } from 'sdk/db';
import { messages } from '../schema.js';

export default async function (message) {
  // Save this message.
  await db.insert(messages)
    .values({ chatId: message.chat.id, text: message.text })
    .run();

  // Count how many we've stored for this chat.
  const count = await db.$count(messages, eq(messages.chatId, message.chat.id));

  await api.sendMessage({
    chat_id: message.chat.id,
    text: `Saved. That's ${count} message(s) from this chat so far.`,
  });
}
```

Deploy the updated handler with `npx tgcloud push`, then send your bot a few messages and watch the count climb. The database persists between invocations — that's your bot's memory.
