# Sending files

Source: https://core.telegram.org/bots/api#sending-files

[Documentation index](../llms.txt)

There are three ways to send files (photos, stickers, audio, media, etc.):

1. If the file is already stored somewhere on the Telegram servers, you don't need to reupload it: each file object has a **file\_id** field, simply pass this **file\_id** as a parameter instead of uploading. There are **no limits** for files sent this way.
2. Provide Telegram with an HTTP URL for the file to be sent. Telegram will download and send the file. 5 MB max size for photos and 20 MB max for other types of content.
3. Post the file using multipart/form-data in the usual way that files are uploaded via the browser. 10 MB max size for photos, 50 MB for other files.

**Sending by file\_id**

- It is not possible to change the file type when resending by **file\_id**. I.e. a [video](video.md) can't be [sent as a photo](sendphoto.md), a [photo](photosize.md) can't be [sent as a document](senddocument.md), etc.
- It is not possible to resend thumbnails.
- Resending a photo by **file\_id** will send all of its [sizes](photosize.md).
- **file\_id** is unique for each individual bot and **can't** be transferred from one bot to another.
- **file\_id** uniquely identifies a file, but a file can have different valid **file\_id**s even for the same bot.

**Sending by URL**

- When sending by URL the target file must have the correct MIME type (e.g., audio/mpeg for [sendAudio](sendaudio.md), etc.).
- In [sendDocument](senddocument.md), sending by URL will currently only work for **.PDF** and **.ZIP** files.
- To use [sendVoice](sendvoice.md), the file must have the type audio/ogg and be no more than 1MB in size. 1-20MB voice notes will be sent as files.
- Other configurations may work but we can't guarantee that they will.
