# editMessageReplyMarkup

Source: https://core.telegram.org/bots/api#editmessagereplymarkup

[Documentation index](../llms.txt)

Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited [Message](message.md) is returned, otherwise *True* is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message to be edited was sent |
| chat\_id | Integer or String | Optional | Required if *inline\_message\_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`. |
| message\_id | Integer | Optional | Required if *inline\_message\_id* is not specified. Identifier of the message to edit. |
| inline\_message\_id | String | Optional | Required if *chat\_id* and *message\_id* are not specified. Identifier of the inline message. |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for an [inline keyboard](../external/bots/features.md#inline-keyboards) |
