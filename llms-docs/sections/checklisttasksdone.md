# ChecklistTasksDone

Source: https://core.telegram.org/bots/api#checklisttasksdone

[Documentation index](../llms.txt)

Describes a service message about checklist tasks marked as done or not done.

| Field | Type | Description |
| --- | --- | --- |
| checklist\_message | [Message](message.md) | *Optional*. Message containing the checklist whose tasks were marked as done or not done. Note that the [Message](message.md) object in this field will not contain the *reply\_to\_message* field even if it itself is a reply. |
| marked\_as\_done\_task\_ids | Array of Integer | *Optional*. Identifiers of the tasks that were marked as done |
| marked\_as\_not\_done\_task\_ids | Array of Integer | *Optional*. Identifiers of the tasks that were marked as not done |
