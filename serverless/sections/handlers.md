# Handlers

Source: https://core.telegram.org/bots/serverless#handlers

[Documentation index](../llms.txt)

A handler is a module in `handlers/` whose default export the platform invokes when a matching update arrives.

```js
// handlers/message.js
import { api } from 'sdk';

export default async function (message) {
  await api.sendMessage({
    chat_id: message.chat.id,
    text: `You said: ${message.text ?? '(no text)'}`,
  });
}
```

A handler receives the update's **payload** as its argument — the platform unwraps the Telegram [Update](../external/bots/api/types/update.md) for you. `handlers/message.js` gets the [Message](../external/bots/api/types/message.md) (i.e. `update.message`); `handlers/callback_query.js` gets the [CallbackQuery](../external/bots/api/types/callbackquery.md); and so on. The handler's **second argument** is a per‑invocation context object, `ctx`. It carries the raw `Update` as `ctx.update` — reach for it when you need something outside the payload, like `update_id`.

A handler can be `async` (usually is) and may return a value. It reaches the Bot API, the database, and outbound HTTP through the SDK.

You don't need a real update to test a handler. `npx tgcloud run` executes it on the platform with the payload you supply and your current local code:

```bash
npx tgcloud run handlers/message '{ chat: { id: 1 }, text: "hi" }'
```

The argument is the payload — the same object your handler receives — in JSON5. To supply the handler's `ctx` (its second argument), add `--ctx`, e.g. `--ctx '{ update: { update_id: 1 } }'`. This runs against your **local** files, so you can try changes before deploying them. See [`run`](run.md).
