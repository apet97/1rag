---
title: "How to find userID via API"
url: "https://clockify.me/help/troubleshooting/how-to-find-userid-in-the-api"
category: "troubleshooting"
slug: "how-to-find-userid-in-the-api"
---

# How to find userID via API

1 min read

To retrieve the **userID** of a user, use the following endpoint:

**Endpoint**:

```
[GET](https://docs.clockify.me/#tag/User/operation/getLoggedUser)[https://api.clockify.me/api/v1/user](https://docs.clockify.me/#tag/User/operation/getLoggedUser)
```

This endpoint returns only the currently logged\-in user. 

To get all users or a specific user’s ID, use the `/v1/users` endpoint to fetch the full user list from the workspace.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
