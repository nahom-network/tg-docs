# deleteMyCommands

Source: https://core.telegram.org/bots/api#deletemycommands

[Documentation index](../llms.txt)

Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, [higher level commands](determining-list-of-commands.md) will be shown to affected users. Returns *True* on success.

| Parameter     | Type                                                                  | Required | Description                                                                                                                                                                               |
| ------------- | --------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scope         | [BotCommandScope](botcommandscope.md) | Optional | A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to [BotCommandScopeDefault](botcommandscopedefault.md). |
| language_code | String                                                                | Optional | A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands.                           |
