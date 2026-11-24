# 2. Link your bot

Source: https://core.telegram.org/bots/serverless#2-link-your-bot

[Documentation index](../llms.txt)

Every project is tied to one bot. Connect them with `login`, which asks for your CLI access token ([@BotFather](https://t.me/BotFather) → your bot → Serverless → CLI Access → Access token — a separate token from your [bot's API token](https://core.telegram.org/bots/api.md#authorizing-your-bot)) and stores it locally:

```bash
npx tgcloud login
```

The token has the form `app<id>:<secret>`. The CLI keeps it in `.tgcloud/`, which is git‑ignored, and never prints the secret part. Login is the only time you are asked for it — see [Authentication](authentication.md) for how tokens are resolved in CI.
