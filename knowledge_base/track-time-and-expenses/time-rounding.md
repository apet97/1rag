---
title: "Time rounding"
url: "https://clockify.me/help/track-time-and-expenses/time-rounding"
category: "track-time-and-expenses"
slug: "time-rounding"
---

# Time rounding

* [Turn on rounding](#turn-on-rounding)
* [What rounding affects when it's ON](#what-rounding-affects-when-its-on)
* [Rounding options](#rounding-options)

# Time rounding

3 min read

Round time entries up or down to the nearest minutes or hours so your reports are nice and neat, without all the confusing details.

For example, you can round time to the nearest whole minute in reports so you don’t get distracted by seconds when looking at a report. Or, you can round time to the nearest 6 minutes and export them to get all time entries displayed as a nice round number with just one decimal.

Time rounding is a paid feature, which you can enable by [upgrading](https://clockify.me/pricing) your workspace to [Standard](https://clockify.me/help/administration/subscription-plans#standard), [Pro](https://clockify.me/help/administration/subscription-plans#pro), or [Enterprise](https://clockify.me/help/administration/subscription-plans#enterprise) paid plan.

## Turn on rounding [\#](#turn-on-rounding)

To round time entries, go to any report, and toggle the Rounding switch.

To choose a different rounding option, click on the dropdown next to Rounding and choose Settings.

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-21-at-13.22.38-1024x446.png)
Rounding is applied to each time entry. Rounding only affects the reports, meaning that the rounded values will only be displayed in the reports and exports.

## What rounding affects when it’s ON [\#](#what-rounding-affects-when-its-on)

Time rounding only affects the reports and can be turned on and off as you wish.

* **Calculating duration**: Clockify will first round the duration of each time entry, and then add them up.
* **Export**: durations and values will be rounded in the export too.
* **Calculated earnings**: when calculating the value of your billable hours, Clockify takes rounded time entries.
* **Detailed report**: you can’t edit time entries in the Detailed report when the rounding is on.

Time rounding doesn’t change any data, only how it’s displayed, which can always be turned on/off. If you set the rounding to the nearest minute, your 00:10:56 time entry will be displayed as 00:11:00 once you turn the rounding on. And it will go back to 00:10:56 when you turn the rounding off. 

## Rounding options [\#](#rounding-options)

You can set the rounding interval and how you want to round time entries in your workspace settings:

* **Round down** (for example: if the interval is set to 30min, a 1\-29min entry will show up in reports as 0min)
* **Round up** (for example: if the interval is set to 30min, a 1\-29min entry will show up in reports as 30min)
* **Round to nearest** (for example: if the interval is set to 30min, a 1\-14min entry will show up in reports as 0min, and a 16\-29min entry as 30min)

![](https://clockify.me/help/wp-content/uploads/2018/03/rounding.png)
If your duration format is set to hh: mm in your Workspace settings, time entry will be rounded up to a minute. For example, if you tracked 0 hours, 1 minute, and 15 seconds (00:01:15\), the entry will be shown as 0 hours and 2 minutes (00:02\). This is not a part of the time rounding feature and you can change the duration format in the Workspace settings on any plan, including the free plan.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
