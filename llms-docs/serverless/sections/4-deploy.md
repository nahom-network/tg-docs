# 4. Deploy

Source: https://core.telegram.org/bots/serverless#4-deploy

[Documentation index](../llms.txt)

Send your modules to the cloud:

```bash
npx tgcloud push
```

`push` uploads every changed module in one atomic batch and updates your local record of what the cloud now holds. Your bot is live: open it in Telegram and send it a message — the starter handler echoes it back.

> **Deploying never touches your database.** Pushing code and changing your database schema are deliberately separate steps, so a code deploy can never surprise you with a data migration. That is what the next step is for.
