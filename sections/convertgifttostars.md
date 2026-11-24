# convertGiftToStars

Source: https://core.telegram.org/bots/api#convertgifttostars

[Documentation index](../llms.txt)

Converts a given regular gift to Telegram Stars. Requires the *can\_convert\_gifts\_to\_stars* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| owned\_gift\_id | String | Yes | Unique identifier of the regular gift that should be converted to Telegram Stars |
