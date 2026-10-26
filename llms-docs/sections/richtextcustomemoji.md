# RichTextCustomEmoji

Source: https://core.telegram.org/bots/api#richtextcustomemoji

[Documentation index](../llms.txt)

A custom emoji.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the rich text, always “custom\_emoji” |
| custom\_emoji\_id | String | Unique identifier of the custom emoji. Use [getCustomEmojiStickers](getcustomemojistickers.md) to get full information about the sticker. |
| alternative\_text | String | Alternative emoji for the custom emoji |
