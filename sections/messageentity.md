# MessageEntity

Source: https://core.telegram.org/bots/api#messageentity

[Documentation index](../llms.txt)

This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the entity. Currently, can be “mention” (`@username`), “hashtag” (`#hashtag` or `#hashtag@chatusername`), “cashtag” (`$USD` or `$USD@chatusername`), “bot\_command” (`/start@jobs_bot`), “url” (`https://telegram.org`), “email” (`do-not-reply@telegram.org`), “phone\_number” (`+1-212-555-0123`), “bank\_card\_number” (bank card number), “ton\_address” (address in the TON blockchain), “bold” (**bold text**), “italic” (*italic text*), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “blockquote” (block quotation), “expandable\_blockquote” (collapsed-by-default block quotation), “code” (monowidth string), “pre” (monowidth block), “text\_link” (for clickable text URLs), “text\_mention” (for users [without usernames](https://telegram.org/blog/edit#new-mentions)), “custom\_emoji” (for inline custom emoji stickers), or “date\_time” (for formatted date and time). |
| offset | Integer | Offset in [UTF-16 code units](../external/api/entities.md#entity-length) to the start of the entity |
| length | Integer | Length of the entity in [UTF-16 code units](../external/api/entities.md#entity-length) |
| url | String | *Optional*. For “text\_link” only, URL that will be opened after user taps on the text |
| user | [User](user.md) | *Optional*. For “text\_mention” only, the mentioned user |
| language | String | *Optional*. For “pre” only, the programming language of the entity text |
| custom\_emoji\_id | String | *Optional*. For “custom\_emoji” only, unique identifier of the custom emoji. Use [getCustomEmojiStickers](getcustomemojistickers.md) to get full information about the sticker. |
| unix\_time | Integer | *Optional*. For “date\_time” only, the Unix time associated with the entity |
| date\_time\_format | String | *Optional*. For “date\_time” only, the string that defines the formatting of the date and time. See [date-time entity formatting](formatting-options.md#date-time-entity-formatting) for more details. |
