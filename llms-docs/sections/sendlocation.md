# sendLocation

Source: https://core.telegram.org/bots/api#sendlocation

[Documentation index](../llms.txt)

Use this method to send point on the map. On success, the sent [Message](message.md) is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message will be sent |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username` |
| message\_thread\_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| direct\_messages\_topic\_id | Integer | Optional | Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat |
| ephemeral\_message\_parameters | [EphemeralMessageParameters](ephemeralmessageparameters.md) | Optional | A JSON-serialized object containing the parameters of the ephemeral message to send |
| latitude | Float | Yes | Latitude of the location |
| longitude | Float | Yes | Longitude of the location |
| horizontal\_accuracy | Float | Optional | The radius of uncertainty for the location, measured in meters; 0-1500 |
| live\_period | Integer | Optional | Period in seconds during which the location will be updated (see [Live Locations](https://telegram.org/blog/live-locations)), must be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely. Must be 0 for ephemeral messages. |
| heading | Integer | Optional | For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. |
| proximity\_alert\_radius | Integer | Optional | For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. |
| disable\_notification | Boolean | Optional | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect\_content | Boolean | Optional | Protects the contents of the sent message from forwarding and saving |
| allow\_paid\_broadcast | Boolean | Optional | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](../external/bots/faq.md#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. |
| message\_effect\_id | String | Optional | Unique identifier of the message effect to be added to the message; for private chats only |
| suggested\_post\_parameters | [SuggestedPostParameters](suggestedpostparameters.md) | Optional | A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. |
| reply\_parameters | [ReplyParameters](replyparameters.md) | Optional | Description of the message to reply to |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) or [ReplyKeyboardMarkup](replykeyboardmarkup.md) or [ReplyKeyboardRemove](replykeyboardremove.md) or [ForceReply](forcereply.md) | Optional | Additional interface options. A JSON-serialized object for an [inline keyboard](../external/bots/features.md#inline-keyboards), [custom reply keyboard](../external/bots/features.md#keyboards), instructions to remove a reply keyboard or to force a reply from the user. |
