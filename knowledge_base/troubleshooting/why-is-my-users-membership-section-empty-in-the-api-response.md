---
title: "Why is My User\u2019s Membership Section Empty in the API Response?"
url: "https://clockify.me/help/troubleshooting/why-is-my-users-membership-section-empty-in-the-api-response"
category: "troubleshooting"
slug: "why-is-my-users-membership-section-empty-in-the-api-response"
---

# Why is My User’s Membership Section Empty in the API Response?

* [Answer](#answer)
* [Solution](#solution)

# Why is My User’s Membership Section Empty in the API Response?

1 min read

If you find that the `memberships` section is empty in the API response for getting user’s info, it could be due to the `memberships` parameter being excluded.

## Answer [\#](#answer)

This is due to the change in the API’s `membership` section, where membership data is returned as `empty by default`.

## Solution [\#](#solution)

To resolve this, you need to include the `memberships` query parameter in your API call.

* Add the memberships parameter to your query:
	* Example:
		* `memberships=WORKSPACE`
		* `memberships=PROJECT`
		* `memberships=USERGROUP`
		* `memberships=ALL`or,
* Directly in the URL:

Example: 

```
https://api.clockify.me/api/v1/workspaces/{workspaceId}/users?memberships=WORKSPACE
```

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
