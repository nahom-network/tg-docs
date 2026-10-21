# `login`

Source: https://core.telegram.org/bots/serverless#login

[Documentation index](../llms.txt)

```bash
npx tgcloud login
```

Prompts for your CLI access token — from [@BotFather](https://t.me/BotFather) → your bot → Serverless → CLI Access → Access token, a separate token from your [bot's API token](https://core.telegram.org/bots/api.md#authorizing-your-bot) — validates it against the platform, and saves it to `.tgcloud/credentials`. 

> `login` is the **only** command that asks for a token, and it requires an interactive terminal. In CI, set `TGCLOUD_TOKEN` instead.
