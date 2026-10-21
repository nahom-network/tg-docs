# InputRichBlockAudio

Source: https://core.telegram.org/bots/api#inputrichblockaudio

[Documentation index](../llms.txt)

A block with a music file, corresponding to the HTML tag `<audio>`.

| Field   | Type                                                                    | Description                       |
| ------- | ----------------------------------------------------------------------- | --------------------------------- |
| type    | String                                                                  | Type of the block, always “audio” |
| audio   | [InputMediaAudio](inputmediaaudio.md)   | The audio. Caption is ignored.    |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block  |
