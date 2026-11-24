# RichBlockVideo

Source: https://core.telegram.org/bots/api#richblockvideo

[Documentation index](../llms.txt)

A block with a video, corresponding to the HTML tag `<video>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “video” |
| video | [Video](video.md) | The video |
| has\_spoiler | True | *Optional*. *True*, if the media preview is covered by a spoiler animation |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block |
