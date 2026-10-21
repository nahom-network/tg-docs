# The SDK

Source: https://core.telegram.org/bots/serverless#the-sdk

[Documentation index](../llms.txt)

At runtime a module has one library: `sdk`. It bundles the three things a bot backend needs — a database, the Telegram Bot API, and outbound HTTP — with nothing to install and no credentials to configure. The database (`db`) is covered in [The database](the-database.md); this section covers `api`, `fetch`, and the `console` global.

```js
import { db, api, fetch, InputFile, BotApiError, EndpointError } from 'sdk';   // the whole surface
// or from submodules:
import { table, integer, text, eq, sql } from 'sdk/db';
import { api } from 'sdk/api';
import { fetch } from 'sdk/fetch';
```

| Import | What it is |
|---|---|
| `db` | Database — query builder and schema DSL → [The database](the-database.md) |
| `api` | Telegram Bot API — `api.sendMessage(...)` → [below](the-bot-api.md) |
| `fetch` | Outbound HTTP → [below](http.md) |
| `InputFile` | A file (bytes + name) to upload — works with both `api` and `fetch` → [Files](the-bot-api.md#files) |
| `EndpointError` | Refuse a Mini App's call with a message it can show → [Endpoints](endpoints.md) |

Import your own project modules by relative path with the `.js` extension (`from '../schema.js'`, `from '../lib/cart.js'`). See [The module system](the-module-system.md).

## In this section

- [The Bot API](the-bot-api.md)
- [HTTP](http.md)
- [Logging](logging.md)
