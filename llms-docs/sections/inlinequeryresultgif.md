# InlineQueryResultGif

Source: https://core.telegram.org/bots/api#inlinequeryresultgif

[Documentation index](../llms.txt)

Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the animation.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *gif* |
| id | String | Unique identifier for this result, 1-64 bytes |
| gif\_url | String | A valid URL for the GIF file |
| gif\_width | Integer | *Optional*. Width of the GIF |
| gif\_height | Integer | *Optional*. Height of the GIF |
| gif\_duration | Integer | *Optional*. Duration of the GIF in seconds |
| thumbnail\_url | String | URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result |
| thumbnail\_mime\_type | String | *Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”. |
| title | String | *Optional*. Title for the result |
| caption | String | *Optional*. Caption of the GIF file to be sent, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| show\_caption\_above\_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](../external/bots/features.md#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the GIF animation |
