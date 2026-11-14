# InlineQueryResultLocation

Source: https://core.telegram.org/bots/api#inlinequeryresultlocation

[Documentation index](../llms.txt)

Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the location.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *location* |
| id | String | Unique identifier for this result, 1-64 Bytes |
| latitude | Float | Location latitude in degrees |
| longitude | Float | Location longitude in degrees |
| title | String | Location title |
| horizontal\_accuracy | Float | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 |
| live\_period | Integer | *Optional*. Period in seconds during which the location can be updated, must be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely |
| heading | Integer | *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. |
| proximity\_alert\_radius | Integer | *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](../external/bots/features.md#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the location |
| thumbnail\_url | String | *Optional*. Url of the thumbnail for the result |
| thumbnail\_width | Integer | *Optional*. Thumbnail width |
| thumbnail\_height | Integer | *Optional*. Thumbnail height |
