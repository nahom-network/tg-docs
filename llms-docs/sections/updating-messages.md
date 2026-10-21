# Updating messages

Source: https://core.telegram.org/bots/api#updating-messages

[Documentation index](../llms.txt)

The following methods allow you to change an existing message in the message history instead of sending a new one with a result of an action. This is most useful for messages with [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards) using callback queries, but can also help reduce clutter in conversations with regular chat bots.

Please note, that it is currently only possible to edit messages without *reply_markup* or with [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards).

## In this section

- [editMessageText](editmessagetext.md)
- [editMessageCaption](editmessagecaption.md)
- [editMessageMedia](editmessagemedia.md)
- [editMessageLiveLocation](editmessagelivelocation.md)
- [stopMessageLiveLocation](stopmessagelivelocation.md)
- [editMessageChecklist](editmessagechecklist.md)
- [editMessageReplyMarkup](editmessagereplymarkup.md)
- [stopPoll](stoppoll.md)
- [editEphemeralMessageText](editephemeralmessagetext.md)
- [editEphemeralMessageMedia](editephemeralmessagemedia.md)
- [editEphemeralMessageCaption](editephemeralmessagecaption.md)
- [editEphemeralMessageReplyMarkup](editephemeralmessagereplymarkup.md)
- [approveSuggestedPost](approvesuggestedpost.md)
- [declineSuggestedPost](declinesuggestedpost.md)
- [deleteMessage](deletemessage.md)
- [deleteMessages](deletemessages.md)
- [deleteEphemeralMessage](deleteephemeralmessage.md)
- [deleteMessageReaction](deletemessagereaction.md)
- [deleteAllMessageReactions](deleteallmessagereactions.md)
