---
title: "How to get a specific project via API?"
url: "https://clockify.me/help/troubleshooting/how-to-get-a-specific-project-via-api"
category: "troubleshooting"
slug: "how-to-get-a-specific-project-via-api"
---

# How to get a specific project via API?

1 min read

To retrieve information about a specific project via the API, you need to make a request with the **project ID**.

**Endpoint**:

```
GET /workspaces/{workspaceId}/projects/{projectId}
```

Make sure that you replace `{workspaceId}` and `{projectId}` with the correct IDs for your request.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
