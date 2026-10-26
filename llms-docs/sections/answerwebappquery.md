# answerWebAppQuery

Source: https://core.telegram.org/bots/api#answerwebappquery

[Documentation index](../llms.txt)

Use this method to set the result of an interaction with a [Web App](https://core.telegram.org/bots/webapps) and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a [SentWebAppMessage](sentwebappmessage.md) object is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| web\_app\_query\_id | String | Yes | Unique identifier for the query to be answered |
| result | [InlineQueryResult](inlinequeryresult.md) | Yes | A JSON-serialized object describing the message to be sent |
