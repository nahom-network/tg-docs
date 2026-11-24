# BotFullInfo

Source: https://core.telegram.org/bots/api#botfullinfo

[Documentation index](../llms.txt)

This object contains full information about the bot itself.

| Field | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for this bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. |
| is\_bot | True | Always *True* |
| first\_name | String | Bot's first name |
| username | String | *Optional*. Bot's username |
| active\_usernames | Array of String | *Optional*. If non-empty, the list of all [active usernames](https://telegram.org/blog/topics-in-groups-collectible-usernames#collectible-usernames) of the bot |
| can\_join\_groups | Boolean | *True*, if the bot can be added to groups |
| can\_read\_all\_group\_messages | Boolean | *True*, if [privacy mode](../external/bots/features.md#privacy-mode) is disabled for the bot |
| supports\_guest\_queries | Boolean | *True*, if the bot supports guest queries from chats it is not a member of |
| supports\_inline\_queries | Boolean | *True*, if the bot supports inline queries |
| inline\_query\_placeholder | String | *Optional*. Placeholder for inline queries, which is shown in the input field after the bot's username; omitted if the default placeholder is used |
| needs\_inline\_query\_location | Boolean | *True*, if the bot requests the location of the user with every inline query |
| can\_connect\_to\_business | Boolean | *True*, if the bot can be connected to a user account to manage it |
| has\_main\_web\_app | Boolean | *True*, if the bot has a main Web App |
| has\_topics\_enabled | Boolean | *True*, if the bot has forum topic mode enabled in private chats |
| allows\_users\_to\_create\_topics | Boolean | *True*, if the bot allows users to create and delete topics in private chats |
| has\_topic\_sidebar | Boolean | *True*, if topics in private chats with the bot are shown in a sidebar |
| can\_manage\_bots | Boolean | *True*, if other bots can be created to be controlled by the bot |
| supports\_join\_request\_queries | Boolean | *True*, if the bot supports join request queries and can be assigned to process them |
