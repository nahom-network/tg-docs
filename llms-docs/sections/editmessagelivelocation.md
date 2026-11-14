# editMessageLiveLocation

Source: https://core.telegram.org/bots/api#editmessagelivelocation

[Documentation index](../llms.txt)

Use this method to edit live location messages. A location can be edited until its *live\_period* expires or editing is explicitly disabled by a call to [stopMessageLiveLocation](stopmessagelivelocation.md). On success, if the edited message is not an inline message, the edited [Message](message.md) is returned, otherwise *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message to be edited was sent |
| chat\_id | Integer or String | Optional | Required if *inline\_message\_id* is not specified. Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username`. |
| message\_id | Integer | Optional | Required if *inline\_message\_id* is not specified. Identifier of the message to edit. |
| inline\_message\_id | String | Optional | Required if *chat\_id* and *message\_id* are not specified. Identifier of the inline message. |
| latitude | Float | Yes | Latitude of new location |
| longitude | Float | Yes | Longitude of new location |
| live\_period | Integer | Optional | New period in seconds during which the location can be updated, starting from the message send date. If 0x7FFFFFFF is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current *live\_period* by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then *live\_period* remains unchanged. |
| horizontal\_accuracy | Float | Optional | The radius of uncertainty for the location, measured in meters; 0-1500 |
| heading | Integer | Optional | Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. |
| proximity\_alert\_radius | Integer | Optional | The maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for a new [inline keyboard](../external/bots/features.md#inline-keyboards) |
