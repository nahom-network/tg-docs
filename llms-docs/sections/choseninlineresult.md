# ChosenInlineResult

Source: https://core.telegram.org/bots/api#choseninlineresult

[Documentation index](../llms.txt)

Represents a [result](inlinequeryresult.md) of an inline query that was chosen by the user and sent to their chat partner.

| Field | Type | Description |
| --- | --- | --- |
| result\_id | String | The unique identifier for the result that was chosen |
| from | [User](user.md) | The user that chose the result |
| location | [Location](location.md) | *Optional*. Sender location, only for bots that require user location |
| inline\_message\_id | String | *Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](inlinekeyboardmarkup.md) attached to the message. Will be also received in [callback queries](callbackquery.md) and can be used to [edit](updating-messages.md) the message. |
| query | String | The query that was used to obtain the result |

**Note:** It is necessary to enable [inline feedback](https://core.telegram.org/bots/inline#collecting-feedback) via [@BotFather](https://t.me/botfather) in order to receive these objects in updates.
