# MessageOriginChat

Source: https://core.telegram.org/bots/api#messageoriginchat

[Documentation index](../llms.txt)

The message was originally sent on behalf of a chat to a group chat.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the message origin, always “chat” |
| date | Integer | Date the message was sent originally in Unix time |
| sender\_chat | [Chat](chat.md) | Chat that sent the message originally |
| author\_signature | String | *Optional*. For messages originally sent by an anonymous chat administrator, original message author signature |
