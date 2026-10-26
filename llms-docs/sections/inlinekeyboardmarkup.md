# InlineKeyboardMarkup

Source: https://core.telegram.org/bots/api#inlinekeyboardmarkup

[Documentation index](../llms.txt)

This object represents an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards) that appears right next to the message it belongs to.

| Field | Type | Description |
| --- | --- | --- |
| inline\_keyboard | Array of Array of [InlineKeyboardButton](inlinekeyboardbutton.md) | Array of button rows, each represented by an Array of [InlineKeyboardButton](inlinekeyboardbutton.md) objects |
| force\_reply | Boolean | *Optional*. Pass *True* if the reply interface must be shown to the user, as if they had manually selected the bot's message and tapped 'Reply'. The value of the field can't be changed when the inline keyboard is edited. |
