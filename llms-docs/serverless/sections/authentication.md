# Authentication

Source: https://core.telegram.org/bots/serverless#authentication

[Documentation index](../llms.txt)

A project is tied to one bot by its token, which has the form `app<id>:<secret>`. The `app<id>` part is public and may be printed; the secret never appears in logs or errors. 

The token is resolved in this order:

1. **`TGCLOUD_TOKEN`** environment variable — for CI; never written to disk.
2. **`.tgcloud/credentials`** — written by [`npx tgcloud login`](login.md).
3. Neither → an error pointing you at `npx tgcloud login`.

The CLI **never prompts for a token mid‑command**. Logging in is always the explicit `login` step. If a saved token becomes invalid, the CLI removes it and asks you to `login` again.
