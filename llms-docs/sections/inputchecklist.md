# InputChecklist

Source: https://core.telegram.org/bots/api#inputchecklist

[Documentation index](../llms.txt)

Describes a checklist to create.

| Field | Type | Description |
| --- | --- | --- |
| title | String | Title of the checklist; 1-255 characters after entities parsing |
| parse\_mode | String | *Optional*. Mode for parsing entities in the title. See [formatting options](formatting-options.md) for more details. |
| title\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. List of special entities that appear in the title, which can be specified instead of parse\_mode. Currently, only *bold*, *italic*, *underline*, *strikethrough*, *spoiler*, *custom\_emoji*, and *date\_time* entities are allowed. |
| tasks | Array of [InputChecklistTask](inputchecklisttask.md) | List of 1-30 tasks in the checklist |
| others\_can\_add\_tasks | Boolean | *Optional*. Pass *True* if other users can add tasks to the checklist |
| others\_can\_mark\_tasks\_as\_done | Boolean | *Optional*. Pass *True* if other users can mark tasks as done or not done in the checklist |
