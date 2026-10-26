# setStickerEmojiList

Source: https://core.telegram.org/bots/api#setstickeremojilist

[Documentation index](../llms.txt)

Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sticker | String | Yes | File identifier of the sticker |
| emoji\_list | Array of String | Yes | A JSON-serialized list of 1-20 emoji associated with the sticker |
