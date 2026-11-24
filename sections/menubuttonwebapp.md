# MenuButtonWebApp

Source: https://core.telegram.org/bots/api#menubuttonwebapp

[Documentation index](../llms.txt)

Represents a menu button, which launches a [Web App](../external/bots/webapps.md).

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the button, must be *web\_app* |
| text | String | Text on the button |
| web\_app | [WebAppInfo](webappinfo.md) | Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [answerWebAppQuery](answerwebappquery.md). Alternatively, a `t.me` link to a Web App of the bot can be specified in the object instead of the Web App's URL, in which case the Web App will be opened as if the user pressed the link. |
