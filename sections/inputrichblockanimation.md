# InputRichBlockAnimation

Source: https://core.telegram.org/bots/api#inputrichblockanimation

[Documentation index](../llms.txt)

A block with an animation, corresponding to the HTML tag `<video>.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “animation” |
| animation | [InputMediaAnimation](inputmediaanimation.md) | The animation. Caption is ignored. |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block |
