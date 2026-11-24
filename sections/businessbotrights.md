# BusinessBotRights

Source: https://core.telegram.org/bots/api#businessbotrights

[Documentation index](../llms.txt)

Represents the rights of a business bot.

| Field | Type | Description |
| --- | --- | --- |
| can\_reply | True | *Optional*. *True*, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours |
| can\_read\_messages | True | *Optional*. *True*, if the bot can mark incoming private messages as read |
| can\_delete\_sent\_messages | True | *Optional*. *True*, if the bot can delete messages sent by the bot |
| can\_delete\_all\_messages | True | *Optional*. *True*, if the bot can delete all private messages in managed chats |
| can\_edit\_name | True | *Optional*. *True*, if the bot can edit the first and last name of the business account |
| can\_edit\_bio | True | *Optional*. *True*, if the bot can edit the bio of the business account |
| can\_edit\_profile\_photo | True | *Optional*. *True*, if the bot can edit the profile photo of the business account |
| can\_edit\_username | True | *Optional*. *True*, if the bot can edit the username of the business account |
| can\_change\_gift\_settings | True | *Optional*. *True*, if the bot can change the privacy settings pertaining to gifts for the business account |
| can\_view\_gifts\_and\_stars | True | *Optional*. *True*, if the bot can view gifts and the amount of Telegram Stars owned by the business account |
| can\_convert\_gifts\_to\_stars | True | *Optional*. *True*, if the bot can convert regular gifts owned by the business account to Telegram Stars |
| can\_transfer\_and\_upgrade\_gifts | True | *Optional*. *True*, if the bot can transfer and upgrade gifts owned by the business account |
| can\_transfer\_stars | True | *Optional*. *True*, if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts |
| can\_manage\_stories | True | *Optional*. *True*, if the bot can post, edit and delete stories on behalf of the business account |
