# User

Source: https://core.telegram.org/bots/api#user

[Documentation index](../llms.txt)

This object represents a Telegram user or bot.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. |
| is\_bot | Boolean | *True*, if this user is a bot |
| first\_name | String | User's or bot's first name |
| last\_name | String | *Optional*. User's or bot's last name |
| username | String | *Optional*. User's or bot's username |
| language\_code | String | *Optional*. [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) of the user's language |
| is\_premium | True | *Optional*. *True*, if this user is a Telegram Premium user |
| added\_to\_attachment\_menu | True | *Optional*. *True*, if this user added the bot to the attachment menu |
