# forwardMessage

Source: https://core.telegram.org/bots/api#forwardmessage

[Documentation index](../llms.txt)

Use this method to forward messages of any kind. Service messages and messages with protected content can't be forwarded. On success, the sent [Message](message.md) is returned.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup, or channel in the format `@username` |
| message\_thread\_id | Integer | Optional | Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only |
| direct\_messages\_topic\_id | Integer | Optional | Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat |
| from\_chat\_id | Integer or String | Yes | Unique identifier for the chat where the original message was sent (or username of the target bot, supergroup, or channel in the format `@username`) |
| video\_start\_timestamp | Integer | Optional | New start timestamp for the forwarded video in the message |
| disable\_notification | Boolean | Optional | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| protect\_content | Boolean | Optional | Protects the contents of the forwarded message from forwarding and saving |
| message\_effect\_id | String | Optional | Unique identifier of the message effect to be added to the message; only available when forwarding to private chats |
| suggested\_post\_parameters | [SuggestedPostParameters](suggestedpostparameters.md) | Optional | A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only |
| message\_id | Integer | Yes | Message identifier in the chat specified in *from\_chat\_id* |
