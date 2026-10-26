# editEphemeralMessageMedia

Source: https://core.telegram.org/bots/api#editephemeralmessagemedia

[Documentation index](../llms.txt)

Use this method to edit the media of an ephemeral message. Note that it is not guaranteed that the user will receive the message edit event, especially if they are offline. On success, *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| receiver\_user\_id | Integer | Yes | Identifier of the user who received the message |
| ephemeral\_message\_id | Integer | Yes | Identifier of the ephemeral message to edit |
| media | [InputMedia](inputmedia.md) | Yes | A JSON-serialized object for the new media content of the message |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) |
