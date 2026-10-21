# replaceStickerInSet

Source: https://core.telegram.org/bots/api#replacestickerinset

[Documentation index](../llms.txt)

Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling [deleteStickerFromSet](deletestickerfromset.md), then [addStickerToSet](addstickertoset.md), then [setStickerPositionInSet](setstickerpositioninset.md). Returns *True* on success.

| Parameter   | Type                                                            | Required | Description                                                                                                                                                       |
| ----------- | --------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id     | Integer                                                         | Yes      | User identifier of the sticker set owner                                                                                                                          |
| name        | String                                                          | Yes      | Sticker set name                                                                                                                                                  |
| old_sticker | String                                                          | Yes      | File identifier of the replaced sticker                                                                                                                           |
| sticker     | [InputSticker](inputsticker.md) | Yes      | A JSON-serialized object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged. |
