# `add`

Source: https://core.telegram.org/bots/serverless#add

[Documentation index](../llms.txt)

```bash
npx tgcloud add <target>
```

Scaffolds a single new module, wired up and ready to edit — a handler, an endpoint or a `lib/` module.

```bash
npx tgcloud add handlers/callback_query   # a new update handler
npx tgcloud add endpoints/getProfile      # a new endpoint for the Mini App
npx tgcloud add lib/cart                  # a new shared module
```

> Note that `add` never overwrites an existing file. 

The `<target>` is the module's path (a trailing `.js` is optional). For `handlers/`, the name must be a Telegram update type. The platform advertises the valid set, so an invalid name is rejected up front. `handlers/` and `endpoints/` are flat, while `lib/` may be nested (`lib/payments/stripe`).

The module name is required. Giving **just the directory** is an error — but a helpful one: for `handlers/` it lists the update types you don't already have, so you can copy one.

```bash
$ npx tgcloud add handlers
Error: Specify a name, e.g. "handlers/callback_query". Available handlers/ types: callback_query, inline_query, chat_member, …
```

> `<Tab>` completion offers the same set — see [`completion`](completion.md). 

The generated file has a live `export default`, so the handler is active as soon as you deploy — there's nothing to uncomment. Deploy the new module with [`push`](push.md).
