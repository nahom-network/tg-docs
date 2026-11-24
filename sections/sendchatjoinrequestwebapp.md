# sendChatJoinRequestWebApp

Source: https://core.telegram.org/bots/api#sendchatjoinrequestwebapp

[Documentation index](../llms.txt)

Use this method to process a received chat join request query by showing a Mini App to the user before deciding the outcome. Call [answerChatJoinRequestQuery](answerchatjoinrequestquery.md) to resolve the join request query based on the user interaction with the Mini App. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_join\_request\_query\_id | String | Yes | Unique identifier of the join request query |
| web\_app\_url | String | Yes | An HTTPS URL of a Web App to be opened with additional data as specified in [Initializing Web Apps](../external/bots/webapps.md#initializing-mini-apps) |
