# Poll

Source: https://core.telegram.org/bots/api#poll

[Documentation index](../llms.txt)

This object contains information about a poll.

| Field | Type | Description |
| --- | --- | --- |
| id | String | Unique poll identifier |
| question | String | Poll question, 1-300 characters |
| question\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities that appear in the *question*. Currently, only custom emoji entities are allowed in poll questions |
| options | Array of [PollOption](polloption.md) | List of poll options |
| total\_voter\_count | Integer | Total number of users that voted in the poll |
| is\_closed | Boolean | *True*, if the poll is closed |
| is\_anonymous | Boolean | *True*, if the poll is anonymous |
| type | String | Poll type, currently can be “regular” or “quiz” |
| allows\_multiple\_answers | Boolean | *True*, if the poll allows multiple answers |
| allows\_revoting | Boolean | *True*, if the poll allows to change the chosen answer options |
| members\_only | Boolean | *True* if voting is limited to users who have been members of the chat where the poll was originally sent for more than 24 hours |
| country\_codes | Array of String | *Optional*. A list of two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes indicating the countries from which users can vote in the poll. The country code “FT” is used for users with anonymous numbers. If omitted, then users from any country can participate in the poll. |
| correct\_option\_ids | Array of Integer | *Optional*. Array of 0-based identifiers of the correct answer options. Available only for polls in quiz mode which are closed or were sent (not forwarded) by the bot or to the private chat with the bot. |
| explanation | String | *Optional*. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters |
| explanation\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities like usernames, URLs, bot commands, etc. that appear in the *explanation* |
| explanation\_media | [PollMedia](pollmedia.md) | *Optional*. Media added to the quiz explanation |
| open\_period | Integer | *Optional*. Amount of time in seconds the poll will be active after creation |
| close\_date | Integer | *Optional*. Point in time (Unix timestamp) when the poll will be automatically closed |
| description | String | *Optional*. Description of the poll; for polls inside the [Message](message.md) object only |
| description\_entities | Array of [MessageEntity](messageentity.md) | *Optional*. Special entities like usernames, URLs, bot commands, etc. that appear in the description |
| media | [PollMedia](pollmedia.md) | *Optional*. Media added to the poll description; for polls inside the [Message](message.md) object only |
