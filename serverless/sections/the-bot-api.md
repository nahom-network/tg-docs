# The Bot API

Source: https://core.telegram.org/bots/serverless#the-bot-api

[Documentation index](../llms.txt)

`api` gives you the entire [Telegram Bot API](https://core.telegram.org/bots/api.md). Call any method as `api.<method>(params)`. Every current — and future — Bot API method works with **no SDK update** required.

```js
import { api } from 'sdk';

const me = await api.getMe();                            // → the unwrapped result
await api.sendMessage({ chat_id: id, text: 'Hello!' });
await api.editMessageText({ chat_id, message_id, text: 'Updated' });
await api.answerCallbackQuery({ callback_query_id, text: 'Done' });
```

**The response envelope is unwrapped.** The Bot API normally wraps results in `{ ok: true, result: … }`. `api` returns the `result` directly — `getMe()` resolves to the user object, not to a wrapper. Parameters use the Bot API's own snake_case names (`chat_id`, `message_id`, `reply_markup`, …).

**Failures throw `BotApiError`.** When the Bot API returns `{ ok: false }`, the call throws a `BotApiError` instead of returning a falsy value, so you can't accidentally ignore it. The error carries `.code` (the Bot API `error_code`), `.description` (the human‑readable message), `.method` (which method failed), and `.parameters` (extra data such as `retry_after` on a 429, or `migrate_to_chat_id`). Catch it to handle an expected failure and rethrow the rest:

```js
import { api, BotApiError } from 'sdk';

try {
  await api.deleteMessage({ chat_id, message_id });
} catch (e) {
  if (e instanceof BotApiError && e.code === 400) {
    // 400 = the message is already gone; that's fine here.
  } else {
    throw e;
  }
}
```

##### Files

Work with file **bytes**, not just `file_id`s — upload new files and download existing ones.

**Upload — `InputFile`.** Wrap raw bytes in an `InputFile` (a plain holder: bytes, a filename, and an optional MIME `type`) and pass it wherever a Bot API method expects a file:

```js
import { api, InputFile } from 'sdk';

const doc = new InputFile(bytes, 'report.pdf', { type: 'application/pdf' });
await api.sendDocument({ chat_id, document: doc });

// files nested inside params work too — e.g. an album:
await api.sendMediaGroup({ chat_id, media: [
  { type: 'photo', media: new InputFile(a, 'a.jpg', { type: 'image/jpeg' }) },
  { type: 'photo', media: new InputFile(b, 'b.jpg', { type: 'image/jpeg' }) },
]});
```

The bytes are streamed to Telegram as a real multipart upload — the file isn't buffered whole into a single call to the platform — but Telegram's Bot API limits still apply: a bot can currently upload up to **50 MB** per file (and **10 MB** for a photo).

**Download — by `file_id`.** Two helpers pull a file's bytes back. The platform resolves the `file_id` for you (it runs `getFile` and fetches the content behind the scenes), so you never touch the bot token or a download URL:

```js
const bytes = await api.getFileContent(file_id);          // → Uint8Array (the whole file)

const { file, body } = await api.getFileStream(file_id);  // stream it instead
file.file_unique_id;                                      // the getFile info
for await (const chunk of body) { /* Uint8Array */ }      // or buffer it: await stream.bytes()
```

> Telegram's Bot API caps `getFile` downloads at **20 MB**, so that's the ceiling for both helpers.
