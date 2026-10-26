# editChatSubscriptionInviteLink

Source: https://core.telegram.org/bots/api#editchatsubscriptioninvitelink

[Documentation index](../llms.txt)

Use this method to edit a subscription invite link created by the bot. The bot must have the *can\_invite\_users* administrator rights. Returns the edited invite link as a [ChatInviteLink](chatinvitelink.md) object.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target channel in the format `@username` |
| invite\_link | String | Yes | The invite link to edit |
| name | String | Optional | Invite link name; 0-32 characters |
