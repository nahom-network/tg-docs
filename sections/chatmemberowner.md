# ChatMemberOwner

Source: https://core.telegram.org/bots/api#chatmemberowner

[Documentation index](../llms.txt)

Represents a [chat member](chatmember.md) that owns the chat and has all administrator privileges.

| Field | Type | Description |
| --- | --- | --- |
| status | String | The member's status in the chat, always “creator” |
| user | [User](user.md) | Information about the user |
| is\_anonymous | Boolean | *True*, if the user's presence in the chat is hidden |
| custom\_title | String | *Optional*. Custom title for this user |
