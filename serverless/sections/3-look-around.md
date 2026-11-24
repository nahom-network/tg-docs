# 3. Look around

Source: https://core.telegram.org/bots/serverless#3-look-around

[Documentation index](../llms.txt)

Two commands tell you where things stand at any moment, both fully offline:

```bash
npx tgcloud status     # what has changed locally vs. the deployed copy
npx tgcloud diff       # the line‑by‑line changes
```

Right after `init` everything is new and nothing is deployed yet. `status` shows the starter files waiting to go up.
