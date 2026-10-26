# SuccessfulPayment

Source: https://core.telegram.org/bots/api#successfulpayment

[Documentation index](../llms.txt)

This object contains basic information about a successful payment. Note that if the buyer initiates a chargeback with the relevant payment provider following this transaction, the funds may be debited from your balance. This is outside of Telegram's control.

| Field | Type | Description |
| --- | --- | --- |
| currency | String | Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90) |
| total\_amount | Integer | Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). |
| invoice\_payload | String | Bot-specified invoice payload |
| subscription\_expiration\_date | Integer | *Optional*. Expiration date of the subscription, in Unix time; for recurring payments only |
| is\_recurring | True | *Optional*. *True*, if the payment is a recurring payment for a subscription |
| is\_first\_recurring | True | *Optional*. *True*, if the payment is the first payment for a subscription |
| shipping\_option\_id | String | *Optional*. Identifier of the shipping option chosen by the user |
| order\_info | [OrderInfo](orderinfo.md) | *Optional*. Order information provided by the user |
| telegram\_payment\_charge\_id | String | Telegram payment identifier |
| provider\_payment\_charge\_id | String | Provider payment identifier |
