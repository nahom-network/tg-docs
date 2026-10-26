# refundStarPayment

Source: https://core.telegram.org/bots/api#refundstarpayment

[Documentation index](../llms.txt)

Refunds a successful payment in [Telegram Stars](https://t.me/BotNews/90). Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user\_id | Integer | Yes | Identifier of the user whose payment will be refunded |
| telegram\_payment\_charge\_id | String | Yes | Telegram payment identifier |
