# InlineQueryResultContact

Source: https://core.telegram.org/bots/api#inlinequeryresultcontact

[Documentation index](../llms.txt)

Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use *input\_message\_content* to send a message with the specified content instead of the contact.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the result, must be *contact* |
| id | String | Unique identifier for this result, 1-64 Bytes |
| phone\_number | String | Contact's phone number |
| first\_name | String | Contact's first name |
| last\_name | String | *Optional*. Contact's last name |
| vcard | String | *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes |
| reply\_markup | [InlineKeyboardMarkup](inlinekeyboardmarkup.md) | *Optional*. [Inline keyboard](../external/bots/features.md#inline-keyboards) attached to the message |
| input\_message\_content | [InputMessageContent](inputmessagecontent.md) | *Optional*. Content of the message to be sent instead of the contact |
| thumbnail\_url | String | *Optional*. Url of the thumbnail for the result |
| thumbnail\_width | Integer | *Optional*. Thumbnail width |
| thumbnail\_height | Integer | *Optional*. Thumbnail height |
