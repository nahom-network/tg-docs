# MessageGenerationStopped

Source: https://core.telegram.org/bots/api#messagegenerationstopped

[Documentation index](../llms.txt)

This object describes an update about a user stopping message generation.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](chat.md) | Chat in which the message is generated |
| message_thread_id | Integer | *Optional*. Unique identifier of the message thread in which the message is generated |
| draft_id | Integer | Unique identifier of the message draft which was stopped |
