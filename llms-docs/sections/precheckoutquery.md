# PreCheckoutQuery

Source: https://core.telegram.org/bots/api#precheckoutquery

[Documentation index](../llms.txt)

This object contains information about an incoming pre-checkout query.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique query identifier |
| from | [User](user.md) | User who sent the query |
| currency | String | Three-letter ISO 4217 [currency](../external/bots/payments.md#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90) |
| total\_amount | Integer | Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). |
| invoice\_payload | String | Bot-specified invoice payload |
| shipping\_option\_id | String | *Optional*. Identifier of the shipping option chosen by the user |
| order\_info | [OrderInfo](orderinfo.md) | *Optional*. Order information provided by the user |
