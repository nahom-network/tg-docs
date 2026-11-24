# InputMediaVoiceNote

Source: https://core.telegram.org/bots/api#inputmediavoicenote

[Documentation index](../llms.txt)

Represents a voice message file to be sent.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the media, must be *voice\_note* |
| media | String | File to send. Pass a file\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file\_attach\_name>" to upload a new one using multipart/form-data under <file\_attach\_name> name. [More information on Sending Files »](sending-files.md) |
| caption | String | *Optional*. Caption of the voice message to be sent, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| duration | Integer | *Optional*. Duration of the voice message in seconds |
