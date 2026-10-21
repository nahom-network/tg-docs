# savePreparedKeyboardButton

Source: https://core.telegram.org/bots/api#savepreparedkeyboardbutton

[Documentation index](../llms.txt)

Stores a keyboard button that can be used by a user within a Mini App. Returns a [PreparedKeyboardButton](preparedkeyboardbutton.md) object.

| Parameter | Type                                                                | Required | Description                                                                                                                                           |
| --------- | ------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id   | Integer                                                             | Yes      | Unique identifier of the target user that can use the button                                                                                          |
| button    | [KeyboardButton](keyboardbutton.md) | Yes      | A JSON-serialized object describing the button to be saved. The button must be of the type *request_users*, *request_chat*, or *request_managed_bot*. |
