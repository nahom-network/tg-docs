# Contact

Source: https://core.telegram.org/bots/api#contact

[Documentation index](../llms.txt)

This object represents a phone contact.

| Field | Type | Description |
| --- | --- | --- |
| phone\_number | String | Contact's phone number |
| first\_name | String | Contact's first name |
| last\_name | String | *Optional*. Contact's last name |
| user\_id | Integer | *Optional*. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. |
| vcard | String | *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard) |
