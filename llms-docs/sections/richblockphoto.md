# RichBlockPhoto

Source: https://core.telegram.org/bots/api#richblockphoto

[Documentation index](../llms.txt)

A block with a photo, corresponding to the HTML tag `<img>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “photo” |
| photo | Array of [PhotoSize](photosize.md) | Available sizes of the photo |
| has\_spoiler | True | *Optional*. *True*, if the media preview is covered by a spoiler animation |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block |
