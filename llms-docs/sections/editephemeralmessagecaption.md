# editEphemeralMessageCaption

Source: https://core.telegram.org/bots/api#editephemeralmessagecaption

[Documentation index](../llms.txt)

Use this method to edit the caption of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| receiver\_user\_id | Integer | Yes | Identifier of the user who received the message |
| ephemeral\_message\_id | Integer | Yes | Identifier of the ephemeral message to edit |
| caption | String | Optional | New caption of the message, 0-1024 characters after entities parsing |
| parse\_mode | String | Optional | Mode for parsing entities in the message caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | Optional | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| show\_caption\_above\_media | Boolean | Optional | Pass *True* if the caption must be shown above the message media. Supported only for animation, photo and video messages. |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) |
