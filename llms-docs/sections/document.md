# Document

Source: https://core.telegram.org/bots/api#document

[Documentation index](../llms.txt)

This object represents a general file (as opposed to [photos](photosize.md), [voice messages](voice.md) and [audio files](audio.md)).

| Field | Type | Description |
| --- | --- | --- |
| file\_id | String | Identifier for this file, which can be used to download or reuse the file |
| file\_unique\_id | String | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file. |
| thumbnail | [PhotoSize](photosize.md) | *Optional*. Document thumbnail as defined by the sender |
| file\_name | String | *Optional*. Original filename as defined by the sender |
| mime\_type | String | *Optional*. MIME type of the file as defined by the sender |
| file\_size | Integer | *Optional*. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value. |
