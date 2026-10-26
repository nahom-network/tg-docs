# OwnedGiftUnique

Source: https://core.telegram.org/bots/api#ownedgiftunique

[Documentation index](../llms.txt)

Describes a unique gift received and owned by a user or a chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the gift, always “unique” |
| gift | [UniqueGift](uniquegift.md) | Information about the unique gift |
| owned\_gift\_id | String | *Optional*. Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only |
| sender\_user | [User](user.md) | *Optional*. Sender of the gift if it is a known user |
| send\_date | Integer | Date the gift was sent in Unix time |
| is\_saved | True | *Optional*. *True*, if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only |
| can\_be\_transferred | True | *Optional*. *True*, if the gift can be transferred to another owner; for gifts received on behalf of business accounts only |
| transfer\_star\_count | Integer | *Optional*. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift |
| next\_transfer\_date | Integer | *Optional*. Point in time (Unix timestamp) when the gift can be transferred. If it is in the past, then the gift can be transferred now. |
