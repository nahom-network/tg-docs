# `status`

Source: https://core.telegram.org/bots/serverless#status

[Documentation index](../llms.txt)

```bash
npx tgcloud status
```

Shows, per file, what has changed between your working directory and the deployed copy: modified, new, deleted, unchanged. It works offline, comparing against the state of the cloud as of your last `push`, `pull` or `fetch`. It also warns about stray `.js` files inside `tgcloud/` that won't be deployed.

For a project with a Mini App, `status` also shows what changed in its build folder since the last deploy.
