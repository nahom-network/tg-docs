# CallbackQuery

> Part of the [Telegram Bot API](/bots/api.md). Canonical location: [CallbackQuery](/bots/api#callbackquery).

This object represents an incoming callback query from a callback button in an [inline keyboard](/bots/features.md#inline-keyboards) or in a [rich message](/bots/api/types/richmessage.md). If the button that originated the query belongs to a message sent by the bot, the field *message* will be present, unless the field *inline_message_id* is used instead as specified by the parameter *callback_query_mode* of the method [setMySettings](/bots/api/methods/setmysettings.md). If the button belongs to a message sent via the bot (in [inline mode](/bots/api.md#inline-mode)), the field *inline_message_id* will be present. Exactly one of the fields *data* or *game_short_name* will be present.

|Field|Type|Description|
|-----------|
|id|String|Unique identifier for this query|
|from|[User](/bots/api/types/user.md)|Sender|
|message|[MaybeInaccessibleMessage](/bots/api/types/maybeinaccessiblemessage.md)|*Optional*. Message sent by the bot with the callback button that originated the query|
|inline_message_id|String|*Optional*. Identifier of the message sent via the bot in inline mode, that originated the query. Can also be present for messages sent by the bot, depending on the parameter *callback_query_mode* of the method [setMySettings](/bots/api/methods/setmysettings.md).|
|chat_instance|String|Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in [games](/bots/api.md#games).|
|data|String|*Optional*. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.|
|game_short_name|String|*Optional*. Short name of a [Game](/bots/api/types/game.md) to be returned, serves as the unique identifier for the game|

>**NOTE:** After the user presses a callback button, Telegram clients will display a progress bar until you call [answerCallbackQuery](/bots/api/methods/answercallbackquery.md). It is, therefore, necessary to react by calling [answerCallbackQuery](/bots/api/methods/answercallbackquery.md) even if no notification to the user is needed (e.g., without specifying any of the optional parameters).
