# RichTextAnchorLink

Source: https://core.telegram.org/bots/api#richtextanchorlink

[Documentation index](../llms.txt)

A link to an anchor.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the rich text, always “anchor\_link” |
| text | [RichText](richtext.md) | The link text |
| anchor\_name | String | The name of the anchor. If the name is empty, then the link brings back to the top of the message. |
