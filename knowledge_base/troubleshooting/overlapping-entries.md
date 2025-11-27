---
title: "Overlapping time entries"
url: "https://clockify.me/help/troubleshooting/overlapping-entries"
category: "troubleshooting"
slug: "overlapping-entries"
---

# Overlapping time entries

* [Why do overlapping time entries happen](#why-do-overlapping-time-entries-happen)
* [Recommended solution: Enable Force Timer](#recommended-solution-enable-force-timer)

# Overlapping time entries

2 min read

Overlapping time entries are expected behavior in Clockify unless the Force Timer feature is enabled. If the system were designed to prevent overlapping time entries, it would need to block users from adding time during already\-tracked periods or automatically adjust overlapping entries. 

## Why do overlapping time entries happen [\#](#why-do-overlapping-time-entries-happen)

There are two main ways users can create overlapping time entries:

1. Simultaneous use of manual entry and a timer

Users may manually log time while also running a timer without properly coordinating start and end times. This often results in entries that unintentionally overlap.

 2\. Manual durations without precise timing

Instead of specifying exact start and end times, users may enter total durations (e.g., “2 hours”), which can overlap with existing time entries if they don’t verify the timeframes. 

**Common scenarios**

* A user starts a timer at 10:00 AM, then later manually logs time from 9:30 AM to 11:00 AM.
* A user stops one timer and immediately starts another one (overlap happens here, usually with the compact mode enabled)
* Multiple time entries are created with overlapping durations because users are unaware of existing entries

## Recommended solution: Enable Force Timer [\#](#recommended-solution-enable-force-timer)

To prevent overlapping time entries, we recommend enabling the Force Timer feature. 

What Force Timer feature does:

* Prevents manual time entry—users can only track time using the timer
* Ensures no overlaps—since time must be tracked in real time, overlapping entries are automatically avoided
* Keeps data clean—Your reports, calendars, and logs will be consistent and reliable

**How to enable Force Timer**

1. Click on the three dots next to your workspace name
2. Select “Workspace settings” from the drop\-down menu
3. Navigate to the “Permissions” tab
4. Scroll down to the bottom of the page and enable the Force Timer feature

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXfYq6KslWqA2ZjN1amUI3nK_rK2zCPzeRrIC7RtQvQ9lGeTjpudkYySDHTyzRUBWmH9YNspVmiwfxZE6PPm3rJA0W8TwljsRsGlRerCPChCYCTJvZiHIAKd8uYlHIlnqDWY3lbuNw.png)
The Force Timer feature is a workspace\-wide setting and will apply to all users. This feature is available on our PRO and Enterprise plans. 

Still having issues? The Clockify Support Team will be happy to look into it and assist you further. Please contact us at [support@clockify.me](mailto:support@clockify.me) and include the following details:

1. A screenshot of the time entries in question from the detailed report
2. Information on whether the Force Timer feature is enabled in your workspace
3. Information about your current duration format

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
