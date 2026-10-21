# `push`

Source: https://core.telegram.org/bots/serverless#push

[Documentation index](../llms.txt)

```bash
npx tgcloud push [files...]
```

Deploys your project to the cloud in one atomic batch.

With **no arguments**, it deploys the whole project, and the deployed state is made to mirror your folder exactly — modules you deleted locally are removed in the cloud.

With **file or directory arguments** (`npx tgcloud push tgcloud/handlers/message.js`, `npx tgcloud push handlers/`), it deploys only the changes in those files. A targeted push never deletes other modules. A target may be spelled as the file path (`tgcloud/handlers/message.js`), the path inside `tgcloud/` (`handlers/message.js`) or the module name (`handlers/message`) — they all mean the same module.

Its one option is `--force` — to skip the concurrency check and overwrite whatever is in the cloud. Only use it when you're sure (see [Staying in sync](staying-in-sync.md)). 

If `tgcloud.jsonc` names a static folder, a full `push` deploys it in the same batch — only the files that changed are uploaded — and prints the site's address. Build first, because `push` never runs your build (`npm run deploy` does both). `npx tgcloud push dist/` deploys the static files alone, and a push that names only modules leaves them untouched.

After a deploy, if `schema.js` changed and the database is out of sync, `push` prints a summary of the pending changes and suggests `npx tgcloud migrate`. It never applies them itself.
