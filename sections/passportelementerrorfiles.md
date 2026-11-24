# PassportElementErrorFiles

Source: https://core.telegram.org/bots/api#passportelementerrorfiles

[Documentation index](../llms.txt)

Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *files* |
| type | String | The section of the user's Telegram Passport which has the issue, one of “utility\_bill”, “bank\_statement”, “rental\_agreement”, “passport\_registration”, “temporary\_registration” |
| file\_hashes | Array of String | List of base64-encoded file hashes |
| message | String | Error message |
