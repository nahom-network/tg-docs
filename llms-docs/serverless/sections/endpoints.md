# Endpoints

Source: https://core.telegram.org/bots/serverless#endpoints

[Documentation index](../llms.txt)

An endpoint is a module in `endpoints/` that your **Mini App** calls — the place for anything the front‑end can't do on its own, like reading and writing the database, calling the Bot API, or talking to outside services with your secrets.

```js
// endpoints/getProfile.js
import { db, EndpointError } from 'sdk';
import { eq } from 'sdk/db';
import { profiles } from '../schema.js';

export default async function (input, ctx) {
  const user = ctx.initData.user;
  const profile = await db.select().from(profiles).where(eq(profiles.userId, user.id)).get();
  if (!profile) throw new EndpointError('Profile not found', { userId: user.id });
  return profile;
}
```

The first argument, `input`, is the JSON object the Mini App sent. The second, `ctx`, carries **`ctx.initData`** — the Mini App's [init data](https://core.telegram.org/bots/webapps.md#webappinitdata) (`user`, `chat`, `start_param`, `auth_date`, …), already **verified by the platform**. It has the same shape as `Telegram.WebApp.initDataUnsafe` on the client, but here you can trust it. A call without valid init data is rejected with `401` before your code runs, so `ctx.initData.user` really is the person who opened your Mini App. Endpoints can only be called this way — from your bot's Mini App, by a Telegram user — so there is no public API to protect and no login to build.

Whatever the endpoint returns is sent back as JSON. To refuse a call, `throw new EndpointError(description, parameters?)`. The Mini App gets the description and the `parameters` object as they are. If you need to branch on the kind of error in the front‑end, put a code in `parameters` — `{ code: 'OUT_OF_STOCK' }`. Any other exception is reported as a generic internal error, and the real message goes only to your logs, so internals never leak to the client.

##### Calling an endpoint from the Mini App

The Mini App calls an endpoint by name with `Telegram.WebApp.Serverless.call` from the official [Mini Apps SDK](https://core.telegram.org/bots/webapps.md#serverless), `telegram-web-app.js` — the script your Mini App already includes. It sends the init data for you and calls back with an error or the endpoint's result:

```js
Telegram.WebApp.Serverless.call('getProfile', { lang: 'en' }, function (err, profile) {
  if (err) {
    // err.message — the description; err.parameters — what your EndpointError carried
    if (err.type === 'ENDPOINT_ERROR') showMessage(err.message);
    return;
  }
  render(profile);
});
```

The input is optional and must be a plain object. Without it the call is `Serverless.call('getProfile', callback)`.

`err.type` is `'ENDPOINT_ERROR'` when your endpoint threw an `EndpointError`. Any other value means the platform refused the call or the endpoint failed unexpectedly, for example `'UNAUTHORIZED'` when the init data is missing or invalid.

Endpoint names are like JavaScript identifiers — letters, digits and `_`, not starting with a digit (`getProfile`, `place_order`). Scaffold one with [`npx tgcloud add endpoints/<name>`](add.md), and try it without the Mini App with [`run`](run.md), passing the init data yourself:

```bash
npx tgcloud run endpoints/getProfile '{}' --ctx '{ initData: { user: { id: 1, first_name: "Ann" } } }'
```
