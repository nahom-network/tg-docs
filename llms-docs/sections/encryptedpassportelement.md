# EncryptedPassportElement

Source: https://core.telegram.org/bots/api#encryptedpassportelement

[Documentation index](../llms.txt)

Describes documents or other Telegram Passport elements shared with the bot by the user.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Element type. One of “personal\_details”, “passport”, “driver\_license”, “identity\_card”, “internal\_passport”, “address”, “utility\_bill”, “bank\_statement”, “rental\_agreement”, “passport\_registration”, “temporary\_registration”, “phone\_number”, “email”. |
| data | String | *Optional*. Base64-encoded encrypted Telegram Passport element data provided by the user; available only for “personal\_details”, “passport”, “driver\_license”, “identity\_card”, “internal\_passport” and “address” types. Can be decrypted and verified using the accompanying [EncryptedCredentials](encryptedcredentials.md). |
| phone\_number | String | *Optional*. User's verified phone number; available only for “phone\_number” type |
| email | String | *Optional*. User's verified email address; available only for “email” type |
| files | Array of [PassportFile](passportfile.md) | *Optional*. Array of encrypted files with documents provided by the user; available only for “utility\_bill”, “bank\_statement”, “rental\_agreement”, “passport\_registration” and “temporary\_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](encryptedcredentials.md). |
| front\_side | [PassportFile](passportfile.md) | *Optional*. Encrypted file with the front side of the document, provided by the user; available only for “passport”, “driver\_license”, “identity\_card” and “internal\_passport”. The file can be decrypted and verified using the accompanying [EncryptedCredentials](encryptedcredentials.md). |
| reverse\_side | [PassportFile](passportfile.md) | *Optional*. Encrypted file with the reverse side of the document, provided by the user; available only for “driver\_license” and “identity\_card”. The file can be decrypted and verified using the accompanying [EncryptedCredentials](encryptedcredentials.md). |
| selfie | [PassportFile](passportfile.md) | *Optional*. Encrypted file with the selfie of the user holding a document, provided by the user; available if requested for “passport”, “driver\_license”, “identity\_card” and “internal\_passport”. The file can be decrypted and verified using the accompanying [EncryptedCredentials](encryptedcredentials.md). |
| translation | Array of [PassportFile](passportfile.md) | *Optional*. Array of encrypted files with translated versions of documents provided by the user; available if requested for “passport”, “driver\_license”, “identity\_card”, “internal\_passport”, “utility\_bill”, “bank\_statement”, “rental\_agreement”, “passport\_registration” and “temporary\_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](encryptedcredentials.md). |
| hash | String | Base64-encoded element hash for using in [PassportElementErrorUnspecified](passportelementerrorunspecified.md) |
