# getUserProfilePhotos

Source: https://core.telegram.org/bots/api#getuserprofilephotos

[Documentation index](../llms.txt)

Use this method to get a list of profile pictures for a user. Returns a [UserProfilePhotos](userprofilephotos.md) object.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| user_id | Integer | Yes | Unique identifier of the target user |
| offset | Integer | Optional | Sequential number of the first photo to be returned. By default, all photos are returned. |
| limit | Integer | Optional | Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100. |
