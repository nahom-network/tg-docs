# setBusinessAccountProfilePhoto

Source: https://core.telegram.org/bots/api#setbusinessaccountprofilephoto

[Documentation index](../llms.txt)

Changes the profile photo of a managed business account. Requires the *can\_edit\_profile\_photo* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| photo | [InputProfilePhoto](inputprofilephoto.md) | Yes | The new profile photo to set |
| is\_public | Boolean | Optional | Pass *True* to set the public photo, which will be visible even if the main photo is hidden by the business account's privacy settings. An account can have only one public photo. |
