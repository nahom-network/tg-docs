# RichTextDateTime

Source: https://core.telegram.org/bots/api#richtextdatetime

[Documentation index](../llms.txt)

Formatted date and time.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the rich text, always “date\_time” |
| text | [RichText](richtext.md) | The text |
| unix\_time | Integer | The Unix time associated with the entity |
| date\_time\_format | String | The string that defines the formatting of the date and time. See [date-time entity formatting](formatting-options.md#date-time-entity-formatting) for more details. |
