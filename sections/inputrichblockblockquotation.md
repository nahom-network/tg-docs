# InputRichBlockBlockQuotation

Source: https://core.telegram.org/bots/api#inputrichblockblockquotation

[Documentation index](../llms.txt)

A block quotation, corresponding to the HTML tag `<blockquote>.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “blockquote” |
| blocks | Array of [InputRichBlock](inputrichblock.md) | Content of the block |
| credit | [RichText](richtext.md) | *Optional*. Credit of the block |
