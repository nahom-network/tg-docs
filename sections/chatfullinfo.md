# ChatFullInfo

Source: https://core.telegram.org/bots/api#chatfullinfo

[Documentation index](../llms.txt)

This object contains full information about a chat.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. |
| type | String | Type of the chat, can be either “private”, “group”, “supergroup” or “channel” |
| title | String | *Optional*. Title, for supergroups, channels and group chats |
| username | String | *Optional*. Username, for private chats, supergroups and channels if available |
| first\_name | String | *Optional*. First name of the other party in a private chat |
| last\_name | String | *Optional*. Last name of the other party in a private chat |
| is\_forum | True | *Optional*. *True*, if the supergroup chat is a forum (has [topics](https://telegram.org/blog/topics-in-groups-collectible-usernames#topics-in-groups) enabled) |
| is\_direct\_messages | True | *Optional*. *True*, if the chat is the direct messages chat of a channel |
| accent\_color\_id | Integer | Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See [accent colors](accent-colors.md) for more details. |
| max\_reaction\_count | Integer | The maximum number of reactions that can be set on a message in the chat |
| photo | [ChatPhoto](chatphoto.md) | *Optional*. Chat photo |
| active\_usernames | Array of String | *Optional*. If non-empty, the list of all [active chat usernames](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames); for private chats, supergroups and channels |
| birthdate | [Birthdate](birthdate.md) | *Optional*. For private chats, the date of birth of the user |
| business\_intro | [BusinessIntro](businessintro.md) | *Optional*. For private chats with business accounts, the intro of the business |
| business\_location | [BusinessLocation](businesslocation.md) | *Optional*. For private chats with business accounts, the location of the business |
| business\_opening\_hours | [BusinessOpeningHours](businessopeninghours.md) | *Optional*. For private chats with business accounts, the opening hours of the business |
| personal\_chat | [Chat](chat.md) | *Optional*. For private chats, the personal channel of the user |
| parent\_chat | [Chat](chat.md) | *Optional*. Information about the corresponding channel chat; for direct messages chats only |
| available\_reactions | Array of [ReactionType](reactiontype.md) | *Optional*. List of available reactions allowed in the chat. If omitted, then all [emoji reactions](reactiontypeemoji.md) are allowed. |
| background\_custom\_emoji\_id | String | *Optional*. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background |
| profile\_accent\_color\_id | Integer | *Optional*. Identifier of the accent color for the chat's profile background. See [profile accent colors](profile-accent-colors.md) for more details. |
| profile\_background\_custom\_emoji\_id | String | *Optional*. Custom emoji identifier of the emoji chosen by the chat for its profile background |
| emoji\_status\_custom\_emoji\_id | String | *Optional*. Custom emoji identifier of the emoji status of the chat or the other party in a private chat |
| emoji\_status\_expiration\_date | Integer | *Optional*. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any |
| bio | String | *Optional*. Bio of the other party in a private chat |
| has\_private\_forwards | True | *Optional*. *True*, if privacy settings of the other party in the private chat allows to use `tg://user?id=<user_id>` links only in chats with the user |
| has\_restricted\_voice\_and\_video\_messages | True | *Optional*. *True*, if the privacy settings of the other party restrict sending voice and video note messages in the private chat |
| join\_to\_send\_messages | True | *Optional*. *True*, if users need to join the supergroup before they can send messages |
| join\_by\_request | True | *Optional*. *True*, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators |
| description | String | *Optional*. Description, for groups, supergroups and channel chats |
| invite\_link | String | *Optional*. Primary invite link, for groups, supergroups and channel chats |
| pinned\_message | [Message](message.md) | *Optional*. The most recent pinned message (by sending date) |
| permissions | [ChatPermissions](chatpermissions.md) | *Optional*. Default chat member permissions, for groups and supergroups |
| accepted\_gift\_types | [AcceptedGiftTypes](acceptedgifttypes.md) | Information about types of gifts that are accepted by the chat or by the corresponding user for private chats |
| can\_send\_paid\_media | True | *Optional*. *True*, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats. |
| slow\_mode\_delay | Integer | *Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds |
| unrestrict\_boost\_count | Integer | *Optional*. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions |
| message\_auto\_delete\_time | Integer | *Optional*. The time after which all messages sent to the chat will be automatically deleted; in seconds |
| has\_aggressive\_anti\_spam\_enabled | True | *Optional*. *True*, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. |
| has\_hidden\_members | True | *Optional*. *True*, if non-administrators can only get the list of bots and administrators in the chat |
| has\_protected\_content | True | *Optional*. *True*, if messages from the chat can't be forwarded to other chats |
| has\_visible\_history | True | *Optional*. *True*, if new chat members will have access to old messages; available only to chat administrators |
| sticker\_set\_name | String | *Optional*. For supergroups, name of the group sticker set |
| can\_set\_sticker\_set | True | *Optional*. *True*, if the bot can change the group sticker set |
| custom\_emoji\_sticker\_set\_name | String | *Optional*. For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group. |
| linked\_chat\_id | Integer | *Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. |
| location | [ChatLocation](chatlocation.md) | *Optional*. For supergroups, the location to which the supergroup is connected |
| rating | [UserRating](userrating.md) | *Optional*. For private chats, the rating of the user if any |
| first\_profile\_audio | [Audio](audio.md) | *Optional*. For private chats, the first audio added to the profile of the user |
| unique\_gift\_colors | [UniqueGiftColors](uniquegiftcolors.md) | *Optional*. The color scheme based on a unique gift that must be used for the chat's name, message replies and link previews |
| paid\_message\_star\_count | Integer | *Optional*. The number of Telegram Stars a general user has to pay to send a message to the chat |
| guard\_bot | [User](user.md) | *Optional*. The bot that processes join request queries in the chat. The field is only available to chat administrators. |
| community | [Community](community.md) | *Optional*. The [Community](community.md) to which the chat belongs |
| ton\_wallet\_card | [TonWalletCard](tonwalletcard.md) | *Optional*. For private chats, the TON wallet card of the user, which is shown on their profile page |
| share\_theme | [ChatShareTheme](chatsharetheme.md) | *Optional*. For private chats, supergroups and channels, the theme of the screen for sharing a link to the user or the chat; omitted if the default theme is used |
