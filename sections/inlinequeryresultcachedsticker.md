# InlineQueryResultCachedSticker

Source: https://core.telegram.org/bots/api#inlinequeryresultcachedsticker

[Documentation index](../llms.txt)

Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the sticker.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *sticker* |
| id | String | Unique identifier for this result, 1-64 bytes |
| sticker\_file\_id | String | A valid file identifier of the sticker |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](../external/bots/features.md#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the sticker |
