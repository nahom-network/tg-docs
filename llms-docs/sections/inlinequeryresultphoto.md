# InlineQueryResultPhoto

Source: https://core.telegram.org/bots/api#inlinequeryresultphoto

[Documentation index](../llms.txt)

Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the photo.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *photo* |
| id | String | Unique identifier for this result, 1-64 bytes |
| photo\_url | String | A valid URL of the photo. Photo must be in **JPEG** format. Photo size must not exceed 5MB. |
| thumbnail\_url | String | URL of the thumbnail for the photo |
| photo\_width | Integer | *Optional*. Width of the photo |
| photo\_height | Integer | *Optional*. Height of the photo |
| title | String | *Optional*. Title for the result |
| description | String | *Optional*. Short description of the result |
| caption | String | *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the photo caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| show\_caption\_above\_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the photo |
