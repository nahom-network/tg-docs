# StoryAreaTypeSuggestedReaction

Source: https://core.telegram.org/bots/api#storyareatypesuggestedreaction

[Documentation index](../llms.txt)

Describes a story area pointing to a suggested reaction. Currently, a story can have up to 5 suggested reaction areas.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the area, always “suggested\_reaction” |
| reaction\_type | [ReactionType](reactiontype.md) | Type of the reaction |
| is\_dark | Boolean | *Optional*. Pass *True* if the reaction area has a dark background |
| is\_flipped | Boolean | *Optional*. Pass *True* if reaction area corner is flipped |
