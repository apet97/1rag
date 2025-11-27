---
title: "Create projects & clients"
url: "https://clockify.me/help/projects/creating-projects"
category: "projects"
slug: "creating-projects"
---

# Create projects & clients

* [Create projects](#create-projects)
* [Archive projects](#archive-projects)
* [Delete projects](#delete-projects)
* [Merge projects](#merge-projects)
* [Manage people on projects](#manage-people-on-projects)
* [Project status](#project-status)
* [Project note](#project-note)
* [Project name/client/color](#project-name-client-color)
* [Set project's billable rate](#set-projects-billable-rate)
* [Filter and sort projects](#filter-and-sort-projects)
* [Create project from a template](#create-project-from-a-template)
* [Add and edit tasks in a bulk](#add-and-edit-tasks-in-a-bulk)
* [Manage clients](#manage-clients)
* [Archive clients](#archive-clients)

# Create projects \& clients

10 min read

Projects are useful for grouping and [categorizing time entries](https://clockify.me/help/track-time-and-expenses/categorizing-time-entries) that belong to the same type of work. Projects make it easier to analyze data, generate more useful reports, and see where and how you spend time.

Each project typically belongs to some client, but you can create a project without a client (e.g. internal company stuff). A client can have multiple projects, but a project can belong to only one client. 

You can also [import projects and clients](https://clockify.me/help/track-time-and-expenses/import-timesheets) from a file.

For an overall guidance on projects, watch the video and follow the instructions below.

User interface displayed in this video may not correspond to the latest version of the app.  

## Create projects [\#](#create-projects)

By default, only admins can create projects. However, this set of permissions can be modified if **Who can create projects and clients** is set to **Admins and managers** or **Anyone** in the **Workspace settings**.

![](https://clockify.me/help/wp-content/uploads/2022/05/image_1-1.png)
Who can create projects if selected:

* **Admins** (default): admins
* **Admins and project managers**: admins and project manager
* **Anyone**: admins, projects managers, team managers, regular users

The person who creates the project automatically becomes its project manager meaning that they can view all tracked time on their projects, set estimates, add tasks, manage project access and modify all other aspects of the project.  

To create a project:

1. Go to Projects and click **Create new project**
2. Name the project
3. Select client (you can also create a new client here, by typing a name and clicking **Create client**)
4. Choose a project color from the **Custom** section or **[color picker](https://clockify.me/help/projects/creating-projects#color-picker)**
5. Choose visibility (public or private)
6. Click **Create**

Once you’ve created a project, you can select it when tracking time. If you’ve set the project as private (visible only to a certain [group](https://clockify.me/help/administration/user-groups)), then only people who are on the project will be able to select it when tracking time. You can also adjust the size of columns (name, client, status, access) to make sure all data is properly displayed.

![](https://clockify.me/help/wp-content/uploads/2018/01/Screenshot-2025-05-30-at-09.18.47-1-1024x449.png)
If you use the Clockify browser extension, you can track time on projects and tasks from the **Projects** page. 

For more information, check out the [Browser extension](https://clockify.me/help/apps/chrome-extension#track-time-from-projects-page) page.

### Quick create [\#](#quick-create)

You can also add a project directly from the project picker while creating a new time entry.

Click on the **\+Project** field to get a drop\-down list of projects and start typing the name of your new project. Once you start typing the drop\-down list will try to suggest a matching (existing) project name.

If that project does not exist, you will be offered the option to create a new project.

Click on the **\+ Create new project** button and a popup window with additional options will appear allowing you to name your project, assign a client, apply a project template and select if the project will be public or private. 

You can also use a keyboard shortcut **Ctrl /** **^ (Control) \+ Enter** to quickly create a project without additional details.

![](https://clockify.me/help/wp-content/uploads/2018/01/Screenshot-2025-05-30-at-09.29.02-1024x513.png)
### Color picker [\#](#color-picker)

The **Custom** section in the **color picker** for Projects allows you to save up to 8 custom colors.   
If you haven’t used custom colors yet, the section will show a **\+** sign prompting you to add new ones. 

![](https://clockify.me/help/wp-content/uploads/2018/01/Screenshot-2025-03-19-at-13.14.27.png)
Custom colors are consistent across all devices and modes.

## Archive projects [\#](#archive-projects)

Once you complete a project, you can archive it, so it’s no longer visible when tracking time.

**To archive a project:**

1. Go to the **Projects** page
2. Click three dots next to the project you want to archive
3. Select **Archive**

You can check the **Also mark all tasks as done** box in a screen that pops up requiring you to confirm the action and all the tasks in the archived project will be marked as **done**. 

Once the project is archived you will be able to delete it.

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-20-at-15.51.11-1024x162.png)
**To see archived projects**, click the **Active** filter at the top of the page, change it to **Archived** and click **APPLY FILTER** to confirm the action. 

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-20-at-15.53.43-1024x171.png)
**To restore an archived project**, click three dots next to it and select **Restore**.

**When you archive a project:**

* All its data is still available
* Project’s time entries will still be shown in reports
* Archived projects won’t appear in reports as filters unless you select **All** or **Archived**
* Archived projects won’t be available in the project picker when creating new time entries
* Archived projects won’t appear on **Projects** page (unless you select **Archived in the filter**)

You can also archive tags and clients the same way you can archive projects. 

## Delete projects [\#](#delete-projects)

Projects can only be deleted once they are archived.

**To delete a project:**

1. Go to Projects page
2. Select **Archived** or **All** from the drop\-down menu
3. Click three dots next to the archived project’s name
4. Select **Delete**
5. Confirm the action

Deleting a project will remove it from all time entries it is assigned to, but time will remain. 

## Merge projects [\#](#merge-projects)

While it’s not possible to merge projects, you can filter entries of one of the projects you want to merge and assign it to the other project [in the Detailed report](https://clockify.me/help/reports/detailed-report#editing-time-entries). 

It is also possible to update multiple time entries at the same time with the [Bulk edit](https://clockify.me/help/track-time-and-expenses/editing-time-entries#update-multiple-time-entries-in-a-bulk) feature in the Detailed report.

Then, simply [archive](https://clockify.me/help/projects/creating-projects#archiving-projects) and [delete](https://clockify.me/help/projects/creating-projects#deleting-projects) the project you don’t need. 

## Manage people on projects [\#](#manage-people-on-projects)

To see how to change the project’s privacy settings, manage user access to a project, or set users as project managers, visit [this help article](https://clockify.me/help/projects/managing-people-on-projects).

## Project status [\#](#project-status)

When you and your team start tracking time for projects and tasks, you’ll be able to track progress on each project using Project status. 

To learn more about how to use project status, visit [this help article](https://clockify.me/help/projects/tracking-project-progress).

## Project note [\#](#project-note)

You can add additional information to projects by using a project note.  To learn more about how to format a project note, visit [this help article](https://clockify.me/help/projects/formatting-project-note).

## Project name/client/color [\#](#project-name-client-color)

If you need to edit project name, client, color, or any other type of project setting, you can do that in the **Settings** tab. 

1. Go to the Projects page
2. Choose the project
3. Switch to the Project settings tab
4. Edit project name, change/add client/project color

Changes you make will be immediately visible.

## Set project’s billable rate [\#](#set-projects-billable-rate)

Clockify has 4 types of [billable rates](https://clockify.me/help/reports/rates/hourly-rates), one of which is the project billable rate. If set, this billable rate gets applied to each time entry created for this project. 

The project billable rate can be overwritten by Projects’ member rate which you define in the [projects’ Access](https://clockify.me/help/projects/managing-people-on-projects) tab if you want different users on the project to have different billable rates.

**To set a billable rate for a specific project:**

1. Go to the Projects page
2. Click on the name of the specific project
3. Switch to the Project settings tab
4. Set billable rate for the project

**To set different pricing per client at the project level:**

1. Create different projects
2. Assign them to respective clients
3. Go to Projects and click the project name (which will bring you to Project edit page)
4. Switch to the Project Settings tab
5. Set the desired billable rate for the project.
6. Repeat for each project for the specific client

## Filter and sort projects [\#](#filter-and-sort-projects)

When you have a lot of projects, it can be difficult finding what you need. That’s when filters come in handy.

You can filter projects by their active status, client, users who are part of it, billability, and name.

You can sort projects alphabetically by clicking **Name** on the header of the project table. It is possible to sort projects by Client and Status as well.

## Create project from a template [\#](#create-project-from-a-template)

If you have a lot of similar projects, it’s a good idea to set up a template so you don’t have to create the same project over and over.

Projects you create with an existing template will have settings such as Billable Rates, Estimates, Tasks and Team already applied.

[Project templates](https://clockify.me/help/projects/project-templates) are a paid feature, which you can enable once you upgrade your account.

## Add and edit tasks in a bulk [\#](#add-and-edit-tasks-in-a-bulk)

Admins and owners can add and edit multiple tasks to multiple projects in a bulk. This option is available with all paid subscription plans.

After selecting projects, user can modify visibility, access, client, color, billability and tasks in the **Bulk edit** screen. 

![](https://clockify.me/help/wp-content/uploads/2022/12/Screenshot-2022-12-30-at-11.35.57-556x1024.png)
By modifying tasks, user can be adding and editing the tasks in the selected projects.   
If the **Add to existing** option is selected, user is adding a task to all the selected projects. Up to 20 tasks can be added.   
If the **Overwrite existing** option is selected, user is deleting all active and completed tasks in the selected projects and adding the newly created tasks.

After all the changes are saved, the newly added tasks will be visible in the task list in the alphabetical order. 

## Manage clients [\#](#manage-clients)

By default, **owners** and **admins** can create clients. However, this set of permissions can be modified if **Who can create projects and clients** is set to **Admins and managers** or **Anyone** in the **Workspace settings**.

![](https://clockify.me/help/wp-content/uploads/2022/05/image.png)
Who can create clients if selected:

* **Admins** (default): admins
* **Admins and project managers**: admins and project manager
* **Anyone**: admins, projects managers, team managers, regular users

Regular users will be able to create clients when they create a new project. However, they still won’t be able to see the **Clients** page.

### How owners and admins can create clients [\#](#how-owners-and-admins-can-create-clients)

If you’re the owner or an admin of the workspace, to create a client simply:

1. Go to **Clients** page from sidebar
2. Enter the client’s name in the **Add new client** field
3. Click **Add**

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-20-at-10.15.22-1024x293.png)
### How project managers can create clients [\#](#how-project-managers-can-create-clients)

Project managers can create clients from the project picker when creating new time entry:

1. Start tracking time from the **Time tracking** page
2. Click the **\+Project** button to create new project
3. In **Create new project** screen:
	* Enter project name
	* Select client name, or add new:
		* Type client name in the search field
		* Click **Add \<client\_name\>** client  
		or
		* Use **Ctrl /** **^ (Control) \+ Enter** shortcut

![](https://clockify.me/help/wp-content/uploads/2018/01/Screenshot-2024-06-20-at-10.01.29.png)

### How regular users can create clients [\#](#how-regular-users-can-create-clients)

If you want **regular users** to be able to add clients:

1. Admin or owner needs to set **Who can create projects and clients** to **Anyone**
2. A regular user can then go to the **Projects** page to create a project
3. Click **Select client**
4. Enter client name
5. Click **Create client** or press **Ctrl / ^ (Control) \+ Enter**

If you want to create a client only, simply create the client with the mentioned steps above and cancel the project creation.

![](https://clockify.me/help/wp-content/uploads/2018/01/Screenshot-2025-05-30-at-09.39.39-1024x488.png)
### How to edit already existing clients [\#](#how-to-edit-already-existing-clients)

1. Go to the **Clients** page from the sidebar
2. Click the pen icon for the Client you’d like to edit
3. Edit: **Client Name**, **Client Address**, **Client Note** (An additional note related to the client such as the most important information, instructions, links to important document and much more), **[Currency](https://clockify.me/help/track-time-and-expenses/multiple-currencies#assign-currency-to-client)**

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-20-at-16.00.30-658x1024.png)
## Archive clients [\#](#archive-clients)

Only owners and admins of the workspace can archive clients. Only after the client is archived you will be able to delete it. 

1. Go to Clients page from sidebar
2. Click on three dots next to the client’s name
3. Choose Archive
4. Confirm the action in the pop\-up window. There you will also have the option to archive all projects assigned to that client

### Delete clients [\#](#delete-clients)

 Only owners and admins of the workspace can delete clients. Clients can only be deleted after being archived**.** 

1. Go to Clients page from sidebar
2. Select Show archived or Show all from the drop\-down menu
3. Click on three dots next to the archived client’s name
4. Choose Delete
5. Confirm the action

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
