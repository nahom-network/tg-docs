# Message

Source: https://core.telegram.org/bots/api#message

[Documentation index](../llms.txt)

This object represents a message.

| Field | Type | Description |
| --- | --- | --- |
| message\_id | Integer | Unique message identifier inside this chat; 0 for ephemeral messages. In specific instances (e.g., a message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent. |
| message\_thread\_id | Integer | *Optional*. Unique identifier of a message thread or forum topic to which the message belongs; for supergroups and private chats only |
| direct\_messages\_topic | [DirectMessagesTopic](directmessagestopic.md) | *Optional*. Information about the direct messages chat topic that contains the message |
| from | [User](user.md) | *Optional*. Sender of the message; may be empty for messages sent to channels. For backward compatibility, if the message was sent on behalf of a chat, the field contains a fake sender user in non-channel chats. |
| sender\_chat | [Chat](chat.md) | *Optional*. Sender of the message when sent on behalf of a chat. For example, the supergroup itself for messages sent by its anonymous administrators or a linked channel for messages automatically forwarded to the channel's discussion group. For backward compatibility, if the message was sent on behalf of a chat, the field *from* contains a fake sender user in non-channel chats. |
| sender\_boost\_count | Integer | *Optional*. If the sender of the message boosted the chat, the number of boosts added by the user |
| sender\_business\_bot | [User](user.md) | *Optional*. The bot that actually sent the message on behalf of the business account. Available only for outgoing messages sent on behalf of the connected business account. |
| sender\_tag | String | *Optional*. Tag or custom title of the sender of the message; for supergroups only |
| receiver\_user | [User](user.md) | *Optional*. For ephemeral messages, the user who received the message |
| ephemeral\_message\_id | Integer | *Optional*. For ephemeral messages, identifier of the ephemeral message inside this chat. The identifier may be reused for another ephemeral message after the message is deleted or expires. |
| date | Integer | Date the message was sent in Unix time. It is always a positive number, representing a valid date. |
| guest\_query\_id | String | *Optional*. The unique identifier for the guest query. Use this identifier with the method [answerGuestQuery](answerguestquery.md) to send a response message. If non-empty, the message belongs to the chat where the guest bot was summoned, which may not coincide with other existing bot chats sharing the same identifier. |
| business\_connection\_id | String | *Optional*. Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier. |
| chat | [Chat](chat.md) | Chat the message belongs to |
| forward\_origin | [MessageOrigin](messageorigin.md) | *Optional*. Information about the original message for forwarded messages |
| is\_topic\_message | True | *Optional*. *True*, if the message is sent to a topic in a forum supergroup or a private chat with the bot |
| is\_automatic\_forward | True | *Optional*. *True*, if the message is a channel post that was automatically forwarded to the connected discussion group |
| reply\_to\_message | [Message](message.md) | *Optional*. For replies in the same chat and message thread, the original message. Note that the [Message](message.md) object in this field will not contain further *reply\_to\_message* fields even if it itself is a reply. If the message is a reply to an ephemeral message, then this field may be omitted. |
| external\_reply | [ExternalReplyInfo](externalreplyinfo.md) | *Optional*. Information about the message that is being replied to, which may come from another chat or forum topic |
| quote | [TextQuote](textquote.md) | *Optional*. For replies that quote part of the original message, the quoted part of the message |
| reply\_to\_story | [Story](story.md) | *Optional*. For replies to a story, the original story |
| reply\_to\_checklist\_task\_id | Integer | *Optional*. Identifier of the specific checklist task that is being replied to |
| reply\_to\_poll\_option\_id | String | *Optional*. Persistent identifier of the specific poll option that is being replied to |
| via\_bot | [User](user.md) | *Optional*. Bot through which the message was sent |
| guest\_bot\_caller\_user | [User](user.md) | *Optional*. For a message sent by a guest bot, this is the user whose original message triggered the bot's response |
| guest\_bot\_caller\_chat | [Chat](chat.md) | *Optional*. For a message sent by a guest bot, this is the chat whose original message triggered the bot's response |
| edit\_date | Integer | *Optional*. Date the message was last edited in Unix time |
| has\_protected\_content | True | *Optional*. *True*, if the message can't be forwarded |
| is\_from\_offline | True | *Optional*. *True*, if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message |
| is\_paid\_post | True | *Optional*. *True*, if the message is a paid post. Note that such posts must not be deleted for 24 hours to receive the payment and can't be edited. |
| media\_group\_id | String | *Optional*. The unique identifier inside this chat of a media message group this message belongs to |
| author\_signature | String | *Optional*. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator |
| paid\_star\_count | Integer | *Optional*. The number of Telegram Stars that were paid by the sender of the message to send it |
| text | String | *Optional*. For text messages, the actual UTF-8 text of the message |
| entities | Array of [MessageEntity](messageentity.md) | *Optional*. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text |
| link\_preview\_options | [LinkPreviewOptions](linkpreviewoptions.md) | *Optional*. Options used for link preview generation for the message, if it is a text message and link preview options were changed |
| suggested\_post\_info | [SuggestedPostInfo](suggestedpostinfo.md) | *Optional*. Information about suggested post parameters if the message is a suggested post in a channel direct messages chat. If the message is an approved or declined suggested post, then it can't be edited. |
| effect\_id | String | *Optional*. Unique identifier of the message effect added to the message |
| rich\_message | [RichMessage](richmessage.md) | *Optional*. Message is a rich formatted message |
| animation | [Animation](animation.md) | *Optional*. Message is an animation, information about the animation. For backward compatibility, when this field is set, the *document* field will also be set. |
| audio | [Audio](audio.md) | *Optional*. Message is an audio file, information about the file |
| document | [Document](document.md) | *Optional*. Message is a general file, information about the file |
| live\_photo | [LivePhoto](livephoto.md) | *Optional*. Message is a live photo, information about the live photo. For backward compatibility, when this field is set, the *photo* field will also be set. |
| paid\_media | [PaidMediaInfo](paidmediainfo.md) | *Optional*. Message contains paid media; information about the paid media |
| photo | Array of [PhotoSize](photosize.md) | *Optional*. Message is a photo, available sizes of the photo |
| sticker | [Sticker](sticker.md) | *Optional*. Message is a sticker, information about the sticker |
| story | [Story](story.md) | *Optional*. Message is a forwarded story |
| video | [Video](video.md) | *Optional*. Message is a video, information about the video |
| video\_note | [VideoNote](videonote.md) | *Optional*. Message is a [video note](https://telegram.org/blog/video-messages-and-telescope), information about the video message |
| voice | [Voice](voice.md) | *Optional*. Message is a voice message, information about the file |
| caption | String | *Optional*. Caption for the animation, audio, document, paid media, photo, video or voice |
| caption\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption |
| show\_caption\_above\_media | True | *Optional*. *True*, if the caption must be shown above the message media |
| has\_media\_spoiler | True | *Optional*. *True*, if the message media is covered by a spoiler animation |
| checklist | [Checklist](checklist.md) | *Optional*. Message is a checklist |
| contact | [Contact](contact.md) | *Optional*. Message is a shared contact, information about the contact |
| dice | [Dice](dice.md) | *Optional*. Message is a dice with random value |
| game | [Game](game.md) | *Optional*. Message is a game, information about the game. [More about games »](games.md) |
| poll | [Poll](poll.md) | *Optional*. Message is a native poll, information about the poll |
| venue | [Venue](venue.md) | *Optional*. Message is a venue, information about the venue. For backward compatibility, when this field is set, the *location* field will also be set. |
| location | [Location](location.md) | *Optional*. Message is a shared location, information about the location |
| new\_chat\_members | Array of [User](user.md) | *Optional*. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members) |
| left\_chat\_member | [User](user.md) | *Optional*. A member was removed from the group, information about them (this member may be the bot itself) |
| chat\_owner\_left | [ChatOwnerLeft](chatownerleft.md) | *Optional*. Service message: chat owner has left |
| chat\_owner\_changed | [ChatOwnerChanged](chatownerchanged.md) | *Optional*. Service message: chat owner has changed |
| new\_chat\_title | String | *Optional*. A chat title was changed to this value |
| new\_chat\_photo | Array of [PhotoSize](photosize.md) | *Optional*. A chat photo was change to this value |
| delete\_chat\_photo | True | *Optional*. Service message: the chat photo was deleted |
| group\_chat\_created | True | *Optional*. Service message: the group has been created |
| supergroup\_chat\_created | True | *Optional*. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply\_to\_message if someone replies to a very first message in a directly created supergroup. |
| channel\_chat\_created | True | *Optional*. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply\_to\_message if someone replies to a very first message in a channel. |
| message\_auto\_delete\_timer\_changed | [MessageAutoDeleteTimerChanged](messageautodeletetimerchanged.md) | *Optional*. Service message: auto-delete timer settings changed in the chat |
| migrate\_to\_chat\_id | Integer | *Optional*. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. |
| migrate\_from\_chat\_id | Integer | *Optional*. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier. |
| pinned\_message | [MaybeInaccessibleMessage](maybeinaccessiblemessage.md) | *Optional*. Specified message was pinned. Note that the [Message](message.md) object in this field will not contain further *reply\_to\_message* fields even if it itself is a reply. |
| invoice | [Invoice](invoice.md) | *Optional*. Message is an invoice for a [payment](payments.md), information about the invoice. [More about payments »](payments.md) |
| successful\_payment | [SuccessfulPayment](successfulpayment.md) | *Optional*. Message is a service message about a successful payment, information about the payment. [More about payments »](payments.md) |
| refunded\_payment | [RefundedPayment](refundedpayment.md) | *Optional*. Message is a service message about a refunded payment, information about the payment. [More about payments »](payments.md) |
| users\_shared | [UsersShared](usersshared.md) | *Optional*. Service message: users were shared with the bot |
| chat\_shared | [ChatShared](chatshared.md) | *Optional*. Service message: a chat was shared with the bot |
| gift | [GiftInfo](giftinfo.md) | *Optional*. Service message: a regular gift was sent or received |
| unique\_gift | [UniqueGiftInfo](uniquegiftinfo.md) | *Optional*. Service message: a unique gift was sent or received |
| gift\_upgrade\_sent | [GiftInfo](giftinfo.md) | *Optional*. Service message: upgrade of a gift was purchased after the gift was sent |
| connected\_website | String | *Optional*. The domain name of the website on which the user has logged in. [More about Telegram Login »](https://core.telegram.org/widgets/login) |
| write\_access\_allowed | [WriteAccessAllowed](writeaccessallowed.md) | *Optional*. Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method [requestWriteAccess](https://core.telegram.org/bots/webapps#initializing-mini-apps) |
| passport\_data | [PassportData](passportdata.md) | *Optional*. Telegram Passport data |
| proximity\_alert\_triggered | [ProximityAlertTriggered](proximityalerttriggered.md) | *Optional*. Service message: a user in the chat triggered another user's proximity alert while sharing Live Location |
| boost\_added | [ChatBoostAdded](chatboostadded.md) | *Optional*. Service message: user boosted the chat |
| chat\_background\_set | [ChatBackground](chatbackground.md) | *Optional*. Service message: chat background set |
| checklist\_tasks\_done | [ChecklistTasksDone](checklisttasksdone.md) | *Optional*. Service message: some tasks in a checklist were marked as done or not done |
| checklist\_tasks\_added | [ChecklistTasksAdded](checklisttasksadded.md) | *Optional*. Service message: tasks were added to a checklist |
| community\_chat\_added | [CommunityChatAdded](communitychatadded.md) | *Optional*. Service message: chat or bot added to a [Community](community.md) |
| community\_chat\_joined | [CommunityChatJoined](communitychatjoined.md) | *Optional*. Service message: chat was joined by a user from a [Community](community.md) |
| community\_chat\_removed | [CommunityChatRemoved](communitychatremoved.md) | *Optional*. Service message: chat or bot removed from a [Community](community.md) |
| direct\_message\_price\_changed | [DirectMessagePriceChanged](directmessagepricechanged.md) | *Optional*. Service message: the price for paid messages in the corresponding direct messages chat of a channel has changed |
| forum\_topic\_created | [ForumTopicCreated](forumtopiccreated.md) | *Optional*. Service message: forum topic created |
| forum\_topic\_edited | [ForumTopicEdited](forumtopicedited.md) | *Optional*. Service message: forum topic edited |
| forum\_topic\_closed | [ForumTopicClosed](forumtopicclosed.md) | *Optional*. Service message: forum topic closed |
| forum\_topic\_reopened | [ForumTopicReopened](forumtopicreopened.md) | *Optional*. Service message: forum topic reopened |
| general\_forum\_topic\_hidden | [GeneralForumTopicHidden](generalforumtopichidden.md) | *Optional*. Service message: the 'General' forum topic hidden |
| general\_forum\_topic\_unhidden | [GeneralForumTopicUnhidden](generalforumtopicunhidden.md) | *Optional*. Service message: the 'General' forum topic unhidden |
| giveaway\_created | [GiveawayCreated](giveawaycreated.md) | *Optional*. Service message: a scheduled giveaway was created |
| giveaway | [Giveaway](giveaway.md) | *Optional*. The message is a scheduled giveaway message |
| giveaway\_winners | [GiveawayWinners](giveawaywinners.md) | *Optional*. A giveaway with public winners was completed |
| giveaway\_completed | [GiveawayCompleted](giveawaycompleted.md) | *Optional*. Service message: a giveaway without public winners was completed |
| managed\_bot\_created | [ManagedBotCreated](managedbotcreated.md) | *Optional*. Service message: user created a bot that will be managed by the current bot |
| paid\_message\_price\_changed | [PaidMessagePriceChanged](paidmessagepricechanged.md) | *Optional*. Service message: the price for paid messages has changed in the chat |
| poll\_option\_added | [PollOptionAdded](polloptionadded.md) | *Optional*. Service message: answer option was added to a poll |
| poll\_option\_deleted | [PollOptionDeleted](polloptiondeleted.md) | *Optional*. Service message: answer option was deleted from a poll |
| suggested\_post\_approved | [SuggestedPostApproved](suggestedpostapproved.md) | *Optional*. Service message: a suggested post was approved |
| suggested\_post\_approval\_failed | [SuggestedPostApprovalFailed](suggestedpostapprovalfailed.md) | *Optional*. Service message: approval of a suggested post has failed |
| suggested\_post\_declined | [SuggestedPostDeclined](suggestedpostdeclined.md) | *Optional*. Service message: a suggested post was declined |
| suggested\_post\_paid | [SuggestedPostPaid](suggestedpostpaid.md) | *Optional*. Service message: payment for a suggested post was received |
| suggested\_post\_refunded | [SuggestedPostRefunded](suggestedpostrefunded.md) | *Optional*. Service message: payment for a suggested post was refunded |
| video\_chat\_scheduled | [VideoChatScheduled](videochatscheduled.md) | *Optional*. Service message: video chat scheduled |
| video\_chat\_started | [VideoChatStarted](videochatstarted.md) | *Optional*. Service message: video chat started |
| video\_chat\_ended | [VideoChatEnded](videochatended.md) | *Optional*. Service message: video chat ended |
| video\_chat\_participants\_invited | [VideoChatParticipantsInvited](videochatparticipantsinvited.md) | *Optional*. Service message: new participants invited to a video chat |
| web\_app\_data | [WebAppData](webappdata.md) | *Optional*. Service message: data sent by a Web App |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message. `login_url` buttons are represented as ordinary `url` buttons. |
