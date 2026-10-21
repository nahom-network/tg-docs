# Building with AI

Source: https://core.telegram.org/bots/serverless#building-with-ai

[Documentation index](../llms.txt)

Prefer to build with an AI assistant — or is the only coder on your team an AI? You can still ship a bot. We've taken a first step to make an AI agent feel at home in a project: every new one is scaffolded with an `AGENTS.md` and a `docs/tgcloud-sdk.md` reference that agentic coding tools read automatically. 

Together with a small, self‑contained runtime — one SDK, no npm packages to wrangle — that gives the assistant a running start on the conventions generic codegen tends to miss here: relative imports with `.js`, no foreign keys, every `db` call is async, one handler per update type, and the two‑step `push`/`migrate` flow.

Try it:

```bash
npm create @tgcloud/bot my-bot
cd my-bot
opencode            # or Claude Code, Cursor, … — any agent that reads AGENTS.md
```

Then just ask, in plain language:

> Write a bot that remembers each person's to‑do list — add an item when they send text, and show the whole list when they send /list.

The assistant edits `schema.js` and your handlers for you; you review, test a change instantly with `npx tgcloud run`, then go live with `npx tgcloud push` and `npx tgcloud migrate`. `AGENTS.md` is part of your project — edit it as the bot grows so the guidance stays accurate.
