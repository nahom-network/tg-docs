# setChatMemberTag

Source: https://core.telegram.org/bots/api#setchatmembertag

[Documentation index](../llms.txt)

Use this method to set a tag for a regular member in a group or a supergroup. The bot must be an administrator in the chat for this to work and must have the *can\_manage\_tags* administrator right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| user\_id | Integer | Yes | Unique identifier of the target user |
| tag | String | Optional | New tag for the member; 0-16 characters, emoji are not allowed |
