---
title: "Approve entries & time off requests for Workspace members"
url: "https://clockify.me/help/getting-started/getting-started-as-admin-and-workspace-owner/approve-entries-time-off-requests-for-workspace-members"
category: "getting-started"
slug: "approve-entries-time-off-requests-for-workspace-members"
---

# Approve entries & time off requests for Workspace members

* [Key concepts](#key-concepts)
* [Access permissions](#access-permissions)
* [Configure approval permissions](#configure-approval-permissions)
* [Approve time entries](#approve-time-entries)
* [Approve time off requests](#approve-time-off-requests)
* [Manage Team and Project manager roles](#manage-team-and-project-manager-roles)
* [Send reminders to approve time entries](#send-reminders-to-approve-time-entries)
* [Notifications for time entries \& time off requests](#notifications-for-time-entries-&-time-off-requests)
* [FAQ](#faq)

# Approve entries \& time off requests for Workspace members

10 min read

As a Workspace Admin or Owner, managing time entries and time off requests is crucial to make sure that team members’ time is accurately tracked, and that planned absences are accounted for. This guide will walk you through the process of approving time entries and time off requests, including how to edit, reject, and send reminders.

## Key concepts [\#](#key-concepts)

* **Time entries**: Hours tracked by team members for their work on various projects or tasks
* **Time off requests**: Requests submitted by employees to take time off, such as vacation or sick leave
* **Approval workflow**: The process by which you review and either approve or reject time entries and time off requests

## Access permissions [\#](#access-permissions)

* **Workspace Admins and Owners** can approve, reject, and edit time entries and time off requests for all team members
* **Team managers** (if enabled) can approve, reject, and edit the time entries and requests for users they manage
* **Project managers** (if enabled) can approve or reject time entries and time off requests for team members working on their assigned projects

## Configure approval permissions [\#](#configure-approval-permissions)

To configure approval permissions for your workspace:

1. Navigate to **Workspace settings** \> **Permissions** tab
2. In the **Who can approve submitted timesheets and expenses** section, choose:
	* **Admins \& Team managers**: Team members can approve time entries for users they manage
	* **Admins \& Project managers**: Project managers can approve time entries for users on their assigned projects

If a user has both Admin and Manager roles, the Admin role will override the other roles. For example, an Admin who is also a Team Manager will have the permissions of both roles.

## Approve time entries [\#](#approve-time-entries)

To approve or reject time entries:

1. Go to the **Approvals** page in your dashboard
2. In the **Pending tab**, you’ll see time entries waiting for approval. Each entry will show the **author**, **time**, and **status** (e.g. pending, approved, rejected)

### Review time entries [\#](#review-time-entries)

Each time entry will include:

* **User name**: Team member who submitted time
* **Project and task**: Project or task to which the time is assigned
* **Logged time**: Number of hours worked
* **Description**: Notes or description provided by the team member

You can filter the entries by user, group, or date range to make it easier to review.

### Approve or reject time entries [\#](#approve-or-reject-time-entries)

* **Approve time entry**: If everything looks good, click the **Approve** button. The entry will be marked as approved and locked.
* **Reject time entry**: If there are issues with the entry (e.g. incorrect hours), click **Reject**. A prompt will ask you to leave a rejection note. The user will be notified of the rejection via email.

### Bulk approve or reject time entries [\#](#bulk-approve-or-reject-time-entries)

To approve or reject multiple time entries at once:

1. **Select the checkboxes** next to the entries you wish to approve or reject
2. Click the **Approve** or **Reject** button at the top of the page to apply your action to all selected entries

### Bulk submit entries for others [\#](#bulk-submit-entries-for-others)

Submit multiple unsubmitted timesheets from other users at once. 

1. Go to the **Approval** page and choose the **Unsubmitted** tab
2. Check the boxes next to the timesheets you’d like to submit
3. Or the box at the top of the column to select all timesheets in that submission period
4. Click **Submit** to confirm the action in the popup window

### Edit pending time entries [\#](#edit-pending-time-entries)

Admins can edit any user’s pending time entries directly. Team managers can only edit pending time entries for their team members.

To edit a pending time entry:

1. Go to the **Pending** tab on the **Approvals** page
2. Click on the **edit pen icon** next to the time entry
3. In the **Edit time entry** screen, make the necessary changes:
	* Adjust **time and date**
	* Edit the **description** or **project/task**
	* Change the **billability** status

After making the necessary changes, click **Save** to finalize the change.

### Approval notifications [\#](#approval-notifications)

* The **user** will receive an email notification when their time entry is approved
* The **manager** will be notified when a time entry is submitted for approval
* **Admins** will be notified when a user submits their timesheet (if they have the necessary Manager role for that user)

## Approve time off requests [\#](#approve-time-off-requests)

Time off requests can be approved through the **Requests tab** under the **Time Off** page.

**Filter** requests by **status** (pending, approved, rejected), by **group** or a specific **team member** or by a **time range**.

Each request will show:

* **Team member**: The employee requesting time off
* **Period**: The start and end dates of the requested time off
* **Requested time**: Number of requested days/hours
* **Policy**: Policy under which the request has been submitted
* **Status**: Pending, approved, or rejected

When you request a time off, the app checks your available balance. If you have insufficient leave, the request will appear in red and cannot be approved until the balance is adjusted.   
If negative balance is enabled, Clockify will display the number of negative days or hours allowed. If the request exceeds this limit, you won’t be able to submit it. 

### Approve or reject time off requests [\#](#approve-or-reject-time-off-requests)

To approve or reject a time off request:

1. Go to the **Time off** page
2. Find/filter out pending time off request in the **Requests** tab
3. Click **Approve** or choose **Reject** from the three\-dots menu
	* If you reject the request, leave a **note** to explain the reason
	* The user will receive an email notification if their request is approved or rejected

Or open the email you received after the request has been submitted and approve/reject. 

### Reject previously approved time off requests [\#](#reject-previously-approved-time-off-requests)

If you need to reject a previously approved request (e.g. due to a scheduling conflict), you can do so by:

1. Find/filter out the request in the **Requests** tab
2. Click **Reject** and leave a rejection note

The user will be notified of the rejection via email.

### View time off in timeline [\#](#view-time-off-in-timeline)

To get a quick overview of upcoming time off for your team, use the Timeline view:

1. Go to the **Time off** page
2. Select the **Timeline** tab

The timeline shows a **30\-day** view of all upcoming leaves, with each entry marked by the color of its time off policy.

You can customize the colors for approved, pending, and holiday time off.

## Manage Team and Project manager roles [\#](#manage-team-and-project-manager-roles)

As an Admin, you can assign **Team manager** or **Project manager** roles to team members, allowing them to approve time entries and time off requests for their team or project members.

To assign a manager role:

1. Go to the **Team** page
2. Find the user you wish to assign a manager role to and click **\+ Role**
3. Select **Team manager** or **Project manager**
	* For Team managers, select the **users/groups** they will be responsible for
	* For Project managers, select the **projects** they will manage

Click **Save** to confirm the role assignment.

Once a user has a manager role, they will have access to the **Approvals page** to manage timesheets and time off requests for their assigned team or project.

## Send reminders to approve time entries [\#](#send-reminders-to-approve-time-entries)

As an Admin, you can send reminders to Team or Project managers who have pending time entries to approve.

To send reminders:

1. Go to the **Approvals** page
2. If there are pending time entries for users assigned to a Team or Project manager, the **Remind to approve** button will be enabled
3. Click **Remind to approve** to send an email reminder to the respective managers to approve their team members’ time entries

## Notifications for time entries \& time off requests [\#](#notifications-for-time-entries-time-off-requests)

* **Time entry submitted**: Users are notified when their time entry is submitted for approval
* **Time entry approved**: Users are notified when their time entry is approved
* **Time entry rejected**: Users receive an email with a note explaining why their time entry was rejected
* **Time off submitted**: Users are notified when their time off request is submitted
* **Time off approved**: Users are notified when their time off request is approved
* **Time off rejected**: Users receive an email with a note explaining why their time off request was rejected
* **Approval withdrawn**: If an approval is withdrawn, both the user and the Admins will be notified via email

Approved time entries can be withdrawn, but once you approve a time off request, it cannot be withdrawn.

## FAQ [\#](#faq)

#### Can I approve multiple time entries at once? [\#](#can-i-approve-multiple-time-entries-at-once)

Yes, you can approve or reject multiple time entries simultaneously:

1. On the **Approvals** page, select the checkboxes next to the time entries you wish to approve or reject
2. Click **Approve** or **Reject** at the top of the page to apply your action to all selected entries

#### Can I edit a time entry after it has been approved? [\#](#can-i-edit-a-time-entry-after-it-has-been-approved)

No, once a time entry is approved, it is locked and cannot be edited. However, as an Admin, you can **withdraw approval**, make edits, and then re\-approve the entry.

#### How can I view all team members’ time off for better planning? [\#](#how-can-i-view-all-team-members-time-off-for-better-planning)

You can view team members’ scheduled leaves in the **Timeline** tab:

1. Go to the **Time off** section
2. In the **Timeline**, you can view leaves for the next **30 days** or choose a custom time range
3. Approved time off is marked **green**, pending requests are **orange**, and holidays are **gray**

#### Can I reject a time off request after it’s been approved? [\#](#can-i-reject-a-time-off-request-after-its-been-approved)

Yes, you can reject a previously approved time off request:

1. Click on the approved request in the **Requests** tab
2. Click **Reject** and providing a **rejection note**
3. The employee will receive a notification via email explaining why their request was rejected.

#### How are users notified when their time entries or time off requests are approved or rejected? [\#](#how-are-users-notified-when-their-time-entries-or-time-off-requests-are-approved-or-rejected)

* For time entries:
	* **User** receives an email when their time entry is approved or rejected
	* **Manager** receives notification when time entries are submitted for approval
* For time off requests:
	* **User** receives an email notification when their time off request is approved or rejected
	* **Manager** receives notification when a time off request is submitted

#### Can a user edit their own time entry after submission? [\#](#can-a-user-edit-their-own-time-entry-after-submission)

No, users cannot edit their own time entries once submitted. Only Admins and managers with the appropriate permissions can edit or approve time entries. If a user needs changes, they can ask a manager to edit it on their behalf.

#### What should I do if a user claims they submitted a time entry, but I can’t find it? [\#](#what-should-i-do-if-a-user-claims-they-submitted-a-time-entry-but-i-cant-find-it)

Check if the user might have submitted their time in a **different workspace**. Each user has their own personal workspace, and sometimes they may accidentally track time there instead of the correct workspace. As an Admin, you can check their personal workspace to see if the time was logged there.

#### Can I customize the colors for time off requests on the timeline? [\#](#can-i-customize-the-colors-for-time-off-requests-on-the-timeline)

Yes, you can customize the colors for approved, pending, and holiday time off:

1. Go to the **Time off** policy settings
2. When creating or editing a policy, you can change the colors for approved requests (green), pending requests (orange), and holidays (gray)

#### What happens if I reject a time entry by mistake? [\#](#what-happens-if-i-reject-a-time-entry-by-mistake)

If you accidentally reject a time entry, you can ask the user to resubmit it. Alternatively, as an Admin, you can manually edit the time entry and approve it again.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
