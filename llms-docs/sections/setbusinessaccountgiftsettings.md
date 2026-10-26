# setBusinessAccountGiftSettings

Source: https://core.telegram.org/bots/api#setbusinessaccountgiftsettings

[Documentation index](../llms.txt)

Changes the privacy settings pertaining to incoming gifts in a managed business account. Requires the *can\_change\_gift\_settings* business bot right. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| business\_connection\_id | String | Yes | Unique identifier of the business connection |
| show\_gift\_button | Boolean | Yes | Pass *True* if a button for sending a gift to the user or by the business account must always be shown in the input field |
| accepted\_gift\_types | [AcceptedGiftTypes](acceptedgifttypes.md) | Yes | Types of gifts accepted by the business account |
