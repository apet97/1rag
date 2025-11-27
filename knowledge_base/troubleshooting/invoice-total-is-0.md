---
title: "Invoice total is $0"
url: "https://clockify.me/help/troubleshooting/invoice-total-is-0"
category: "troubleshooting"
slug: "invoice-total-is-0"
---

# Invoice total is $0

* [Non\-billable time entries won’t appear on invoices](#non-billable-time-entries-won’t-appear-on-invoices)
* [The hourly rate is $0](#the-hourly-rate-is-$0)
* [A more specific $0 rate is overriding your intended rate](#a-more-specific-$0-rate-is-overriding-your-intended-rate)

# Invoice total is $0

3 min read

If your invoice shows a total of $0, or no time entries at all, it usually means the time entries are missing a billable rate or weren’t marked as billable to begin with. Here’s how to find and fix the issue. 

## Non\-billable time entries won’t appear on invoices [\#](#non-billable-time-entries-wont-appear-on-invoices)

Clockify invoices only include billable time entries. If your entries were tracked as non\-billable, they won’t be available for import into the invoice at all. The invoice will appear empty. 

How to check:

1. Navigate to the Detailed report and select the relevant date range
2. Look for the billable icon (dollar sign) next to your entries
3. If the icon is grayed out, the entry is not billable

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXf9DtxpBO5JBQy7em03Gy40nLOx9N2y-fIOQJn2UABMx1_qOj-KN-Uaj-VKcODGx-KwvFc6qWEET15z6tVXr25hoAM7qTrpJwTVAa-3vkUfez_aHZ6KdxetW2lP_bbpLfQ9Nr-t.png)
To fix it:

1. Select the entries by clicking the checkbox next to “time entry’
2. Select Bulk Edit
3. Check the billable checkbox and toggle the button
4. Save changes

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXeSXYB1AIZQAI0oHe7zO4wThTD3V_fSFzyLBhHjzaoqvG3tq-KBnBYodjk3Ng_L3we1FCBNukzKi7DFgz7c6UOLRryBlUI9dMA0x-6G8xgkv4kTGiDx6fCM9xRkUbDJT_mL5OJo.png)
After marking the entries as billable, return to the invoice and try importing again. 

## The hourly rate is $0 [\#](#the-hourly-rate-is-0)

If your entries are billable but still not showing a total, the applied hourly rate is likely set to $0\. Clockify will treat that as valid time with no cost. 

Where to check:

* **Project rate**

1. Navigate to the Projects page from the sidebar
2. Find the project from the list and click to open it
3. Navigate to the “Settings” tab and check the hourly rate

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXezvz-v-EJLxuGCO5HJJ6uh-oDF0Zkj183-oQuicJrsNQ5a842XJQ6xJRHzFoYI3dqv7JAQAUEpJ34ajl52RhYxh34jX4pmAbL2bBKJLeovsbNgsJZ8_gnGmCv2gj_wt2HGDcM1MQ.png)
* Workspace rate

1. Click on the three dots next to the workspace name
2. Select “Workspace settings”
3. Scroll a bit down and check the workspace rate

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXefqynNFvcZlike9STNOH_5eKT4MSLvTXZbkmEaeh6NLmgZUrYHwMpynYzHnIcvMdI-3xBnlF8BKdfQcU-8c-hFW5Cl-8dTV47Tss0J_FuS-nFgR1qD7ClVhCcX2t89KzQpfmPP.png)
* **Team member rate**

1. Navigate to the Team tab from the sidebar
2. Check the Rate column next to each user

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXfweHziwzDsCnBY-BUPn74xiap2msP8_uro1L6fyvZ8A0BR9AIyxdwBRQ6q965VT_IdRk7v1Vgt6sPDSP8NPV0TGYSFM7FyB-f2l5F7GMu9_RZTtnew5NQq8LrQzAzATjC3oZBXrg.png)
* **Task rate**

1. Navigate to the Projects page from the sidebar
2. Click on a project to open it
3. Navigate to the Tasks tab
4. Check the rate next to each task

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXcxv5UMBA0eTuPfegmhf-Hzr6xRZDqqxMIn0zWqYJTCDBDHuUJZOb2K4jlpv5p_Tz7X9PRwCiPbSd9ErCcxvwoRlavOYVxy7w4f96beSLFHCEPJd0lEGcP3owOUEhXMfKrFQvl-Cg.png)
* **Project member rate**

1. Navigate to the Projects page
2. Click on the project to open it
3. Navigate to the Access tab
4. Check or change the rate next to each user

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXeEbLyIeIQS7vZ_zwvalD18dnk_HXZrn2Vsrc7PFmYorucSFdLPAvzHqDBGvvDzbmJ-Xe7WtntUpkdvWTD2rnRRqj7lQkmzN5lMsMOOaiGqJFxChd1uGFOWcyv50z_mkHDPetcVmw.png)
## A more specific $0 rate is overriding your intended rate [\#](#a-more-specific-0-rate-is-overriding-your-intended-rate)

Clockify follows a rate hierarchy, where more specific rates override more general ones. So even if you’ve set a project or workspace rate, a blank $0 project member or a task rate can silently override it, resulting in an empty invoice or a $0 total.

Rate hierarchy from lowest to highest:

1. Workspace rate
2. Project rate
3. Team rate
4. Task rate
5. Project member rate

What to do:

Start by checking for any blank or 0$ rates at the top of the hierarchy (Task or Project Member), and work your way down. These will override the more general rates and lead to a $\- invoice total. 

Still having issues? The Clockify Support Team will be happy to look into it and assist you further. Please contact us at support@clockify.me and include the following details:

1. A screenshot of the invoice in question
2. A screenshot of the Detailed report showing billable time
3. Confirmation on which rates were set and where

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
