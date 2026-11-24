# setMySettings

Source: https://core.telegram.org/bots/api#setmysettings

[Documentation index](../llms.txt)

Use this method to change settings of the bot. Settings that aren't specified remain unchanged. Returns *True* on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| supports\_inline\_queries | Boolean | Optional | Pass *True* to enable [inline mode](inline-mode.md) for the bot or *False* to disable it |
| inline\_query\_placeholder | String | Optional | New placeholder for inline queries, which is shown in the input field after the bot's username. Pass an empty string to use the default placeholder. |
| needs\_inline\_query\_location | Boolean | Optional | Pass *True* to request the location of the user with every inline query to the bot or *False* to stop requesting it |
| inline\_feedback\_share\_denominator | Integer | Optional | Denominator of the share of [chosen inline results](choseninlineresult.md) received by the bot; the bot receives 1 out of *inline\_feedback\_share\_denominator* chosen results. Must be one of 1, 10, 100, or 1000. Pass 0 to stop receiving chosen inline results. |
| can\_join\_groups | Boolean | Optional | Pass *True* to allow adding the bot to groups or *False* to disallow it |
| can\_read\_all\_group\_messages | Boolean | Optional | Pass *True* to disable [privacy mode](../external/bots/features.md#privacy-mode) for the bot or *False* to enable it |
| can\_connect\_to\_business | Boolean | Optional | Pass *True* to allow connecting the bot to user accounts to manage them or *False* to disallow it |
| can\_manage\_bots | Boolean | Optional | Pass *True* to allow creating other bots that will be controlled by the bot or *False* to disallow it |
| supports\_guest\_queries | Boolean | Optional | Pass *True* to allow guest queries to the bot from chats it isn't a member of or *False* to disallow them |
| supports\_join\_request\_queries | Boolean | Optional | Pass *True* to allow assigning the bot to process join request queries or *False* to disallow it |
| has\_topics\_enabled | Boolean | Optional | Pass *True* to enable forum topic mode in private chats with the bot or *False* to disable it |
| allows\_users\_to\_create\_topics | Boolean | Optional | Pass *True* to allow users to create and delete topics in private chats with the bot or *False* to disallow it |
| has\_topic\_sidebar | Boolean | Optional | Pass *True* to show topics in private chats with the bot in a sidebar or *False* to stop showing them in a sidebar |
| can\_communicate\_with\_bots | Boolean | Optional | Pass *True* to allow the bot to communicate with other bots in groups, private chats, and through business accounts or *False* to disallow it |
| callback\_query\_mode | String | Optional | Mode in which the bot receives [callback queries](callbackquery.md) from buttons in messages sent by the bot. Must be one of “default” (the field *message* is always used and contains an [InaccessibleMessage](inaccessiblemessage.md) if the message is inaccessible to the bot), “auto” (the field *inline\_message\_id* is used instead of the field *message* if the message is inaccessible to the bot; the field *message* can still contain an inaccessible message if the message has just been deleted), or “inline” (the field *inline\_message\_id* is always used instead of the field *message*). |
