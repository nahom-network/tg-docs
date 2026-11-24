# ChatMemberRestricted

Source: https://core.telegram.org/bots/api#chatmemberrestricted

[Documentation index](../llms.txt)

Represents a [chat member](chatmember.md) that is under certain restrictions in the chat. Supergroups only.

| Field | Type | Description |
| --- | --- | --- |
| status | String | The member's status in the chat, always “restricted” |
| tag | String | *Optional*. Tag of the member |
| user | [User](user.md) | Information about the user |
| is\_member | Boolean | *True*, if the user is a member of the chat at the moment of the request |
| can\_send\_messages | Boolean | *True*, if the user is allowed to send text messages, rich messages, contacts, giveaways, giveaway winners, invoices, locations and venues |
| can\_send\_audios | Boolean | *True*, if the user is allowed to send audios |
| can\_send\_documents | Boolean | *True*, if the user is allowed to send documents |
| can\_send\_photos | Boolean | *True*, if the user is allowed to send photos |
| can\_send\_videos | Boolean | *True*, if the user is allowed to send videos |
| can\_send\_video\_notes | Boolean | *True*, if the user is allowed to send video notes |
| can\_send\_voice\_notes | Boolean | *True*, if the user is allowed to send voice notes |
| can\_send\_polls | Boolean | *True*, if the user is allowed to send polls and checklists |
| can\_send\_other\_messages | Boolean | *True*, if the user is allowed to send animations, games, stickers, widgets and use inline bots |
| can\_add\_web\_page\_previews | Boolean | *True*, if the user is allowed to add web page previews to their messages |
| can\_react\_to\_messages | Boolean | *True*, if the user is allowed to react to messages |
| can\_edit\_tag | Boolean | *True*, if the user is allowed to edit their own tag |
| can\_change\_info | Boolean | *True*, if the user is allowed to change the chat title, photo and other settings |
| can\_invite\_users | Boolean | *True*, if the user is allowed to invite new users to the chat |
| can\_pin\_messages | Boolean | *True*, if the user is allowed to pin messages |
| can\_manage\_topics | Boolean | *True*, if the user is allowed to create forum topics |
| until\_date | Integer | Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever. |
