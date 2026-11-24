# November 9, 2026

Source: https://core.telegram.org/bots/api#november-9-2026

[Documentation index](../llms.txt)

**Bot API 10.4**

**Widgets**

- Added the class [Widget](widget.md) and the field *widget* to the classes [Message](message.md) and [ExternalReplyInfo](externalreplyinfo.md) for messages with [HTML widgets](../external/bots/widgets.md).
- Added the method [sendWidget](sendwidget.md), allowing bots to send messages with HTML widgets. Currently, in the production environment, widgets can be sent only to private chats, and sent widgets automatically have protected content and therefore can't be forwarded.
- Added the method [sendSharedWidget](sendsharedwidget.md), allowing bots to send again shared widgets created by the bot.
- Added the class [WidgetQuery](widgetquery.md) and the field *widget_query* to the class [Update](update.md) for queries sent to the bot by widgets in messages sent by the bot or via the bot.
- Added the class [SharedWidgetQuery](sharedwidgetquery.md) and the field *shared_widget_query* to the class [Update](update.md) for queries sent to the bot from forwarded messages with shared widgets.
- Added the classes [WidgetQueryType](widgetquerytype.md), [WidgetQueryTypeData](widgetquerytypedata.md), [WidgetQueryTypeSignData](widgetquerytypesigndata.md), [WidgetQueryTypeSentTransaction](widgetquerytypesenttransaction.md) and [WidgetQueryWallet](widgetquerywallet.md), describing the type of a query from a widget. A query can contain data for the bot together with the TON wallet card of the user, data signed by a TON wallet of the user, or a notification about a transaction sent from a TON wallet of the user.
- Added the method [answerWidgetQuery](answerwidgetquery.md), allowing bots to answer queries from widgets.
- Added the method [editMessageWidgetData](editmessagewidgetdata.md), allowing bots to change data of a widget in a message.
- Added the method [editSharedWidgetData](editsharedwidgetdata.md), allowing bots to change public data of a shared widget.
- Added the classes [InputWidgetMessageContent](inputwidgetmessagecontent.md) and [InputSharedWidgetMessageContent](inputsharedwidgetmessagecontent.md), allowing bots to send widgets in response to inline queries. Currently, widgets can't be sent in response to inline queries in the production environment.
- Widget messages can't be copied using the methods [copyMessage](copymessage.md) and [copyMessages](copymessages.md).
- The right *can_send_other_messages* in the classes [ChatPermissions](chatpermissions.md) and [ChatMemberRestricted](chatmemberrestricted.md) now also allows sending widgets.

**Ephemeral messages**

- Allowed bots to send ephemeral replies to callback queries in any chat except channel direct messages chats by specifying *callback_query_id* without *receiver_user_id* in the parameter *ephemeral_message_parameters* of the methods [sendMessage](sendmessage.md), [sendRichMessage](sendrichmessage.md), [sendAnimation](sendanimation.md), [sendAudio](sendaudio.md), [sendContact](sendcontact.md), [sendDocument](senddocument.md), [sendLivePhoto](sendlivephoto.md), [sendLocation](sendlocation.md), [sendPhoto](sendphoto.md), [sendSticker](sendsticker.md), [sendVenue](sendvenue.md), [sendVideo](sendvideo.md), [sendVideoNote](sendvideonote.md) and [sendVoice](sendvoice.md).
- The field *receiver_user_id* of the class [EphemeralMessageParameters](ephemeralmessageparameters.md) and the parameter *chat_id* of the mentioned methods are optional now.

**Quotes from rich messages**

- Added the field *rich_texts* to the class [TextQuote](textquote.md) for quotes chosen from a [RichMessage](richmessage.md).
- Added the field *quote_rich_texts* to the class [ReplyParameters](replyparameters.md), allowing bots to quote rich messages.

**TON wallet**

- Added the classes [TonWalletCard](tonwalletcard.md), [TonWalletCardSticker](tonwalletcardsticker.md), [TonNft](tonnft.md) and [TonNftAttribute](tonnftattribute.md), and the field *ton_wallet_card* to the class [ChatFullInfo](chatfullinfo.md).
- Added the class [TonWalletTransfer](tonwallettransfer.md) and the field *ton_wallet_transfer* to the class [Message](message.md) for service messages about transfers with a TON wallet.
- Renamed the class StoryAreaPosition to [AreaPosition](areaposition.md), because it is now also used to describe the position of stickers on TON wallet cards.

**Chat share themes**

- Added the classes [ChatShareTheme](chatsharetheme.md), [ChatShareThemeEmoji](chatsharethemeemoji.md) and [ChatShareThemeUniqueGift](chatsharethemeuniquegift.md), and the field *share_theme* to the class [ChatFullInfo](chatfullinfo.md), describing the theme of the screen for sharing a link to a user or a chat.
- Added the classes [EmojiType](emojitype.md), [EmojiTypeEmoji](emojitypeemoji.md) and [EmojiTypeCustomEmoji](emojitypecustomemoji.md).
- Added the classes [ChatShareThemeBackdrop](chatsharethemebackdrop.md) and [ChatShareThemeBackdrops](chatsharethemebackdrops.md) and the method [getChatShareThemeBackdrops](getchatsharethemebackdrops.md).

**Gifts**

- Added the method [getUniqueGift](getuniquegift.md), allowing bots to get information about a unique gift by its name.
- Added the method [deleteBusinessAccountGift](deletebusinessaccountgift.md), allowing bots to delete regular gifts owned by a managed business account without receiving Telegram Stars for them.

**General**

- Allowed users with a Telegram Premium subscription to assign secondary usernames ending with “agent”, “ai”, “app”, “game”, or “gay” to up to 2 owned bots. Such usernames can be suggested in the field *suggested_username* of the class [KeyboardButtonRequestManagedBot](keyboardbuttonrequestmanagedbot.md).
- Added the class [RichTextTonAddress](richtexttonaddress.md) representing an address in the TON blockchain in a [RichMessage](richmessage.md).
- Added the type “ton_address” to the class [MessageEntity](messageentity.md) for addresses in the TON blockchain.
- Added the type “bank_card_number” to the class [MessageEntity](messageentity.md) for bank card numbers.
- Added the parameters *custom_description_parse_mode* and *custom_description_entities* to the methods [verifyUser](verifyuser.md) and [verifyChat](verifychat.md).
- Added the class [PaidMessagesWaived](paidmessageswaived.md) and the field *paid_messages_waived* to the class [Message](message.md) for service messages about the sender using a link which allows sending messages without paying Telegram Stars.
- Added the ability to create links to topics in private chats with the bot in the format `https://t.me/<bot_username>/<message_thread_id>. Such a link opens the topic only for the user in the private chat with whom the topic exists.
