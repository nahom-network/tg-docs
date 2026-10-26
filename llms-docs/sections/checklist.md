# Checklist

Source: https://core.telegram.org/bots/api#checklist

[Documentation index](../llms.txt)

Describes a checklist.

| Field | Type | Description |
| --- | --- | --- |
| title | String | Title of the checklist |
| title\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities that appear in the checklist title |
| tasks | Array of [ChecklistTask](checklisttask.md) | List of tasks in the checklist |
| others\_can\_add\_tasks | True | *Optional*. *True*, if users other than the creator of the list can add tasks to the list |
| others\_can\_mark\_tasks\_as\_done | True | *Optional*. *True*, if users other than the creator of the list can mark tasks as done or not done |
