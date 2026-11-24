# InputPaidMediaPhoto

Source: https://core.telegram.org/bots/api#inputpaidmediaphoto

[Documentation index](../llms.txt)

The paid media to send is a photo.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the media, must be *photo* |
| media | String | File to send. Pass a file\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file\_attach\_name>” to upload a new one using multipart/form-data under <file\_attach\_name> name. [More information on Sending Files »](sending-files.md) |
