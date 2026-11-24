# declineSuggestedPost

Source: https://core.telegram.org/bots/api#declinesuggestedpost

[Documentation index](../llms.txt)

Use this method to decline a suggested post in a direct messages chat. The bot must have the 'can\_manage\_direct\_messages' administrator right in the corresponding channel chat. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chat\_id | Integer | Yes | Unique identifier for the target direct messages chat |
| message\_id | Integer | Yes | Identifier of a suggested post message to decline |
| comment | String | Optional | Comment for the creator of the suggested post; 0-128 characters |
