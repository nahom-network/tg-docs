# InputMediaVideo

Source: https://core.telegram.org/bots/api#inputmediavideo

[Documentation index](../llms.txt)

Represents a video to be sent.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the media, must be *video* |
| media | String | File to send. Pass a file\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file\_attach\_name>” to upload a new one using multipart/form-data under <file\_attach\_name> name. [More information on Sending Files »](sending-files.md) |
| thumbnail | String | *Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file\_attach\_name>” if the thumbnail was uploaded using multipart/form-data under <file\_attach\_name>. [More information on Sending Files »](sending-files.md) |
| cover | String | *Optional*. Cover for the video in the message. Pass a file\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file\_attach\_name>” to upload a new one using multipart/form-data under <file\_attach\_name> name. [More information on Sending Files »](sending-files.md) |
| start\_timestamp | Integer | *Optional*. Start timestamp for the video in the message |
| caption | String | *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the video caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| show\_caption\_above\_media | Boolean | *Optional*. Pass *True* if the caption must be shown above the message media |
| width | Integer | *Optional*. Video width |
| height | Integer | *Optional*. Video height |
| duration | Integer | *Optional*. Video duration in seconds |
| supports\_streaming | Boolean | *Optional*. Pass *True* if the uploaded video is suitable for streaming |
| has\_spoiler | Boolean | *Optional*. Pass *True* if the video needs to be covered with a spoiler animation |
