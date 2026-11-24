# `run`

Source: https://core.telegram.org/bots/serverless#run

[Documentation index](../llms.txt)

```bash
npx tgcloud run <module> [args] [--ctx <json5>]
```

Executes a handler or an endpoint on the platform **without deploying**, using your current local files. This is the fast inner loop for testing logic.

- `<module>` — a bare name (searched under `handlers/` and `endpoints/`) or a path like `handlers/message`. A bare name that exists in both directories must be spelled with its directory.
- `[args]` — the payload passed to the handler, written in [JSON5](https://json5.org) so you can skip quoting keys. It's the update‑type object your handler receives (e.g. a Message for `handlers/message`), or the `input` of an endpoint, and it must be an **object** — not an array or a bare string.
- `--ctx <json5>` — the module's context object (its second argument), also JSON5. Use it to supply what your code reads off `ctx` — the raw update for a handler, `--ctx '{ update: { update_id: 1 } }'`, or the init data for an endpoint, `--ctx '{ initData: { user: { id: 1 } } }'`. `run` doesn't verify it, since you're testing your logic, not the platform's checks.

```bash
npx tgcloud run handlers/message '{ chat: { id: 1 }, text: "hi" }'
```

The platform runs the module against the module space assembled from your **local** project (so locally‑changed `lib/` code is used too) and returns the return value, anything logged with `console.*`, and the elapsed time. Read big arguments from a file with `npx tgcloud run handlers/message "$(cat message.json5)"`.
