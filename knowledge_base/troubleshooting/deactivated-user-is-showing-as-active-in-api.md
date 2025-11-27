---
title: "Deactivated user is displayed as active in API"
url: "https://clockify.me/help/troubleshooting/deactivated-user-is-showing-as-active-in-api"
category: "troubleshooting"
slug: "deactivated-user-is-showing-as-active-in-api"
---

# Deactivated user is displayed as active in API

* [Explanation](#explanation)
* [Solution](#solution)

# Deactivated user is displayed as active in API

1 min read

If you encounter an issue where a deactivated user is showing as `ACTIVE` via the API, it’s important to understand how Clockify handles user status.

## Explanation [\#](#explanation)

When a user is deactivated from a specific workspace, their account is not deleted from the Clockify database.  
If the user is a member of multiple workspaces, their account will remain active in other workspaces.

## Solution [\#](#solution)

* Ensure you are using the correct endpoint:
	* **Workspace users**: [`GET /v1/workspaces/{{ws id}}/users`](https://docs.clockify.me/#tag/User/operation/getUsersOfWorkspace)
* To check membership status in a specific workspace, use the query parameter `?memberships=ALL`:
	* Example: `GET /v1/workspaces/{{ws id}}/users/?memberships=ALL`

If the status still shows `ACTIVE`, it is expected behavior. The user is still considered **active** in the system due to their presence in other workspaces.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
