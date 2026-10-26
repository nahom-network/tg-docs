# InputContactMessageContent

Source: https://core.telegram.org/bots/api#inputcontactmessagecontent

[Documentation index](../llms.txt)

Represents the [content](inputmessagecontent.md) of a contact message to be sent as the result of an inline query.

| Field | Type | Description |
| --- | --- | --- |
| phone\_number | String | Contact's phone number |
| first\_name | String | Contact's first name |
| last\_name | String | *Optional*. Contact's last name |
| vcard | String | *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes |
