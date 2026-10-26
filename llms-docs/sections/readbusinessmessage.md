# readBusinessMessage

Source: https://core.telegram.org/bots/api#readbusinessmessage

[Documentation index](../llms.txt)

Marks incoming message as read on behalf of a business account. Requires the *can\_read\_messages* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection on behalf of which to read the message |
| chat\_id | Integer | Yes | Unique identifier of the chat in which the message was received. The chat must have been active in the last 24 hours. |
| message\_id | Integer | Yes | Unique identifier of the message to mark as read |
