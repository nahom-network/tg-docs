# PassportElementErrorTranslationFile

Source: https://core.telegram.org/bots/api#passportelementerrortranslationfile

[Documentation index](../llms.txt)

Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

| Field | Type | Description |
| --- | --- | --- |
| source | String | Error source, must be *translation\_file* |
| type | String | Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver\_license”, “identity\_card”, “internal\_passport”, “utility\_bill”, “bank\_statement”, “rental\_agreement”, “passport\_registration”, “temporary\_registration” |
| file\_hash | String | Base64-encoded file hash |
| message | String | Error message |
