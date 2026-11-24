# sendGift

Source: https://core.telegram.org/bots/api#sendgift

[Documentation index](../llms.txt)

Sends a gift to the given user or channel chat. The gift can't be converted to Telegram Stars by the receiver. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user\_id | Integer | Optional | Required if *chat\_id* is not specified. Unique identifier of the target user who will receive the gift. |
| chat\_id | Integer or String | Optional | Required if *user\_id* is not specified. Unique identifier for the chat that will receive the gift or username of the channel in the format `@username`. |
| gift\_id | String | Yes | Identifier of the gift; limited gifts can't be sent to channel chats |
| pay\_for\_upgrade | Boolean | Optional | Pass *True* to pay for the gift upgrade from the bot's balance, thereby making the upgrade free for the receiver |
| text | String | Optional | Text that will be shown along with the gift; 0-128 characters |
| text\_parse\_mode | String | Optional | Mode for parsing entities in the text. See [formatting options](formatting-options.md) for more details. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, “custom\_emoji”, and “date\_time” are ignored. |
| text\_entities | Array of [MessageEntity](messageentity.md) | Optional | A JSON-serialized list of special entities that appear in the gift text. It can be specified instead of *text\_parse\_mode*. Entities other than “bold”, “italic”, “underline”, “strikethrough”, “spoiler”, “custom\_emoji”, and “date\_time” are ignored. |
