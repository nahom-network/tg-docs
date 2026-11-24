# HTTP

Source: https://core.telegram.org/bots/serverless#http

[Documentation index](../llms.txt)

`fetch` is a `fetch`‑like client for calling the outside world — third‑party APIs, webhooks, anything over HTTP.

```js
import { fetch } from 'sdk';

const res = await fetch('https://api.example.com/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Pavel' }),
});
if (!res.ok) throw new Error(res.statusText);
const data = await res.json();
```

The response mirrors the web platform: `res.status`, `res.statusText`, `res.ok` (true for 200–299), `res.url`, `res.headers` (`.get()`, `.has()`, `.keys()`, `.entries()`), and body readers `await res.json()` / `await res.text()`. 

> You can also read the body incrementally as a **stream** — `for await (const chunk of res.body) { … }` — which is how you consume server‑sent events or token‑by‑token output from **AI APIs**.

Body helpers set the matching `Content-Type` for you:

```js
await fetch(url, { method: 'POST', body: fetch.body.json({ a: 1 }) }); // application/json
await fetch(url, { method: 'POST', body: fetch.body.form({ a: 1 }) }); // x-www-form-urlencoded
await fetch(url, { method: 'POST', body: fetch.body.text('hi') });     // text/plain
```

Request bodies can also carry **files and raw bytes**: pass a `Uint8Array`, an `InputFile`, or a `FormData` (for `multipart/form-data`) as `body`, and the bytes are streamed out — so you can upload to a third‑party API the same way you send files to Telegram:

```js
import { fetch, FormData, InputFile } from 'sdk';

const form = new FormData();
form.append('file', new InputFile(bytes, 'photo.jpg', { type: 'image/jpeg' }));
form.append('caption', 'from my bot');
const res = await fetch('https://api.example.com/upload', { method: 'POST', body: form });
```

It otherwise behaves like the standard `fetch` you already know, with **two constraints**: 

- The **response** is read as text — `await res.json()` / `await res.text()`, or streamed chunk‑by‑chunk with `res.body`.
- The **total response is capped at 30 MB**. That cap covers the whole response — streaming with `res.body` lets you process a large body incrementally, but it does not raise the limit.
