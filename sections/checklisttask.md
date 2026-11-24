# ChecklistTask

Source: https://core.telegram.org/bots/api#checklisttask

[Documentation index](../llms.txt)

Describes a task in a checklist.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier of the task |
| text | String | Text of the task |
| text\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities that appear in the task text |
| completed\_by\_user | [User](user.md) | *Optional*. User that completed the task; omitted if the task wasn't completed by a user |
| completed\_by\_chat | [Chat](chat.md) | *Optional*. Chat that completed the task; omitted if the task wasn't completed by a chat |
| completion\_date | Integer | *Optional*. Point in time (Unix timestamp) when the task was completed; 0 if the task wasn't completed |
