# `completion`

Source: https://core.telegram.org/bots/serverless#completion

[Documentation index](../llms.txt)

> **Note:** tab‑completion works only when a bare `tgcloud` is on your `PATH` — so install it globally (`npm install -g @tgcloud/cli`) or otherwise put the binary on your `PATH`. It can't hook into `npx`.

```bash
tgcloud completion <bash|zsh|fish>
```

Prints a shell completion script to stdout. Enable it once, then `<Tab>` completes commands, flags, module directories, the handler update‑types you don't have yet, and your local runnable modules.

```bash
# bash — needs the bash-completion package:
echo 'eval "$(tgcloud completion bash)"' >> ~/.bashrc

# zsh — ensure `autoload -U compinit && compinit` runs in your ~/.zshrc:
echo 'eval "$(tgcloud completion zsh)"' >> ~/.zshrc

# fish:
tgcloud completion fish > ~/.config/fish/completions/tgcloud.fish
```

Restart your shell (or re‑source the file) afterwards. Running `tgcloud completion` with no shell prints these instructions again.
