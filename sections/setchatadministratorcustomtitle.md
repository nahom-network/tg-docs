# setChatAdministratorCustomTitle

Source: https://core.telegram.org/bots/api#setchatadministratorcustomtitle

[Documentation index](../llms.txt)

Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| user\_id | Integer | Yes | Unique identifier of the target user |
| custom\_title | String | Yes | New custom title for the administrator; 0-16 characters, emoji are not allowed |
