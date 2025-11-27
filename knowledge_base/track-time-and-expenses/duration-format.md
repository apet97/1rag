---
title: "Duration format"
url: "https://clockify.me/help/track-time-and-expenses/duration-format"
category: "track-time-and-expenses"
slug: "duration-format"
---

# Duration format

* [How duration formats are implemented](#how-duration-formats-are-implemented)
* [Set up duration format](#set-up-duration-format)

# Duration format

2 min read

Efficient time tracking is at Clockify’s core, and we understand that different users prefer different ways of representing duration. With preferred duration format, you can see, enter, and export time in format that suits your needs.

Clockify has three different duration formats: 

* Full (hh:mm:ss)
* Compact (h:mm)
* Decimal (h.hh)

## How duration formats are implemented [\#](#how-duration-formats-are-implemented)

* Full: ‘2’ \= 2 minutes
* Compact: ‘2’ \= 2 minutes
* Decimal: ‘2’ \= 2 hours
* All formats:
	* ‘2h’ \= 2 hours
	* ‘2m’ \= 2 minutes
* Full format only:
	* ‘2s’ \= 2 seconds; other formats show 0:00 for less than 1 minute
	* ‘120s’ \= 2 minutes

*Decimal duration format (e.g. 2\.5 hours) would be ideal for a freelancer who is invoicing clients based on hourly rates. This format simplifies the billing process and is useful to those who need time entries in a numeric form.*

Decimal format is a paid feature you can enable by [upgrading](https://clockify.me/pricing) your workspace to any of our paid plans.

## Set up duration format [\#](#set-up-duration-format)

To set up duration format on your workspace: 

1. Navigate to the workspace name
2. Open the menu
3. Choose **Workspace settings** from the dropdown
4. Find duration format in the **General** tab
5. Choose one from the dropdown

![](https://lh7-us.googleusercontent.com/9vuuijacRSCPJNBk3t6d_Pa8G3SPhZt7VvEqC1K-Yozc-_F9RkciCRJkvjNL4wP06VqeSZTc6liCTsyxHFSzYcdGFheKcpX-gmTUJ2vXHwz9B9jgMavPYbrwYyXBVl8nfypSTXzlf9CtPl58z4PFCAE)
Once you selected duration format:

* That duration format is displayed everywhere in the interface (tracker, timesheet, reports, invoices etc.)
* Duration in PDF/Excel and CSV report exports is in that format
* Cells in all duration inputs interpret time in that format (e.g. if you type 1, it is considered to be 1h)

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-20-at-14.54.34-1024x319.png)

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
