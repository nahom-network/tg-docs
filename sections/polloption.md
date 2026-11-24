# PollOption

Source: https://core.telegram.org/bots/api#polloption

[Documentation index](../llms.txt)

This object contains information about one answer option in a poll.

| Field | Type | Description |
| --- | --- | --- |
| persistent\_id | String | Unique identifier of the option, persistent on option addition and deletion |
| text | String | Option text, 1-100 characters |
| text\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities that appear in the option *text*. Currently, only custom emoji entities are allowed in poll option texts |
| media | [PollMedia](pollmedia.md) | *Optional*. Media added to the poll option |
| voter\_count | Integer | Number of users who voted for this option; may be 0 if unknown |
| added\_by\_user | [User](user.md) | *Optional*. User who added the option; omitted if the option wasn't added by a user after poll creation |
| added\_by\_chat | [Chat](chat.md) | *Optional*. Chat that added the option; omitted if the option wasn't added by a chat after poll creation |
| addition\_date | Integer | *Optional*. Point in time (Unix timestamp) when the option was added; omitted if the option existed in the original poll |
