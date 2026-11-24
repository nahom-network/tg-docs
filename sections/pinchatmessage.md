# pinChatMessage

Source: https://core.telegram.org/bots/api#pinchatmessage

[Documentation index](../llms.txt)

Use this method to add a message to the list of pinned messages in a chat. In private chats and channel direct messages chats, all non-service messages can be pinned. Conversely, the bot must be an administrator with the 'can\_pin\_messages' right or the 'can\_edit\_messages' right to pin messages in groups and channels respectively. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message will be pinned |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target channel in the format `@username` |
| message\_id | Integer | Yes | Identifier of a message to pin |
| disable\_notification | Boolean | Optional | Pass *True* if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats. |
