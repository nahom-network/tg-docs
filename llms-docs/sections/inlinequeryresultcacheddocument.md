# InlineQueryResultCachedDocument

Source: https://core.telegram.org/bots/api#inlinequeryresultcacheddocument

[Documentation index](../llms.txt)

Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the file.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *document* |
| id | String | Unique identifier for this result, 1-64 bytes |
| title | String | Title for the result |
| document\_file\_id | String | A valid file identifier for the file |
| description | String | *Optional*. Short description of the result |
| caption | String | *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the document caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](../external/bots/features.md#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the file |
