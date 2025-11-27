---
title: "How to export data via API"
url: "https://clockify.me/help/troubleshooting/how-to-export-data-via-api"
category: "troubleshooting"
slug: "how-to-export-data-via-api"
---

# How to export data via API

1 min read

You can export data (e.g. reports) using the following API call. The key\-value parameter for export type is `exportType`. Available values include `JSON`, `CSV`, `XLSX`, and `PDF`.

#### **Example: Exporting Detailed Report as CSV**

```
[POST /v1/workspaces/{workspaceId}/reports/detailed](https://docs.clockify.me/#tag/Time-Entry-Report/operation/generateDetailedReport)
```

Headers:

```
"X-Api-Key": "yourApiKey", 
 
"Content-Type":"application/json"

  
```

Body: 

```
{

  "dateRangeStart": "2024-01-01T00:00:00.000",

  "dateRangeEnd": "2024-12-31T23:59:59.000",

  "exportType": "CSV",

  "detailedFilter": {

    "page": 1,

    "pageSize": 1000

  }

}

```

#### **Example: Exporting Summary Report as CSV**

```
[POST /v1/workspaces/{workspaceId}/reports/summary](https://docs.clockify.me/#tag/Time-Entry-Report/operation/generateSummaryReport)
```

Headers:

```
"X-Api-Key": "yourApiKey", 
 
"Content-Type":"application/json"
```

 

Body:

```
{

  "dateRangeStart": "2018-11-01T00:00:00Z",

  "dateRangeEnd": "2018-11-30T23:59:59.999Z",

  "exportType": "JSON",

  "summaryFilter": {

    "groups": 1,

    "sortColumn": GROUP

    "summaryChartType": "PROJECT"

    "page": 1,

    "pageSize": 1000

  }

}
```

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
