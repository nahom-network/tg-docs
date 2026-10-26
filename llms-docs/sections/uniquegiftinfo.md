# UniqueGiftInfo

Source: https://core.telegram.org/bots/api#uniquegiftinfo

[Documentation index](../llms.txt)

Describes a service message about a unique gift that was sent or received.

| Field | Type | Description |
| --- | --- | --- |
| gift | [UniqueGift](uniquegift.md) | Information about the gift |
| origin | String | Origin of the gift. Currently, either “upgrade” for gifts upgraded from regular gifts, “transfer” for gifts transferred from other users or channels, “resale” for gifts bought from other users, “gifted\_upgrade” for upgrades purchased after the gift was sent, or “offer” for gifts bought or sold through gift purchase offers. |
| text | String | *Optional*. Text of the message that was added to the gift |
| entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities that appear in the text |
| is\_private | True | *Optional*. *True*, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them |
| last\_resale\_currency | String | *Optional*. For gifts bought from other users, the currency in which the payment for the gift was done. Currently, one of “XTR” for Telegram Stars or “TON” for TON grams. |
| last\_resale\_amount | Integer | *Optional*. For gifts bought from other users, the price paid for the gift in either Telegram Stars or nanograms |
| owned\_gift\_id | String | *Optional*. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts |
| transfer\_star\_count | Integer | *Optional*. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift |
| next\_transfer\_date | Integer | *Optional*. Point in time (Unix timestamp) when the gift can be transferred. If it is in the past, then the gift can be transferred now. |
