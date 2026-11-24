# Update

Source: https://core.telegram.org/bots/api#update

[Documentation index](../llms.txt)

This [object](available-types.md) represents an incoming update.  
At most **one** of the optional fields can be present in any given update.

| Field | Type | Description |
| --- | --- | --- |
| update\_id | Integer | The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This identifier becomes especially handy if you're using [webhooks](setwebhook.md), since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially. |
| message | [Message](message.md) | *Optional*. New incoming message of any kind - text, photo, sticker, etc. |
| edited\_message | [Message](message.md) | *Optional*. New version of a message that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot. |
| channel\_post | [Message](message.md) | *Optional*. New incoming channel post of any kind - text, photo, sticker, etc. |
| edited\_channel\_post | [Message](message.md) | *Optional*. New version of a channel post that is known to the bot and was edited. This update may at times be triggered by changes to message fields that are either unavailable or not actively used by your bot. |
| business\_connection | [BusinessConnection](businessconnection.md) | *Optional*. The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot |
| business\_message | [Message](message.md) | *Optional*. New message from a connected business account |
| edited\_business\_message | [Message](message.md) | *Optional*. New version of a message from a connected business account |
| deleted\_business\_messages | [BusinessMessagesDeleted](businessmessagesdeleted.md) | *Optional*. Messages were deleted from a connected business account |
| guest\_message | [Message](message.md) | *Optional*. New guest message. The bot can use the field *Message.guest\_query\_id* and the method [answerGuestQuery](answerguestquery.md) to send a message in response. |
| message\_reaction | [MessageReactionUpdated](messagereactionupdated.md) | *Optional*. A reaction to a message was changed by a user. The bot must be an administrator in the chat and must explicitly specify `"message_reaction"` in the list of *allowed\_updates* to receive these updates. The update isn't received for reactions set by bots. |
| message\_reaction\_count | [MessageReactionCountUpdated](messagereactioncountupdated.md) | *Optional*. Reactions to a message with anonymous reactions were changed. The bot must be an administrator in the chat and must explicitly specify `"message_reaction_count"` in the list of *allowed\_updates* to receive these updates. The updates are grouped and can be sent with delay up to a few minutes. |
| inline\_query | [InlineQuery](inlinequery.md) | *Optional*. New incoming [inline](inline-mode.md) query |
| chosen\_inline\_result | [ChosenInlineResult](choseninlineresult.md) | *Optional*. The result of an [inline](inline-mode.md) query that was chosen by a user and sent to their chat partner. Please see our documentation on the [feedback collecting](../external/bots/inline.md#collecting-feedback) for details on how to enable these updates for your bot. |
| callback\_query | [CallbackQuery](callbackquery.md) | *Optional*. New incoming callback query |
| shipping\_query | [ShippingQuery](shippingquery.md) | *Optional*. New incoming shipping query. Only for invoices with flexible price. |
| pre\_checkout\_query | [PreCheckoutQuery](precheckoutquery.md) | *Optional*. New incoming pre-checkout query. Contains full information about checkout. |
| purchased\_paid\_media | [PaidMediaPurchased](paidmediapurchased.md) | *Optional*. A user purchased paid media with a non-empty payload sent by the bot in a non-channel chat |
| poll | [Poll](poll.md) | *Optional*. New poll state. Bots receive only updates about manually stopped polls and polls, which are sent by the bot. |
| poll\_answer | [PollAnswer](pollanswer.md) | *Optional*. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself. |
| my\_chat\_member | [ChatMemberUpdated](chatmemberupdated.md) | *Optional*. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user. |
| chat\_member | [ChatMemberUpdated](chatmemberupdated.md) | *Optional*. A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify `"chat_member"` in the list of *allowed\_updates* to receive these updates. |
| chat\_join\_request | [ChatJoinRequest](chatjoinrequest.md) | *Optional*. A request to join the chat has been sent. The bot must have the *can\_invite\_users* administrator right in the chat to receive these updates. |
| chat\_boost | [ChatBoostUpdated](chatboostupdated.md) | *Optional*. A chat boost was added or changed. The bot must be an administrator in the chat to receive these updates. |
| removed\_chat\_boost | [ChatBoostRemoved](chatboostremoved.md) | *Optional*. A boost was removed from a chat. The bot must be an administrator in the chat to receive these updates. |
| managed\_bot | [ManagedBotUpdated](managedbotupdated.md) | *Optional*. A new bot was created to be managed by the bot, or token or owner of a managed bot was changed |
| subscription | [BotSubscriptionUpdated](botsubscriptionupdated.md) | *Optional*. User payment subscription has changed |
| stopped\_message\_generation | [MessageGenerationStopped](messagegenerationstopped.md) | *Optional*. A user asked the bot to stop the generation of a message |
