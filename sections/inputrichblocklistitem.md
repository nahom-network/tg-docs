# InputRichBlockListItem

Source: https://core.telegram.org/bots/api#inputrichblocklistitem

[Documentation index](../llms.txt)

An item of a list to be sent.

| Field | Type | Description |
| --- | --- | --- |
| blocks | Array of [InputRichBlock](inputrichblock.md) | The content of the item |
| has\_checkbox | True | *Optional*. Pass *True* if the item has a checkbox |
| is\_checked | True | *Optional*. Pass *True* if the item has a checked checkbox |
| value | Integer | *Optional*. For ordered lists, the numeric value of the item label |
| type | String | *Optional*. For ordered lists, the type of the item label; must be one of “a” for lowercase letters, “A” for uppercase letters, “i” for lowercase Roman numerals, “I” for uppercase Roman numerals, or “1” for decimal numbers |
