# UniqueGiftColors

Source: https://core.telegram.org/bots/api#uniquegiftcolors

[Documentation index](../llms.txt)

This object contains information about the color scheme for a user's name, message replies and link previews based on a unique gift.

| Field | Type | Description |
| --- | --- | --- |
| model\_custom\_emoji\_id | String | Custom emoji identifier of the unique gift's model |
| symbol\_custom\_emoji\_id | String | Custom emoji identifier of the unique gift's symbol |
| light\_theme\_main\_color | Integer | Main color used in light themes; RGB format |
| light\_theme\_other\_colors | Array of Integer | List of 1-3 additional colors used in light themes; RGB format |
| dark\_theme\_main\_color | Integer | Main color used in dark themes; RGB format |
| dark\_theme\_other\_colors | Array of Integer | List of 1-3 additional colors used in dark themes; RGB format |
