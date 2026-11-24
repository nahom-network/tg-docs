# RichTextTextMention

Source: https://core.telegram.org/bots/api#richtexttextmention

[Documentation index](../llms.txt)

A mention of a Telegram user by their identifier.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the rich text, always “text_mention” |
| text | [RichText](richtext.md) | The text |
| user | [User](user.md) | The mentioned user |
