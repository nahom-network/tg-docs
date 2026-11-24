# InputMediaLivePhoto

Source: https://core.telegram.org/bots/api#inputmedialivephoto

[Documentation index](../llms.txt)

Represents a live photo to be sent.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the media, must be *live\_photo* |
| media | String | Video of the live photo to send. Pass a file\_id to send a file that exists on the Telegram servers (recommended) or pass “attach://<file\_attach\_name>” to upload a new one using multipart/form-data under <file\_attach\_name> name. [More information on Sending Files »](sending-files.md). Sending live photos by a URL is currently unsupported. |
| photo | String | The static photo to send. Pass a file\_id to send a file that exists on the Telegram servers (recommended) or pass “attach://<file\_attach\_name>” to upload a new one using multipart/form-data under <file\_attach\_name> name. [More information on Sending Files »](sending-files.md). Sending live photos by a URL is currently unsupported. |
| caption | String | *Optional*. Caption of the live photo to be sent, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the live photo caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| show\_caption\_above\_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| has\_spoiler | Boolean | *Optional*. Pass *True* if the live photo needs to be covered with a spoiler animation |
