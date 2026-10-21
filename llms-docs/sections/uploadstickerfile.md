# uploadStickerFile

Source: https://core.telegram.org/bots/api#uploadstickerfile

[Documentation index](../llms.txt)

Use this method to upload a file with a sticker for later use in the [createNewStickerSet](createnewstickerset.md), [addStickerToSet](addstickertoset.md), or [replaceStickerInSet](replacestickerinset.md) methods (the file can be used multiple times). Returns the uploaded [File](file.md) on success.

| Parameter      | Type                                                      | Required | Description                                                                                                                                                                                                             |
| -------------- | --------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id        | Integer                                                   | Yes      | User identifier of sticker file owner                                                                                                                                                                                   |
| sticker        | [InputFile](inputfile.md) | Yes      | A file with the sticker in.WEBP,.PNG,.TGS, or.WEBM format. See <https://core.telegram.org/stickers> for technical requirements. [More information on Sending Files »](sending-files.md) |
| sticker_format | String                                                    | Yes      | Format of the sticker, must be one of “static”, “animated”, “video”                                                                                                                                                     |
