# WidgetQueryWallet

Source: https://core.telegram.org/bots/api#widgetquerywallet

[Documentation index](../llms.txt)

This object describes a TON wallet of the user, which is used in a query from a widget.

| Field | Type | Description |
| --- | --- | --- |
| address | String | Address of the wallet |
| amount | String | Balance of the wallet, in the *smallest units* of the cryptocurrency, as a decimal number |
| public\_key | String | *Optional*. Hex-encoded public key of the wallet; omitted if unknown |
| state\_init | String | *Optional*. Base64-encoded serialized StateInit of the wallet contract; omitted if and only if *public\_key* is omitted |
