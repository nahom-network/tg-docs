# stopPoll

Source: https://core.telegram.org/bots/api#stoppoll

[Documentation index](../llms.txt)

Use this method to stop a poll which was sent by the bot. On success, the stopped [Poll](poll.md) is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message to be edited was sent |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username` |
| message\_id | Integer | Yes | Identifier of the original message with the poll |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for a new message [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) |
