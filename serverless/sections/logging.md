# Logging

Source: https://core.telegram.org/bots/serverless#logging

[Documentation index](../llms.txt)

The standard global `console` is available — nothing to import, it's just there as in any JavaScript. Its output is captured and shown by `npx tgcloud run`, which makes it your primary debugging tool during development.

```js
console.log('processing', { chatId: id });   // log / debug — plain
console.info('started');                     // info  — blue
console.warn('rate limited');                // warn  — yellow
console.error(err);                          // error — red, with a stack trace
```

Each line is tagged with the `[file:line]` it came from. `console.error` and `console.trace` append a full stack, while `console.warn` does not. When you `npx tgcloud run` a module, these lines are printed with a colored prefix per level, the time since the run started, and the origin — see [`run`](run.md).
