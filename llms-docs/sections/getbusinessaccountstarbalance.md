# getBusinessAccountStarBalance

Source: https://core.telegram.org/bots/api#getbusinessaccountstarbalance

[Documentation index](../llms.txt)

Returns the amount of Telegram Stars owned by a managed business account. Requires the *can_view_gifts_and_stars* business bot right. Returns [StarAmount](staramount.md) on success.

| Parameter              | Type   | Required | Description                                  |
| ---------------------- | ------ | -------- | -------------------------------------------- |
| business_connection_id | String | Yes      | Unique identifier of the business connection |
