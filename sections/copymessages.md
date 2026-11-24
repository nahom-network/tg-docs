# copyMessages

Source: https://core.telegram.org/bots/api#copymessages

[Documentation index](../llms.txt)

Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz [poll](poll.md) can be copied only if the value of the field *correct\_option\_ids* is known to the bot. The method is analogous to the method [forwardMessages](forwardmessages.md), but the copied messages don't have a link to the original message. Album grouping is kept for copied messages. On success, an Array of [MessageId](messageid.md) of the sent messages is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup or channel in the format `@username` |
| message\_thread\_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| direct\_messages\_topic\_id | Integer | Optional | Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat |
| from\_chat\_id | Integer or String | Yes | Unique identifier for the chat where the original messages were sent (or username of the target bot, supergroup or channel in the format `@username`) |
| message\_ids | Array of Integer | Yes | A JSON-serialized list of 1-100 identifiers of messages in the chat *from\_chat\_id* to copy. The identifiers must be specified in a strictly increasing order. |
| disable\_notification | Boolean | Optional | Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect\_content | Boolean | Optional | Protects the contents of the sent messages from forwarding and saving |
| remove\_caption | Boolean | Optional | Pass *True* to copy the messages without their captions |
