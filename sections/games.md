# Games

Source: https://core.telegram.org/bots/api#games

[Documentation index](../llms.txt)

Your bot can offer users **HTML5 games** to play solo or to compete against each other in groups and one-on-one chats. Create games via [@BotFather](https://t.me/botfather) using the */newgame* command. Please note that this kind of power requires responsibility: you will need to accept the terms for each game that your bots will be offering.

- Games are a new type of content on Telegram, represented by the [Game](game.md) and [InlineQueryResultGame](inlinequeryresultgame.md) objects.
- Once you've created a game via [BotFather](https://t.me/botfather), you can send games to chats as regular messages using the [sendGame](sendgame.md) method, or use [inline mode](inline-mode.md) with [InlineQueryResultGame](inlinequeryresultgame.md).
- If you send the game message without any buttons, it will automatically have a 'Play *GameName*' button. When this button is pressed, your bot gets a [CallbackQuery](callbackquery.md) with the *game_short_name* of the requested game. You provide the correct URL for this particular user and the app opens the game in the in-app browser.
- You can manually add multiple buttons to your game message. Please note that the first button in the first row **must always** launch the game, using the field *callback_game* in [InlineKeyboardButton](inlinekeyboardbutton.md). You can add extra buttons according to taste: e.g., for a description of the rules, or to open the game's official community.
- To make your game more attractive, you can upload a GIF animation that demonstrates the game to the users via [BotFather](https://t.me/botfather) (see [Lumberjack](https://t.me/gamebot?game=lumberjack) for example).
- A game message will also display high scores for the current chat. Use [setGameScore](setgamescore.md) to post high scores to the chat with the game, add the *disable_edit_message* parameter to disable automatic update of the message with the current scoreboard.
- Use [getGameHighScores](getgamehighscores.md) to get data for in-game high score tables.
- You can also add an extra [sharing button](../external/bots/games.md#sharing-your-game-to-telegram-chats) for users to share their best score to different chats.
- For examples of what can be done using this new stuff, check the [@gamebot](https://t.me/gamebot) and [@gamee](https://t.me/gamee) bots.

## In this section

- [sendGame](sendgame.md)
- [Game](game.md)
- [CallbackGame](callbackgame.md)
- [setGameScore](setgamescore.md)
- [getGameHighScores](getgamehighscores.md)
- [GameHighScore](gamehighscore.md)
