# editMessageText

Source: https://core.telegram.org/bots/api#editmessagetext

[Documentation index](../llms.txt)

Use this method to edit text, rich and [game](games.md) messages. On success, if the edited message is not an inline message, the edited [Message](message.md) is returned, otherwise *True* is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message to be edited was sent |
| chat\_id | Integer or String | Optional | Required if *inline\_message\_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup, or channel in the format `@username`. |
| message\_id | Integer | Optional | Required if *inline\_message\_id* is not specified. Identifier of the message to edit. |
| inline\_message\_id | String | Optional | Required if *chat\_id* and *message\_id* are not specified. Identifier of the inline message. |
| text | String | Optional | New text of the message, 1-4096 characters after entity parsing; required if *rich\_message* isn't specified |
| parse\_mode | String | Optional | Mode for parsing entities in the message text. See [formatting options](formatting-options.md) for more details. |
| entities | Array of [MessageEntity](messageentity.md) | Optional | A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse\_mode* |
| link\_preview\_options | [LinkPreviewOptions](linkpreviewoptions.md) | Optional | Link preview generation options for the message |
| rich\_message | [InputRichMessage](inputrichmessage.md) | Optional | New rich content of the message; required if *text* isn't specified. Direct upload of new files and explicit upload of files by a URL isn't supported when an inline message is edited. |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for an [inline keyboard](../external/bots/features.md#inline-keyboards) |
