# October 6, 2026

Source: https://core.telegram.org/bots/serverless#october-6-2026

[Documentation index](../llms.txt)

- Added [Mini App hosting](mini-app-front-end.md). The build output of your Mini App's front‑end is deployed together with the bot and served at `https://app<app_id>.tgcloud.ai/`.
- Added [endpoints](endpoints.md), the functions your Mini App calls with [Telegram.WebApp.Serverless.call](https://core.telegram.org/bots/webapps.md#serverless).
- Updated the [CLI](command-line-interface.md) to version 0.2.0.
- Added the project config file [tgcloud.jsonc](mini-app-front-end.md).
- Project modules can now be imported by [relative path](the-module-system.md), with the `.js` extension.
- All modules now live in the `tgcloud/` folder. Run [npx tgcloud upgrade](upgrade.md) once in a project created with an earlier version of the CLI.
