# KeyboardButtonRequestManagedBot

Source: https://core.telegram.org/bots/api#keyboardbuttonrequestmanagedbot

[Documentation index](../llms.txt)

This object defines the parameters for the creation of a managed bot. Information about the created bot will be shared with the bot using the update *managed\_bot* and a [Message](message.md) with the field *managed\_bot\_created*.

| Field | Type | Description |
| --- | --- | --- |
| request\_id | Integer | Signed 32-bit identifier of the request. Must be unique within the message. |
| suggested\_name | String | *Optional*. Suggested name for the bot |
| suggested\_username | String | *Optional*. Suggested username for the bot. The username must end with “bot”. If the user creating the bot has a Telegram Premium subscription, then the username can also end with “agent”, “ai”, “app”, “game”, or “gay”; in this case, the username will be assigned to the bot as a secondary username, and a regular username ending with “bot” will be assigned to the bot automatically. |
