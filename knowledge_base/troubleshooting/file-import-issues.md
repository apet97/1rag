---
title: "CSV File import issues"
url: "https://clockify.me/help/troubleshooting/file-import-issues"
category: "troubleshooting"
slug: "file-import-issues"
---

# CSV File import issues

* [Required headers are missing or incorrect](#required-headers-are-missing-or-incorrect)
* [Date, time, and duration formats don’t match Clockify settings](#date-time-and-duration-formats-don’t-match-clockify-settings )
* [Excel formatting issues](#excel-formatting-issues)
* [The file is not comma\-delimited](#the-file-is-not-comma-delimited)
* [Missing or incomplete field values](#missing-or-incomplete-field-values)

# CSV File import issues

3 min read

If your CSV file fails to import into Clockify, it’s usually due to formatting issues or missing required data. Below are the most common reasons why imports fail and how to fix them.

## Required headers are missing or incorrect [\#](#required-headers-are-missing-or-incorrect)

Your CSV file must include the following required column headers, written in English. 

* Project
* Client
* User
* Email
* Task
* Tag
* Start date
* Start time
* Duration

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfmX4gbO7tSuWnq9QsjQ9BVnuPDlrJWGWICtNxVq7-cnL6pndoHqtWkgLJlkgZ8sBeP6vDBsTlLY09lTcFTwU0DZaQzExyX-obTCoSZkBbgRvhKfTHDkKe-VdN0sJOazdyhYQNB?key=XZmssafXgdhlV2XB9mRUkEGN)
You can find the full list of supported columns [here](https://clockify.me/help/track-time-and-expenses/import-timesheets).

Headers must be spelled correctly in English, free of extra spaces or characters. If any of these are missing or incorrectly formatted, your import will fail.

## Date, time, and duration formats don’t match Clockify settings  [\#](#date-time-and-duration-formats-dont-match-clockify-settings)

Clockify reads your CSV file based on your account and workspace formatting settings. The start date, start time, and duration fields must follow these settings. 

Date and time format:

1. Click on your profile picture in the upper right corner
2. Select “Preferences.”
3. Under the General tab, check your Date and Time formats

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc98LJctDwe53snIQhsIWAqrYNv2OTw65cRHopA0Q2_7S73mOIgnVAP7bsZAgjXmBP4ejfOh085FUUL8t4tozApMp2NU6lEgywYcheQ-UUD9-oXvB326RsmnAKQau27ckNVmm32lQ?key=XZmssafXgdhlV2XB9mRUkEGN)
Duration format:

1. Click on the three dots next to your workspace name
2. Click on the “Workspace settings”
3. Under the General tab, check the Duration format:

* Decimal
* Full
* Compact

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcNCRxpmpt1pGE2uC4FLHWy7qM5DWvHkcHwD0Soz4L3a_ZNK-ZWq-DYdr54AkCC3CgWd0Js0swj_2A2awMuO5zOQZMdiZHo4M-c6v-vRiDIMU0SnKCdfXtKsXtM-EsPmXq-ssyrCw?key=XZmssafXgdhlV2XB9mRUkEGN)
Your CSV file must match these formats exactly; otherwise, the file will be rejected. 

## Excel formatting issues [\#](#excel-formatting-issues)

If you opened or edited your CSV file in Excel, it might have changed the formatting (e.g., dates, times, or stripped leading zeroes). This often breaks the import.

To prevent that, we recommend opening and editing your CSV file in Google Sheets, which maintains correct formatting. 

## The file is not comma\-delimited [\#](#the-file-is-not-comma-delimited)

Clockify expects CSV files to use commas as delimiters. If your file uses semicolons instead, the import will not work. 

How to check if your file is comma\-delimited:

1. Open the CSV file in a plain text editor (like Notepad)
2. Check the character separating values:

* If values are separated by commas, the format is correct
* If you see semicolons (;), you’ll need to convert the delimiters to commas.

You can also open the file in Google Sheets and re\-download it as CSV. Google Sheets will automatically format it correctly using commas as delimiters. 

## Missing or incomplete field values [\#](#missing-or-incomplete-field-values)

Even if all required fields are present, your import can still fail if some fields are left empty in your CSV file. 

Check your workspace required field settings:

1. Click on the three dots next to your workspace name
2. Select “Workspace settings”
3. At the top of the page, check if the Timesheet is enabled. If it is, Project becomes a required field by default
4. Scroll down to the “Do not allow saving time without” section to see if additional fields (e.g., Description, Task, Tag) are marked as required.

If any of these required fields are empty in your CSV, the import will not succeed. 

Custom fields:

If your workspace requires custom fields, you must also include those in your CSV, with valid data for each entry. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdib4uAG_dSXJBD8p_WFNatmsUCoO_PBkEd35ksymJeDsUudFzW0geYj4TCOANcNP4LUrWD5uUg2lVQMdXpgxhnsSBzdLDVdmo8QVIF5h73uCObtSKU7z35vz3H0uHvFvHRLK5y-w?key=XZmssafXgdhlV2XB9mRUkEGN)
To streamline the import process:

1. Temporarily disable all required fields in your workspace settings
2. Import only the essential time entry data
3. After the import, re\-enable your required fields

This approach saves time and avoids needing to populate every single field in advance. 

Still having issues? The Clockify Support Team will be happy to look into it and assist you further. Please contact us at [support@clockify.me](mailto:support@clockify.me) and provide us with the following information:

1. A copy of the CSV file you’re trying to import
2. A screenshot of any error messages you’re getting when importing the file

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
