# InputRichBlockExpandableBlockQuotation

Source: https://core.telegram.org/bots/api#inputrichblockexpandableblockquotation

[Documentation index](../llms.txt)

A block quotation, corresponding to the HTML tag `<blockquote>` with custom attribute `"expandable"`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “expandable\_blockquote” |
| blocks | Array of [InputRichBlock](inputrichblock.md) | Content of the block |
| credit | [RichText](richtext.md) | *Optional*. Credit of the block |
