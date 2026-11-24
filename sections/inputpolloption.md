# InputPollOption

Source: https://core.telegram.org/bots/api#inputpolloption

[Documentation index](../llms.txt)

This object contains information about one answer option in a poll to be sent.

| Field | Type | Description |
| --- | --- | --- |
| text | String | Option text, 1-100 characters |
| text_parse_mode | String | *Optional*. Mode for parsing entities in the text. See [formatting options](formatting-options.md) for more details. Currently, only custom emoji entities are allowed. |
| text_entities | Array of [MessageEntity](messageentity.md) | *Optional*. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of *text_parse_mode*. |
| media | [InputPollOptionMedia](inputpolloptionmedia.md) | *Optional*. Media added to the poll option |
