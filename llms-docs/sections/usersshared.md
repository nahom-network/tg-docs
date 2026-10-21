# UsersShared

Source: https://core.telegram.org/bots/api#usersshared

[Documentation index](../llms.txt)

This object contains information about the users whose identifiers were shared with the bot using a [KeyboardButtonRequestUsers](keyboardbuttonrequestusers.md) button.

| Field      | Type                                                                 | Description                                 |
| ---------- | -------------------------------------------------------------------- | ------------------------------------------- |
| request_id | Integer                                                              | Identifier of the request                   |
| users      | Array of [SharedUser](shareduser.md) | Information about users shared with the bot |
