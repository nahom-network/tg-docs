# RichBlockDocument

Source: https://core.telegram.org/bots/api#richblockdocument

[Documentation index](../llms.txt)

A block with a general file, corresponding to the custom HTML tag `<tg-document>`.

| Field    | Type                                                                    | Description                          |
| -------- | ----------------------------------------------------------------------- | ------------------------------------ |
| type     | String                                                                  | Type of the block, always “document” |
| document | [Document](document.md)                 | The document                         |
| caption  | [RichBlockCaption](richblockcaption.md) | *Optional*. Caption of the block     |
