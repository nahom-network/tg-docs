# postStory

Source: https://core.telegram.org/bots/api#poststory

[Documentation index](../llms.txt)

Posts a story on behalf of a managed business account. Requires the *can\_manage\_stories* business bot right. Returns [Story](story.md) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| content | [InputStoryContent](inputstorycontent.md) | Yes | Content of the story |
| active\_period | Integer | Yes | Period after which the story is moved to the archive, in seconds; must be one of `6 * 3600`, `12 * 3600`, `86400`, or `2 * 86400` |
| caption | String | Optional | Caption of the story, 0-2048 characters after entities parsing |
| parse\_mode | String | Optional | Mode for parsing entities in the story caption. See [formatting options](formatting-options.md) for more details. |
| caption\_entities | Array of [MessageEntity](messageentity.md) | Optional | A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\_mode* |
| areas | Array of [StoryArea](storyarea.md) | Optional | A JSON-serialized list of clickable areas to be shown on the story |
| post\_to\_chat\_page | Boolean | Optional | Pass *True* to keep the story accessible after it expires |
| protect\_content | Boolean | Optional | Pass *True* if the content of the story must be protected from forwarding and screenshotting |
