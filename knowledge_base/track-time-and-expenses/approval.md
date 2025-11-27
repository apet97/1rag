---
title: "Approve time & expenses"
url: "https://clockify.me/help/track-time-and-expenses/approval"
category: "track-time-and-expenses"
slug: "approval"
---

# Approve time & expenses

* [Approve time](#approve-time)
* [Approve expenses](#approve-expenses)
* [Reject submitted request](#reject-submitted-request)
* [Bulk approve/reject](#bulk-approve-reject)
* [Notifications](#notifications)

# Approve time \& expenses

8 min read

This article describes the process by which Admins and Managers review and approve tracked time entries and expenses submitted by team members. This way, time and budget spent on a project can be precisely estimated and allocated.

User interface displayed in this video may not correspond to the latest version of the app.

Approving **tracked time** is available on Standard and higher subscription plans and can be performed by workspace Admins, Project managers or Team managers.  
Approving **tracked expenses** is available on PRO and higher subscription plans and can be performed by workspace Admins, Project managers or Team managers.

*Imagine you are a project manager overseeing a team of developers working on a project for a client. Users working on a project submit tracked expenses during project\-related activities, such as software licenses or travel expenses. As the project manager, you review these submissions to make sure they align with project and task budgets and client agreements. Once approved, these entries are integrated into project reports and invoices, providing clients with the billing information.*

Depending on the permissions defined in the **Workspace settings**, submitted time \& expenses can be managed from the **Approvals** page in the following way:

* Admin: approve, reject, edit
* Team manager (if enabled): approve, reject, edit
* Project manager (if enabled): approve, reject

To modify these permissions:

1. Navigate to the [**Workspace** settings](https://clockify.me/help/track-time-and-expenses/workspaces#workspace-settings) \> **Permissions** tab
2. In the **Who can approve submitted timesheets and expenses** section choose:  
![](https://clockify.me/help/wp-content/uploads/2020/04/Screenshot-2024-07-22-at-12.35.36.png)
	* **Admins and team managers**  
	\*Team members can approve timesheets and expenses submitted by their team members
	* **Admins \& project managers**  
	\*Project managers can approve timesheets and expenses submitted by members assigned to the projects they manage.   
	  
	\*Admins can approve time for everyone.

If a user has Admin and any other manager role, Admin role will override every other role. If a user has both Project and Team manager roles, they will have a union of permissions that combine both of these roles.  

## Approve time [\#](#approve-time)

Each time approval request contains the following information: 

* Author of the submitted request
* Time of the submitted request
* Status:
	* Unsubmitted/Rejected
	* Pending
	* Approved

Whenever there’s a timesheet that’s waiting for approval, you’ll see an orange dot as an indicator in the sidebar.

**Pending** **tab**

Lists timesheets that are waiting for approval. You can approve all requests at once, or filter by user or group.

**Remind to approve**

If there are Team or Project managers that are supervising teams or project assignees, you, as an Admin, can click **Remind to approve** to send an email reminder to each Team or Project manager to approve their team members’ timesheets.  

To send managers reminder to approve:

1. Go to the **Approvals** page
2. If members have assigned Team or Project managers, **Remind to approve** button will be enabled
3. Reminder to approve submitted request will be sent to managers’ emails

To see a full timesheet, click on the request to see it in more detail.

### Edit pending time request [\#](#edit-pending-time-request)

Admins can edit other user’s pending requests directly from the **Pending** tab in the **Approvals** page.  
Unless time entries are locked, Team managers can edit their team’s pending requests. 

![](https://lh7-us.googleusercontent.com/vVYJ56dIjZ9lb18HQ_GGnQ4sfP24L_U3kona1L-lejvQ-xdV4ODGDpdKzdlQr-2mCjAr-fXYngyVDWACMKOt4vMIHixy_hP8Pt2hbp4XZRmtxU3svZMZykIzhv6542ohKcfExsGN0pKtuVjW6xcyVD4)
To edit pending request:

1. Go to **Approvals** page
2. In **Pending** tab, choose submitted timesheet
3. Click on edit pen icon next to time entry
4. In Edit time entry screen, you can edit the following:
	* Time and date
	* Description
	* Project
	* Billability
	* Duplicate/delete entry

![](https://lh7-us.googleusercontent.com/MftYJ1NLZYRF0yi9eIUfGh6VtBy_wpVF0I1u4vHwvGbGoFH1XY7hkkJXVAGYrxo-dxLUKxpyjxU3sfhHRRn8Xr6--Ty2jc2nsrgqED7qNq01mfrD6g3sngIQHprcGV_t9ycfhprIV0EHs-ku7rkXmi4)
After you’ve made all the necessary changes, click **SAVE** to complete the action.

### Assign manager role [\#](#assign-manager-role)

In addition to Admins, Team managers can also approve timesheets for the users they manage. Project managers can approve time for members working on the project they manage.

As an Admin, you can make person Team/Project manager:

1. Go to **Team** page
2. Click on **\+ Role** for the person you wish to make a manager
3. Check **Team / Project Manager**
4. For Team manager, select users/groups to whom they can view and approve timesheets  
![](https://clockify.me/help/wp-content/uploads/2020/04/Screenshot-2024-07-22-at-12.59.02.png)
5. For Project manager, select projects to view and approve timesheets for project assignees’  
![](https://clockify.me/help/wp-content/uploads/2020/04/Screenshot-2024-07-22-at-13.02.01.png)
6. Save changes

Once a person has [Team or Project manager](https://clockify.me/help/administration/user-roles-and-permissions/manager-role) role, they can see the **Approval** page in the sidebar with members/project visible to them. 

## Approve expenses [\#](#approve-expenses)

As is the case with approving time, if there is some expense waiting for approval, you’ll see an orange dot as an indicator in the sidebar.

If you’d like to submit the Expenses approval in the **Approvals** page:

1. Navigate to the **Approvals** page
2. Click the **Unsubmitted** tab

Here’s the list of all the unsubmitted expense approvals with the member’s name, total time, number of approved time off hours and total amount of expenses all grouped based on the time period. If you expand one and click on the unsubmitted expenses, you’ll be redirected to the **Timesheet** page with all the time entries that can be submitted. 

To continue the process: 

4. Click the **SUBMIT FOR APPROVAL**
5. Confirmation screen appears
6. Click **SUBMIT** to confirm the action

Once the expense has been approved, it cannot be edited in any way.

### Edit pending expenses [\#](#edit-pending-expenses)

Admins can edit other user’s expenses directly from the **Pending** tab in the **Approvals** page.  
Team managers can edit their team’s pending requests unless time expenses are locked.

To edit pending expense:

1. Go to **Approvals** page
2. Choose submitted timesheet in **Pending** tab
3. Click on edit icon
4. In **Edit expense** screen, edit the following:
	* Date
	* Project/Task
	* Category
	* Amount
	* Billability
	* Add/delete receipt
	* Delete request

![](https://clockify.me/help/wp-content/uploads/2024/05/edit_expenses-747x1024.png)
After you’ve made all the necessary changes, click **SAVE** to complete the action.

If the timesheet is waiting for approval, the **Approvals** item in the sidebar is marked with an orange dot.

## Reject submitted request [\#](#reject-submitted-request)

Rejecting a submitted request needs to be done on the **Approvals** page. 

To reject a request:

1. Go to the **Approvals** page, **Pending** tab
2. Open the request
3. Click **Reject** in the upper right corner
4. Leave a note  
![](https://lh7-us.googleusercontent.com/Kvwiqo-PrdODXggW0-m6MrOvMSeo-zD2eQjTHLEK5RATQi-Uu_xdKEz2KzPi8KYLH40W5OtMfH-CxDafXk5OXgZe2jSDdBY8GLJJqdHb5lRd3_pw1qVsBTjm93OLHGSjH7Dt1hMirlNriu_6SJhhlrM)
5. Click **Reject** to complete the action

As a result: 

* Approval request is deleted
* Pending label is removed
* User receives an email with a note elaborating on the reason for rejection

![](https://clockify.me/help/wp-content/uploads/2024/07/timesheet_rejected-1024x801.png)
If a member submitted a timesheet with entries that are wrongly submitted, you can: 

* Reject the entire timesheet then edit and resubmit the entry (as Owner/Admin, or their Team manager)
* Go to the [Detailed report](https://clockify.me/help/reports/detailed-report) and manually correct the mistake (only as Owner/Admin, or their Team manager)

Once you approve time, time entries are permanently locked. Even Admins can’t make any edits.

If you invoice time after approval and want to mark what’s been invoiced, you can import approved time entries into an [invoice](https://clockify.me/help/projects/invoicing) and approved time entries will automatically get an invoiced tag so you can see what’s been invoiced and filter reports by status.

If the start and end time include an overnight period, there will be a superscript number next to the end time, showing how many additional days the time entry covers.

## Bulk approve/reject [\#](#bulk-approve-reject)

In Clockify, you can approve multiple pending timesheets and expenses from the **Approval** page.

To perform bulk action: 

1. Go to the **Approval** page and choose the **Pending** tab
2. Check the boxes next to the timesheet you want to process  
You can choose multiple across different submission periods.
3. Click **Approve**/**Reject** button that appears

![](https://clockify.me/help/wp-content/uploads/2020/04/Screenshot-2025-11-06-at-14.03.13-1024x310.png)
Click **Approve** and then confirm the action in the pop\-up. 

![](https://clockify.me/help/wp-content/uploads/2020/04/image-2.png)
If you choose to reject, a pop\-up will appear requiring you to add a rejection note before confirming.

### Archive tab [\#](#archive-tab)

You can review all your approval history to see if all the required changes have been made. 

1. Go to the **Archive** tab under the **Approvals** page
2. Use the filter option above to **Show approved/rejected/withdrawn**
3. The Archive will display all previously submitted timesheets with that status

![](https://clockify.me/help/wp-content/uploads/2020/04/Screenshot-2025-11-06-at-13.50.08.png)
When you click on the timesheet marked **rejected**, you will see the **detailed view** that includes: 

* User name and submission period
* Date \& time of submission
* Timesheet details (time entries, expenses)
* Rejection comment explaining why timesheet wasn’t approved (if rejected)

## Notifications [\#](#notifications)

* User’s manager is notified if Timesheet is submitted
* User who submitted the timesheet is notified if Timesheet is approved
* User receives an email and note if Timesheet is rejected
* User and all the Admins receive an email if Approval is withdrawn

If you’re Admin and want to receive an email notification when a user submits their timesheet, you need to have a [Manager](https://clockify.me/help/administration/user-roles-and-permissions/manager-role) role for users you manage. This means that, for certain users, you’ll be:

* Admin and Team manager
* Admin and Project manager
* Team and Project manager
* Admin, Team and Project manager

In these cases, user role permissions encompass all permissions defined within that specific role.

You can send email reminders to both users to submit their unsubmitted timesheets, and managers to approve their team members’ timesheets.

![](https://lh7-us.googleusercontent.com/ZnrNIATr93x8jKZEyH6ZOEad3-dme_hwdFwTAPeZya6JtBlC7BTiJmHc1vi1dEz6ZG1tvgeUesh7XoW7_xfBdfVh-Suy7fO4LRROGhF6Z-JwymJBYDw3AGmS_70QmoTUxifp5YFqF3iND3dYqBhZBag)

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
