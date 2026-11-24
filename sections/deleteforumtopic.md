# deleteForumTopic

Source: https://core.telegram.org/bots/api#deleteforumtopic

[Documentation index](../llms.txt)

Use this method to delete a forum topic along with all its messages in a forum supergroup chat or a private chat with a user. In the case of a supergroup chat the bot must be an administrator in the chat for this to work and must have the *can\_delete\_messages* administrator rights. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer or String | Yes | Unique identifier for the target chat or username of the target supergroup in the format `@username` |
| message\_thread\_id | Integer | Yes | Unique identifier for the target message thread of the forum topic |
