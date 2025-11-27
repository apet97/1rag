---
title: "The rate change won\u2019t apply to time entries"
url: "https://clockify.me/help/troubleshooting/rate-change-wont-apply"
category: "troubleshooting"
slug: "rate-change-wont-apply"
---

# The rate change won’t apply to time entries

* [A more specific rate is overriding the one you changed](#a-more-specific-rate-is-overriding-the-one-you-changed)
* [The rate wasn’t applied to past time entries](#the-rate-wasn’t-applied-to-past-time-entries)
* [The time entries are approved](#the-time-entries-are-approved)

# The rate change won’t apply to time entries

3 min read

If your updated hourly rate isn’t showing up in reports, it’s likely because something else is overriding it or preventing the update. Here’s what to check and how to fix it. 

## A more specific rate is overriding the one you changed [\#](#a-more-specific-rate-is-overriding-the-one-you-changed)

Clockify prioritizes rates in the following order (from lowest to highest priority):

1. Workspace rate
2. Project rate
3. Team rate
4. Task rate
5. Project member rate

More specific rates will override less specific ones. Even if you change the team rate, for example, the project member rate will take precedence.

What to do:

Check and adjust the specific rate that may be overriding the one you intended to change: 

* **Workspace rate**

1. Click on the three dots next to the workspace name
2. Select “Workspace settings”
3. Scroll a bit down and check the workspace rate

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXf2Dy01aHax4fF4KM19_elxgFgngJPoSjz5MP4QLPRlsnWz7ixs2A47hOhg2kbtpVGkluKVEJM2IeHsT_p_n1eMmEisGcUAtGdDJLiWV3KyC5mOTX0-e-45Y3_XiXRj6EEGIZunfA.png)
* **Project rate**

1. Navigate to the Projects page from the sidebar
2. Find the project from the list and click to open it
3. Navigate to the “Settings” tab and check the hourly rate

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXco480jowLtHXb8ushNh1t6E_MF9p0K_t8tkKikxd6M_zWFG4wiRxg-3NIPhchag0jPZs7x1VkhRMmX_hgixIx0g9hcFYvEgplgqzQmIm4yimpk7ZUOwCI6SDf2VfBzvn9fIOh0.png)
* **Team member rate**

1. Navigate to the Team tab from the sidebar
2. Check the Rate column next to each user

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXcF-Wbg5gFYhuvhK15lnjJQDmEk2K8gtS-mXPL4DYE8SueAYZUR3KirAS9WOO-5CLEtZyzmBBVrPjjX7ncTxX6vxX-c_1fQhgnE-7IUAQ-ZZCHBQFcbAAx8JawTtmI0MUBnxnE.png)
* **Task rate**

1. Navigate to the Projects page from the sidebar
2. Click on a project to open it
3. Navigate to the Tasks tab
4. Check the rate next to each task

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXei9vbAZjthLLB98WUWEBiL3vUitZkOwpHtzRC6fE0B818bpHTH9r-8yhJPKmUDzUY8-C8kLX6HtnUnn94Mq40kAu73vYe3u7nzS730ILfOwE8ylLlrgIgP-E2fNkIWve2xAtMj.png)
* **Project member rate**

1. Navigate to the Projects page
2. Click on the project to open it
3. Navigate to the Access tab
4. Check or change the rate next to each user

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXeb11ZEqmUBEuL8y2mNlG0hKTSK6V1BoSnHZC0hg1Oj4tpwALv6EHVUeMfGKrAr_J3C0snZHnP4qMQLschpOy_Vibeni0LfKTBVg9gSXTzKLBQp5KrlhcMXlZq9WyHZ1rr79cp9.png)

## The rate wasn’t applied to past time entries [\#](#the-rate-wasnt-applied-to-past-time-entries)

Even if you set the right rate, Clockify won’t retroactively apply it to past time entries unless you explicitly choose to do so. 

What to do: 

* If you’re on a paid plan, go back to the rate settings and check the “Apply to all past and future time entries” option when saving.

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXfPDPfVn6U24Hnqx15YN9bJf3-BFeCj3_mTnUfA7bCZBqo9OF_-IMIUEe3REkMvM-BXYJicuzhpzGKu0kDat9KjlNw7f9q3a3n_NMZ2UcSiJCvxktgveoAD7ZWgFZcWuBWhhSqYfQ.png)
* If you’re on a free plan, go to the Detailed report, find the affected time entries, and toggle the billable icon off and on to refresh the rate.

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXfqhzsdxEZ7ZrzgUX3_HHDe-HfIi4Fa0DVQJTQIAg2h79z0lAMnwir4nTSNiGKPp88XRnQniSTOVrPGy3Rf7EnjsKDoNT99cu6nqE18v3lKT8eAZaiC2crxcVAv5Mw2DKpIAwEe-A.gif)

## The time entries are approved [\#](#the-time-entries-are-approved)

Approved time entries are locked, including their hourly rate. If a time entry is approved, rate changes won’t apply even if everything else is correct.

What to do: 

You’ll need to withdraw the timesheet to unlock it and update it:

1. Go to the Approvals tab from the sidebar
2. Open the Archive tab
3. Locate and click on the timesheet in question to open it
4. In the upper right corner, click Withdraw
5. Go back to your rate settings and update the rate
6. Once the rate is correctly applied, you can resubmit the timesheet for approval

![](https://clockify.me/help/wp-content/uploads/2025/06/Screenshot-2025-08-04-at-18.26.45-1-1024x496.png)
Still having issues? The Clockify Support Team will be happy to look into it and assist you further. Please contact us at support@clockify.me and include the following details:

1. Information about which rate you’re trying to apply
2. Whether you’re on a free or a paid plan
3. A screenshot of the rate settings you’ve changed

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
