# ExternalReplyInfo

Source: https://core.telegram.org/bots/api#externalreplyinfo

[Documentation index](../llms.txt)

This object contains information about a message that is being replied to, which may come from another chat or forum topic.

| Field | Type | Description |
| --- | --- | --- |
| origin | [MessageOrigin](messageorigin.md) | Origin of the message replied to by the given message |
| chat | [Chat](chat.md) | *Optional*. Chat the original message belongs to. Available only if the chat is a supergroup or a channel. |
| message\_id | Integer | *Optional*. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel. |
| link\_preview\_options | [LinkPreviewOptions](linkpreviewoptions.md) | *Optional*. Options used for link preview generation for the original message, if it is a text message |
| animation | [Animation](animation.md) | *Optional*. Message is an animation, information about the animation |
| audio | [Audio](audio.md) | *Optional*. Message is an audio file, information about the file |
| document | [Document](document.md) | *Optional*. Message is a general file, information about the file |
| live\_photo | [LivePhoto](livephoto.md) | *Optional*. Message is a live photo, information about the live photo |
| paid\_media | [PaidMediaInfo](paidmediainfo.md) | *Optional*. Message contains paid media; information about the paid media |
| photo | Array of [PhotoSize](photosize.md) | *Optional*. Message is a photo, available sizes of the photo |
| sticker | [Sticker](sticker.md) | *Optional*. Message is a sticker, information about the sticker |
| story | [Story](story.md) | *Optional*. Message is a forwarded story |
| video | [Video](video.md) | *Optional*. Message is a video, information about the video |
| video\_note | [VideoNote](videonote.md) | *Optional*. Message is a [video note](https://telegram.org/blog/video-messages-and-telescope), information about the video message |
| voice | [Voice](voice.md) | *Optional*. Message is a voice message, information about the file |
| widget | [Widget](widget.md) | *Optional*. Message is an HTML widget, information about the widget |
| has\_media\_spoiler | True | *Optional*. *True*, if the message media is covered by a spoiler animation |
| checklist | [Checklist](checklist.md) | *Optional*. Message is a checklist |
| contact | [Contact](contact.md) | *Optional*. Message is a shared contact, information about the contact |
| dice | [Dice](dice.md) | *Optional*. Message is a dice with random value |
| game | [Game](game.md) | *Optional*. Message is a game, information about the game. [More about games »](games.md) |
| giveaway | [Giveaway](giveaway.md) | *Optional*. Message is a scheduled giveaway, information about the giveaway |
| giveaway\_winners | [GiveawayWinners](giveawaywinners.md) | *Optional*. A giveaway with public winners was completed |
| invoice | [Invoice](invoice.md) | *Optional*. Message is an invoice for a [payment](payments.md), information about the invoice. [More about payments »](payments.md) |
| location | [Location](location.md) | *Optional*. Message is a shared location, information about the location |
| poll | [Poll](poll.md) | *Optional*. Message is a native poll, information about the poll |
| venue | [Venue](venue.md) | *Optional*. Message is a venue, information about the venue |
