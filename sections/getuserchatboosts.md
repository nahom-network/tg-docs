# getUserChatBoosts

Source: https://core.telegram.org/bots/api#getuserchatboosts

[Documentation index](../llms.txt)

Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a [UserChatBoosts](userchatboosts.md) object.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the chat or username of the channel in the format `@username` |
| user\_id | Integer | Yes | Unique identifier of the target user |
