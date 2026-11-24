# RichBlockVoiceNote

Source: https://core.telegram.org/bots/api#richblockvoicenote

[Documentation index](../llms.txt)

A block with a voice note, corresponding to the HTML tag `<audio>`.

| Field | Type | Description |
| --- | --- | --- |
| type | String | Type of the block, always “voice\_note” |
| voice\_note | [Voice](voice.md) | The voice note |
| caption | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block |
