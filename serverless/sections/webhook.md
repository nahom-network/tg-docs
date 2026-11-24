# `webhook`

Source: https://core.telegram.org/bots/serverless#webhook

[Documentation index](../llms.txt)

```bash
npx tgcloud webhook
npx tgcloud webhook sync [--drop-pending]
```

Telegram delivers updates to your bot through a webhook, which the platform manages for you — you never point it anywhere by hand. `npx tgcloud webhook` shows its current state: the URL, the `allowed_updates` list, how many updates are pending, the last delivery error (if any), and whether it is **in sync** with your deployed handlers.

"In sync" means the webhook points at the platform and its `allowed_updates` match the handlers you've deployed — so Telegram delivers exactly the update types you handle, and nothing else. Deploying a new handler (or removing one) can leave the webhook out of sync until it's refreshed; `npx tgcloud status` flags this too.

`npx tgcloud webhook sync` fixes it — it re‑points the webhook at the platform and rebuilds `allowed_updates` from your deployed handlers. Add `--drop-pending` to discard updates Telegram had already queued before the sync (otherwise they're delivered once the webhook is healthy again).
