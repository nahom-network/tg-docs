# ChatAdministratorRights

Source: https://core.telegram.org/bots/api#chatadministratorrights

[Documentation index](../llms.txt)

Represents the rights of an administrator in a chat.

| Field | Type | Description |
| --- | --- | --- |
| is\_anonymous | Boolean | *True*, if the user's presence in the chat is hidden |
| can\_manage\_chat | Boolean | *True*, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages, ignore slow mode, and send messages to the chat without paying Telegram Stars. Implied by any other administrator privilege. |
| can\_delete\_messages | Boolean | *True*, if the administrator can delete messages of other users |
| can\_manage\_video\_chats | Boolean | *True*, if the administrator can manage video chats |
| can\_restrict\_members | Boolean | *True*, if the administrator can restrict, ban or unban chat members, or access supergroup statistics |
| can\_promote\_members | Boolean | *True*, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user) |
| can\_change\_info | Boolean | *True*, if the user is allowed to change the chat title, photo and other settings |
| can\_invite\_users | Boolean | *True*, if the user is allowed to invite new users to the chat |
| can\_post\_stories | Boolean | *True*, if the administrator can post stories to the chat |
| can\_edit\_stories | Boolean | *True*, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive |
| can\_delete\_stories | Boolean | *True*, if the administrator can delete stories posted by other users |
| can\_post\_messages | Boolean | *Optional*. *True*, if the administrator can post messages in the channel, approve suggested posts, or access channel statistics; for channels only |
| can\_edit\_messages | Boolean | *Optional*. *True*, if the administrator can edit messages of other users and can pin messages; for channels only |
| can\_pin\_messages | Boolean | *Optional*. *True*, if the user is allowed to pin messages; for groups and supergroups only |
| can\_manage\_topics | Boolean | *Optional*. *True*, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only |
| can\_manage\_direct\_messages | Boolean | *Optional*. *True*, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only |
| can\_manage\_tags | Boolean | *Optional*. *True*, if the administrator can edit the tags of regular members; for groups and supergroups only |
| can\_send\_welcome\_messages | Boolean | *True*, if the administrator can manage chat welcome messages or directly send them in the case of bots |
