# ChatMemberLeft

Source: https://core.telegram.org/bots/api#chatmemberleft

[Documentation index](../llms.txt)

Represents a [chat member](chatmember.md) that isn't currently a member of the chat, but may join it themselves.

| Field  | Type                                            | Description                                    |
| ------ | ----------------------------------------------- | ---------------------------------------------- |
| status | String                                          | The member's status in the chat, always “left” |
| user   | [User](user.md) | Information about the user                     |
