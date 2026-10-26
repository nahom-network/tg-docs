# InlineQueryResultGame

Source: https://core.telegram.org/bots/api#inlinequeryresultgame

[Documentation index](../llms.txt)

Represents a [Game](game.md).

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *game* |
| id | String | Unique identifier for this result, 1-64 bytes |
| game\_short\_name | String | Short name of the game |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) attached to the message |
