# InlineQueryResultVideo

Source: https://core.telegram.org/bots/api#inlinequeryresultvideo

[Documentation index](../llms.txt)

Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the video.

> If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you **must** replace its content using *input\_message\_content*.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *video* |
| id | String | Unique identifier for this result, 1-64 bytes |
| video\_url | String | A valid URL for the embedded video player or video file |
| mime\_type | String | MIME type of the content of the video URL, “text/html” or “video/mp4” |
| thumbnail\_url | String | URL of the thumbnail (JPEG only) for the video |
| title | String | Title for the result |
| caption | String | *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the video caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| show\_caption\_above\_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| video\_width | Integer | *Optional*. Video width |
| video\_height | Integer | *Optional*. Video height |
| video\_duration | Integer | *Optional*. Video duration in seconds |
| description | String | *Optional*. Short description of the result |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the video. This field is **required** if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video). |
