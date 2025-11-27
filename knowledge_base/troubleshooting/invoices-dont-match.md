---
title: "Reports and invoices don\u2019t match"
url: "https://clockify.me/help/troubleshooting/invoices-dont-match"
category: "troubleshooting"
slug: "invoices-dont-match"
---

# Reports and invoices don’t match

* [Reports calculate time with more decimals than invoices](#reports-calculate-time-with-more-decimals-than-invoices)
* [Invoices round each entry before calculating totals](#invoices-round-each-entry-before-calculating-totals)
* [How to match invoices and reports](#how-to-match-invoices-and-reports)
* [How to enable time rounding](#how-to-enable-time-rounding)

# Reports and invoices don’t match

3 min read

If you’re noticing small differences between the amounts shown in your reports and invoices, it’s not an error. This happens because Clockify calculated them in slightly different ways to keep things precise. 

## Reports calculate time with more decimals than invoices [\#](#reports-calculate-time-with-more-decimals-than-invoices)

Clockify tracks time with multiple decimal places, like 1\.375 hours, for example. 

* Reports show time in full format (unless changed in the Workspace Settings), like 1:15:45 or 1 hour, 15 minutes, and 45 seconds.
* Invoices, on the other hand, convert and round time to two decimal places, like 1\.26 hours.

This difference in how time is handled leads to small variations in total. 

## Invoices round each entry before calculating totals [\#](#invoices-round-each-entry-before-calculating-totals)

When generating an invoice, Clockify rounds each time entry to 2 decimals before multiplying by the rate. Reports calculate total time first, then multiply.

**Example:**

You tracked three entries:

* Entry 1: 1:15:45
* Entry 2: 2:45:30
* Entry 3: 0:59:50

Report totals: 

* Total time \= 5:01:05 (5 hours, 1 minute, 5 seconds)
* At $100/h \-\> $501\.08

Invoice totals:

* Entry 1: 1:15:45 \-\> 1\.26h
* Entry 2: 2:45:30 \-\> 2\.76h
* Entry 3: 0:59:50 \-\> 1\.00h
* Total \= 1\.26 \+ 2\.76 \+ 1\.00 \= 5\.02h
* At $100/h \-\> $502\.00

The invoice ends up showing $502\.00, while the report shows $501\.08, a $0\.92 difference due to rounding conversion. 

## How to match invoices and reports [\#](#how-to-match-invoices-and-reports)

To make both features calculate time in the same way, turn on time rounding for all time entries. 

Best option: 

* Set rounding to the nearest 6 minutes (which equals 0\.1h).

Clockify uses 0\.1 hours \= 6 minutes as the rounding base, Since both reports and invoices will round each time entry the same way, to the nearest 6\-minute block, you get consistent results across the board.

**Example:**

Let’s say you have this time entry: 

* Actual tracked time: 1:07:00 \= 1\.1166… hours

Without rounding:

* Report uses 1\.1166h \-\> $111\.66
* Invoice rounds: 1\.12h \-\> $112\.00

$0\.34 difference

With rounding to the nearest six minutes:

* 1:07:00 rounds to 1\.1h (because 6 minutes \= 0\.1h)
* Both report and invoice use 1\.1h \-\> $110\.00

By rounding to a number divisible by 6, all entries land on the same time unit (e.g., 1\.0h, 1\.1h, 1\.2h…), which removes all seconds that cause mismatches.

## How to enable time rounding [\#](#how-to-enable-time-rounding)

1. Click on the three dots next to the Workpsace name
2. Select “Workpsace settings”
3. Scroll down and navigate to the Time Rounding section
4. Choose “Round up to 6 minutes”

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXdtdl2F4pDdWqqB7d4z9nVNw64g_kcW9s1J3as30xrDcRLTtdWOpkxqgohn0TcO_j5tfIerZxlZsW5PrjRUnqD1jD1GSkb81m01jDcdtHPxtBwJJarIQWy0mAWczF_0OYpx7J3HYw.png)
Still having issues? The Clockify Support Team will be happy to look into it and assist you further. Please contact us at support@clockify.me and include the following details:

1. A screenshot of the detailed report and invoice you’re comparing
2. Information about the duration format set in your workspace
3. A screenshot of the hourly rate

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
