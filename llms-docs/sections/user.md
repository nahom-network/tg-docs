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
| can\_join\_groups | Boolean | *Optional*. *True*, if the bot can be invited to groups. Returned only in [getMe](getme.md). |
| can\_read\_all\_group\_messages | Boolean | *Optional*. *True*, if [privacy mode](https://core.telegram.org/bots/features#privacy-mode) is disabled for the bot. Returned only in [getMe](getme.md). |
| supports\_guest\_queries | Boolean | *Optional*. *True*, if the bot supports guest queries from chats it is not a member of. Returned only in [getMe](getme.md). |
| supports\_inline\_queries | Boolean | *Optional*. *True*, if the bot supports inline queries. Returned only in [getMe](getme.md). |
| can\_connect\_to\_business | Boolean | *Optional*. *True*, if the bot can be connected to a user account to manage it. Returned only in [getMe](getme.md). |
| has\_main\_web\_app | Boolean | *Optional*. *True*, if the bot has a main Web App. Returned only in [getMe](getme.md). |
| has\_topics\_enabled | Boolean | *Optional*. *True*, if the bot has forum topic mode enabled in private chats. Returned only in [getMe](getme.md). |
| allows\_users\_to\_create\_topics | Boolean | *Optional*. *True*, if the bot allows users to create and delete topics in private chats. Returned only in [getMe](getme.md). |
| can\_manage\_bots | Boolean | *Optional*. *True*, if other bots can be created to be controlled by the bot. Returned only in [getMe](getme.md). |
| supports\_join\_request\_queries | Boolean | *Optional*. *True*, if the bot supports join request queries and can be assigned to process them. Returned only in [getMe](getme.md). |
