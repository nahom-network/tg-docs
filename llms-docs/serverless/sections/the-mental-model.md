# The mental model

Source: https://core.telegram.org/bots/serverless#the-mental-model

[Documentation index](../llms.txt)

You work in **three places**, and they map cleanly onto each other:

| Where | What lives there |
|---|---|
| Your project folder | JavaScript modules — schema, shared code, update handlers, Mini App endpoints — and, if you have one, the Mini App's front‑end |
| The cloud | The deployed copy of those modules, your bot's database, and the Mini App's files |
| The `tgcloud` CLI | The bridge — it shows you differences and syncs them |

You never SSH into anything. You edit files locally, run `npx tgcloud push`, and the platform takes it from there. Your bot's traffic is handled by the deployed modules; your database persists between invocations.

A project has just four kinds of code, all inside one `tgcloud/` folder:

```bash
tgcloud/
├─ endpoints/  # functions your Mini App calls
├─ handlers/   # functions that react to Telegram update types
├─ lib/        # shared code you import from anywhere
└─ schema.js   # your database tables
```

When an update arrives — a message, a button press, an inline query — Telegram routes it to the matching handler (`handlers/message.js`, `handlers/callback_query.js`, …) and calls its default export. That function talks to the Bot API and the database through the SDK, and returns. That is the whole loop. An update with no matching handler is simply ignored, so you add only the handlers you need.

A Mini App is optional. If your bot has one, its front‑end lives in the same project, next to `tgcloud/`. Serverless hosts its build output and runs the `endpoints/` it calls. See [Mini App front‑end](mini-app-front-end.md).
