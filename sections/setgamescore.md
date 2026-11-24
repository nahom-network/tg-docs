# setGameScore

Source: https://core.telegram.org/bots/api#setgamescore

[Documentation index](../llms.txt)

Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the [Message](message.md) is returned, otherwise *True* is returned. Returns an error, if the new score is not greater than the user's current score in the chat and *force* is *False*.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user\_id | Integer | Yes | User identifier |
| score | Integer | Yes | New score, must be non-negative |
| force | Boolean | Optional | Pass *True* if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters. |
| disable\_edit\_message | Boolean | Optional | Pass *True* if the game message should not be automatically edited to include the current scoreboard |
| chat\_id | Integer | Optional | Required if *inline\_message\_id* is not specified. Unique identifier for the target chat. |
| message\_id | Integer | Optional | Required if *inline\_message\_id* is not specified. Identifier of the sent message. |
| inline\_message\_id | String | Optional | Required if *chat\_id* and *message\_id* are not specified. Identifier of the inline message. |
