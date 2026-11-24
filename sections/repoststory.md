# repostStory

Source: https://core.telegram.org/bots/api#repoststory

[Documentation index](../llms.txt)

Reposts a story on behalf of a business account from another business account. Both business accounts must be managed by the same bot, and the story on the source account must have been posted (or reposted) by the bot. Requires the *can\_manage\_stories* business bot right for both business accounts. Returns [Story](story.md) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| from\_chat\_id | Integer | Yes | Unique identifier of the chat which posted the story that should be reposted |
| from\_story\_id | Integer | Yes | Unique identifier of the story that should be reposted |
| active\_period | Integer | Yes | Period after which the story is moved to the archive, in seconds; must be one of `6 * 3600`, `12 * 3600`, `86400`, or `2 * 86400` |
| post\_to\_chat\_page | Boolean | Optional | Pass *True* to keep the story accessible after it expires |
| protect\_content | Boolean | Optional | Pass *True* if the content of the story must be protected from forwarding and screenshotting |
