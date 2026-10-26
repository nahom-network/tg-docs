# InputRichBlockVideo

Source: https://core.telegram.org/bots/api#inputrichblockvideo

[Documentation index](../llms.txt)

A block with a video, corresponding to the HTML tag `<video>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “video” |
| video | [InputMediaVideo](inputmediavideo.md) | The video. Caption is ignored. |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block |
