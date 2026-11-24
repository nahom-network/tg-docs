# sendMediaGroup

Source: https://core.telegram.org/bots/api#sendmediagroup

[Documentation index](../llms.txt)

Use this method to send a group of photos, live photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an Array of [Message](message.md) objects that were sent is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message will be sent |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username` |
| message\_thread\_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| direct\_messages\_topic\_id | Integer | Optional | Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat |
| media | Array of [InputMediaAudio](inputmediaaudio.md), [InputMediaDocument](inputmediadocument.md), [InputMediaLivePhoto](inputmedialivephoto.md), [InputMediaPhoto](inputmediaphoto.md) and [InputMediaVideo](inputmediavideo.md) | Yes | A JSON-serialized Array describing messages to be sent, must include 2-10 items |
| disable\_notification | Boolean | Optional | Sends messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect\_content | Boolean | Optional | Protects the contents of the sent messages from forwarding and saving |
| allow\_paid\_broadcast | Boolean | Optional | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](../external/bots/faq.md#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. |
| message\_effect\_id | String | Optional | Unique identifier of the message effect to be added to the message; for private chats only |
| reply\_parameters | [ReplyParameters](replyparameters.md) | Optional | Description of the message to reply to |
