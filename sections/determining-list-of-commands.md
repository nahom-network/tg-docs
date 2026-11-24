# Determining list of commands

Source: https://core.telegram.org/bots/api#determining-list-of-commands

[Documentation index](../llms.txt)

The following algorithm is used to determine the list of commands for a particular user viewing the bot menu. The first list of commands which is set is returned:

**Commands in the chat with the bot**

- botCommandScopeChat + language\_code
- botCommandScopeChat
- botCommandScopeAllPrivateChats + language\_code
- botCommandScopeAllPrivateChats
- botCommandScopeDefault + language\_code
- botCommandScopeDefault

**Commands in group and supergroup chats**

- botCommandScopeChatMember + language\_code
- botCommandScopeChatMember
- botCommandScopeChatAdministrators + language\_code (administrators only)
- botCommandScopeChatAdministrators (administrators only)
- botCommandScopeChat + language\_code
- botCommandScopeChat
- botCommandScopeAllChatAdministrators + language\_code (administrators only)
- botCommandScopeAllChatAdministrators (administrators only)
- botCommandScopeAllGroupChats + language\_code
- botCommandScopeAllGroupChats
- botCommandScopeDefault + language\_code
- botCommandScopeDefault
