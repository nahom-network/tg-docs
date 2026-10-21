# getChatMenuButton

Source: https://core.telegram.org/bots/api#getchatmenubutton

[Documentation index](../llms.txt)

Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns [MenuButton](menubutton.md) on success.

| Parameter | Type    | Required | Description                                                                                                      |
| --------- | ------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
| chat_id   | Integer | Optional | Unique identifier for the target private chat. If not specified, the bot's default menu button will be returned. |
