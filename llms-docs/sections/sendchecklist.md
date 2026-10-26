# sendChecklist

Source: https://core.telegram.org/bots/api#sendchecklist

[Documentation index](../llms.txt)

Use this method to send a checklist on behalf of a connected business account. On success, the sent [Message](message.md) is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection on behalf of which the message will be sent |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot in the format `@username` |
| checklist | [InputChecklist](inputchecklist.md) | Yes | A JSON-serialized object for the checklist to send |
| disable\_notification | Boolean | Optional | Sends the message silently. Users will receive a notification with no sound. |
| protect\_content | Boolean | Optional | Protects the contents of the sent message from forwarding and saving |
| message\_effect\_id | String | Optional | Unique identifier of the message effect to be added to the message |
| reply\_parameters | [ReplyParameters](replyparameters.md) | Optional | A JSON-serialized object for description of the message to reply to |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) |
