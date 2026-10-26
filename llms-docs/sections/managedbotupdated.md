# ManagedBotUpdated

Source: https://core.telegram.org/bots/api#managedbotupdated

[Documentation index](../llms.txt)

This object contains information about the creation, token update, or owner update of a bot that is managed by the current bot.

| Field | Type | Description |
| --- | --- | --- |
| user | [User](user.md) | User that created the bot |
| bot | [User](user.md) | Information about the bot. Token of the bot can be fetched using the method [getManagedBotToken](getmanagedbottoken.md). |
