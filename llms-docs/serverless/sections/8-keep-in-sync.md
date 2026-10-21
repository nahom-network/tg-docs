# 8. Keep in sync

Source: https://core.telegram.org/bots/serverless#8-keep-in-sync

[Documentation index](../llms.txt)

As you work, a handful of commands keep your local project and the cloud aligned: `npx tgcloud status` shows what changed, `npx tgcloud push` deploys, `npx tgcloud pull` brings your local project in line with the cloud, `npx tgcloud fetch` checks what is deployed without touching your files, and `npx tgcloud reset` discards local changes. 

> If two people (or two machines) deploy to the same bot, the platform detects the conflict and `push` stops to let you `pull` first — you can never silently overwrite someone else's work. See [Staying in sync](staying-in-sync.md).
