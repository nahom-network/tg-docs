# setManagedBotAccessSettings

Source: https://core.telegram.org/bots/api#setmanagedbotaccesssettings

[Documentation index](../llms.txt)

Use this method to change the access settings of a managed bot. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user\_id | Integer | Yes | User identifier of the managed bot whose access settings will be changed |
| is\_access\_restricted | Boolean | Yes | Pass *True* if only selected users can access the bot. The bot's owner can always access it. |
| added\_user\_ids | Array of Integer | Optional | A JSON-serialized list of up to 10 identifiers of users who will have access to the bot in addition to its owner. Ignored if *is\_access\_restricted* is *False*. |
