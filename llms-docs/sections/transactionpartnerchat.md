# TransactionPartnerChat

Source: https://core.telegram.org/bots/api#transactionpartnerchat

[Documentation index](../llms.txt)

Describes a transaction with a chat.

| Field | Type                                            | Description                                      |
| ----- | ----------------------------------------------- | ------------------------------------------------ |
| type  | String                                          | Type of the transaction partner, always “chat”   |
| chat  | [Chat](chat.md) | Information about the chat                       |
| gift  | [Gift](gift.md) | *Optional*. The gift sent to the chat by the bot |
