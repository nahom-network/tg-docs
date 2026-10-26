# TransactionPartnerUser

Source: https://core.telegram.org/bots/api#transactionpartneruser

[Documentation index](../llms.txt)

Describes a transaction with a user.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the transaction partner, always “user” |
| transaction\_type | String | Type of the transaction, currently one of “invoice\_payment” for payments via invoices, “paid\_media\_payment” for payments for paid media, “gift\_purchase” for gifts sent by the bot, “premium\_purchase” for Telegram Premium subscriptions gifted by the bot, “business\_account\_transfer” for direct transfers from managed business accounts |
| user | [User](user.md) | Information about the user |
| affiliate | [AffiliateInfo](affiliateinfo.md) | *Optional*. Information about the affiliate that received a commission via this transaction. Can be available only for “invoice\_payment” and “paid\_media\_payment” transactions. |
| invoice\_payload | String | *Optional*. Bot-specified invoice payload. Can be available only for “invoice\_payment” transactions. |
| subscription\_period | Integer | *Optional*. The duration of the paid subscription. Can be available only for “invoice\_payment” transactions. |
| paid\_media | Array of [PaidMedia](paidmedia.md) | *Optional*. Information about the paid media bought by the user; for “paid\_media\_payment” transactions only |
| paid\_media\_payload | String | *Optional*. Bot-specified paid media payload. Can be available only for “paid\_media\_payment” transactions. |
| gift | [Gift](gift.md) | *Optional*. The gift sent to the user by the bot; for “gift\_purchase” transactions only |
| premium\_subscription\_duration | Integer | *Optional*. Number of months the gifted Telegram Premium subscription will be active for; for “premium\_purchase” transactions only |
