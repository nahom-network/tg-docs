# upgradeGift

Source: https://core.telegram.org/bots/api#upgradegift

[Documentation index](../llms.txt)

Upgrades a given regular gift to a unique gift. Requires the *can\_transfer\_and\_upgrade\_gifts* business bot right. Additionally requires the *can\_transfer\_stars* business bot right if the upgrade is paid. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| owned\_gift\_id | String | Yes | Unique identifier of the regular gift that should be upgraded to a unique one |
| keep\_original\_details | Boolean | Optional | Pass *True* to keep the original gift text, sender and receiver in the upgraded gift |
| star\_count | Integer | Optional | The amount of Telegram Stars that will be paid for the upgrade from the business account balance. If `gift.prepaid_upgrade_star_count > 0`, then pass 0, otherwise, the *can\_transfer\_stars* business bot right is required and `gift.upgrade_star_count` must be passed. |
