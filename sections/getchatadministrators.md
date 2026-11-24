# getChatAdministrators

Source: https://core.telegram.org/bots/api#getchatadministrators

[Documentation index](../llms.txt)

Use this method to get a list of administrators in a chat. Returns an Array of [ChatMember](chatmember.md) objects.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup or channel in the format `@username` |
| return\_bots | Boolean | Optional | Pass *True* to additionally receive all bots that are administrators of the chat. By default, bots other than the current bot are omitted. |
