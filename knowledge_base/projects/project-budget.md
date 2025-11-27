---
title: "Track budget & estimates"
url: "https://clockify.me/help/projects/project-budget"
category: "projects"
slug: "project-budget"
---

# Track budget & estimates

* [Define project budget](#define-project-budget)
* [Recurring estimates](#recurring-estimates)
* [Estimates in reports](#estimates-in-reports)
* [Permissions](#permissions)

# Track budget \& estimates

4 min read

If you have fixed fee projects, you can track their progress and see how much of the budget was spent by setting estimates in monetary terms. You’ll also get alerts when you’re about to go over budget.

Project budget is a paid feature you can enable by [upgrading](https://clockify.me/pricing) your workspace to Pro or Enterprise plan.

![](https://clockify.me/help/wp-content/uploads/2024/03/project-budget-11.png)
## Define project budget [\#](#define-project-budget)

To set project budget: 

1. Go to the **Projects** page
2. Choose project and click on project’s **Settings** tab
3. In **Project estimate** section, select **Project budget**  
![](https://clockify.me/help/wp-content/uploads/2020/11/Screenshot-2024-06-13-at-16.20.50.png)
	* You can set an overall project budget using the **Manual** option
	* Or, you can choose **Task\-based** and then define budget for each individual task on the project (the project’s overall progress will always be the sum of all its task budgets).

When project budget is selected, project’s status tab and its progress bar will reflect the billable amount of each entry on the project vs the budget, and show you how much was spent and how much remains.

You can also choose to include billable expenses as part of project budget by enabling **Budget includes billable expenses**.

[Alerts](https://clockify.me/help/projects/alerts) always consider project status, and will be sent no matter if the project estimate is defined in time or budget.

## Recurring estimates [\#](#recurring-estimates)

If you have projects that have different budgets over different time periods, you can set the **Budget (or Estimate) resets** after the time period you set in the project’s Settings tab located below the estimate section.

**![](https://lh7-us.googleusercontent.com/iXXE0lQq4sduK-dhRU59CBQMZDjXzcW6tVQJ6ErcNBAA9mM_ckuDS3ftCjHTYVzBd8P_1HYFl7PruD-zcdoXYZNgQDrDhqbXJ7ZKs7dGRbbpneVhAH_tkmJI1DOqYXzpQZDX-1jWmnpOhKRby6IO_D4)**

Project estimate can be reset for one of these three periods: 

* Week (Monday is default week day)
* Month (default time period, 1st of the month is default day)
* Year (January is default month, 1st of the month is default day, 00:00 is default hour)

To set the estimate reset on a weekly/monthly/yearly basis: 

1. Go to **Projects** page in sidebar
2. Choose **Settings** tab
3. Navigate to **Project estimate** section
4. Turn the **Reset estimate every \<period\> on the \<date\> at \<time\>** switch on

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-13-at-16.26.02.png)
Now, when estimate resets after each \<week/month/year\>, on each \<date\> at each \<time\>, the progress bar for the project will return to 0%. 

This action can be performed by admins and owners and is available to project managers for the projects they are assigned to when **Who can see hourly rates and amounts** is set to **Anyone**. 

After you set the estimate period, it is applied to all previous time periods. Also, only time entries that belong to the currently set time period will be displayed in the **Tracked vs Estimated** section of the [project status](https://clockify.me/help/projects/tracking-project-progress).   
Alerts also take into consideration the reset option.

Time format in the estimate is the one set in the [Profile settings](https://clockify.me/help/administration/profile-settings).

If estimate reset is turned on: 

* Info about currency per time is defined in the **Project estimate**
* Reset period is specified on project and displayed when you hover over one project
* With **Task\-based estimate type**, **Time estimate**, **Project budget**, **Tracked**, **Amount**, **Status** and **Progress** are also reset
* Change is applied to **Alerts** and **Audit log**

## Estimates in reports [\#](#estimates-in-reports)

Only admins can see, share, and download estimates in reports.

To see estimates and budget for each project and task in the report: 

1. Open the **Summary report**
2. Turn **Show estimate** on

![](https://clockify.me/help/wp-content/uploads/2024/06/image-1.png)
Estimates and budget for each project and task are displayed next to tracked time.

You can also download the report with estimates via export, or share the estimate numbers when you share a report.

Exported files will have estimates only if the level of grouping is either **Project** or **Task**, or both. Also, keep in mind that the **Show estimate** switch needs to be turned on.

## Permissions [\#](#permissions)

Who can see budget depends on the permissions set in the **Who can see hourly rates** **and amounts** and **Who can see project status** in the Workspace settings. 

![](https://clockify.me/help/wp-content/uploads/2024/05/Screenshot-2024-05-27-at-08.41.50-1.png)

![](https://clockify.me/help/wp-content/uploads/2024/05/Screenshot-2024-05-27-at-08.42.39-1-1024x182.png)

If set to Admins:

* Only Admins can see and set project budget on all projects

If set to Anyone:

* Admins and Project managers\* can see and set project budget   
\**Project managers can set project budget if they can see billable rates*
* Regular users can only see project budget and progress of the project

For more information check out [Understanding user roles \& access permissions.](https://clockify.me/help/administration/user-roles-and-permissions/who-can-do-what)

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
