# WriteAccessAllowed

Source: https://core.telegram.org/bots/api#writeaccessallowed

[Documentation index](../llms.txt)

This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method [requestWriteAccess](../external/bots/webapps.md#initializing-mini-apps).

| Field | Type | Description |
| --- | --- | --- |
| from\_request | Boolean | *Optional*. *True*, if the access was granted after the user accepted an explicit request from a Web App sent by the method [requestWriteAccess](../external/bots/webapps.md#initializing-mini-apps) |
| web\_app\_name | String | *Optional*. Name of the Web App, if the access was granted when the Web App was launched from a link |
| from\_attachment\_menu | Boolean | *Optional*. *True*, if the access was granted when the bot was added to the attachment or side menu |
