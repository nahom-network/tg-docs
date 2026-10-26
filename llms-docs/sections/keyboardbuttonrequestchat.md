# KeyboardButtonRequestChat

Source: https://core.telegram.org/bots/api#keyboardbuttonrequestchat

[Documentation index](../llms.txt)

This object defines the criteria used to request a suitable chat. Information about the selected chat will be shared with the bot when the corresponding button is pressed. The bot will be granted requested rights in the chat if appropriate. [More about requesting chats »](https://core.telegram.org/bots/features#chat-and-user-selection).

| Field | Type | Description |
| --- | --- | --- |
| request\_id | Integer | Signed 32-bit identifier of the request, which will be received back in the [ChatShared](chatshared.md) object. Must be unique within the message. |
| chat\_is\_channel | Boolean | Pass *True* to request a channel chat, pass *False* to request a group or a supergroup chat |
| chat\_is\_forum | Boolean | *Optional*. Pass *True* to request a forum supergroup, pass *False* to request a non-forum chat. If not specified, no additional restrictions are applied. |
| chat\_has\_username | Boolean | *Optional*. Pass *True* to request a supergroup or a channel with a username, pass *False* to request a chat without a username. If not specified, no additional restrictions are applied. |
| chat\_is\_created | Boolean | *Optional*. Pass *True* to request a chat owned by the user. Otherwise, no additional restrictions are applied. |
| user\_administrator\_rights | [ChatAdministratorRights](chatadministratorrights.md) | *Optional*. A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of *bot\_administrator\_rights*. If not specified, no additional restrictions are applied. |
| bot\_administrator\_rights | [ChatAdministratorRights](chatadministratorrights.md) | *Optional*. A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of *user\_administrator\_rights*. If not specified, no additional restrictions are applied. |
| bot\_is\_member | Boolean | *Optional*. Pass *True* to request a chat with the bot as a member. Otherwise, no additional restrictions are applied. |
| request\_title | Boolean | *Optional*. Pass *True* to request the chat's title |
| request\_username | Boolean | *Optional*. Pass *True* to request the chat's username |
| request\_photo | Boolean | *Optional*. Pass *True* to request the chat's photo |
