# RichBlockSlideshow

Source: https://core.telegram.org/bots/api#richblockslideshow

[Documentation index](../llms.txt)

A slideshow, corresponding to the custom HTML tag `<tg-slideshow>.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “slideshow” |
| blocks | Array of [RichBlock](richblock.md) | Elements of the slideshow |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block |
