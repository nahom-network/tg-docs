# GiveawayCompleted

Source: https://core.telegram.org/bots/api#giveawaycompleted

[Documentation index](../llms.txt)

This object represents a service message about the completion of a giveaway without public winners.

| Field | Type | Description |
| --- | --- | --- |
| winner\_count | Integer | Number of winners in the giveaway |
| unclaimed\_prize\_count | Integer | *Optional*. Number of undistributed prizes |
| giveaway\_message | [Message](message.md) | *Optional*. Message with the giveaway that was completed, if it wasn't deleted |
| is\_star\_giveaway | True | *Optional*. *True*, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway. |
