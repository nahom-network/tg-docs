# editMessageChecklist

Source: https://core.telegram.org/bots/api#editmessagechecklist

[Documentation index](../llms.txt)

Use this method to edit a checklist on behalf of a connected business account. On success, the edited [Message](message.md) is returned.

| Parameter              | Type                                                                            | Required | Description                                                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| business_connection_id | String                                                                          | Yes      | Unique identifier of the business connection on behalf of which the message will be sent                                         |
| chat_id                | Integer or String                                                               | Yes      | Unique identifier for the target chat or username of the target bot in the format `@username`                                    |
| message_id             | Integer                                                                         | Yes      | Unique identifier for the target message                                                                                         |
| checklist              | [InputChecklist](inputchecklist.md)             | Yes      | A JSON-serialized object for the new checklist                                                                                   |
| reply_markup           | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | Optional | A JSON-serialized object for the new [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) for the message |
