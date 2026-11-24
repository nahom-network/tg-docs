# sendVoice

Source: https://core.telegram.org/bots/api#sendvoice

[Documentation index](../llms.txt)

Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as [Audio](audio.md) or [Document](document.md)). On success, the sent [Message](message.md) is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Optional | Unique identifier of the business connection on behalf of which the message will be sent |
| chat\_id | Integer or String | Optional | Unique identifier for the target chat or username of the target bot, supergroup, or channel in the format `@username`; required unless the message is sent as an ephemeral reply to a callback query |
| message\_thread\_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| direct\_messages\_topic\_id | Integer | Optional | Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat |
| ephemeral\_message\_parameters | [EphemeralMessageParameters](ephemeralmessageparameters.md) | Optional | A JSON-serialized object containing the parameters of the ephemeral message to send |
| voice | [InputFile](inputfile.md) or String | Yes | Audio file to send. Pass a file\_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More information on Sending Files »](sending-files.md) |
| caption | String | Optional | Voice message caption, 0-1024 characters after entities parsing |
| parse\_mode | String | Optional | Mode for parsing entities in the voice message caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | Optional | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| duration | Integer | Optional | Duration of the voice message in seconds |
| disable\_notification | Boolean | Optional | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect\_content | Boolean | Optional | Protects the contents of the sent message from forwarding and saving |
| allow\_paid\_broadcast | Boolean | Optional | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](../external/bots/faq.md#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. |
| message\_effect\_id | String | Optional | Unique identifier of the message effect to be added to the message; for private chats only |
| suggested\_post\_parameters | [SuggestedPostParameters](suggestedpostparameters.md) | Optional | A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. |
| reply\_parameters | [ReplyParameters](replyparameters.md) | Optional | Description of the message to reply to |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) or [ReplyKeyboardMarkup](replykeyboardmarkup.md) or [ReplyKeyboardRemove](replykeyboardremove.md) or [ForceReply](forcereply.md) | Optional | Additional interface options. A JSON-serialized object for an [inline keyboard](../external/bots/features.md#inline-keyboards), [custom reply keyboard](../external/bots/features.md#keyboards), instructions to remove a reply keyboard or to force a reply from the user. |
