---
title: "Targets & reminders"
url: "https://clockify.me/help/administration/targets-reminders"
category: "administration"
slug: "targets-reminders"
---

# Targets & reminders

* [Set up timesheet reminders](#set-up-timesheet-reminders)
* [Emails for admins and managers](#emails-for-admins-and-managers)
* [Edit reminders](#edit-reminders)
* [Key considerations](#key-considerations-)

# Targets \& reminders

5 min read

In Clockify, you can set time tracking targets for your team, ensuring they stay on top of their daily, weekly, and monthly hours. If a team member doesn’t meet their target or logs more time than needed, they will automatically receive an email reminder.  
Managers and admins can also get notified on a daily, weekly, or monthly basis about team members who have missed their targets or tracked too much time.

Targets and reminders is a paid feature, which you can enable by [upgrading](https://clockify.me/pricing) to Standard, Pro, or Enterprise plan.

There are also **You forgot to start the timer** [reminders](https://clockify.me/help/track-time-and-expenses/idle-detection-reminders#reminders), which you can enable inside [time tracking apps](https://clockify.me/apps) (desktop app and browser extension, free feature).

![](https://clockify.me/help/wp-content/uploads/2018/08/Screenshot-2025-03-07-at-09.57.12-1024x234.png)
### Types of reminders [\#](#types-of-reminders)

1. **User reminders** notify individual users if they haven’t tracked enough hours for a specified period (daily/weekly/monthly)
2. **Manager/Admin/Owner reminders** inform team managers, admins and owners when any workspace member misses their target hours

## Set up timesheet reminders [\#](#set-up-timesheet-reminders)

As an owner or admin, you can configure reminders for your users on the **Team page** \> **Reminders tab**.   
Here’s how to customize them:

1. Choose **Their work capacity** to set reminders based on each user’s individual work capacity (calculated automatically)
2. Select **Custom time** to set a fixed target of hours   
You can define the target hours for each user for daily, weekly, or monthly tracking.

![](https://clockify.me/help/wp-content/uploads/2018/08/Screenshot-2025-03-07-at-10.00.41-1024x258.png)
Once configured, Clockify will automatically send reminder emails when a team member doesn’t meet their target or logs more than the target number of hours.

### **Customize reminder settings**

For **Daily**, **Weekly**, and **Monthly** reminders:

* **Period selection**: When setting reminders, you can select the time period (Daily, Weekly, Monthly)
* **Target type**: Choose whether reminders are based on the user’s work capacity or a custom\-defined time target. If custom time is selected, you will be prompted to enter a specific number of hours.
	* **Defaults**:
		* Daily: 8 hours
		* Weekly: 40 hours
		* Monthly: 160 hours
	* **Adjustable limits**: The field for custom hours has a minimum of 0 hours and a maximum of:
		* Daily: 24 hours
		* Weekly: 168 hours
		* Monthly: 744 hours

### User\-specific reminders [\#](#user-specific-reminders)

* **Daily reminders**: If you’ve set **Day**, team members will receive the reminder email the following day (you can choose workdays for when people have to fulfill their targets)
* **Weekly reminders**: If you’ve configured a weekly reminder, team members will receive the notification on the first day of the next week ([week start](https://clockify.me/help/getting-started/clockify-glossary#week-start)). The default start day of the week can be set by the Owner or Admin in the Workspace settings under the **Week start** section. However, individual users can have their own Week start adjusted if the Owner or Admin updates their settings on the [Team page \> Edit profile](https://clockify.me/help/administration/edit-profiles).  
*For example, if Monday is set as the default start day but your first working day is Wednesday, reminders will be scheduled starting from Wednesday, aligning with your personal schedule. The reminder system will always use the user’s specific information. To ensure consistency, it’s a good idea for users to coordinate their start days, times, and time zones if possible.*
* **Monthly reminder**: If you’ve set a **Month**, team members will receive the reminder email on the first day of the next month

![](https://clockify.me/help/wp-content/uploads/2018/08/Screenshot-2025-03-07-at-10.08.48.png)
You can set up multiple reminder rules for each user or group (e.g. 7 hours per day minimum, but 40 hours per week and 150 hours per month).

**User groups for bulk reminders**

To save time, you can allocate users to [groups](https://clockify.me/help/administration/user-groups). This allows you to assign reminders to multiple people at once instead of selecting each user individually.

**Time off and holidays**

There are no reminders during time off. Users on holidays or who have approved time off will not receive reminders for the days they’re absent.

Users who haven’t verified their email address won’t receive reminders.

## Emails for admins and managers [\#](#emails-for-admins-and-managers)

If you wish to receive an email when someone forgets to log their time or they log too much time, click on a reminder’s **Them** option, and select who also needs to receive the email (admin, team manager). 

![](https://clockify.me/help/wp-content/uploads/2023/11/Screenshot-2023-11-28-at-11.59.19.png)
The reminders for them will include:

* **Missed targets**: When a team member’s tracked time is below the target, it will appear in red text in the email
* **Summary email**: All daily, weekly, and monthly reminders for team members can be included in one email
* **Customized notes**: The subject and email body will include a note with details about the specific time off taken by the user

![](https://clockify.me/help/wp-content/uploads/2018/08/Screenshot-2025-03-07-at-10.10.37.png)
## Edit reminders [\#](#edit-reminders)

To edit a reminder simply click on the highlighted section (users, hours, etc.).

## Key considerations [\#](#key-considerations)

* **Time off calculations**: When a user requests time off (daily, half\-day, or hourly), the system recalculates their available capacity. If the user has taken time off, their recalculated work capacity will be used for reminders.
	* **Full day off**: The daily work capacity is set to 0 hours
	* **Half day off**: The daily work capacity is halved
	* **Hourly off**: The work capacity is reduced based on the approved hours
* **Non\-working days**: If a user is on a holiday or non\-working day, no reminders will be sent for that day.
* **Custom time target**: If you set a custom time target, this will not be recalculated by the system, except for holidays, non\-working days, or approved time off.

### **Double time off requests**

To prevent double time off requests, the system checks for overlapping requests:

* **For the same user**: A warning will appear if a time off request overlaps with an existing pending or approved request
* **For another user**: A warning will appear if a time off request overlaps with another user’s request

No reminders will be sent for weekends, holidays, or time off (whole days, half\-days, or hourly policies).

In cases where tracked time is compared to the defined target, the email notifications will include a note indicating the time off taken that day

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
