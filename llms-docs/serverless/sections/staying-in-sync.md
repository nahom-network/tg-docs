# Staying in sync

Source: https://core.telegram.org/bots/serverless#staying-in-sync

[Documentation index](../llms.txt)

Every project has a monotonically increasing **revision** in the cloud, bumped on each deploy. The CLI remembers the revision it last synced with and sends it on each `push`. If the cloud has moved ahead — because another machine or teammate deployed — the push is **rejected** instead of silently overwriting their work, and the CLI offers three ways forward:

```bash
npx tgcloud fetch           # see what changed in the cloud, then re-check
npx tgcloud pull            # bring the latest into your working files
npx tgcloud push --force    # overwrite the cloud state (dangerous)
```

This optimistic‑concurrency check is why you can share a bot across a team without a lockstep deploy process. Commands exit non‑zero on failure — a rejected deploy, a failed migration, an authentication error, a module that threw during `run` — so they compose cleanly in scripts and CI pipelines.
