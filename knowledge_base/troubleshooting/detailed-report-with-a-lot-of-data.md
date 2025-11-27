---
title: "Detailed report with a lot of data"
url: "https://clockify.me/help/troubleshooting/detailed-report-with-a-lot-of-data"
category: "troubleshooting"
slug: "detailed-report-with-a-lot-of-data"
---

# Detailed report with a lot of data

1 min read

To fetch detailed time entry reports, use the following endpoint: 

```
[POST /v1/workspaces/{workspaceId}/reports/detailed](https://docs.clockify.me/#tag/Time-Entry-Report/operation/generateDetailedReport)
```

Add `page` and `pageSize` parameters to manage large datasets.

**Example**:

* `page: 1`
* `pageSize: 1000`

If you have more than 1000 entries, create a script or manually change the page number in the body (`page: 1`, `page: 2`, etc.).

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
