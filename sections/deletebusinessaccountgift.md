# deleteBusinessAccountGift

Source: https://core.telegram.org/bots/api#deletebusinessaccountgift

[Documentation index](../llms.txt)

Deletes a regular gift owned by a managed business account without receiving Telegram Stars for it. Requires the *can\_convert\_gifts\_to\_stars* business bot right. The gift can be deleted only if it isn't limited (the field *total\_count* of the [Gift](gift.md) is omitted) and wasn't refunded. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| owned\_gift\_id | String | Yes | Unique identifier of the regular gift that should be deleted |
