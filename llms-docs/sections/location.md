# Location

Source: https://core.telegram.org/bots/api#location

[Documentation index](../llms.txt)

This object represents a point on the map.

| Field | Type | Description |
| --- | --- | --- |
| latitude | Float | Latitude as defined by the sender |
| longitude | Float | Longitude as defined by the sender |
| horizontal\_accuracy | Float | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 |
| live\_period | Integer | *Optional*. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only. |
| heading | Integer | *Optional*. The direction in which user is moving, in degrees; 1-360. For active live locations only. |
| proximity\_alert\_radius | Integer | *Optional*. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only. |
