# deleteChatStickerSet

Source: https://core.telegram.org/bots/api#deletechatstickerset

[Documentation index](../llms.txt)

Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field *can\_set\_sticker\_set* optionally returned in [getChat](getchat.md) requests to check if the bot can use this method. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
