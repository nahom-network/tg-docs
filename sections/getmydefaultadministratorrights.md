# getMyDefaultAdministratorRights

Source: https://core.telegram.org/bots/api#getmydefaultadministratorrights

[Documentation index](../llms.txt)

Use this method to get the current default administrator rights of the bot. Returns [ChatAdministratorRights](chatadministratorrights.md) on success.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| for_channels | Boolean | Optional | Pass *True* to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned. |
