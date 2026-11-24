# RichBlockAnimation

Source: https://core.telegram.org/bots/api#richblockanimation

[Documentation index](../llms.txt)

A block with an animation, corresponding to the HTML tag `<video>.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “animation” |
| animation | [Animation](animation.md) | The animation |
| has_spoiler | True | *Optional*. *True*, if the media preview is covered by a spoiler animation |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block |
