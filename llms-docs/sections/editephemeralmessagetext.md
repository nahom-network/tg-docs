# editEphemeralMessageText

Source: https://core.telegram.org/bots/api#editephemeralmessagetext

[Documentation index](../llms.txt)

Use this method to edit an ephemeral text or rich message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| receiver\_user\_id | Integer | Yes | Identifier of the user who received the message |
| ephemeral\_message\_id | Integer | Yes | Identifier of the ephemeral message to edit |
| text | String | Optional | New text of the message, 1-4096 characters after entity parsing; required if *rich\_message* isn't specified |
| parse\_mode | String | Optional | Mode for parsing entities in the message text. See [formatting options](formatting-options.md) for more details. |
| entities | Array of [MessageEntity](messageentity.md) | Optional | A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse\_mode* |
| rich\_message | [InputRichMessage](inputrichmessage.md) | Optional | New rich content of the message; required if *text* isn't specified |
| link\_preview\_options | [LinkPreviewOptions](linkpreviewoptions.md) | Optional | Link preview generation options for the message |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for an [inline keyboard](../external/bots/features.md#inline-keyboards) |
