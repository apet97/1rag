---
title: "Lock timesheets"
url: "https://clockify.me/help/track-time-and-expenses/lock-timesheets"
category: "track-time-and-expenses"
slug: "lock-timesheets"
---

# Lock timesheets

* [Steps to lock timesheets](#steps-to-lock-timesheets)
* [Automatic lock](#automatic-lock)
* [How to set automatic lock](#how-to set-automatic-lock)
* [Lock today's time](#lock-todays-time)
* [Lock expenses](#lock-expenses)

# Lock timesheets

3 min read

You can prevent employees from editing their old time entries or adding new entries to past dates by locking timesheets. Once you lock timesheets, you can safely send your reports to your clients or accountant knowing the data will stay accurate.

Lock timesheets is a paid feature, which you can enable by [upgrading](https://clockify.me/pricing) your workspace to [Standard](https://clockify.me/help/administration/subscription-plans#standard), [Pro](https://clockify.me/help/administration/subscription-plans#pro), or [Enterprise](https://clockify.me/help/administration/subscription-plans#enterprise) plan.

![](https://clockify.me/help/wp-content/uploads/2018/03/lock.png)

## Steps to lock timesheets [\#](#steps-to-lock-timesheets)

1. Navigate to the workspace name
2. Open menu
3. Choose **Workspace settings** from the dropdown
4. Switch to the **Permissions** tab
5. Toggle **Lock entries** switch to activate
6. Specify a date before which all time entries will be locked
7. Changes will be automatically saved upon selecting the date or toggling the **Lock entries** switch

![](https://clockify.me/help/wp-content/uploads/2023/09/Screenshot-2023-09-07-at-12.44.06-300x87.png)
When entries are locked before, for example, April 15th, it means that regular users won’t be able to:

* Edit any time entries with the date April 14th or earlier
* Add new time entries with the date April 14th or earlier

 
Locking timesheets doesn’t affect administrators. Admins can still edit and add time in the locked period.

To unlock, move the switch back, and everyone will be able to edit all their time entries and add new ones to any date they want.

If you lock timesheets each month and have users across timezones, you should set the lock to the 2nd of each month. If you set it to 1st of the month, your team that’s in the later timezone won’t be able to enter dates for the last day in the previous month due to timezone difference.

## Automatic lock [\#](#automatic-lock)

Set automatic lock and the lock date will get auto\-updated each day, week, or month so you don’t have to do it manually anymore.

![](https://clockify.me/help/wp-content/uploads/2023/09/Screenshot-2023-09-07-at-12.42.42-1024x172.png)
## How to set automatic lock [\#](#how-to-set-automatic-lock)

1. Open the menu next to the workspace name
2. Go to workspace settings and switch to the Permissions tab
3. Switch **Automatically update lock date** to ON
4. Select lock frequency (weekly, monthly, older than x days/weeks/months)

When selecting the **Weekly** option, you have to select two days: when the lock date gets updated (e.g. Wednesday) and the first day of the week in your company (e.g. Monday).  This way, when a new week starts (on Monday), your team can still add their missing hours for the previous week before that week gets locked (which happens on Wednesday).

When the automatic lock is enabled, you won’t be able to manually set a lock date.

When you set **auto\-update lock date older than 1 day**, it means that at every end of the day, the lock date will be automatically updated so users cannot edit their yesterday’s hours.

 The daily lock is updated every day at midnight, using the workspace owner’s time zone.

If you lock timesheets monthly and have users across timezones, you should set auto\-lock to the 2nd of each month – otherwise, your team that’s in the later timezone won’t be able to enter dates for the last day in the month.

## Lock today’s time [\#](#lock-todays-time)

You can’t lock current or future dates.

To prevent people from adding time manually for today or the future (or changing the start/end time of their entries), you need to enable the [Force timer](https://clockify.me/help/track-time-and-expenses/force-timer).

## Lock expenses [\#](#lock-expenses)

If you’re using expenses, keep in mind that lock date also affects expenses, meaning regular users won’t be able to add or edit expenses for locked dates.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
