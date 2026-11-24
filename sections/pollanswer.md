# PollAnswer

Source: https://core.telegram.org/bots/api#pollanswer

[Documentation index](../llms.txt)

This object represents an answer of a user in a non-anonymous poll.

| Field | Type | Description |
| --- | --- | --- |
| poll\_id | String | Unique poll identifier |
| voter\_chat | [Chat](chat.md) | *Optional*. The chat that changed the answer to the poll, if the voter is anonymous |
| user | [User](user.md) | *Optional*. The user that changed the answer to the poll, if the voter isn't anonymous |
| option\_ids | Array of Integer | 0-based identifiers of chosen answer options. May be empty if the vote was retracted. |
| option\_persistent\_ids | Array of String | Persistent identifiers of the chosen answer options. May be empty if the vote was retracted. |
