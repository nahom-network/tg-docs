# savePreparedInlineMessage

Source: https://core.telegram.org/bots/api#savepreparedinlinemessage

[Documentation index](../llms.txt)

Stores a message that can be sent by a user of a Mini App. Returns a [PreparedInlineMessage](preparedinlinemessage.md) object.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user\_id | Integer | Yes | Unique identifier of the target user that can use the prepared message |
| result | [InlineQueryResult](inlinequeryresult.md) | Yes | A JSON-serialized object describing the message to be sent |
| allow\_user\_chats | Boolean | Optional | Pass *True* if the message can be sent to private chats with users |
| allow\_bot\_chats | Boolean | Optional | Pass *True* if the message can be sent to private chats with bots |
| allow\_group\_chats | Boolean | Optional | Pass *True* if the message can be sent to group and supergroup chats |
| allow\_channel\_chats | Boolean | Optional | Pass *True* if the message can be sent to channel chats |
