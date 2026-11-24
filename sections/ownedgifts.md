# OwnedGifts

Source: https://core.telegram.org/bots/api#ownedgifts

[Documentation index](../llms.txt)

Contains the list of gifts received and owned by a user or a chat.

| Field | Type | Description |
| --- | --- | --- |
| total_count | Integer | The total number of gifts owned by the user or the chat |
| gifts | Array of [OwnedGift](ownedgift.md) | The list of gifts |
| next_offset | String | *Optional*. Offset for the next request. If empty, then there are no more results. |
