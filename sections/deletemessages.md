# deleteMessages

Source: https://core.telegram.org/bots/api#deletemessages

[Documentation index](../llms.txt)

Use this method to delete multiple messages simultaneously. If some of the specified messages can't be found, they are skipped. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup, or channel in the format `@username` |
| message\_ids | Array of Integer | Yes | A JSON-serialized list of 1-100 identifiers of messages to delete. See [deleteMessage](deletemessage.md) for limitations on which messages can be deleted. |
