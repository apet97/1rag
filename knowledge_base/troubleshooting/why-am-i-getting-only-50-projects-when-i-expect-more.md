---
title: "Why am I getting only 50 projects when I expect more?"
url: "https://clockify.me/help/troubleshooting/why-am-i-getting-only-50-projects-when-i-expect-more"
category: "troubleshooting"
slug: "why-am-i-getting-only-50-projects-when-i-expect-more"
---

# Why am I getting only 50 projects when I expect more?

* [Solution](#solution)

# Why am I getting only 50 projects when I expect more?

1 min read

Users may report that despite setting a large page\-size limit, they only get 50 results. This issue is usually caused by incorrect formatting in the request.

## Solution [\#](#solution)

* When setting parameters for page\-size, ensure there are **no spaces** before or after the \= sign.
	* **Incorrect**: `page-size = 5000`
	* **Correct**: `page-size=5000`
* Incorrect formatting causes the API to default to the 50\-page limit.

Once the correct page size is set, you should receive the full set of results.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
