# On the go with BotFather

Source: https://core.telegram.org/bots/serverless#on-the-go-with-botfather

[Documentation index](../llms.txt)

Down to just your phone? The whole project lives in [@BotFather](https://t.me/BotFather) too — open your bot → **Serverless** and you get everything the CLI manages, on a touchscreen:

- **Handlers** — create, edit, and test‑run update handlers; BotFather keeps the webhook in sync with the handlers you have (the same *In sync* / *Out of sync* the CLI reports).
- **Endpoints** — the functions your Mini App calls.
- **Library** — your shared `lib/` modules.
- **Database** — edit `schema.js` in the same Drizzle‑like syntax, review pending changes, and apply them; **Save** deploys.
- **Mini App Files** — the front‑end your users open in Telegram.
- **CLI Access** — grab the CLI access token here when you're back at a keyboard.

It's one and the same cloud project, so you can start a handler on your phone and `npx tgcloud pull` it to your laptop later — nothing is tied to a single client. Running a handler even shows its **Console** output right in the chat, just like [`npx tgcloud run`](run.md).
