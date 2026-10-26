# ShippingQuery

Source: https://core.telegram.org/bots/api#shippingquery

[Documentation index](../llms.txt)

This object contains information about an incoming shipping query.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique query identifier |
| from | [User](user.md) | User who sent the query |
| invoice\_payload | String | Bot-specified invoice payload |
| shipping\_address | [ShippingAddress](shippingaddress.md) | User specified shipping address |
