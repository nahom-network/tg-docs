# PassportElementErrorDataField

Source: https://core.telegram.org/bots/api#passportelementerrordatafield

[Documentation index](../llms.txt)

Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *data* |
| type | String | The section of the user's Telegram Passport which has the error, one of “personal\_details”, “passport”, “driver\_license”, “identity\_card”, “internal\_passport”, “address” |
| field\_name | String | Name of the data field which has the error |
| data\_hash | String | Base64-encoded data hash |
| message | String | Error message |
