---
title: "How to create or edit an expense via API"
url: "https://clockify.me/help/troubleshooting/how-to-create-or-edit-an-expense-via-api"
category: "troubleshooting"
slug: "how-to-create-or-edit-an-expense-via-api"
---

# How to create or edit an expense via API

* [Steps to create/edit an expense via API](#steps-to-create-edit-an-expense-via-api)

# How to create or edit an expense via API

1 min read

These instructions explain how to create or edit an expense using the Clockify API, which requires a specific formatting technique. Expenses are handled differently compared to other API requests in Clockify.

## Steps to create/edit an expense via API [\#](#steps-to-create-edit-an-expense-via-api)

* **Log in to Postman**: Ensure you are logged into your Postman account
* **Create a POST (create expense) or PUT (edit expense) request**:
	* Set the request path to   
	[`/v1/workspaces/{workspaceId}/expenses`](https://docs.clockify.me/#tag/Expense/operation/createExpense)
* **Set headers**:
	* Add `X-Api-Key` for authentication
	* Set `Content-Type` to `multipart/form-data`
* **Body format**:
	* Choose `form-data` instead of `raw` for the body type
	* Enter the following keys and corresponding values (without quotes):
		* **KEY**: `user_id`, `date, project_id`, `category_id`, `notes`, `amount`, `billable`
		* **VALUE**: Enter the data values directly (no quotations around the values)
* **Send the request**: After sending, check the status of the request
	* If successful, you should see a `201 Created` response
	* The response will be displayed in **JSON** format

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
