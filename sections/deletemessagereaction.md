# deleteMessageReaction

Source: https://core.telegram.org/bots/api#deletemessagereaction

[Documentation index](../llms.txt)

Use this method to remove a reaction from a message in a group or a supergroup chat. The bot must have the 'can\_delete\_messages' administrator right in the chat. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| message\_id | Integer | Yes | Identifier of the target message |
| user\_id | Integer | Optional | Identifier of the user whose reaction will be removed, if the reaction was added by a user |
| actor\_chat\_id | Integer | Optional | Identifier of the chat whose reaction will be removed, if the reaction was added by a chat |
