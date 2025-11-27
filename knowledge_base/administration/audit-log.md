---
title: "Audit log"
url: "https://clockify.me/help/administration/audit-log"
category: "administration"
slug: "audit-log"
---

# Audit log

* [Enable audit log](#enable-audit-log)
* [Run audit](#run-audit)
* [Filter logs](#filter-logs)
* [Previous and new value of 'update' events](#previous-and-new-value-of-update-events)

# Audit log

4 min read

Record every activity within your workspace and get a comprehensive record of actions, users that initiated them and timestamps for easy reference later on.

Audit log is a paid feature, which you can enable by [upgrading](https://clockify.me/pricing) your workspace to the ENTERPRISE plan.

## Enable audit log [\#](#enable-audit-log)

To start recording actions:

1. Open the menu next to the workspace name
2. Choose **Workspace settings**
3. Activate audit log
4. Select change you wish to record (change to time entries, projects, clients, tags)

For example, if you check time entries, you’ll get a record in audit log whenever someone creates a new time entry, edits their existing entry, or deletes it. 

Audit log also records cascade changes. For example, if you have a time entry on some project, and that project is updated (e.g. it’s renamed or deleted), you’ll get a record log for both **Project updated** and for **Time entry updated**. This only happens if you record both changes in workspace settings. For example, if you record changes to time entries but not to projects, you won’t get a record in audit log when a project is updated.

## Run audit [\#](#run-audit)

1. Open the menu next to the workspace name
2. Choose **Workspace settings** \> **Audit** tab
3. Choose date
4. Choose author
5. Choose actions
6. Click **Run report**

Once you get the report, you can review events in the table (timestamp, author, and action), and expand for more details.

You can also export audit log as a CSV file and analyze it in Excel or some other program. 

Because audit log files can be huge, it takes a while to generate them. You can wait and download it once it’s finished, or you can choose to receive it via email within half an hour.

Audit logs older than 1 year are automatically deleted (due to their enormous size). We recommend exporting them each month and storing them personally for archive purposes.

![](https://clockify.me/help/wp-content/uploads/2024/06/audit_log_running_report-1024x487.png)
## Filter logs [\#](#filter-logs)

You can filter audit log by: 

### Actions [\#](#actions)

Actions dropdown contains a list of actions grouped by entity type: time entry, project, task, client, tag, expenses.

| **TIME ENTRY** | **PROJECT** | **TASK** | **CLIENT** | **TAG** | **EXPENSES** |
| --- | --- | --- | --- | --- | --- |
| Created time (personal, timer) | Created project | Created task | Created client | Created tag | Created expense (personal) |
| Created time (personal, manual) | Created project (import) | Created task (import) | Created client (import) | Created tag (import) | Created expense (for other) |
| Created time (import) | Created project (QuickBooks) | Updated task (personal) | Created client (QuickBooks) | Updated tag | Restored expense (personal) |
| Created time (kiosk) | Updated project | Updated task (for other) | Updated client | Deleted tag | Restored expense (for other) |
| Created time (for other) | Deleted project | Deleted task | Deleted client |  | Updated expense (personal) |
| Restored time (personal) |  |  |  |  | Updated expense (for other) |
| Restored time (for other) |  |  |  |  | Deleted expense (personal) |
| Updated time (personal) |  |  |  |  | Deleted expense (for other) |
| Updated time (for other) |  |  |  |  |  |
| Deleted time (personal) |  |  |  |  |  |
| Deleted time (for other) |  |  |  |  |  |

### Authors (users) [\#](#authors-users)

Authors are all active or archived workspace users.   
Check **System** if you’d like to see activities logged by the app.

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-05-at-10.57.37.png)
### Date [\#](#date)

Filter logs by date. Open date picker and choose date range. 

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-05-at-11.25.49-1024x507.png)
Maximum date range is 30 days.

## Previous and new value of ‘update’ events [\#](#previous-and-new-value-of-update-events)

‘Update’ events in Audit log contain more details about what has been updated on your workspace (e.g. project name change, setting up billable rate, added estimate…). Once you expand the event on the Audit log page in the report you run, you’ll get more information about the ‘update’ event in question.

![](https://clockify.me/help/wp-content/uploads/2024/06/expand_update_event-1024x525.png)

‘Update’ event: rename project

We recommend enabling Audit log from the moment you start using Clockify. This way, you will always have previous and new value of all your ‘update’ events. If you use Clockify and enable Audit log for some object later, you might not have access to the previous value because it wasn’t recording events at that moment.

*For example, if you create a time entry while audit log is off, and you later enable it and you update the same entry, audit log will show that it’s been updated but you won’t be able to compare the previous and new value. However, if you update that entry again, audit log will show both the previous edit as previous value and what exactly has been updated in the new value.*

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
