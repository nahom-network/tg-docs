# November 22, 2026

Source: https://core.telegram.org/bots/api#november-22-2026

[Documentation index](../llms.txt)

**Bot API 10.5**

**Bot Settings**

- Added the method [setMySettings](setmysettings.md), allowing bots to change their settings, including inline mode settings, privacy mode, the ability to be added to groups, forum topic mode in private chats, and the mode of receiving callback queries.
- Added the ability to receive callback queries from buttons in messages sent by the bot with the field *inline\_message\_id* instead of the field *message* in the class [CallbackQuery](callbackquery.md), depending on the parameter *callback\_query\_mode* of the method [setMySettings](setmysettings.md).
- Added the ability for bots to show the list of topics in a sidebar in private chats with the bot using the parameter *has\_topic\_sidebar* of the method [setMySettings](setmysettings.md).
- Split out the class [BotFullInfo](botfullinfo.md) from the class [User](user.md) and changed the return type of the method [getMe](getme.md) to *BotFullInfo*. The fields that were returned only in [getMe](getme.md) were removed from the class [User](user.md).
- Added the field *active\_usernames* to the class [BotFullInfo](botfullinfo.md), allowing the bot to get the list of all its active usernames.
- Added the field *inline\_query\_placeholder* to the class [BotFullInfo](botfullinfo.md), allowing the bot to get its placeholder for inline queries.
- Added the field *needs\_inline\_query\_location* to the class [BotFullInfo](botfullinfo.md), allowing the bot to check whether it requests the location of the user with every inline query.
- Added the field *has\_topic\_sidebar* to the class [BotFullInfo](botfullinfo.md), allowing the bot to check whether topics in private chats with the bot are shown in a sidebar.

**General**

- Added the ability for bot owners to invite up to 10 users at once to private chats with the bot by pressing the link `https://t.me/botinvite/<bot_username>`. The bot can send messages to the invited users.
- Added the field *inviter* to the class [WriteAccessAllowed](writeaccessallowed.md) for service messages about users invited to the private chat with the bot by the owner of the bot.
- Replaced the field *text* with the field *blocks* in the classes [RichBlockExpandableBlockQuotation](richblockexpandableblockquotation.md) and [InputRichBlockExpandableBlockQuotation](inputrichblockexpandableblockquotation.md), allowing expandable block quotations to contain arbitrary blocks.
