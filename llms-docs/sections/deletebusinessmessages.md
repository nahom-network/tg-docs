# deleteBusinessMessages

Source: https://core.telegram.org/bots/api#deletebusinessmessages

[Documentation index](../llms.txt)

Delete messages on behalf of a business account. Requires the *can\_delete\_sent\_messages* business bot right to delete messages sent by the bot itself, or the *can\_delete\_all\_messages* business bot right to delete any message. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection on behalf of which to delete the messages |
| message\_ids | Array of Integer | Yes | A JSON-serialized list of 1-100 identifiers of messages to delete. All messages must be from the same chat. See [deleteMessage](deletemessage.md) for limitations on which messages can be deleted. |
