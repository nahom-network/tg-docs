# InputRichBlockPhoto

Source: https://core.telegram.org/bots/api#inputrichblockphoto

[Documentation index](../llms.txt)

A block with a photo, corresponding to the HTML tag `<img>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “photo” |
| photo | [InputMediaPhoto](inputmediaphoto.md) | The photo. Caption is ignored. |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block |
