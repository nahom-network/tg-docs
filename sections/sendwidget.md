# sendWidget

Source: https://core.telegram.org/bots/api#sendwidget

[Documentation index](../llms.txt)

Use this method to send a message with an [HTML widget](../external/bots/widgets.md). Currently, in the production environment, widgets can be sent only to private chats, and sent widgets automatically have protected content and therefore can't be forwarded. On success, the sent [Message](message.md) is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| message\_thread\_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| html | String | Yes | HTML code of the widget, 1-32768 bytes. The code must not exceed 4096 bytes when compressed by zlib with the maximum compression level. |
| width | Integer | Optional | Width of the widget in logical pixels; omit if the widget must occupy the whole width of the message bubble. The width is clamped by the app to the range from 200 to the maximum width of the message bubble. |
| height | Integer | Optional | Height of the widget in logical pixels; omit if the height of the widget isn't fixed. The height is clamped by the app to the range 50-600. |
| public\_data | String | Optional | Public data of the widget, 0-1024 bytes, which will be available wherever the widget is shown. If the widget is shared, then all messages with it will have the same public data. |
| chat\_data | String | Optional | Data of the widget, which is specific to the message, 0-1024 bytes |
| caption | String | Optional | Widget caption, 0-1024 characters after entities parsing |
| parse\_mode | String | Optional | Mode for parsing entities in the widget caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | Optional | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| show\_caption\_above\_media | Boolean | Optional | Pass *True* if the caption must be shown above the widget |
| allow\_queries | Boolean | Optional | Pass *True* to allow the widget to send queries to the bot |
| is\_shared | Boolean | Optional | Pass *True* to create a shared widget, which can be sent again using the method [sendSharedWidget](sendsharedwidget.md) |
| disable\_notification | Boolean | Optional | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect\_content | Boolean | Optional | Protects the contents of the sent message from forwarding and saving |
| allow\_paid\_broadcast | Boolean | Optional | Pass *True* to allow up to 1000 messages per second, ignoring [broadcasting limits](../external/bots/faq.md#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. |
| message\_effect\_id | String | Optional | Unique identifier of the message effect to be added to the message; for private chats only |
| reply\_parameters | [ReplyParameters](replyparameters.md) | Optional | Description of the message to reply to |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) or [ReplyKeyboardMarkup](replykeyboardmarkup.md) or [ReplyKeyboardRemove](replykeyboardremove.md) or [ForceReply](forcereply.md) | Optional | Additional interface options. A JSON-serialized object for an [inline keyboard](../external/bots/features.md#inline-keyboards), [custom reply keyboard](../external/bots/features.md#keyboards), instructions to remove a reply keyboard or to force a reply from the user. |
