# GiveawayWinners

Source: https://core.telegram.org/bots/api#giveawaywinners

[Documentation index](../llms.txt)

This object represents a message about the completion of a giveaway with public winners.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](chat.md) | The chat that created the giveaway |
| giveaway\_message\_id | Integer | Identifier of the message with the giveaway in the chat |
| winners\_selection\_date | Integer | Point in time (Unix timestamp) when winners of the giveaway were selected |
| winner\_count | Integer | Total number of winners in the giveaway |
| winners | Array of [User](user.md) | List of up to 100 winners of the giveaway |
| additional\_chat\_count | Integer | *Optional*. The number of other chats the user had to join in order to be eligible for the giveaway |
| prize\_star\_count | Integer | *Optional*. The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only |
| premium\_subscription\_month\_count | Integer | *Optional*. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only |
| unclaimed\_prize\_count | Integer | *Optional*. Number of undistributed prizes |
| only\_new\_members | True | *Optional*. *True*, if only users who had joined the chats after the giveaway started were eligible to win |
| was\_refunded | True | *Optional*. *True*, if the giveaway was canceled because the payment for it was refunded |
| prize\_description | String | *Optional*. Description of additional giveaway prize |
