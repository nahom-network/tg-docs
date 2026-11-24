# WidgetQueryTypeSignData

Source: https://core.telegram.org/bots/api#widgetquerytypesigndata

[Documentation index](../llms.txt)

The query contains data signed by a TON wallet of the user who sent the query. The data is signed for the domain `bot<bot_id>`, where `<bot_id>` is the identifier of the bot.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the query, always “sign\_data” |
| wallet | [WidgetQueryWallet](widgetquerywallet.md) | The wallet that signed the data |
| sign\_data | String | JSON-serialized signed data |
