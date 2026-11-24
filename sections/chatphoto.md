# ChatPhoto

Source: https://core.telegram.org/bots/api#chatphoto

[Documentation index](../llms.txt)

This object represents a chat photo.

| Field | Type | Description |
| --- | --- | --- |
| small\_file\_id | String | File identifier of small (160x160) chat photo. This file\_id can be used only for photo download and only for as long as the photo is not changed. |
| small\_file\_unique\_id | String | Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| big\_file\_id | String | File identifier of big (640x640) chat photo. This file\_id can be used only for photo download and only for as long as the photo is not changed. |
| big\_file\_unique\_id | String | Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
