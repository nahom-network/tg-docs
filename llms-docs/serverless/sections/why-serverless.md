# Why serverless

Source: https://core.telegram.org/bots/serverless#why-serverless

[Documentation index](../llms.txt)

A Telegram bot is, at heart, a program that reacts to updates. Traditionally you had to host that program somewhere that is always on, reachable, and secure — and then keep it that way. Telegram Serverless removes that layer entirely:

- **No infrastructure.** There is no machine to rent, patch, or monitor. Your code runs on demand and scales with your bot automatically.
- **Batteries included.** The Telegram Bot API, an SQLite‑backed database, and outbound HTTP are available to every module out of the box — nothing to install, no credentials to wire up.
- **Fast, isolated execution.** Each invocation runs in a lightweight V8 isolate, close to Telegram's own systems, so calls to the Bot API and your database are quick and reliable.
- **A real developer workflow.** A project lives in a folder on your machine under version control. You edit files, see exactly what changed, deploy atomically, and roll your database schema forward with reviewed migrations — the way you already work with everything else.
