# OwnedGiftRegular

Source: https://core.telegram.org/bots/api#ownedgiftregular

[Documentation index](../llms.txt)

Describes a regular gift owned by a user or a chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the gift, always “regular” |
| gift | [Gift](gift.md) | Information about the regular gift |
| owned\_gift\_id | String | *Optional*. Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only |
| sender\_user | [User](user.md) | *Optional*. Sender of the gift if it is a known user |
| send\_date | Integer | Date the gift was sent in Unix time |
| text | String | *Optional*. Text of the message that was added to the gift |
| entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities that appear in the text |
| is\_private | True | *Optional*. *True*, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them |
| is\_saved | True | *Optional*. *True*, if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only |
| can\_be\_upgraded | True | *Optional*. *True*, if the gift can be upgraded to a unique gift; for gifts received on behalf of business accounts only |
| was\_refunded | True | *Optional*. *True*, if the gift was refunded and isn't available anymore |
| convert\_star\_count | Integer | *Optional*. Number of Telegram Stars that can be claimed by the receiver instead of the gift; omitted if the gift cannot be converted to Telegram Stars; for gifts received on behalf of business accounts only |
| prepaid\_upgrade\_star\_count | Integer | *Optional*. Number of Telegram Stars that were paid for the ability to upgrade the gift |
| is\_upgrade\_separate | True | *Optional*. *True*, if the gift's upgrade was purchased after the gift was sent; for gifts received on behalf of business accounts only |
| unique\_gift\_number | Integer | *Optional*. Unique number reserved for this gift when upgraded. See the *number* field in [UniqueGift](uniquegift.md). |
