---
title: "Clockify API overview"
url: "https://clockify.me/help/getting-started/clockify-api-overview"
category: "getting-started"
slug: "clockify-api-overview"
---

# Clockify API overview

3 min read

The [Clockify API](https://docs.clockify.me/) enables you to automate, extend, and integrate Clockify’s time tracking features with your own systems and workflows. Whether you’re syncing time data with some management tool or integrating with a custom project management system, the API offers the flexibility and control you need.

### What can you do with the API? [\#](#what-can-you-do-with-the-api)

* **Time tracking automation \& approvals**
	* Start, stop, and manage time entries
	* Edit time entries (e.g. description, duration, project)
	* Retrieve time logs for reports or analysis

* **User and workspace management**
	* List and manage users within a workspace
	* Create or update user profiles
	* Assign users to projects or teams
	* Filter users by role, project membership, email, or workspace status
	* Add users to a workspace
	* Manage custom fields for users and time entries
	* Update user\-specific costs and hourly rates
	* Get daily capacity for workspace users

* **Clients, projects, and tasks**
	* Create, update, and delete clients, projects, and tasks
	* Manage tasks within projects
	* Assign users and roles to projects
	* Create, read, update, and delete (CRUD) user groups
	* CRUD assignments

* **Time off management**
	* Create and manage holidays and time\-off policies
	* Automate time\-off requests and approvals

* **Reports and exports**
	* Generate summary and detailed reports
	* Export time tracking data for payroll, billing, or analysis
* **Custom integrations**
	* Integrate with CRMs, project management tools, payroll systems, and more
	* Automate internal workflows using real\-time or scheduled API interactions

### Permissions \& access control [\#](#permissions-access-control)

API actions follow the same permission model as the Clockify UI. Only users with the appropriate roles and [access levels](https://clockify.me/help/administration/user-roles-and-permissions/who-can-do-what) in the app can perform specific actions via the API.

### Documentation \& support [\#](#documentation-support)

You’ll find everything you need to get started including setup instructions, authentication, available endpoints, and usage examples in our [API documentation](https://docs.clockify.me/).

While we don’t offer custom API integration or development services, our Support team is happy to assist with:

* Troubleshooting errors
* Investigating unexpected behavior
* Clarifying how specific API features work

\*\*\*

To help us assist you faster, please include the following details in your message:

* Endpoint and method
	* The exact API endpoint you’re calling
	* HTTP method used (GET, POST, etc.)
* Full curl request (without API key)  

	* Include headers, body payload (if any), and query parameters
	* Redact any sensitive information like API keys or tokens
* Full response  

	* Status code and full response body, including any error messages

### **Interested in custom API Integration?**

While we don’t provide custom API development services, you have options to:

* Explore our [Marketplace](https://marketplace.cake.com/) and discover ready\-made add\-ons
* Build your own by diving into our [developer documentation](https://dev-docs.marketplace.cake.com/) and get started

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
