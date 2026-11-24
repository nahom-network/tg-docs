# RichBlockCollage

Source: https://core.telegram.org/bots/api#richblockcollage

[Documentation index](../llms.txt)

A collage, corresponding to the custom HTML tag `<tg-collage>.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “collage” |
| blocks | Array of [RichBlock](richblock.md) | Elements of the collage |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block |
