# InlineQueryResultCachedVoice

Source: https://core.telegram.org/bots/api#inlinequeryresultcachedvoice

[Documentation index](../llms.txt)

Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the voice message.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *voice* |
| id | String | Unique identifier for this result, 1-64 bytes |
| voice\_file\_id | String | A valid file identifier for the voice message |
| title | String | Voice message title |
| caption | String | *Optional*. Caption, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the voice message |
