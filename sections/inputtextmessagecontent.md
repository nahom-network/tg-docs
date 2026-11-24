# InputTextMessageContent

Source: https://core.telegram.org/bots/api#inputtextmessagecontent

[Documentation index](../llms.txt)

Represents the [content](inputmessagecontent.md) of a text message to be sent as the result of an inline query.

| Field | Type | Description |
| --- | --- | --- |
| message\_text | String | Text of the message to be sent, 1-4096 characters |
| parse\_mode | String | *Optional*. Mode for parsing entities in the message text. See [formatting options](formatting-options.md) for more details. |
| entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in message text, which can be specified instead of *parse\_mode* |
| link\_preview\_options | [LinkPreviewOptions](linkpreviewoptions.md) | *Optional*. Link preview generation options for the message |
