# EncryptedCredentials

Source: https://core.telegram.org/bots/api#encryptedcredentials

[Documentation index](../llms.txt)

Describes data required for decrypting and authenticating [EncryptedPassportElement](encryptedpassportelement.md). See the [Telegram Passport Documentation](https://core.telegram.org/passport#receiving-information) for a complete description of the data decryption and authentication processes.

| Field | Type | Description |
| --- | --- | --- |
| data | String | Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for [EncryptedPassportElement](encryptedpassportelement.md) decryption and authentication |
| hash | String | Base64-encoded data hash for data authentication |
| secret | String | Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption |
