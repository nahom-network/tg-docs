# transferBusinessAccountStars

Source: https://core.telegram.org/bots/api#transferbusinessaccountstars

[Documentation index](../llms.txt)

Transfers Telegram Stars from the business account balance to the bot's balance. Requires the *can\_transfer\_stars* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| star\_count | Integer | Yes | Number of Telegram Stars to transfer; 1-10000 |
