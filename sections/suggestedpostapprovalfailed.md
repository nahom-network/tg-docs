# SuggestedPostApprovalFailed

Source: https://core.telegram.org/bots/api#suggestedpostapprovalfailed

[Documentation index](../llms.txt)

Describes a service message about the failed approval of a suggested post. Currently, only caused by insufficient user funds at the time of approval.

| Field | Type | Description |
| --- | --- | --- |
| suggested\_post\_message | [Message](message.md) | *Optional*. Message containing the suggested post whose approval has failed. Note that the [Message](message.md) object in this field will not contain the *reply\_to\_message* field even if it itself is a reply. |
| price | [SuggestedPostPrice](suggestedpostprice.md) | Expected price of the post |
