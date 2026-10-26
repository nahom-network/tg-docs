# deleteAllMessageReactions

Source: https://core.telegram.org/bots/api#deleteallmessagereactions

[Documentation index](../llms.txt)

Use this method to remove up to 10000 recent reactions in a group or a supergroup chat added by a given user or chat. The bot must have the 'can\_delete\_messages' administrator right in the chat. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| user\_id | Integer | Optional | Identifier of the user whose reactions will be removed, if the reactions were added by a user |
| actor\_chat\_id | Integer | Optional | Identifier of the chat whose reactions will be removed, if the reactions were added by a chat |
