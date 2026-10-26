# InputChecklistTask

Source: https://core.telegram.org/bots/api#inputchecklisttask

[Documentation index](../llms.txt)

Describes a task to add to a checklist.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier of the task; must be positive and unique among all task identifiers currently present in the checklist |
| text | String | Text of the task; 1-100 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the text. See [formatting options](formatting-options.md) for more details. |
| text\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the text, which can be specified instead of parse\_mode. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, *custom\_emoji*, and *date\_time* entities are allowed. |
