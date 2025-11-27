---
title: "How to get information about custom fields for time entries"
url: "https://clockify.me/help/troubleshooting/how-to-get-information-about-custom-fields-for-time-entries"
category: "troubleshooting"
slug: "how-to-get-information-about-custom-fields-for-time-entries"
---

# How to get information about custom fields for time entries

1 min read

To retrieve custom field data for time entries, use the following endpoint:

```
POST https://reports.api.clockify.me/v1/workspaces/{workspaceId}/reports/detailed
```

Include the **custom fields filter** in the request body according to the API documentation.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
