# InputRichBlockDocument

Source: https://core.telegram.org/bots/api#inputrichblockdocument

[Documentation index](../llms.txt)

A block with a general file, corresponding to the custom HTML tag `<tg-document>`.

| Field    | Type                                                                        | Description                          |
| -------- | --------------------------------------------------------------------------- | ------------------------------------ |
| type     | String                                                                      | Type of the block, always “document” |
| document | [InputMediaDocument](inputmediadocument.md) | The document. Caption is ignored.    |
| caption  | [RichBlockCaption](richblockcaption.md)     | *Optional*. Caption of the block     |
