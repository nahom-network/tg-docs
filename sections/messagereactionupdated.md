# MessageReactionUpdated

Source: https://core.telegram.org/bots/api#messagereactionupdated

[Documentation index](../llms.txt)

This object represents a change of a reaction on a message performed by a user.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](chat.md) | The chat containing the message the user reacted to |
| message\_id | Integer | Unique identifier of the message inside the chat |
| user | [User](user.md) | *Optional*. The user that changed the reaction, if the user isn't anonymous |
| actor\_chat | [Chat](chat.md) | *Optional*. The chat on behalf of which the reaction was changed, if the user is anonymous |
| date | Integer | Date of the change in Unix time |
| old\_reaction | Array of [ReactionType](reactiontype.md) | Previous list of reaction types that were set by the user |
| new\_reaction | Array of [ReactionType](reactiontype.md) | New list of reaction types that have been set by the user |
