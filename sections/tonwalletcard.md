# TonWalletCard

Source: https://core.telegram.org/bots/api#tonwalletcard

[Documentation index](../llms.txt)

This object describes a TON wallet card, which is shown on the profile page of a user to everyone.

| Field | Type | Description |
| --- | --- | --- |
| address | String | Address of the wallet |
| amount | String | Balance of the wallet, in the *smallest units* of the cryptocurrency, as a decimal number |
| stickers | Array of [TonWalletCardSticker](tonwalletcardsticker.md) | Stickers placed on the card |
| background\_nft\_address | String | *Optional*. Address of the NFT of one of the stickers, whose colors must be used for the card background; omitted if the default background must be used |
