# PollOptionAdded

Source: https://core.telegram.org/bots/api#polloptionadded

[Documentation index](../llms.txt)

Describes a service message about an option added to a poll.

| Field | Type | Description |
| --- | --- | --- |
| poll\_message | [MaybeInaccessibleMessage](maybeinaccessiblemessage.md) | *Optional*. Message containing the poll to which the option was added, if known. Note that the [Message](message.md) object in this field will not contain the *reply\_to\_message* field even if it itself is a reply. |
| option\_persistent\_id | String | Unique identifier of the added option |
| option\_text | String | Option text |
| option\_text\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities that appear in the *option\_text* |
