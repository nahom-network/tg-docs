# MessageOriginUser

Source: https://core.telegram.org/bots/api#messageoriginuser

[Documentation index](../llms.txt)

The message was originally sent by a known user.

| Field       | Type                                            | Description                                       |
| ----------- | ----------------------------------------------- | ------------------------------------------------- |
| type        | String                                          | Type of the message origin, always “user”         |
| date        | Integer                                         | Date the message was sent originally in Unix time |
| sender_user | [User](user.md) | User that sent the message originally             |
