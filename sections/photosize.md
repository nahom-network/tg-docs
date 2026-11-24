# PhotoSize

Source: https://core.telegram.org/bots/api#photosize

[Documentation index](../llms.txt)

This object represents one size of a photo or a [file](document.md) / [sticker](sticker.md) thumbnail.

| Field | Type | Description |
| --- | --- | --- |
| file\_id | String | Identifier for this file, which can be used to download or reuse the file |
| file\_unique\_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| width | Integer | Photo width |
| height | Integer | Photo height |
| file\_size | Integer | *Optional*. File size in bytes |
