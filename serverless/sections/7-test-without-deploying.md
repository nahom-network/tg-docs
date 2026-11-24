# 7. Test without deploying

Source: https://core.telegram.org/bots/serverless#7-test-without-deploying

[Documentation index](../llms.txt)

You don't have to deploy to try a change. `npx tgcloud run` executes a handler on the platform using your **local** files, without publishing them:

```bash
npx tgcloud run handlers/message '{ chat: { id: 1 }, text: "hello" }'
```

The argument is the payload your handler receives — for `handlers/message`, a [Message](../external/bots/api/types/message.md) — written in [JSON5](https://json5.org) (so you can skip quoting keys). The command prints anything the handler logged with `console.*`, the return value, and how long it took. This is the tightest loop for iterating on logic — no deploy, no waiting for a real message.
