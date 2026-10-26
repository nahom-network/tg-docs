# InlineQueryResultVoice

Source: https://core.telegram.org/bots/api#inlinequeryresultvoice

[Documentation index](../llms.txt)

Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the the voice message.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *voice* |
| id | String | Unique identifier for this result, 1-64 bytes |
| voice\_url | String | A valid URL for the voice recording |
| title | String | Recording title |
| caption | String | *Optional*. Caption, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| voice\_duration | Integer | *Optional*. Recording duration in seconds |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the voice recording |
