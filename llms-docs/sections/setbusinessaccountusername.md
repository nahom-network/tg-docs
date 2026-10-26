# setBusinessAccountUsername

Source: https://core.telegram.org/bots/api#setbusinessaccountusername

[Documentation index](../llms.txt)

Changes the username of a managed business account. Requires the *can\_change\_username* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| username | String | Optional | The new value of the username for the business account; 0-32 characters |
