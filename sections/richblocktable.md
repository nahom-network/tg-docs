# RichBlockTable

Source: https://core.telegram.org/bots/api#richblocktable

[Documentation index](../llms.txt)

A table, corresponding to the HTML tag `<table>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “table” |
| cells | Array of Array of [RichBlockTableCell](richblocktablecell.md) | Cells of the table |
| is\_bordered | True | *Optional*. *True*, if the table has borders |
| is\_striped | True | *Optional*. *True*, if the table is striped |
| is\_compact | True | *Optional*. *True*, if table cells have smaller indents |
| caption | [RichText](richtext.md) | *Optional*. Caption of the table |
