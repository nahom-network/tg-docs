# RichBlockBlockQuotation

Source: https://core.telegram.org/bots/api#richblockblockquotation

[Documentation index](../llms.txt)

A block quotation, corresponding to the HTML tag `<blockquote>.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “blockquote” |
| blocks | Array of [RichBlock](richblock.md) | Content of the block |
| credit | [RichText](richtext.md) | *Optional*. Credit of the block |
