# Gift

Source: https://core.telegram.org/bots/api#gift

[Documentation index](../llms.txt)

This object represents a gift that can be sent by the bot.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the gift |
| sticker | [Sticker](sticker.md) | The sticker that represents the gift |
| star\_count | Integer | The number of Telegram Stars that must be paid to send the sticker |
| upgrade\_star\_count | Integer | *Optional*. The number of Telegram Stars that must be paid to upgrade the gift to a unique one |
| is\_premium | True | *Optional*. *True*, if the gift can only be purchased by Telegram Premium subscribers |
| has\_colors | True | *Optional*. *True*, if the gift can be used (after being upgraded) to customize a user's appearance |
| total\_count | Integer | *Optional*. The total number of gifts of this type that can be sent by all users; for limited gifts only |
| remaining\_count | Integer | *Optional*. The number of remaining gifts of this type that can be sent by all users; for limited gifts only |
| personal\_total\_count | Integer | *Optional*. The total number of gifts of this type that can be sent by the bot; for limited gifts only |
| personal\_remaining\_count | Integer | *Optional*. The number of remaining gifts of this type that can be sent by the bot; for limited gifts only |
| background | [GiftBackground](giftbackground.md) | *Optional*. Background of the gift |
| unique\_gift\_variant\_count | Integer | *Optional*. The total number of different unique gifts that can be obtained by upgrading the gift |
| publisher\_chat | [Chat](chat.md) | *Optional*. Information about the chat that published the gift |
