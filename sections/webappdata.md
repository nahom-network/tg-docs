# WebAppData

Source: https://core.telegram.org/bots/api#webappdata

[Documentation index](../llms.txt)

Describes data sent from a [Web App](../external/bots/webapps.md) to the bot.

| Field | Type | Description |
| --- | --- | --- |
| data | String | The data. Be aware that a bad client can send arbitrary data in this field. |
| button_text | String | Text of the *web_app* keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field. |
