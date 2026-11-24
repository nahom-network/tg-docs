# getGameHighScores

Source: https://core.telegram.org/bots/api#getgamehighscores

[Documentation index](../llms.txt)

Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. Returns an Array of [GameHighScore](gamehighscore.md) objects.

> This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and their neighbors are not among them. Please note that this behavior is subject to change.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user\_id | Integer | Yes | Target user id |
| chat\_id | Integer | Optional | Required if *inline\_message\_id* is not specified. Unique identifier for the target chat. |
| message\_id | Integer | Optional | Required if *inline\_message\_id* is not specified. Identifier of the sent message. |
| inline\_message\_id | String | Optional | Required if *chat\_id* and *message\_id* are not specified. Identifier of the inline message. |
