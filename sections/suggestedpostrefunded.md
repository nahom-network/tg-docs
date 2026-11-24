# SuggestedPostRefunded

Source: https://core.telegram.org/bots/api#suggestedpostrefunded

[Documentation index](../llms.txt)

Describes a service message about a payment refund for a suggested post.

| Field | Type | Description |
| --- | --- | --- |
| suggested\_post\_message | [Message](message.md) | *Optional*. Message containing the suggested post. Note that the [Message](message.md) object in this field will not contain the *reply\_to\_message* field even if it itself is a reply. |
| reason | String | Reason for the refund. Currently, one of “post\_deleted” if the post was deleted within 24 hours of being posted or removed from scheduled messages without being posted, or “payment\_refunded” if the payer refunded their payment. |
