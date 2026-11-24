# PassportElementErrorTranslationFiles

Source: https://core.telegram.org/bots/api#passportelementerrortranslationfiles

[Documentation index](../llms.txt)

Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *translation\_files* |
| type | String | Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver\_license”, “identity\_card”, “internal\_passport”, “utility\_bill”, “bank\_statement”, “rental\_agreement”, “passport\_registration”, “temporary\_registration” |
| file\_hashes | Array of String | List of base64-encoded file hashes |
| message | String | Error message |
