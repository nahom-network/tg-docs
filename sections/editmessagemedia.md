# editMessageMedia

Source: https://core.telegram.org/bots/api#editmessagemedia

[Documentation index](../llms.txt)

Use this method to edit animation, audio, document, live photo, photo, or video messages, or to replace a text or a rich message with a media. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo, a live photo, or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file\_id or specify a URL. On success, if the edited message is not an inline message, the edited [Message](message.md) is returned, otherwise *True* is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within **48 hours** from the time they were sent.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message to be edited was sent |
| chat\_id | Integer or String | Optional | Required if *inline\_message\_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup, or channel in the format `@username`. |
| message\_id | Integer | Optional | Required if *inline\_message\_id* is not specified. Identifier of the message to edit. |
| inline\_message\_id | String | Optional | Required if *chat\_id* and *message\_id* are not specified. Identifier of the inline message. |
| media | [InputMedia](inputmedia.md) | Yes | A JSON-serialized object for the new media content of the message |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for a new [inline keyboard](../external/bots/features.md#inline-keyboards) |
