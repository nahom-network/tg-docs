# ChatLocation

Source: https://core.telegram.org/bots/api#chatlocation

[Documentation index](../llms.txt)

Represents a location to which a chat is connected.

| Field    | Type                                                    | Description                                                                  |
| -------- | ------------------------------------------------------- | ---------------------------------------------------------------------------- |
| location | [Location](location.md) | The location to which the supergroup is connected. Can't be a live location. |
| address  | String                                                  | Location address; 1-64 characters, as defined by the chat owner              |
