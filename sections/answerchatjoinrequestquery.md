# answerChatJoinRequestQuery

Source: https://core.telegram.org/bots/api#answerchatjoinrequestquery

[Documentation index](../llms.txt)

Use this method to process a received chat join request query. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_join\_request\_query\_id | String | Yes | Unique identifier of the join request query |
| result | String | Yes | Result of the query. Must be either “approve” to allow the user to join the chat, “decline” to disallow the user to join the chat, or “queue” to leave the decision to other administrators. |
