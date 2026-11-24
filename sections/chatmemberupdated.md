# ChatMemberUpdated

Source: https://core.telegram.org/bots/api#chatmemberupdated

[Documentation index](../llms.txt)

This object represents changes in the status of a chat member.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](chat.md) | Chat the user belongs to |
| from | [User](user.md) | Performer of the action, which resulted in the change |
| date | Integer | Date the change was done in Unix time |
| old\_chat\_member | [ChatMember](chatmember.md) | Previous information about the chat member |
| new\_chat\_member | [ChatMember](chatmember.md) | New information about the chat member |
| invite\_link | [ChatInviteLink](chatinvitelink.md) | *Optional*. Chat invite link, which was used by the user to join the chat; for joining by invite link events only |
| via\_join\_request | Boolean | *Optional*. *True*, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator |
| via\_chat\_folder\_invite\_link | Boolean | *Optional*. *True*, if the user joined the chat via a chat folder invite link |
