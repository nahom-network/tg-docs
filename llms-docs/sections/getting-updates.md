# Getting updates

Source: https://core.telegram.org/bots/api#getting-updates

[Documentation index](../llms.txt)

There are two mutually exclusive ways of receiving updates for your bot - the [getUpdates](getupdates.md) method on one hand and [webhooks](setwebhook.md) on the other. Incoming updates are stored on the server until the bot receives them either way, but they will not be kept longer than 24 hours.

Regardless of which option you choose, you will receive JSON-serialized [Update](update.md) objects as a result.

## In this section

- [Update](update.md)
- [getUpdates](getupdates.md)
- [setWebhook](setwebhook.md)
- [deleteWebhook](deletewebhook.md)
- [getWebhookInfo](getwebhookinfo.md)
- [WebhookInfo](webhookinfo.md)
