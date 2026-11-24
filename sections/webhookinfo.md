# WebhookInfo

Source: https://core.telegram.org/bots/api#webhookinfo

[Documentation index](../llms.txt)

Describes the current status of a webhook.

| Field | Type | Description |
| --- | --- | --- |
| url | String | Webhook URL, may be empty if webhook is not set up |
| has\_custom\_certificate | Boolean | *True*, if a custom certificate was provided for webhook certificate checks |
| pending\_update\_count | Integer | Number of updates awaiting delivery |
| ip\_address | String | *Optional*. Currently used webhook IP address |
| last\_error\_date | Integer | *Optional*. Unix time for the most recent error that happened when trying to deliver an update via webhook |
| last\_error\_message | String | *Optional*. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook |
| last\_synchronization\_error\_date | Integer | *Optional*. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters |
| max\_connections | Integer | *Optional*. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery |
| allowed\_updates | Array of String | *Optional*. A list of update types the bot is subscribed to. Defaults to all update types except *chat\_member*, *message\_reaction*, and *message\_reaction\_count*. |
