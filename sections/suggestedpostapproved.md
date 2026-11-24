# SuggestedPostApproved

Source: https://core.telegram.org/bots/api#suggestedpostapproved

[Documentation index](../llms.txt)

Describes a service message about the approval of a suggested post.

| Field | Type | Description |
| --- | --- | --- |
| suggested\_post\_message | [Message](message.md) | *Optional*. Message containing the suggested post. Note that the [Message](message.md) object in this field will not contain the *reply\_to\_message* field even if it itself is a reply. |
| price | [SuggestedPostPrice](suggestedpostprice.md) | *Optional*. Amount paid for the post |
| send\_date | Integer | Date when the post will be published |
