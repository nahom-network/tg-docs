# setStickerMaskPosition

Source: https://core.telegram.org/bots/api#setstickermaskposition

[Documentation index](../llms.txt)

Use this method to change the [mask position](maskposition.md) of a mask sticker. The sticker must belong to a sticker set that was created by the bot. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sticker | String | Yes | File identifier of the sticker |
| mask_position | [MaskPosition](maskposition.md) | Optional | A JSON-serialized object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position. |
