# verifyChat

Source: https://core.telegram.org/bots/api#verifychat

[Documentation index](../llms.txt)

Verifies a chat [on behalf of the organization](https://telegram.org/verify#third-party-verification) which is represented by the bot. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target bot, supergroup, or channel in the format `@username`. Channel direct messages chats can't be verified. |
| custom\_description | String | Optional | Custom description for the verification; 0-70 characters. Must be empty if the organization isn't allowed to provide a custom verification description. |
| custom\_description\_parse\_mode | String | Optional | Mode for parsing entities in the custom description. See [formatting options](formatting-options.md) for more details. Only “text\_link” entities are supported. |
| custom\_description\_entities | Array of [MessageEntity](messageentity.md) | Optional | A JSON-serialized list of special entities that appear in the custom description, which can be specified instead of *custom\_description\_parse\_mode*. Only “text\_link” entities are supported. |
