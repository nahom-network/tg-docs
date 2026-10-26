# BusinessMessagesDeleted

Source: https://core.telegram.org/bots/api#businessmessagesdeleted

[Documentation index](../llms.txt)

This object is received when messages are deleted from a connected business account.

| Field | Type | Description |
| --- | --- | --- |
| business\_connection\_id | String | Unique identifier of the business connection |
| chat | [Chat](chat.md) | Information about a chat in the business account. The bot may not have access to the chat or the corresponding user. |
| message\_ids | Array of Integer | The list of identifiers of deleted messages in the chat of the business account |
