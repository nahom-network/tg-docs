# PollOptionDeleted

Source: https://core.telegram.org/bots/api#polloptiondeleted

[Documentation index](../llms.txt)

Describes a service message about an option deleted from a poll.

| Field | Type | Description |
| --- | --- | --- |
| poll\_message | [MaybeInaccessibleMessage](maybeinaccessiblemessage.md) | *Optional*. Message containing the poll from which the option was deleted, if known. Note that the [Message](message.md) object in this field will not contain the *reply\_to\_message* field even if it itself is a reply. |
| option\_persistent\_id | String | Unique identifier of the deleted option |
| option\_text | String | Option text |
| option\_text\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities that appear in the *option\_text* |
