# setBusinessAccountName

Source: https://core.telegram.org/bots/api#setbusinessaccountname

[Documentation index](../llms.txt)

Changes the first and last name of a managed business account. Requires the *can\_change\_name* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| first\_name | String | Yes | The new value of the first name for the business account; 1-64 characters |
| last\_name | String | Optional | The new value of the last name for the business account; 0-64 characters |
