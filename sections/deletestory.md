# deleteStory

Source: https://core.telegram.org/bots/api#deletestory

[Documentation index](../llms.txt)

Deletes a story previously posted by the bot on behalf of a managed business account. Requires the *can\_manage\_stories* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| story\_id | Integer | Yes | Unique identifier of the story to delete |
