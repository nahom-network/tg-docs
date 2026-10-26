# SuggestedPostDeclined

Source: https://core.telegram.org/bots/api#suggestedpostdeclined

[Documentation index](../llms.txt)

Describes a service message about the rejection of a suggested post.

| Field | Type | Description |
| --- | --- | --- |
| suggested\_post\_message | [Message](message.md) | *Optional*. Message containing the suggested post. Note that the [Message](message.md) object in this field will not contain the *reply\_to\_message* field even if it itself is a reply. |
| comment | String | *Optional*. Comment with which the post was declined |
