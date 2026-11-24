# editStory

Source: https://core.telegram.org/bots/api#editstory

[Documentation index](../llms.txt)

Edits a story previously posted by the bot on behalf of a managed business account. Requires the *can\_manage\_stories* business bot right. Returns [Story](story.md) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| story\_id | Integer | Yes | Unique identifier of the story to edit |
| content | [InputStoryContent](inputstorycontent.md) | Yes | Content of the story |
| caption | String | Optional | Caption of the story, 0-2048 characters after entities parsing |
| parse\_mode | String | Optional | Mode for parsing entities in the story caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | Optional | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| areas | Array of [StoryArea](storyarea.md) | Optional | A JSON-serialized list of clickable areas to be shown on the story |
