# InputRichBlockCollage

Source: https://core.telegram.org/bots/api#inputrichblockcollage

[Documentation index](../llms.txt)

A collage, corresponding to the custom HTML tag `<tg-collage>`.

| Field   | Type                                                                         | Description                         |
| ------- | ---------------------------------------------------------------------------- | ----------------------------------- |
| type    | String                                                                       | Type of the block, always “collage” |
| blocks  | Array of [InputRichBlock](inputrichblock.md) | Elements of the collage             |
| caption | [RichBlockCaption](richblockcaption.md)      | *Optional*. Caption of the block    |
