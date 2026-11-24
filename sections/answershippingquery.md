# answerShippingQuery

Source: https://core.telegram.org/bots/api#answershippingquery

[Documentation index](../llms.txt)

If you sent an invoice requesting a shipping address and the parameter *is\_flexible* was specified, the Bot API will send an [Update](update.md) with a *shipping\_query* field to the bot. Use this method to reply to shipping queries. On success, *True* is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| shipping\_query\_id | String | Yes | Unique identifier for the query to be answered |
| ok | Boolean | Yes | Pass *True* if delivery to the specified address is possible and *False* if there are any problems (for example, if delivery to the specified address is not possible) |
| shipping\_options | Array of [ShippingOption](shippingoption.md) | Optional | Required if *ok* is *True*. A JSON-serialized Array of available shipping options. |
| error\_message | String | Optional | Required if *ok* is *False*. Error message in human readable form that explains why it is impossible to complete the order (e.g. “Sorry, delivery to your desired address is unavailable”). Telegram will display this message to the user. |
