# KeyboardButtonRequestUsers

Source: https://core.telegram.org/bots/api#keyboardbuttonrequestusers

[Documentation index](../llms.txt)

This object defines the criteria used to request suitable users. Information about the selected users will be shared with the bot when the corresponding button is pressed. [More about requesting users »](https://core.telegram.org/bots/features#chat-and-user-selection)

| Field | Type | Description |
| --- | --- | --- |
| request\_id | Integer | Signed 32-bit identifier of the request that will be received back in the [UsersShared](usersshared.md) object. Must be unique within the message. |
| user\_is\_bot | Boolean | *Optional*. Pass *True* to request bots, pass *False* to request regular users. If not specified, no additional restrictions are applied. |
| user\_is\_premium | Boolean | *Optional*. Pass *True* to request premium users, pass *False* to request non-premium users. If not specified, no additional restrictions are applied. |
| max\_quantity | Integer | *Optional*. The maximum number of users to be selected; 1-10. Defaults to 1. |
| request\_name | Boolean | *Optional*. Pass *True* to request the users' first and last names |
| request\_username | Boolean | *Optional*. Pass *True* to request the users' usernames |
| request\_photo | Boolean | *Optional*. Pass *True* to request the users' photos |
