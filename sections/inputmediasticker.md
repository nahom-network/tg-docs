# InputMediaSticker

Source: https://core.telegram.org/bots/api#inputmediasticker

[Documentation index](../llms.txt)

Represents a sticker file to be sent.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the media, must be *sticker* |
| media | String | File to send. Pass a file\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a .WEBP sticker from the Internet, or pass “attach://<file\_attach\_name>” to upload a new .WEBP, .TGS, or .WEBM sticker using multipart/form-data under <file\_attach\_name> name. [More information on Sending Files »](sending-files.md) |
| emoji | String | *Optional*. Emoji associated with the sticker; only for just uploaded stickers |
