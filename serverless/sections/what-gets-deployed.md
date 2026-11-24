# What gets deployed

Source: https://core.telegram.org/bots/serverless#what-gets-deployed

[Documentation index](../llms.txt)

When you `npx tgcloud push`, the CLI gathers every `.js` file under `schema.js`, `lib/`, `handlers/`, and `endpoints/`, and sends that exact set as your project's module space — together with the Mini App's build folder, if `tgcloud.jsonc` names one (see below). Anything present in the cloud but absent from your project is removed, so the deployed state always mirrors your folder — deletions included. Nothing outside `tgcloud/` is deployed as code — the rest of the project root is yours. Inside `tgcloud/`, a `.js` file that isn't in one of those locations (`tgcloud/util.js`, `tgcloud/helpers/x.js`) is flagged, so it doesn't silently go undeployed. Markdown, dotfiles, and `.tgcloud/` are never deployed.
