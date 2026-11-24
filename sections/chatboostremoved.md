# ChatBoostRemoved

Source: https://core.telegram.org/bots/api#chatboostremoved

[Documentation index](../llms.txt)

This object represents a boost removed from a chat.

| Field | Type | Description |
| --- | --- | --- |
| chat | [Chat](chat.md) | Chat which was boosted |
| boost\_id | String | Unique identifier of the boost |
| remove\_date | Integer | Point in time (Unix timestamp) when the boost was removed |
| source | [ChatBoostSource](chatboostsource.md) | Source of the removed boost |
