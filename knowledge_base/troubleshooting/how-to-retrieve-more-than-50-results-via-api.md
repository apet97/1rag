---
title: "How to retrieve more than 50 results via API"
url: "https://clockify.me/help/troubleshooting/how-to-retrieve-more-than-50-results-via-api"
category: "troubleshooting"
slug: "how-to-retrieve-more-than-50-results-via-api"
---

# How to retrieve more than 50 results via API

1 min read

By default, Clockify API returns only 50 results per page. If you want to retrieve more than 50 results, you can modify the `page-size` and `page` parameters.

#### **For GET requests:**

* **Modify the parameters**: Add the following parameters at the end of your API endpoint:
	* `page=<page_number>`
	* `page-size=<desired_size>` (max 5000 for base and 1000 for report endpoints)
* Example:
	* To retrieve more than 50 time entries, use:

```
https://api.clockify.me/api/v1/workspaces/{WorkspaceID}/user/{UserID}/time-entries?page=2&page-size=200
```

#### **For POST requests:**

* **Adjust the `page` and `page-size`**:
	* In the request payload, within the `detailedFilter` section, specify the page and page\-size.
* Example:

```
{

  "dateRangeStart": "2021-05-28T05:00:00.000000Z",

  "dateRangeEnd": "2021-05-29T00:00:00.000000Z",

  "detailedFilter": {

    "page": 1,

    "page-size": 200

  }

}
```

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
