# InlineQueryResultArticle

Source: https://core.telegram.org/bots/api#inlinequeryresultarticle

[Documentation index](../llms.txt)

Represents a link to an article or web page.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *article* |
| id | String | Unique identifier for this result, 1-64 Bytes |
| title | String | Title of the result |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | Content of the message to be sent |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](../external/bots/features.md#inline-keyboards) attached to the message |
| url | String | *Optional*. URL of the result |
| description | String | *Optional*. Short description of the result |
| thumbnail\_url | String | *Optional*. Url of the thumbnail for the result |
| thumbnail\_width | Integer | *Optional*. Thumbnail width |
| thumbnail\_height | Integer | *Optional*. Thumbnail height |
