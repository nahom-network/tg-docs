# CallbackQuery

Source: https://core.telegram.org/bots/api#callbackquery

[Documentation index](../llms.txt)

This object represents an incoming callback query from a callback button in an [inline keyboard](../external/bots/features.md#inline-keyboards) or in a [rich message](richmessage.md). If the button that originated the query belongs to a message sent by the bot, the field *message* will be present, unless the field *inline\_message\_id* is used instead as specified by the parameter *callback\_query\_mode* of the method [setMySettings](setmysettings.md). If the button belongs to a message sent via the bot (in [inline mode](inline-mode.md)), the field *inline\_message\_id* will be present. Exactly one of the fields *data* or *game\_short\_name* will be present.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier for this query |
| from | [User](user.md) | Sender |
| message | [MaybeInaccessibleMessage](maybeinaccessiblemessage.md) | *Optional*. Message sent by the bot with the callback button that originated the query |
| inline\_message\_id | String | *Optional*. Identifier of the message sent via the bot in inline mode, that originated the query. Can also be present for messages sent by the bot, depending on the parameter *callback\_query\_mode* of the method [setMySettings](setmysettings.md). |
| chat\_instance | String | Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in [games](games.md). |
| data | String | *Optional*. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data. |
| game\_short\_name | String | *Optional*. Short name of a [Game](game.md) to be returned, serves as the unique identifier for the game |

> **NOTE:** After the user presses a callback button, Telegram clients will display a progress bar until you call [answerCallbackQuery](answercallbackquery.md). It is, therefore, necessary to react by calling [answerCallbackQuery](answercallbackquery.md) even if no notification to the user is needed (e.g., without specifying any of the optional parameters).
