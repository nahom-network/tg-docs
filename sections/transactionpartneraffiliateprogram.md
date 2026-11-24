# TransactionPartnerAffiliateProgram

Source: https://core.telegram.org/bots/api#transactionpartneraffiliateprogram

[Documentation index](../llms.txt)

Describes the affiliate program that issued the affiliate commission received via this transaction.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the transaction partner, always “affiliate\_program” |
| sponsor\_user | [User](user.md) | *Optional*. Information about the bot that sponsored the affiliate program |
| commission\_per\_mille | Integer | The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users |
