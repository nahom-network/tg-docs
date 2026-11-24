# EphemeralMessageParameters

Source: https://core.telegram.org/bots/api#ephemeralmessageparameters

[Documentation index](../llms.txt)

| Field | Type | Description |
| --- | --- | --- |
| receiver\_user\_id | Integer | Identifier of the user who will receive the message. It is not guaranteed that the user will receive the message, especially if they are offline. See [here](ephemeral-messages-and-commands.md) for more details. |
| callback\_query\_id | String | *Optional*. Identifier of the callback query which triggered the message, if any |
| replace\_callback\_query\_message | Boolean | *Optional*. Pass *True* if the ephemeral message must be shown in place of the original message. Must be *False* for callback queries from ephemeral messages, which must be edited using regular *editEphemeralMessage…* methods. |
