# forwardMessages

Source: https://core.telegram.org/bots/api#forwardmessages

[Documentation index](../llms.txt)

Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded, they are skipped. Service messages and messages with protected content can't be forwarded. Album grouping is kept for forwarded messages. On success, an Array of [MessageId](messageid.md) of the sent messages is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup, or channel in the format `@username` |
| message\_thread\_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| direct\_messages\_topic\_id | Integer | Optional | Identifier of the direct messages topic to which the messages will be forwarded; required if the messages are forwarded to a direct messages chat |
| from\_chat\_id | Integer or String | Yes | Unique identifier for the chat where the original messages were sent (or username of the target bot, supergroup, or channel in the format `@username`) |
| message\_ids | Array of Integer | Yes | A JSON-serialized list of 1-100 identifiers of messages in the chat *from\_chat\_id* to forward. The identifiers must be specified in a strictly increasing order. |
| disable\_notification | Boolean | Optional | Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect\_content | Boolean | Optional | Protects the contents of the forwarded messages from forwarding and saving |
