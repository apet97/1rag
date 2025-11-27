---
title: "Customize reports"
url: "https://clockify.me/help/reports/creating-custom-reports"
category: "reports"
slug: "creating-custom-reports"
---

# Customize reports

* [Create custom report](#create-custom-report)
* [Additional dimensions](#additional-dimensions)
* [Overlapping entries](#overlapping-entries)

# Customize reports

3 min read

If Clockify’s built\-in reports and [customization options](https://clockify.me/help/reports/customize-exports) don’t provide the structure you need, create your own report using pivot tables in Excel/Google Sheets.

Simply export the Detailed report’s as CSV or Excel, and you can create any kind of report you want:

* Total hours (or amount) broken down by client \> project \> task \> description
* Monthly report with total hours (or amount) per project (or user) per day

[![pivot report](https://clockify.me/help/wp-content/uploads/2019/08/pivot-report.png)](https://docs.google.com/spreadsheets/d/1c7oG8zhIUYcFre8GWg39xjJNiyPjqS88igXcn9FpuQM/edit#gid=1624600682)
[See example (Google Sheets)](https://docs.google.com/spreadsheets/d/1c7oG8zhIUYcFre8GWg39xjJNiyPjqS88igXcn9FpuQM/edit#gid=1124667396)

## Create custom report [\#](#create-custom-report)

Create a custom report in the following way:

1. Export Clockify’s Detailed report in CSV or Excel and open it in Google Sheets or Excel
2. Select the whole table
3. Excel: go to Insert \> Pivot Table; Google Sheets: go to Insert \> Pivot Table
4. Click OK
5. Choose what fields to show in rows/columns, and what to display as values. Example: “Row: Project”, “Column: User”, “Value: Duration (decimal)”

## Additional dimensions [\#](#additional-dimensions)

You can enrich reports using [custom fields](https://clockify.me/help/track-time-and-expenses/custom-fields) on time entries. Your users can track all sorts of things, like expenses, mileage, units, etc. 

You can also add metadata to time entries using custom fields on projects. That way, you’ll have more options for grouping time in pivot tables.

[Download sample report with custom fields (Excel)](https://clockify.me/downloads/samples/report-detailed-sample-custom-fields.xlsx)

![](https://clockify.me/help/wp-content/uploads/2020/02/detailed-report-pivot-custom-fields-3.png)
## Overlapping entries [\#](#overlapping-entries)

If you have entries with overlapping start and end times, you can easily find them in Excel or Google Sheets.

1. Export Clockify’s Detailed report in CSV
2. Open CSV in Excel/Google Sheets
3. Select all data and sort it by: User\>Start Date\>Start Time
4. Create a new **Overlap** column
5. For the first record, use this formula: \=IF(OR(IF($F1\=$F2, IF($I2\=$I1, IF($L1\>$J2, true, false))),IF($F2\=$F3, IF($I2\=$I3, IF($L2\>$J3, true, false)))),”overlap”, “ok”)
6. Expand and apply the formula for each row
7. Apply conditional formatting to highlight overlapping time entries
8. Create pivot table based on the data in the table
9. In Pivot table, select: **Row:Overlap**, **Value:Overlap (count)**
10. Click on the overlapping count to see only the overlapping entries in a new sheet

How the formula works: Once all the entries are sorted, the formula compares the previous and the next row. If the rows are from the same user and from the same date, it looks if the entry’s start time overlaps with previous entry’s end time or if its end time overlaps with next entry’s start time.

 [See example of overlapping entries (Google Sheets)](https://docs.google.com/spreadsheets/d/1c7oG8zhIUYcFre8GWg39xjJNiyPjqS88igXcn9FpuQM/edit#gid=2085526633) 

[![overlapping entries](https://clockify.me/help/wp-content/uploads/2019/08/overlapping-entries-min.png)](https://docs.google.com/spreadsheets/d/1c7oG8zhIUYcFre8GWg39xjJNiyPjqS88igXcn9FpuQM/edit#gid=2085526633)

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
