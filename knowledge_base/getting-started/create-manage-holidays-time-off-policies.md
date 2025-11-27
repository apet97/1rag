---
title: "Create & manage holidays & time off policies"
url: "https://clockify.me/help/getting-started/getting-started-as-admin-and-workspace-owner/create-manage-holidays-time-off-policies"
category: "getting-started"
slug: "create-manage-holidays-time-off-policies"
---

# Create & manage holidays & time off policies

* [Enable time off](#enable-time-off)
* [Create and manage time off policies](#create-and-manage-time-off-policies)
* [Manage non\-working days](#manage-non-working-days)
* [Create and manage holidays](#create-and-manage-holidays)
* [Archive and delete policies](#archive-and-delete-policies)
* [Edit and delete policies](#edit-and-delete-policies)
* [View and track time off](#view-and-track-time-off)
* [FAQ](#faq)

# Create \& manage holidays \& time off policies

8 min read

This guide will walk you through how to create, manage, and configure time off policies and holidays in your workspace. As a Workspace Admin or Owner, you have full control over these settings, ensuring that your team’s time off is accurately tracked and managed.

## Enable time off [\#](#enable-time-off)

To start managing holidays and time off policies, you first need to enable the Time Off feature in your workspace.

To enable time off:

1. Click the **three\-dot menu** at the top left of your workspace
2. Select **Workspace settings** from the dropdown
3. Scroll down to the **Time off** section
4. Enable **Time off** by checking the box
5. Enable the option to let **Regular users see Time off outside their teams** if needed (optional)

Once enabled, you can create time off policies that fit your workspace’s needs.

## Create and manage time off policies [\#](#create-and-manage-time-off-policies)

Time off policies determine how your team can request and track different types of leave, such as vacation days, sick leave, or personal time off.

To create or manage time off policies:

1. From the sidebar, click on **Time off**
2. Click on the **Settings icon** (gear symbol) on the top\-right of the **Time off** page
3. Select **Manage policies** to create or edit your time off policies

Key fields to define:

* **Assignee**: Choose the members who are eligible to request time off under this policy
* **Time unit**: Define whether the time off is tracked in **days** (e.g., vacation) or **hours** (e.g. banked hours)
* **Requires approval**: Choose whether time off requests require managerial approval. If unchecked, requests will be auto\-approved
* **Balance expiry**:
	* **Never expires**(default) – Balance for this policy won’t have a start or end date and won’t expire.
	* **Has expiry dates** – Accrual and every balance for this policy need to have a startand end date defined.
* **Automatically accrues**: Enable this option to automatically add days or hours to team members’ balances monthly or yearly
* **Start/end date** – Define timeframe during which defined balance can be used
* **Allow negative balance**: Allow employees to request time off even if they have a negative balance (e.g. for sick leave). Optionally, limit the amount of negative balance.  
****Please note that new days added to a balance will not automatically clear a negative balance. They will simply be added to the total amount available.****
* **Allow half day**: If time off policy is calculated in days, you can let people ask for a half\-day leave, choose the first or second half of a day off, even across multiple days
* **Hours**: If time off policy is calculated in hours, you can let people ask for multiple hours off across multiple days
* **Automatically create time entries**: Enable this to automatically track time off requests under the chosen project, including billable hours

## Manage non\-working days [\#](#manage-non-working-days)

Non\-working days (holidays and weekends) can be defined and customized in your workspace settings.

To manage non\-working days:

1. Go to the **Time Off** page.
2. Click on the **Settings icon** and choose **Manage Holidays**.
3. By default, **Saturdays and Sundays** are marked as non\-working days. You can change this by customizing the working days in the **Workspace settings**

## Create and manage holidays [\#](#create-and-manage-holidays)

You can create multiple holidays, customize them, and assign them to specific users or groups.

To create and manage holidays:

1. On the **Time off** page, click the **Settings** icon
2. Select **Manage holidays** from the dropdown menu
3. Define your holiday details:
	* **Holiday name**: Name your holiday (e.g. New Year’s Day)
	* **Assigned members**: Choose which users or groups are eligible for this holiday
	* **Annually occurring**: Choose whether this holiday should repeat annually
	* **Holiday color**: Select a default color or create a custom color for this holiday

To edit or delete holidays:

1. Navigate to the **Time off** page
2. Click the **three dots** next to the holiday you want to edit
3. Select **Edit** or **Delete**
	* Editing allows you to change holiday details like name, assigned users, and color
	* Deleting will permanently remove the holiday from the system

When an employee requests time off, holidays and weekends are excluded from the total time off. 

For example: *If someone requests leave from Jan 1 to Jan 7, and Jan 1 is a holiday, Jan 2 is a Saturday, and Jan 3 is a Sunday, their request will be reduced to 4 days of time off.*

## Archive and delete policies [\#](#archive-and-delete-policies)

You can archive or delete outdated policies, such as old vacation policies or specific leave policies no longer in use.

To archive or delete policies:

1. Go to the **Time off** page
2. Click the **three dots** next to the policy you want to archive or delete
3. Choose **Archive** to remove it from the active policy list (it will not affect balances or requests)
4. If you need to permanently remove a policy, you can delete it after archiving

Deleting a policy removes all requests and balances associated with that policy.

## Edit and delete policies [\#](#edit-and-delete-policies)

If you need to make changes to an existing policy, you can edit its details.

To edit a policy:

1. On the **Time Off** page, click the **three dots** next to the policy
2. Choose **Edit** to update the policy name, members, accrual rules, manage time off balance or other details

### Manage time off balance

Clockify also allows you to manage when and how time off balances can be used by your team members.

**Set policy expiration**

You can define if the balance for a specific time off policy **expires** or **never expires**. This setting affects all users under that policy.

1. Go to **Time off** page and open **Manage policies** in **Settings**
2. Click **Edit**next to the policy you want to change
3. Go to the **Balance expiry** section and choose one of two options:
	* **Never expires** (default)  
	Balance doesn’t have expiry date
	* **Has expiry dates**  
	All future accruals and balances for this policy require defined **start** and **end** date

**Important to note**:

* If you switch policy to **Never expires**, all existing start and end dates on user balances will be removed
* If you switch policy to **Has expiry dates**, all existing balances get a start date of today and all future balances will require a start and end date

When a user requests time off, Clockify always deducts days from the balance that is expiring soonest.

### Delete time off policy [\#](#delete-time-off-policy)

To delete a policy:

1. Follow the same steps as for editing a policy
2. After archiving, select **Delete** to permanently remove the policy from the system

## View and track time off [\#](#view-and-track-time-off)

Once you have set up your time off policies and holidays, you can track your team’s time off requests on the **Timesheet**, **Calendar**, **Time off**, and **Schedule** pages.

**Policy and holiday colors**: The colors you’ve defined for policies and holidays will appear throughout these pages, making it easy to identify types of leave.

## FAQ [\#](#faq)

#### Can I have different policies for different types of leave (vacation, sick leave, etc.)?

Yes, you can create multiple time off policies and assign them to different members or groups based on the type of leave.

#### What happens if I delete a policy?

Deleting a policy will permanently remove all requests, balances, and approvals associated with that policy. Make sure to archive outdated policies if you want to keep the data intact.

#### Can users see each other’s time off requests?

**Admins** can view all time off requests. **Team managers** can view time off for their team members. **Regular users** can only view their own time off, unless the setting **Allow regular users to see time off outside their teams** is enabled.

#### How are holidays treated in time off requests?

Holidays and weekends are automatically excluded from the total time off. If an employee requests time off over a holiday or weekend, those days are not counted toward their leave balance.

#### How do I assign a holiday to specific people?

When creating or editing a holiday, you can assign it to specific users or groups. This allows you to set different holidays for different members (e.g. national holidays for one group, but not another).

#### Can I approve or reject time off requests for my team?

Yes, as an Admin or Team manager, you can approve or reject time off requests for the users assigned to you.

#### Can I track time off across multiple days?

Yes, if your time off policy is set to **days**, you can allow half\-day leave across multiple days. If it’s set to **hours**, you can allow hourly requests across multiple days.

#### Can I set up automatic accrual for time off policies?

Yes, you can configure time off to automatically accrue on a monthly or yearly basis for all team members covered by the policy.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
