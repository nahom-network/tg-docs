# setUserEmojiStatus

Source: https://core.telegram.org/bots/api#setuseremojistatus

[Documentation index](../llms.txt)

Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method [requestEmojiStatusAccess](../external/bots/webapps.md#initializing-mini-apps). Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user\_id | Integer | Yes | Unique identifier of the target user |
| emoji\_status\_custom\_emoji\_id | String | Optional | Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status. |
| emoji\_status\_expiration\_date | Integer | Optional | Expiration date of the emoji status, if any |
