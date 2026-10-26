# Sticker

Source: https://core.telegram.org/bots/api#sticker

[Documentation index](../llms.txt)

This object represents a sticker.

| Field | Type | Description |
| --- | --- | --- |
| file\_id | String | Identifier for this file, which can be used to download or reuse the file |
| file\_unique\_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| type | String | Type of the sticker, currently one of “regular”, “mask”, “custom\_emoji”. The type of the sticker is independent from its format, which is determined by the fields *is\_animated* and *is\_video*. |
| width | Integer | Sticker width |
| height | Integer | Sticker height |
| is\_animated | Boolean | *True*, if the sticker is [animated](https://telegram.org/blog/animated-stickers) |
| is\_video | Boolean | *True*, if the sticker is a [video sticker](https://telegram.org/blog/video-stickers-better-reactions) |
| thumbnail | [PhotoSize](photosize.md) | *Optional*. Sticker thumbnail in the .WEBP or .JPG format |
| emoji | String | *Optional*. Emoji associated with the sticker |
| set\_name | String | *Optional*. Name of the sticker set to which the sticker belongs |
| premium\_animation | [File](file.md) | *Optional*. For premium regular stickers, premium animation for the sticker |
| mask\_position | [MaskPosition](maskposition.md) | *Optional*. For mask stickers, the position where the mask should be placed |
| custom\_emoji\_id | String | *Optional*. For custom emoji stickers, unique identifier of the custom emoji |
| needs\_repainting | True | *Optional*. *True*, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places |
| file\_size | Integer | *Optional*. File size in bytes |
