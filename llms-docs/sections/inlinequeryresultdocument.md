# InlineQueryResultDocument

Source: https://core.telegram.org/bots/api#inlinequeryresultdocument

[Documentation index](../llms.txt)

Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the file. Currently, only **.PDF** and **.ZIP** files can be sent using this method.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *document* |
| id | String | Unique identifier for this result, 1-64 bytes |
| title | String | Title for the result |
| caption | String | *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the document caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| document\_url | String | A valid URL for the file |
| mime\_type | String | MIME type of the content of the file, either “application/pdf” or “application/zip” |
| description | String | *Optional*. Short description of the result |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the file |
| thumbnail\_url | String | *Optional*. URL of the thumbnail (JPEG only) for the file |
| thumbnail\_width | Integer | *Optional*. Thumbnail width |
| thumbnail\_height | Integer | *Optional*. Thumbnail height |
