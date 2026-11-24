# RichBlockDetails

Source: https://core.telegram.org/bots/api#richblockdetails

[Documentation index](../llms.txt)

An expandable block for details disclosure, corresponding to the HTML tag `<details>.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “details” |
| summary | [RichText](richtext.md) | Always shown summary of the block |
| blocks | Array of [RichBlock](richblock.md) | Content of the block |
| is_open | True | *Optional*. *True*, if the content of the block is visible by default |
