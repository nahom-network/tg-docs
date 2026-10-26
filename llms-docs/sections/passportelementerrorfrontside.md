# PassportElementErrorFrontSide

Source: https://core.telegram.org/bots/api#passportelementerrorfrontside

[Documentation index](../llms.txt)

Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *front\_side* |
| type | String | The section of the user's Telegram Passport which has the issue, one of “passport”, “driver\_license”, “identity\_card”, “internal\_passport” |
| file\_hash | String | Base64-encoded hash of the file with the front side of the document |
| message | String | Error message |
