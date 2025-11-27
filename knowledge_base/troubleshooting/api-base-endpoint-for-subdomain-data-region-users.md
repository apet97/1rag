---
title: "API base endpoint for subdomain/data region users"
url: "https://clockify.me/help/troubleshooting/api-base-endpoint-for-subdomain-data-region-users"
category: "troubleshooting"
slug: "api-base-endpoint-for-subdomain-data-region-users"
---

# API base endpoint for subdomain/data region users

1 min read

If you’re working with a **subdomain workspace** or one hosted in a specific **data region**, the base endpoint you’ll use for your API requests differs depending on your setup.

* **For Subdomain (Enterprise plan)**:  
If your workspace is on a subdomain, you should use the following endpoint format:

```
https://subdomainname.clockify.me/api/v1
```

* **For data regions**:  
If your workspace is hosted in a specific region, use one of these region\-specific endpoints:  

	* **Germany**: https://euc1\.clockify.me/api/v1
	* **UK**: https://euw2\.clockify.me/api/api/v1
	* **USA**: https://use2\.clockify.me/api/v1
	* **Australia**: https://apse2\.clockify.me/api/v1
* For general **Cloud users**, the standard endpoint is:

```
https://api.clockify.me/api/v1
```

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
