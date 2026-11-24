# The module system

Source: https://core.telegram.org/bots/serverless#the-module-system

[Documentation index](../llms.txt)

At runtime, a module can see exactly two things: **the platform SDK** and **the other modules in your project**. There are no npm packages, no filesystem, and no network except through the SDK's `fetch`.

Import your own modules the way you would in any JavaScript project — by **relative path, with the `.js` extension** — and the SDK by its name:

```js
// tgcloud/handlers/message.js
import { users } from '../schema.js';              // ✅ the schema module
import { addItem } from '../lib/cart.js';          // ✅ a lib module
import { format } from '../lib/internal/fmt.js';  // ✅ nested lib module
import { db, api, fetch } from 'sdk';              // ✅ the platform SDK
```

```js
// tgcloud/lib/cart.js
import { format } from './internal/fmt.js';        // ✅ a neighbour
import { users } from '../schema.js';
```

A relative import must end in `.js` and can't lead outside `tgcloud/`:

```js
import { users } from '../schema';       // ❌ add the .js
import config from '../../config.js';    // ❌ outside tgcloud/
import { z } from 'zod';                 // ❌ no npm packages
```

Every module also has a **name** — its path inside `tgcloud/` without the extension, such as `schema`, `lib/cart` or `handlers/message`. That name is what `npx tgcloud run` and the CLI's output use, and a module can be imported by it as well (`from 'lib/cart'`, no extension). Prefer relative imports in your code. They are what your editor understands — jump‑to‑definition, autocomplete, rename.

What's available at runtime is exactly two things: **`sdk`** and its submodules (`sdk/db`, `sdk/api`, `sdk/fetch`) — the whole platform surface, see [The SDK](the-sdk.md) — and **your own modules** in `tgcloud/`. That's the complete list. If your code `import`s anything else, it won't resolve. This constraint is what keeps modules fast to load and safe to run.
