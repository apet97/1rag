---
title: "How to make a list of projects with assigned people via API?"
url: "https://clockify.me/help/troubleshooting/how-to-make-a-list-of-projects-with-assigned-people-via-api"
category: "troubleshooting"
slug: "how-to-make-a-list-of-projects-with-assigned-people-via-api"
---

# How to make a list of projects with assigned people via API?

1 min read

If you want to create a list of projects with the people assigned to them, do the following:

* **Tools**:  

	* You will need Postman (or another API tool) for making API calls
	* Convert JSON responses into CSV format for easier handling in Excel (e.g. use [konklone](https://konklone.io/json/), or some other conversion tool)
* **API calls**:  

	* Use the following two endpoints:
		* `GET /v1/users` – To get user information
		* `GET /v1/projects` – To get project information
	* Be mindful of the **page size** and **page number** when fetching project data to ensure you retrieve all projects
* **Convert data to CSV**:  

	* In **Postman**, export the responses to JSON
	* Use **konklone.io** to convert each JSON response to a CSV file
* **Combine data in Excel**:  

	* Open the two CSV files in **Excel**
	* Use **Excel’s conditional formatting** to match the user IDs in the project CSV with the corresponding user names (or emails) from the user CSV
	* You may need to adjust cell sizes to view all data or separate the user IDs into multiple cells

As a result,you’ll have a CSV file listing **projects** in one column and the assigned **user names** in another column.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
