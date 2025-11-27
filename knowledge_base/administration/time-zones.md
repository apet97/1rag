---
title: "Users in different time zones"
url: "https://clockify.me/help/administration/time-zones"
category: "administration"
slug: "time-zones"
---

# Users in different time zones

2 min read

Clockify uses several time zones to record and display time values:

* Time zone from your [Profile settings](https://clockify.me/help/administration/profile-settings) (when you record time in the web app)
* Time zone from your device (when you record time in desktop/mobile app)
* UTC (stored in the database)
* Time zone from your Profile Settings (when displaying recorded time)

When you record time in Clockify mobile or desktop app (e.g. start a timer), your device’s system time is used. When you record time in Clockify web, time from Profile Settings is used. Then, Clockify converts that time to UTC and sends the converted value to the server. When you later view the time in reports, the time zone from your Profile Settings is used.

For example:

*Jörg from Germany works from 09\-10 AM (UTC\+2\) and records that time in Clockify. Clockify converts it to 07\-08 AM (its corresponding UTC value) and stores it in the database. When Emily from New York runs the report, she sees that Jörg worked from 03\-04 AM (displayed in her UTC\-4 time).*

This assumes the system time zone and the time zone in the Profile Settings match. If they don’t match, you will get a notification to fix it. If you don’t fix it,  your timesheet and reports will show different start and end time from the one you recorded.

![](https://clockify.me/help/wp-content/uploads/2024/05/time_zone_mismatch_new_menu.png)
If you wish to see a report in a different time zone (e.g. you want to analyze report for users in their native time zone), you can change your time zone in Profile Settings and then create a shared report (filtered by certain users) that you can open at any time (shared report remembers the time zone during its creation, so you can safely switch to your time zone and view the shared report in the time zone you’ve used during creation).

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
