# BackgroundTypeFill

Source: https://core.telegram.org/bots/api#backgroundtypefill

[Documentation index](../llms.txt)

The background is automatically filled based on the selected colors.

| Field              | Type                                                                | Description                                                      |
| ------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------- |
| type               | String                                                              | Type of the background, always “fill”                            |
| fill               | [BackgroundFill](backgroundfill.md) | The background fill                                              |
| dark_theme_dimming | Integer                                                             | Dimming of the background in dark themes, as a percentage; 0-100 |
