# ChatPermissions

Source: https://core.telegram.org/bots/api#chatpermissions

[Documentation index](../llms.txt)

Describes actions that a non-administrator user is allowed to take in a chat.

| Field | Type | Description |
| --- | --- | --- |
| can\_send\_messages | Boolean | *Optional*. *True*, if the user is allowed to send text messages, rich messages, contacts, giveaways, giveaway winners, invoices, locations and venues |
| can\_send\_audios | Boolean | *Optional*. *True*, if the user is allowed to send audios |
| can\_send\_documents | Boolean | *Optional*. *True*, if the user is allowed to send documents |
| can\_send\_photos | Boolean | *Optional*. *True*, if the user is allowed to send photos |
| can\_send\_videos | Boolean | *Optional*. *True*, if the user is allowed to send videos |
| can\_send\_video\_notes | Boolean | *Optional*. *True*, if the user is allowed to send video notes |
| can\_send\_voice\_notes | Boolean | *Optional*. *True*, if the user is allowed to send voice notes |
| can\_send\_polls | Boolean | *Optional*. *True*, if the user is allowed to send polls and checklists |
| can\_send\_other\_messages | Boolean | *Optional*. *True*, if the user is allowed to send animations, games, stickers, widgets and use inline bots |
| can\_add\_web\_page\_previews | Boolean | *Optional*. *True*, if the user is allowed to add web page previews to their messages |
| can\_react\_to\_messages | Boolean | *Optional*. *True*, if the user is allowed to react to messages. If omitted, defaults to the value of *can\_send\_messages*. |
| can\_edit\_tag | Boolean | *Optional*. *True*, if the user is allowed to edit their own tag. If omitted, defaults to the value of *can\_pin\_messages*. |
| can\_change\_info | Boolean | *Optional*. *True*, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups. |
| can\_invite\_users | Boolean | *Optional*. *True*, if the user is allowed to invite new users to the chat |
| can\_pin\_messages | Boolean | *Optional*. *True*, if the user is allowed to pin messages. Ignored in public supergroups. |
| can\_manage\_topics | Boolean | *Optional*. *True*, if the user is allowed to create forum topics. If omitted, defaults to the value of can\_pin\_messages. |
