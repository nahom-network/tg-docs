# PassportElementErrorFile

Source: https://core.telegram.org/bots/api#passportelementerrorfile

[Documentation index](../llms.txt)

Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *file* |
| type | String | The section of the user's Telegram Passport which has the issue, one of “utility\_bill”, “bank\_statement”, “rental\_agreement”, “passport\_registration”, “temporary\_registration” |
| file\_hash | String | Base64-encoded file hash |
| message | String | Error message |
