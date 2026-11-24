# answerGuestQuery

Source: https://core.telegram.org/bots/api#answerguestquery

[Documentation index](../llms.txt)

Use this method to reply to a received guest message. On success, a [SentGuestMessage](sentguestmessage.md) object is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| guest_query_id | String | Yes | Unique identifier for the query to be answered |
| result | [InlineQueryResult](inlinequeryresult.md) | Yes | A JSON-serialized object describing the message to be sent |
