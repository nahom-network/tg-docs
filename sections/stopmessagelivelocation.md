# stopMessageLiveLocation

Source: https://core.telegram.org/bots/api#stopmessagelivelocation

[Documentation index](../llms.txt)

Use this method to stop updating a live location message before *live\_period* expires. On success, if the message is not an inline message, the edited [Message](message.md) is returned, otherwise *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message to be edited was sent |
| chat\_id | Integer or String | Optional | Required if *inline\_message\_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`. |
| message\_id | Integer | Optional | Required if *inline\_message\_id* is not specified. Identifier of the message with live location to stop. |
| inline\_message\_id | String | Optional | Required if *chat\_id* and *message\_id* are not specified. Identifier of the inline message. |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for a new [inline keyboard](../external/bots/features.md#inline-keyboards) |
