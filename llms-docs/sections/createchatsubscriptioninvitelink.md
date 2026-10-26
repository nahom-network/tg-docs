# createChatSubscriptionInviteLink

Source: https://core.telegram.org/bots/api#createchatsubscriptioninvitelink

[Documentation index](../llms.txt)

Use this method to create a [subscription invite link](https://telegram.org/blog/superchannels-star-reactions-subscriptions#star-subscriptions) for a channel chat. The bot must have the *can\_invite\_users* administrator rights. The link can be edited using the method [editChatSubscriptionInviteLink](editchatsubscriptioninvitelink.md) or revoked using the method [revokeChatInviteLink](revokechatinvitelink.md). Returns the new invite link as a [ChatInviteLink](chatinvitelink.md) object.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target channel chat or username of the target channel in the format `@username` |
| name | String | Optional | Invite link name; 0-32 characters |
| subscription\_period | Integer | Yes | The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days). |
| subscription\_price | Integer | Yes | The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1-10000 |
