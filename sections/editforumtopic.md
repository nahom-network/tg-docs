# editForumTopic

Source: https://core.telegram.org/bots/api#editforumtopic

[Documentation index](../llms.txt)

Use this method to edit name and icon of a topic in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the *can\_manage\_topics* administrator rights, unless it is the creator of the topic. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| message\_thread\_id | Integer | Yes | Unique identifier for the target message thread of the forum topic |
| name | String | Optional | New topic name, 0-128 characters. If not specified or empty, the current name of the topic will be kept. |
| icon\_custom\_emoji\_id | String | Optional | New unique identifier of the custom emoji shown as the topic icon. Use [getForumTopicIconStickers](getforumtopiciconstickers.md) to get all allowed custom emoji identifiers. Pass an empty string to remove the icon. If not specified, the current icon will be kept. |
