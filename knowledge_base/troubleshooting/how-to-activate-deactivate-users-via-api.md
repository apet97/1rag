---
title: "How to activate/deactivate users via API"
url: "https://clockify.me/help/troubleshooting/how-to-activate-deactivate-users-via-api"
category: "troubleshooting"
slug: "how-to-activate-deactivate-users-via-api"
---

# How to activate/deactivate users via API

1 min read

To activate or deactivate a user, use the following API call:

**Endpoint**:

```
[PUT /v1/workspaces/{workspaceId}/users/{userId}](https://docs.clockify.me/#tag/Workspace/operation/updateUserStatus)
```

In the request body, specify the status (`active` or `inactive`) to update the user’s status.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
