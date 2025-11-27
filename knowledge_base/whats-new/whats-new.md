---
title: "November 2025"
url: "https://clockify.me/help/whats-new"
category: "whats-new"
slug: "whats-new"
---

## November 2025

### 🆕 Features

* [Optional balance expiry](https://clockify.me/help/track-time-and-expenses/create-manage-time-off-policy#manage-time-off-balance) – Set up time off balance with no expiration period, or with one
* See [rejected approval requests](https://clockify.me/help/track-time-and-expenses/approval#archive-tab) in Archive tab
* [Bulk submit for others](https://clockify.me/help/track-time-and-expenses/submit-time-expenses-for-approval#bulk-submit-for-others) – Submit multiple unsubmitted timesheets from other users at once
* [Bulk approve/reject](https://clockify.me/help/track-time-and-expenses/approval#bulk-approve-reject) – Approve/reject multiple timesheets at once
* [Recurring invoices](https://clockify.me/help/projects/invoicing#set-up-recurring-invoices) – Set a recurring period and avoid manual creation for regular invoices
* [Send an invoice to multiple email addresses](https://clockify.me/help/projects/sending-invoice-emails#send-invoices-to-multiple-emails)
* [Reminders if invoice is overdue](https://clockify.me/help/projects/invoicing#reminders-if-invoice-is-past-due)
* Android: Pomodoro timer

### ✅ Fixes

* Broken expandability of the description field in Edit time modal on Timesheet page
* Time off entries not being created when time off request is edited after submission
* Time off entries being created for deactivated users
* Error while creating time off request due to switching between half day and full day policies
* “Manage balance” option being accessible to regular users
* Updated time off policy balance not displayed immediately when bulk update is used
* Incorrect last valid day of balance displayed for non\-joined users in “Manage balance” modal
* Balance expiration change when policy with automatic accrual is archived
* Possibility of creating half day time off request outside of the balance’s validity period
* Available negative balance being visible while positive balance isn’t used up
* A case in which “Manage balance” is unavailable when the user is both Owner and Team Manager
* Used balance disappearing while still being within the validity period when all available balance is used up
* Broken sorting of expenses when there is a lot of data to display
* “Without group” filter not persisting after redirection from Summary to Detailed Report
* Team Manager having issues with user search when the user is Project Manager on a large number of projects
* CSV import failing due to custom fields values being mandatory even when custom fields aren’t required fields for creating time entries
* CSV import failing when custom labels are applied on the workspace and in the CSV file

## October 2025

### 🆕 Features

* Time off balance expiration for policies that have an automatic monthly accrual set is extended to the following year
* [Android](https://clockify.me/help/apps/android-app#receive-reminders-and-notifications) \& [iOS](https://clockify.me/help/apps/iphone-app#receive-reminders-and-notifications): Get reminders to start/stop time
* MacOS: [Undo delete](https://clockify.me/help/apps/mac-desktop-app#undo-deleted-discarded-entry)
* [Import Wizard](https://clockify.me/help/track-time-and-expenses/import-timesheets) – Check data before import and view import summary

### ✅ Fixes

* Users unable to access their workspaces when they have multiple regional workspaces but none on global
* Incorrect balance values displayed when policy has negative balance allowed
* Timesheet can’t be approved if there is a long numerical custom field (at least 20 characters)
* Time off entries created even after the originally approved time off request is rejected
* Team manager, who is also Admin, unable to filter approval requests by individual members of user groups they manage
* Amounts shown in shared report even when Hide amount option is active for some users
* Random sorting of user’s approval requests on Approvals page
* Time off policy being created or updated with invalid user or user group IDs
* Use of available balance not being prioritized by expiration date
* Time off entries incorrectly labeled in audit log
* Error when sending audit log email before the export is complete
* Alerts not being sent
* Error when adding time entries as favorites in some cases
* Project\-level empty custom field value not being picked up after custom fields are no longer required to create time entry
* Discrepancy between scheduled hours displayed on Scheduling page and in Attendance report for some users
* Error thrown when “Active” filter is applied on Scheduling page
* Filters reset and table not loaded on Projects page after navigating back from project view
* User who is both TM and PM not being able to retrieve users’ total capacity on workspace
* No “Manage balance” option for Owner who is also Team manager
* Dashboard not loading due to error when setting workspace default currency
* Wrong redirection after user accepts invite to join workspace on subdomain

## September 2025

![](https://clockify.me/help/wp-content/uploads/2025/09/balance-validity-policy-icons-1-1-1024x375.png)
### 🆕 Features

* [Balance validity dates](https://clockify.me/help/track-time-and-expenses/create-manage-time-off-policy#manage-users-balance) – Add start and end dates for each time off balance to specify when that balance can be used
* Time off policy icons – Set custom icons for different time off policies
* iOS: [Split entry](https://clockify.me/help/apps/iphone-app#split-entry) \& [Pomodoro timer](https://clockify.me/help/apps/iphone-app#pomodoro-timer)

### ✅ Fixes

* Switching tabs on Approval page shows data from previous tab
* New project color not shown on project created from template
* Downloading Detailed report with more than 200 thousand entries taking hours
* Incorrect daily working capacity for new full members
* Wrong start date of the forecasted curve when there is no completed curve in the chart
* Admin able to track time on project tasks marked as done
* Incorrect filtering of categories in Detailed report after redirection from Summary report
* Billable amount not displayed in header of exported Detailed report
* Team manager displayed as member of their own team on Approvals page
* Time entry incorrectly being created when a link custom field that is a required field isn’t populated
* User custom field values not visible when exported in certain cases
* Dashboard not loading when there is a lot of data to display
* Discrepancy between tracked and displayed time in reminder email
* Incomplete log when members are added to a project in the Audit log
* Invoice description field displaying only a single line of text
* Incorrect preview of submitted approval request when part of the request has already been submitted, then withdrawn or rejected
* Discrepancy between displayed end dates of approval request periods in Pumble notification, Clockify email, and on Approvals page
* Incorrect calculation of time off values on Approvals page
* Shared report not loading for certain users
* Incorrect data displayed in Assignment report when weekly “Group by” filter is applied

## August 2025

### 🆕 Features

* [Sample data](https://clockify.me/help/administration/free-trial#add-sample-data) available for free trial – Explore Clockify features upon activating the free trial (optional)
* Approved time off requests cannot be deleted through withdrawal
* Future time off entries are now hidden
* Time off entries are now created only on working days
* Test data available on free trial – Populate your workspace with test data on free trial \& see how all features work
* Approve and reject time off requests directly from Pumble
* Reminder to submit timesheets for approval and approve submitted timesheets
* Workspace name included in notifications for users who have multiple Clockify workspaces connected to one Pumble workspace

### ✅ Fixes

* Blank page displayed to users trying to join a workspace without an invitation by using their SSO
* Background color missing on Calendar when time off days are on the weekend
* Project Manager unable to schedule for some users on their projects
* Regular user able to see others’ time off request info and balance
* Pending approval requests occasionally displayed in Unsubmitted tab
* Projects in the timesheet from one workspace visible in other workspaces
* No visible chart when downloading Summary report as PDF
* Scheduled hours discrepancy in the Assignments report for Admin and Regular user
* Date picker on time off’s timeline shows one day more after reloading the page
* Forecasting chart not shown for one specific project
* Client with unassigned project not visible in client dropdown menu in Edit invoice modal
* Time off request rejected twice, resulting in one more day off in Balance
* Copy from last week for another user requiring adding the user to task when they are already added

## July 2025

### 🆕 Features

* [Simple or compound tax per invoice](https://clockify.me/help/projects/invoicing#set-taxation-mode-on-individual-invoices) – Set a simple or compound taxation mode on each individual invoice
* [Team filters](https://cake.com/updates/clockify-q2-2025#team-filters) – Apply filters on the Team page to customize the view and quickly find specific team members, edit their profiles, or assign roles
* [Pumble integration](https://cake.com/updates/clockify-q2-2025#pumble-integration) – Receive messages on [Pumble](https://pumble.com/) for the status of your submitted timesheets, time off balance or requests, and reminders to log or submit time.
* [Improved Windows app](https://cake.com/updates/clockify-q2-2025#improved-windows-app):
	* Upgraded auto tracker (auto start/stop with the app, or for a defined time range; timeline displays the whole day; search field shows suggestions)
	* Added custom color picker for projects
	* Added option to add a task estimate
	* Improved [preferences](https://clockify.me/help/apps/windows-desktop-app#preferences) structure
	* Undo deleting and discarding entries

### ✅ Fixes

* Filtering custom field type number, containing more than 16 digits not possible on the Reports
* Clicking on the Approval button in email does not filter the right user on the Pending tab
* Scheduled shared report contains billable information, while billable hours are disabled
* Summary report not showing the right currency after filtering through Clients
* One time entry left out from grouped time entries
* Summary report grouped by Project and Task shows visual issues when exporting four specific projects
* User unable to create assignment after deleting excess characters in the note field

## June 2025

### 🆕 Features

* [Multiple API keys](https://clockify.me/help/administration/profile-settings#manage-api-keys) – Improve security with various API keys for each integration, app, or add\-on, and manage them directly from Clockify

### ✅ Fixes

* User unable to delete the value from the link custom field set as required
* Project picker not showing full list of projects when there are more than 50 projects grouped
* Pagination on the Clients page doesn’t display the total number of clients
* User gets Approval reminders even if they have unsubscribed from receiving reminders
* User unable to assign tag to a duplicated time entry
* After adding custom field value, invisible custom field turns visible in projects
* Team filtering in Schedule not displaying selected group and a user who is not part of the group
* Reminders arriving for week before when Admin’s week start is earlier than the User’s
* Projects uncheck upon changing project status in Team page for selected Project Managers
* Invalid kiosk URL upon disabling the option for “kiosk login required”
* Exported excel of Summary report not always showing estimates
* Same project coming up twice in Timesheet search
* “Request time off” button is missing when creating a policy for a regular user
* Regular user cannot continue time entry with a task marked as done when task is not a required field
* No option limit for “Select” custom field type causing performance issues
* Regular users unable to change the project on the Calendar if the permission for billable status is set to ‘Admins’
* Team Manager unable to access automatically accrued annual policy on Balance tab
* Added tax amount of 9\.07% to total amount on old duplicated invoices with compound tax mode
* Holiday entries not created when holiday that starts in one year and ends in another
* Group search showing results only when typing the first word of the group name
* Total billable hours in the PDF Detailed report depend on show/hide amount
* Bulk edit doesn’t work for invisible custom fields that are set to be visible on the project
* Team manager able to see time off requests for all members while exporting the time off requests
* Total billable hours in the PDF Detailed report depend on show/hide amount
* Bulk edit doesn’t work for invisible custom fields that are set to be visible on the project
* Team manager able to see time off requests for all members while exporting the time off requests
* User unable to submit an expense for approval
* Approving second half\-day time off request results in error
* Shifting timeline of a Scheduled report with multiple milestones results in error
* Bar graph not changing with filter when date range is set to more than 1 year in Summary report
* Creating a workspace name and organization name with special characters not supported

## May 2025

### 🆕 Features

* Add members to projects when adding time for them – Admin can automatically grant project access to regular users by adding time for them
* [Private add\-ons](https://cake.com/updates/paid-addons#private-addons) – Create private add\-ons on the [CAKE.com Marketplace](https://marketplace.cake.com/) exclusively for your team or clients

### ✅ Fixes

* Changing start time on a long time entry adds one day to start date
* User doesn’t receive a warning message if they try to save a custom field with already existing options
* Assigning inactive users as Team Managers deselects assigned active users
* Custom field selection disappears upon task change
* Withdrawn timesheet remains uneditable
* Admin unable to edit Kiosk PIN and user’s PIN
* Removing task on grouped time entries causes rates to not apply correctly
* Admin unable to change user roles
* User unable to select/find a project while saving time entry
* Project shows users who are not part of the workspace
* Changing workspace to subdomain sets profile language to English
* Different totals shown when creating and editing assignment
* User unable to edit custom field

## April 2025

### ✅ Fixes

* Team Managers can’t mark time entries as “Invoiced” for users they manage
* Time discrepancy between ‘Time off’ in a summary above the bar chart and ‘Time off’ below the bar chart in Approvals
* Reminder to submit timesheet received by a user who submitted the timesheet
* Various issues for project picker and filters
* Loading issue in Scheduling table for Team Managers
* Owner unable to access pages available to Admins
* Dates in the Scheduling table displayed incorrectly when time period is from Sunday to Sunday
* Admin able to edit the Owner’s profile via bulk edit option
* Approval requests display incorrect amount of time off hours
* Expanding the view in the project/task picker with the collapse option enabled shows only up to 50 tasks
* Time off entries created for non\-working days
* Hourly time off not calculated correctly for daily/weekly capacity
* Various custom field issues
* Days added to timeline view after moving back and forth using arrows for a two\-week time period
* Export Assignees file from Kiosk not translated when app’s language is changed
* Regular user able to see entries of other users in the Detailed report
* Changing settings in Project estimate causes Forecasting issues
* Time off entries not created for previously rejected requests after policy updates to not require approval
* Published assignments with a milestone displayed when we filter view for unpublished assignments
* Error messages displayed when we click multiple times fast on the “Most tracked activities” time entry play button on the Dashboard page
* No approval button on an email notifying about requested time off
* Reminder for insufficient tracked hours received by a user who had time off
* Total negative expense amount shown as zero in exported project file
* Time off request showing 8 days instead of 9 days
* Time entry with negative value for start and end date
* Admin unable to send exported audit log report to their email
* Invoice ID spelled backward in downloaded invoice PDF file
* Default capacity not shown as 8h in Create assignment modal
* User receives new assignment notification even if notifying assigned users is turned off
* Holidays not sorted chronologically
* Reminder to submit email reflects Admin’s date range for users who have a different week start
* User unable to open Kiosk after copying its link to another device or new browser tab
* Time correction in recorded time tracker entries computes wrongly
* Approving all timesheets approved all submitted timesheets instead of just filtered ones
* User unable to submit a time off request for a Holiday including a non\-working day
* Bulk edit modal not showing default value of the custom field when only one entry is selected
* Selected projects in Timesheet not sorted alphabetically upon week switch
* Assignment showing one hour earlier in Calendar than actually scheduled
* Modal for editing past assignments not displaying correct rates
* Changing timezone from notification does not affect time tracker until page refresh
* Search time zone input filed keeps input after choosing time zone
* User unable to apply timesheet template
* User unable to download Summary report with sub\-grouping on
* Login with SAML2 results with infinite loader
* Copying the reports URL with custom field filter shows the results but doesn’t show custom field filter is selected
* Assignment’s note displayed split
* Invoice leaving 0\.01 CAD unpaid
* Team members dropdown in Scheduling keeps resizing after releasing mouse click
* Y axis in Shared report showing incorrect time numbers when opened via shared link
* Regular user able to save time into locked period with Undo deleted time entries
* Drag and drop stops working when time entry reaches midnight on the Calendar page
* Invited user unable to join a subdomain workspace
* Newly created long schedules don’t change period if drag \& dropped
* Copy as time entry action in Calendar doesn’t populate duration field
* Save button disabled in Timesheet when we have required custom field
* Scheduled Weekly Summary report graph includes previous week with zero value
* Time cannot be split when time off entry is continued from a previous one
* PDF Export not working for one workspace
* Individual Calendar entries always display start and end times in 24\-hour format
* Project templates don’t apply template color to projects
* Moved assignment results in shortening assignment by one day
* Team manager able to edit running time entry on Calendar page when they don’t have permission
* User unable to export Team page data in Excel
* Discrepancy between Scheduled weekly report and actual tracked hours
* Deleting assignment removes profile picture from selected user
* Task filter in Assignments Report not filtering tasks correctly
* Project Manager unable to see tracked time on projects they are managing in Reports
* Time off day not displayed on a Schedule \& resulting in error after user tries to make an assignment for that day
* Insufficient user information displayed in email for a submitted time off request
* Time entry missing in Timesheet but available in Reports
* User Custom Field Menu in Edit Profile can’t be expanded on Firefox Edge
* Half\-day Time off request did not create a time off entry
* Suggested time entry with custom fields doesn’t save custom field values in manual tracker mode
* Workspace not changed when user changes it from the extension
* App language switching back to English after clearing browser cache
* Description field not widened when additional text is added via Detailed report \[Safari browser]
* Information from the Outlook calendar takes 20 seconds to load
* Users not redirected to Timesheet after Time Tracker page has been hidden
* Can’t add users with accented letters in email on Team page

## March 2025

### 🆕 Features

![](https://clockify.me/help/wp-content/uploads/2025/03/custom-color-picker-1024x298.png)
* [Custom color picker](https://clockify.me/help/projects/creating-projects#color-picker) – Quickly apply your custom colors to new projects
* [Transfer a workspace](https://cake.com/help/account-basics/transfer-workspace-into-another-org/) between organizations in the CAKE.com Suite
* [Set time tracking reminders](https://clockify.me/help/administration/targets-reminders#set-up-timesheet-reminders) in line with the user’s work capacity or a custom number of hours
* Default work capacity for users changed to 8 hours
* Receive a warning in case of [overlapping Time off requests](https://clockify.me/help/administration/targets-reminders#key-considerations)
* Requests tab: Added filter for Specific member to view time off requests by date

### ✅ Fixes

* Mixing data on workspaces
* Selecting multiple tags at once in search results in only the last one being applied
* Timer not running when the app is translated to Dutch
* Team manager can see users in Schedule even if they do not have assignments on selected period
* Clock\-in on a Kiosk with default private project failed for users without access to the project
* Editing Holiday date from today to the future date doesn’t remove the Holiday entry
* Adding user to a Group doesn’t create time off entry on Holidays with automatic time off entries
* Users able to request time off via API on a policy that they are no longer assigned to
* Admins able to change Owner’s kiosk PIN via API
* Project Managers able to access projects they are not assigned to
* Delay on approving timesheets with large number of entries

## February 2025

### 🆕 Features

* [Item\-based taxes](https://cake.com/updates/clockify-q1-2025) – Choose the invoice items to which you will apply taxes
* Added logout URL for OAuth2 configuration, for users to set up redirection after logging out

### ✅ Fixes

* Team Manager sees people they don’t manage in Teammates dropdown in the Calendar
* ‘Insufficient time off balance’ error appearing when not expected on policies with allowed negative balance
* Accessing Reports results in an error and logout
* Already existing invoices not visible \& User unable to create a new one
* Time off entries showing as billable in detailed reports, even though project and task are non\-billable by default
* Client name missing in the ‘Group by’ table when client filter is used in Summary Report
* Double error message appears when creating a project with a name that already exists
* Non\-billable time entry displayed as billable to regular users on the Reports page
* Holiday entries not created for invited users
* Regular users can Archive/Delete projects they created after permissions changed to ‘Admin only’
* Regular users can see billable hours for others when the Billable hours switch is off
* Timer stuck at 0 when using C to continue last entry while the timer is already running
* Launching the kiosk does not log out the user when ‘Kiosk login required’ is off
* Changing projects on the timesheet not possible when Force timer is enabled
* Custom fields on the entry not updated when the project is changed
* Notifications in the app not consistent with the language currently in use

## January 2025

### 🆕 Features

* [CAKE.com Account](https://cake.com/updates/cakecom-account): Log in with one account to all your Workspaces, across Clockify, Plaky, and Pumble
* [Organization](https://cake.com/updates/cakecom-account#cake-organization): Group all your Workspaces, users, and subscriptions, across Clockify, Plaky, and Pumble

## December 2024

### 🆕 Features

* Log in or sign up with your Apple account

### ✅ Fixes

* User able to manually change assignment date to a locked (time off) date
* Blank space shown instead of a zero in the capacity column in the exported Attendance report
* Wrong date format on time off balance update email
* User unable to create or delete custom fields
* Timeline and Requests page showing more days than the Owner requested for invited users
* Weekly reports sent on a day that is not set as a start day of the week
* User in Asia/Manila timezone shown on Timeline without a time off request
* Multiple options with the same name selected in the “Select” and “Multiple select” custom fields
* Requesting 2 days off marks request as 3 days
* User group missing from timeline dropdown
* Bulk editing time on entries later than the current time moves them from ‘Yesterday’ to ‘Today’
* Unsubmitted time date range not displaying time entries in the correct weeks
* Weekly target emails not sent on the user’s week start day

## November 2024

### 🆕 Features

* [Undo deleted entries or expenses](https://cake.com/updates/financial-planning#undo-delete) – Undo deleted time and break entries, or expenses if you accidentally delete them

### ✅ Fixes

* Project status tab not visible to its project manager
* User unable to archive or delete duplicated projects
* Exporting audit log failed
* Policy update notification email displaying a wrong name
* User unable to edit user fields
* Timeline shows no visual difference between half\-day off and a full day off
* Assignments Report displaying scheduled hours only when a decimal format is active
* Option to create a task appears when the user doesn’t have permission to do so
* Kiosk not showing projects when a user presses the Switch button
* Username created with only empty characters
* Team filter in Reports not showing all users

## October 2024

### 🆕 Features

* See [billable amounts and costs](https://cake.com/updates/financial-planning#finance-scheduled-amount-cost) for users, projects, and assignments on a Schedule
* Team Managers and Regular users can now [create assignments](https://cake.com/updates/financial-planning#finance-team-scheduling) for themselves
* Users’ assignments will be created on their first working day if they are assigned on their non\-working or time off days

### ✅ Fixes

* Task estimate shown in Summary report when Project settings have a manual budget estimate
* Bulk editing of custom fields does not update the values ​​of some custom fields
* The cursor does not appear when searching for a time zone
* Improper date display in year\-month view
* Users unable to stop the break timer after Breaks are disabled
* Requests that were previously rejected become approved if ‘Required approval’ is subsequently turned off in the Policy
* Approved Time Off not showing on Timeline for users without assigned Group
* Exports of Detailed reports in Excel and CSV not showing projects and clients
* Deactivated users notified about the workspace switch to the subdomain
* Time entry showing \+1 indicator incorrectly
* Screenshot reappeared after it had been deleted
* Date format in Clockify weekly report email mismatched with the format in the user’s Preferences
* Invoice PDF visual bug on address field when text is displayed right\-to\-left
* Filtering team by email does not work, or shows users who haven’t joined yet
* Currency missing from some items on Expense report downloaded from Invoice
* Duplicated rows without a task in Assignments reports
* Status indicator for approval per project not visible when the page is resized
* UI on the Approval tab different on Firefox and Chrome
* Expense Report page showing a random number
* Failed to download Expense report from an Invoice sent via email
* Custom Field link disappears if we edit the time entry by pull and drag action in the Calendar
* Kiosk showing a default display photo beside the user name instead of the initials
* Admin does not see projects in the project picker on the Scheduling page
* Timesheet template applied everything except one task
* User custom field visible in ‘Add time for others’ section in Detailed Report
* Team Manager unable to edit start time on entries in Detailed Report
* Blank page displayed after a user tries to open a Kiosk on an iPad
* User can’t see templates on Timesheet when one template has two entries with the same project (one with task, one without task)
* Adding the company address in the Invoice requires a refresh to be saved
* User unable to stop running the timer due to the “currently running time entry doesn’t exist on workspace” error
* User custom fields not visible in Detailed Report
* Changing profile language does not translate “This week” and “Last week” on the Unsubmitted tab on the Approval page
* Searching categories in the Create expense modal results in a blank dropdown
* Unavailable HH:MM:SS format in reminders
* Task assignees on projects showing duplicated names
* Assigning all users as Team Managers too slow when there are a lot of users
* Applying timesheet template on a locked week deletes timesheet data from that week
* Shared report chart shows incorrect data

## September 2024

### 🆕 Features

* [Auto tracker grouping (Mac, Windows)](https://cake.com/updates/auto-tracker-grouping) – See the breakdown by app and filter recorded entries by keyword.
* [Budget forecasting](https://cake.com/updates/financial-planning#finance-budget-forecast) – Forecast whether you will go over the estimated budget.
* iOS – Manage Time off requests from your phone.

### ✅ Fixes

* Time off days not crossed out when creating or editing assignments
* Exported balance report not showing an hourly time off policy assigned to a group
* Error 400 appeared on the Assignments report after clicking ‘Show users without time’
* User not automatically verified if signed up with SSO through the email link
* Error 500 on the Schedule/Team page after Holiday assignees are changed to ‘Everyone (including new users)’
* Timesheet template not applied in case time was created through timesheet and workspace has custom fields
* Bulk edit on project’s rates displayed correctly only after refresh
* Custom fields with select options not loading on the Time Tracker page
* Custom fields on random entries in Detailed Report do not show all options
* Multiple visual and functional Approval page bugs
* Project Managers redirected to their time tracker when approving timesheets
* Project alert sent every hour
* Numerical value for the User Custom Field disappears after saving
* Banned users can log in and use the app
* PDF of a Summary Report grouped by ‘Group/Project/Task’ shows empty pie charts
* Time off requests not displayed correctly on the Approval page
* The user cannot start the timer on the favorite project if he previously tried to add manual time entry without the required project
* When ‘Force timer’ is on, we can edit everything except start/end time on the Time tracker and Calendar page, but the same thing on Timesheet is disabled
* Team Manager not seeing “Approvals” in the sidebar
* Regular users able to see and click on checkboxes next to names on the Team page
* Kiosk login page visible even though the Kiosk is disabled in the workspace settings
* Duplicated entries shown twice in the suggested entries list
* Regular user can’t track progress on a private project with task, even if he has access to that project (via user group)

## August 2024

### 🆕 Features

* [Paid CAKE.com Add\-ons](https://cake.com/updates/paid-addons) – Developers can now create and release paid add\-ons for other Clockify users
* [Week start adjustments](https://cake.com/updates/clockify-q3-2024#global-week-start) – Owners or Admins can now set week start day on a workspace level for all workspace members

### ✅ Fixes

* Starting a timer on “Most tracked activities” in the Dashboard returns an error
* Last month’s expense report empty when exported to PDF
* Shared reports do not display clients attached to projects
* New policies not applied to a user after changing their Group
* Project Manager unable to create a new project from a template
* User able to add time to a private project that they are not a part of
* Total amount incorrect when using Compound Taxation mode in the ‘Send Invoice’ modal
* Regular users, Project or Team Managers able to create time off entry by clicking ‘Play’ on a previously created one
* Users not set in alphabetical order on the project Access tab
* ‘Group by’ filter in the Summary Report showing multiple rows for the same group
* Adding a user as a Project Manager to all projects is not being accepted by the system
* Creating two same reminders possible through editing previously different ones
* 400 status code when updating currently running entries and custom fields are not copied on autocomplete
* Invoice with compound taxes not displaying correct balance after partial payment is recorded
* QuickBooks: User getting Sync\_fail error while sending entries from Detailed Report
* User unable to change email address while 2FA is active
* Admin not being able to import a CSV file
* User status filter not working on time off requests
* Team manager unable to add time entry in the Timesheet for one user
* Time off request date filter not working as expected in the \-6 America/ Regina time zone
* User can see a project status even if the permissions ‘Who can see project’ status is set to ‘Admins’
* Changing Project/Client/Task name not reflected everywhere on the Workspace settings page
* Wrong redirection under “your profile settings” link for 2FA setting
* Users are not able to change the entered e\-mail address in the ‘Send Invoice’ modal
* User displayed on the date range when they do not have an assignment
* Assignees filter on Holiday policy showing only Groups
* A dash not displayed when entering 0, 0\.0, or 00 in the rate field

## July 2024

![](https://clockify.me/help/wp-content/uploads/2024/07/approval-project-manager-min.png)
### 🆕 Features

* [Time approval by project managers](https://cake.com/updates/approval-project-manager) – Your project managers can now review and approve time and expenses on their projects.
* [Apply multiple timesheet templates](https://clockify.me/help/track-time-and-expenses/timesheet-view#creating-new-timesheets-quickly) – Combine time and activities from multiple timesheets templates to quickly populate your daily and weekly timesheets
* [Assign expenses to tasks](https://clockify.me/help/track-time-and-expenses/expenses#adding-expenses) – Add an expense to a task and see it reflected in budget
* [Improved overtime column in Attendance report](https://clockify.me/help/reports/attendance-overtime) – Overtime column in Attendance report now only shows values greater than zero. Work column includes a warning symbol for users who worked less than their capacity, with a hover message showing how many hours are left to work.
* Searching by Groups within the Team page

### ✅ Fixes

* Can’t export time off requests
* Discrepancy in hours in automated weekly reports
* Expense amount in audit log doesn’t reflect when unit price in expense category is updated
* Some time entries don’t pick up default custom filed values
* Tracked time on a project is not updated after that project is removed via Calendar
* Clicking on a user’s approved request in Archive doesn’t work
* Some approved time off requests don’t show up on time off timeline
* Custom field number disappears when pasted
* When OAuth is enabled via Okta, workspace login gets locked
* Holidays for deactivated users show up in time off timeline, creating clutter
* Regular user can’t change task’s billable status (if they have that permission)
* Unsubmitted time tab in Approvals doesn’t list users who don’t have time but have expenses
* API: /users/info not returning all users in special cases
* Users not getting email to verify their account after accepting workspace invitation
* User can not download expense reports through invoice mail while on a subdomain
* Double toast appears when you profile name or photo is empty
* Workspace cost rate accepts blank value
* Data duplication in user custom fields
* Add members popup is stuck when adding multiple members
* Regular user can add themselves as a task assignee
* When you create a new project, you can’t edit project details without first refreshing the page
* Bulk editing projects’ amount to “0” doesn’t work on the Project page
* Kiosk link invalid after 24 hours
* Archived tags removed from existing entries
* Reports filter for tasks shows private projects/tasks to managers not managing the private projects
* Exported Report contains filtered values even though the user has not clicked “Apply filter”
* Time Off Request Approval link redirects the Admin to the wrong workspace
* Users able to save time entries longer than 999h by splitting long\-running time entries
* Tag dropdown not showing pagination
* Company holidays not blocked out on the Scheduling page
* Limited Users tab disappears on the Team page upon entering an invalid name in the search box
* Running a timer through the Play button on the Dashboard page not working properly
* User unable to log in to the workspace after the Data region transfer
* Workspace still locked after Data region transfer
* User unable to activate the Kiosk through the Kiosk page
* Today’s time entry saved on yesterday’s date
* Scheduled report link opens a blank page
* Holiday not included in week’s capacity
* Searching for limited users cannot be done by name
* Time Off Balance and Request export shows deactivated users
* Working days not exported for users added a long time ago
* Alerts sent and counting all tracked time on a project disregarding monthly budget reset
* Report showing blank page when exported as PDF
* Decimal numbers cannot be imported into custom fields

## June 2024

### 🆕 Features

* API: List out information about limited users
* Added ‘Test configuration’ button for SSO setup, both Saml2 and OAuth2
* Passwordless login for Kiosk (log in via 2FA email code)

### ✅ Fixes

* Wrong color of a chart in the ‘Group by’ section when the Summary report is exported in PDF
* Hourly time off request displayed in two time zones to an Admin due to different time zones of the requester and Admin
* Filtering Detailed Report for custom fields ‘smaller than’ and “larger than” values does not show results
* A difference of 0\.01 between the amount on the Expense page and the amount on the Approval page
* Unable to verify the pending email change, if the user has a pending invite to a workspace
* Screenshots on Mac and Windows not displayed correctly
* Alerts emails arriving delayed and only at hh:30
* Team Manager sees Task filter on Assignments report
* Amount column does not disappear when the “Hide amount” option is selected in the Detailed Report
* Enable 2FA button on the Force 2FA popup not working
* Scheduled shared report emails show 0 as billable time
* Workspaces in transfer able to install add\-ons
* Excel export doesn’t follow the date format
* Restarting a time entry adds additional time to other time entries
* User unable to stop the timer – permissions error
* Ongoing timer lagging or frozen on the Time Tracker page

## May 2024

![](https://clockify.me/help/wp-content/uploads/2024/05/time-off-entry-1024x341.png)
### 🆕 Features

* [Time off entries](https://clockify.me/help/track-time-and-expenses/track-holidays-time-off) – Create time entries from time off requests so they appear in time reports
* Enhanced topbar navigation (there you can now find Workspace Settings, workspace switcher, app switcher, and subscription management)
* **API**: Added [Custom Fields creation](https://docs.clockify.me/#tag/Custom-fields/operation/create)
* **UI updates**: New styles of the Status and Alerts banners

### ✅ Fixes

* Marking an entry as a break in Detailed Report not possible if the Project field is required
* Editing duplicated time entries reverting to original value on slower networks
* Assignments made after March 31st appear as scheduled a day later on the Calendar’s header
* Daily time tracking reminder sent to a user on their time off day
* User unable to turn time entry into break entry in the Detailed Report when the project is a required field
* PDF Expense report not containing existing expenses with an archived/deleted category
* Users unable to save multiple Workspaces with the same name, or name a Workspace with a single character
* Recorded GPS locations at the bottom of the Activity list cannot be deleted
* Time entry with quotation marks in the description exported from a Detailed report in CSV shown as two separate fields in the pivot table
* Detailed report export in CSV or Excel always showing a ‘Type’ column
* Reactivated users not able to clock in to a kiosk
* Filtered tasks/projects not displayed in the dropdown after the dropdown has been closed and reopened
* When lock time before “today” is enabled, the user can create an entry that was started before “today”
* Audit log showing wrong custom fields for displayed time entries
* Duplicated estimates fields on the exported Summary report (CSV, Excel)

## April 2024

![](https://clockify.me/help/wp-content/uploads/2024/04/split-time-1024x300.png)
### 🆕 Features

* [Split time](https://clockify.me/help/track-time-and-expenses/split-time-entries) – Create two separate time entries from one
* [Data region transfer](https://clockify.me/help/getting-started/data-regions#change-region) – Transfer data from global to regional servers, or from region to region
* [CAKE.com Bundle plan](https://cake.com/bundle) – Get time tracking, project management, and team communication app for a special price and save 53%
* [Export team data](https://clockify.me/help/administration/export-user-info) – Download a list of all your members and their details in CSV \& Excel

### ✅ Fixes

* Date on the Tracker page shows a day behind if a timezone is set to Pacific/Auckland
* Automatic accrual of days under a specific Time off policy with disabled accrual
* Editing entry’s start time on a workspace with h:mm time mode changes the end time by one minute
* Admins able to allow “Require 2FA” after clicking on a resend code option
* Time off balance for a specific user is not updated correctly after an time off request on desktop
* Asia/Almaty time zone displayed incorrectly (\+1 hour)
* Favorite tasks not listed on top when creating an entry in the Calendar
* Unsuccessful import of a file with archived tags to a workspace where tags are a required field (Chrome, Firefox, Safari)
* Exporting members from the Team page resulting in “Download failed” error after loading
* Attendance report page infinitely loading
* Regular user unable to save a project as a template
* Navigating between custom fields with the TAB button while the timer is running sends the cursor to the first field after each successful save
* Changing expense date does not trigger changes in project status
* Regular users able to change task assignees or delete tasks via API
* Admins whose Day start is set to 22h don’t receive tracking reminders
* Sorting on the Accounts tab in Workspace settings not alphabetical
* Prevented double time off requests on slow networks
* Durations on exported Summary and Detailed PDF reports rounded on two instead of four decimal points
* Renamed label for “Projects” not reflected on the Scheduling drop\-down menu
* User able to change the billable status of Expenses even after the option for billable hours is deactivated
* Kiosk logs out after 24 hours even though is set to expire after 999 hours
* Users able to mark a required custom field as invisible after making it required
* Searching by email on the Team page does not return any results
* Regular users unable to add time to private projects they have access to, after copying last week’s timesheet
* Time off policy report exported from the Balance tab showing user removed from that policy
* Exported Team report does not show groups for users who have another active workspace
* Break column not visible in the exported Attendance report

## March 2024

![Favorite time entries in Clockify.](https://clockify.me/help/wp-content/uploads/2024/03/march-2024-favorite-entries-1.png)
### 🆕 Features

* **[Favorite entry](https://clockify.me/help/track-time-and-expenses/favorite-time-entry)** – Pin favorite time entries to the top for a quick start
* Group the Assignment report by groups
* See available hours (based on user’s capacity) in the Assignment report for users or groups
* Differentiate between regular time entries and break entries in your reports
* Expense report sent via invoice email now requires a PIN code to access, for added security

### ✅ Fixes

* Admin can’t return to a Kiosk start page when launching a Kiosk they’re not part of
* Marking tasks as required during a “Clocked in” session on a Kiosk, shows users the “Clocked in” screen when switching tasks instead of the “Switched project” screen
* Filtering “Inactive” users on Time Off tabs doesn’t show a consistent list of users when switching tabs
* Cloned time entry created in the Calendar page by dragging not counted in the tracked column of that project’s progress page
* Changing start week to a different day doesn’t reflect in the date picker of an already created shared report
* Setting the Project’s member rate as 159\.14 changes it to 159\.13 when returning to the Project’s Access page
* List of payments in Invoices displaying the default Workspace currency instead of the specific currency for that client
* Yesterday’s date does not appear crossed out when creating or editing a time entry for regular users after admins lock time before “Today” and then enable Expenses
* Task disappearing from the schedule when switching between the Projects and Team tabs on the scheduling page
* Added task budgets not visible after switching from the Tasks tab to the Progress tab until the page is refreshed
* Project budget estimate showing its previous value in the Status tab after its been set to zero, or after its been turned off and turned on again
* Bulk\-selecting projects or archiving a project in the Projects tab sets their time estimate to zero until the page is reloaded
* Running time entries in the Calendar missing the stop icon
* Two time off badges displayed in the “Planned” section of the weekly Calendar view instead of one after a user makes a time off request for today
* Project template dropdown not responsive if a user does not have any project templates
* An infinite loader displayed on the Time off page on the balance tab when all policies are archived
* Specific receipt showing up on the next page when a PDF Expense report is exported
* Project time estimate different in the exported Summary report from the one in the project status tab
* Entries imported via CSV file not having the “Import” label in the Audit log
* Timesheet withdrawn email showing a random regular user as withdrawer after the approval period has been changed by an Admin
* Client picker not listing all the clients while creating an invoice, if there are more than 50 clients in the workspace
* User dropdown not listing all the users in the Detailed report while bulk editing, if there are more than 50 users in the workspace
* Pie chart in the project status tab showing time estimate instead of a budget estimate, when the user sets the budget estimate manually
* Timesheet columns and table header misaligned on higher zoom and when tags are a required field
* Removing a project with a task on an existing time entry in the Detailed report displays that currency type as “null” before refreshing the page
* “Delete screenshots” modal not showing correct subtracted time after a regular user deletes a screenshot
* Active users converted to inactive users able to access shared reports
* Start time in GPS tracking recorded twice
* Unsubmitted expense not present on the Approvals page/Unsubmitted tab if the Admin has already approved time entries and expenses for the same period
* Incorrect number of visible custom fields while moving fields from available to visible column, and vice versa
* Project manager can add milestones to private projects they don’t have access to
* Task with a duplicated name saved until the page is refreshed, or until rates are changed

## February 2024

![](https://clockify.me/help/wp-content/uploads/2024/02/task-scheduling-min.png)

### 🆕  Features

* [**Schedule tasks**](https://clockify.me/help/projects/scheduling#schedule-projects-and-tasks) – Plan tasks and your team’s labor hours on a timeline.
* **Kiosk launch settings** – Allow managers to launch a kiosk, or turn off login requirements in workspace settings so anyone can launch it.
* Bulk archive/delete clients and tags
* Start breaks via API

### ✅ Fixes

* Team Managers can see Team Dashboard for members that are not in their team
* Clicking on the Timesheet field shows the decimal value multiplied by 100
* Attendance report not sorting correctly by date
* Assignment report not sorting projects alphabetically and months chronologically
* Entry duplication errors when hitting the Add button multiple times
* Owner’s time entries created via kiosk are always marked as non\-billable
* System can send entries to QuickBooks that are longer than QuickBooks’ maximum duration and that have been already sent
* Time Off policy assigned to a group doesn’t apply to all members of the group
* TaskID error showing up when adding a user to the schedule
* Custom fields refusing to set as “no value” after deleting a previously set value
* Not enough details in error message when CSV import fails
* Can’t import CSV file on Windows 10 Firefox
* Projects with special characters (\<, \>) can’t be deleted without removing the Note
* Incorrect balance and status on old invoices created before the partial payment feature
* Spellcheck not working on some pages
* Unable to go back from project budget to time estimate if a time estimate is set
* Turning on/off 2FA in Profile settings logging users out
* The project template doesn’t apply assigned manager roles while creating new projects
* “Copy as time entry” from Calendar events not working for regular users
* “Filter by Access” on the Project page doesn’t recognize group\-assigned projects
* Custom colors don’t apply to projects
* Moving and resizing entries in the Calendar opens a pop\-up to edit an entry instead of moving it (Firefox)
* Summary Report not showing correct graph for a 1\-year time range
* Expenses list not showing up in the PDF report
* Time entry updates made through a Calendar are not saved
* Regular users can’t create entry via Timesheet on private projects
* Tasks can be deleted by their project managers even though the “Who can create tasks” permission is set to “Admins”
* Users able to set a password using blank/space characters
* “Download Failed” pops up when exporting Excel or CSV of a Detailed Report including “Employee ID” as an active custom field
* Unable to add a new project on the Scheduling page when it tries to load too many projects

## January 2024

### ✅ Fixes

* Missing translations on some pages
* Filtering members doesn’t work if members are added via project’s Access tab
* When selecting a project from the Description field on the Time Tracker page, the custom field doesn’t populate with its default value
* Calendar not showing the correct date after being in “sleep mode” for one or more days until the page is refreshed
* If a time off request is approved in one time zone and then changed to another, the calendar and scheduling pages show two time off days instead of one
* Project monthly estimate not including time entries that have same start time as start time of estimate
* Field formatting error when copying and pasting task budget number to another
* “Verify email” banner is displayed for already verified users
* Downloading an invoice in Hebrew inverts descriptions

## December 2023

![](https://clockify.me/help/wp-content/uploads/2024/02/export-invoice-list-min.png)

### [🆕](https://emojipedia.org/new) Features

* [**Export invoices**](https://clockify.me/help/projects/export-invoices)  
Download a list of all your invoices in CSV and Excel.

### ✅ Fixes

* Unable to set 0 as cost rate
* Can’t group by tag/month in Summary report
* Custom fields: Multiple select causes an issue with Detailed report display
* Expenses: Uploaded file misses icon
* Time off: Request displayed in policies history, but not in Requests tab
* Day missing from weekly report email
* Detailed reports: Discard doesn’t stop the downloading
* Approvals: Unable to submit time through Unsubmitted tab
* Time off shows deleted and limited users
* Can’t change policy for a user if they have accrued time
* Audit log report takes too long to generate
* Projects and project page not showing tracked time and amount
* Projects: Searching in client/access filter prompts password update
* Pressing “n” doesn’t start the timer immediately
* Font not rendered properly when exporting Summary report PDF
* Calendar shows time entries as overlapping if they have similar start/end
* Approvals: Not able to submit time if user has only expenses and no time
* Timesheet: Save button is disabled after adding description
* Approval: Approved entries are displayed as not approved
* Users can still access link of deleted kiosk
* Time tracker: Placeholder for required description can be selected and copied
* Expenses: Amount field is empty after entering a 4\-digit number
* Can’t bulk edit colors on projects
* Rows in Timesheet are saved even if some required field is missing
* Attendance report: Incorrect overtime in Excel export
* Timeline in Time Off is not properly displayed
* Attendance report: Team manager filter is not working
* Scheduling: Scroll bar missing
* Weekly report: Total amount earned is missing in PDF export
* Can’t sort shared reports

## November 2023

#### What’s new

* [Multiple currencies](https://clockify.me/help/track-time-and-expenses/multiple-currencies)
* [Recurring estimates/budget](https://clockify.me/help/projects/project-budget#recurring-estimates) (reset weekly/monthly/yearly)

#### What’s fixed

* Scheduling: In edit modal, some days are displayed as unavailable
* Shared weekly report doesn’t show all time entry details
* Screenshots are not properly loaded on first request
* Edit holiday screen won’t open
* Can’t send some time entries to QuickBooks
* Loading detailed report takes too long

## October 2023

#### What’s new

* Kiosk: [Select project/task](https://clockify.me/help/track-time-and-expenses/track-time-on-kiosk#choose-project-task)
* Approvals: See users without any tracked, submitted, or approved time in a week

#### What’s fixed

* Time off balance and history is out of order
* Tag picker won’t open when adding time for others
* Scheduling: Duplicated projects on Team tab
* Weeks sorted incorrectly in Assignment reports

## September 2023

#### What’s new

* [Export projects (Excel/CSV)](https://clockify.me/help/projects/exporting-projects)
* [Track breaks](https://clockify.me/help/apps/mac-desktop-app#tracking-breaks) (Mac, iOS, Android, Windows)
* New column in Detailed report export: Show who approved time (CSV, Excel)

## August 2023

#### What’s new

* [Track breaks](https://clockify.me/help/track-time-and-expenses/breaks-web) (web)
* Auto tracker improvements:
	* Resize and sort columns
	* Search time entries
	* Data storage limit extended to 45 days
* [Start/stop timer widget](https://clockify.me/help/apps/android-app#tracking-time-via-widget) (Android)

#### What’s fixed

* Details on hover for certain dates is not visible in Summary report chart
* Expenses: Can’t upload receipt as PDF
* Projects added to Scheduling won’t appear in Calendar
* Time off: Requests for policies in hours are not properly displayed

## July 2023

#### What’s new

* Time off: [Assign colors to time off policies and holidays](https://clockify.me/help/track-time-and-expenses/create-manage-time-off-policy#create-and-manage-policies)

#### What’s fixed

* Links in custom fields are not clickable
* Billable status not inherited correctly on some entries
* Summary report: When grouped by tag, some tag combinations are listed twice
* Summary Report chart not displaying correct hours
* Single sign\-on: Filled out fields for SAML2 configuration are not displayed in UI

## June 2023

#### What’s new

* Invoicing: [Record payment](https://clockify.me/help/projects/invoicing#record-payment) (plus new “Partially Paid” status)
* Approval: Edit submitted time entries and expenses directly from the Approval page

#### What’s fixed

* Time off: Approval emails are sent twice
* Time entry slightly shorter if moved or copied in Calendar view
* Required custom fields that don’t have default value cannot be edited in Workspace Settings
* Summary report: Long decimal display in CSV export

## May 2023

#### What’s new

* Summary report: See project breakdown in bar chart
* Invoices: Smarter invoice ID generation
* Time off: Request time off in 15\-minute increments
* Kiosk: Search users

#### What’s fixed

* Not possible to save negative amount for expenses
* When exporting Attendance report as CSV or Excel, wrong date format is displayed
* Project manager can’t see projects on Scheduling
* Discrepancy between total amount on Time tracker and Dashboard when decimal format is turned on
* When assigning all active projects to Project manager, archived projects are selected as well
* Project managers are unable to add users to project they manage if they can see only their own time
* Audit log doesn’t record expense approval

## April 2023

#### What’s new

* [Attendance \& overtime report](https://clockify.me/help/reports/attendance-overtime)
* Mark tasks as Done when archiving a project

#### What’s fixed

* One\-day time off request are displayed as two in Timeline tab for UTC time zone
* Break entries are not exported Detailed report Excel or CSV
* In some cases, Calendar displays weekend time as ‘scheduled’ even if not set on Scheduling page
* Project templates don’t carry over estimates
* During single sign\-on configuration, incomplete URL is displayed in Entity ID field
* Can’t sort by progress on Projects page

## March 2023

#### What’s new

* [Export time off requests](https://clockify.me/help/track-time-and-expenses/export-time-off)
* [Bulk edit users](https://clockify.me/help/administration/manage-multiple-members-time-tracking-settings)
* [Customize export](https://clockify.me/help/reports/customize-exports): Show Date of Creation and Date of Approval for each time entry (CSV/Excel)
* Indicator when a time entry spans multiple days
* Invoices: Attach and download invoice’s expenses
* Approval: See person’s time off when approving timesheets
* Scheduling: Project managers can add milestones

#### What’s fixed

* Enabling task filter causes error for some users
* Task assignee picker shows active and archived users regardless of selected status
* Monthly approval causing blank Timesheet for some users
* Time tracker page adds extra minute when editing time entry
* Importing data to workspace throws an error for some users
* Team member filters out users, but some that are not part of the team still appear

## February 2023

#### What’s new

* Selected items in lists are displayed on top
* Screenshots: Option to capture in high resolution

#### What’s fixed

* Scheduling page not loading for some users
* Regular user cannot sort projects by progress
* In Timeline tab in Time off page, table header with dates is not visible on scroll
* For some users, export of detailed report fails for very longer date ranges
* Notes are not displayed in invoice PDF
* Summary report chart changes colors after PDF export
* Schedule: Search is not working on Projects and Team tabs
* Category filter for expense reports doesn’t show archived categories

## January 2023

#### What’s new

* 

#### What’s fixed

* Time on Detailed report page not sorted properly in PDF, CSV and Excel export
* Weekly report is empty if billable hours are turned off in the permission settings
* Reminders are sent to users that don’t have that feature turned on
* Admin not receiving request approval email if user doesn’t have a Team manager
* Updated time entry in audit log displayed as approved and invoiced

## December 2022

#### What’s new

* [Forecasting](https://clockify.me/help/projects/forecasting)
* Scheduling: [Weekly capacity](https://clockify.me/help/projects/scheduling)
* Projects: [Bulk edit tasks](https://clockify.me/help/projects/creating-projects#add-and-edit-tasks-in-a-bulk)
* Approval: [Monthly time period](https://clockify.me/help/track-time-and-expenses/approval)
* Expense report: [Customize PDF export](https://clockify.me/help/track-time-and-expenses/expenses#expense-report)
* [Audit Log](https://clockify.me/help/administration/audit-log): Track changes for Expenses
* QuickBooks: Support for Clockify’s limited users
* [Alerts](https://clockify.me/help/projects/alerts): Set custom percentage
* Choose data formats (number and currency)
* Quickly create new tag in tag picker
* New regional server: [Australia](https://apse2.clockify.me/en/signup)

#### What’s fixed

* User randomly logged out and can’t log in via 2FA until browser cache is cleared
* Wrong error message when a user deactivates and reactivates kiosk
* Modal stays open when a user goes back/forward within the same page
* Date range goes over the limit if longer than allowed date range is selected
* Missing search bar for custom fields with select/multiselect dropdown
* Tags not visible on medium\-sized screens
* Group members don’t see all shared reports on Shared reports page
* Project estimate not responsive on “Project settings” tab
* After refresh Budget column disappears in Tasks tab in Project settings
* With sidebar collapsed, user has no permissions to access workspace settings
* Outlook Calendar connection fails in some cases
* Total time in Time tracker doesn’t change for monthly and semi\-monthly period when new entry is added
* Reminders display wrong assignees
* Wrong number format rounding on Schedule page
* Old policies don’t include limited users
* Expenses with receipts in PDF are not included in Expense report’s PDF export
* Note added to reports in “Customize exports” are not saved
* Some users have issues with creating projects through templates
* User not able to submit time off request for a time policy in hours
* User gets error if generating detailed report for previous year

## November 2022

#### What’s new

* Export [expenses](https://clockify.me/help/track-time-and-expenses/expenses) and receipts in one PDF file

#### What’s fixed

* Some users are unable to connect to QuickBooks integration
* Resizing or moving time entry on Calendar page sometimes fails
* Can’t filtering by client on Projects page
* Calendar page not displayed properly if there are a lot of events in the Outlook calendar
* Calendar icon on Time tracker page displays wrong date
* Multiple issues with deleting time entries from the Timesheet page
* Wrong dates on Approvals page
* Some billable project entries displayed as non\-billable
* Error when user clicks the “Send reminder” button for sending a reminder email for invoices
* Total amount not displayed in PDF export if billable amount is unchecked in Detailed export settings
* If user selects “Today” as total time, there is a mismatch of total hours on Time tracker page
* “Save” button on Timesheet page disabled, but all required fields are filled out
* All projects are listed in picker on Invoices page when the selected client has no projects
* Reports take too long to load, in general
* For some entires, billable amount is displayed as 0
* Clients are listed in random order
* Invoice field glitches if multiline description is added in invoice item field
* Invoice emails are not sent immediately
* Timeline for Time Off is displayed broken when there’s a lot of data

## October 2022

#### What’s new

* [Regional servers](https://clockify.me/help/getting-started/data-regions) (EU, UK, USA)
* [Scheduled vs tracked report](https://clockify.me/help/reports/assignments-report)
* [Send invoices to clients](https://clockify.me/help/projects/sending-invoice-emails)
* [Invoicing](https://clockify.me/help/projects/invoicing#sort-by-time-entry-or-expense-details): More sorting options for items

#### What’s fixed

* End time on “Time tracker” page not displayed correctly
* Regular users can’t see “Invoices” page with “Project/Team” page hidden in permissions
* Manually changed time returns to original value
* “Next” and “Previous” buttons not working properly in Calendar view
* Entry rate is sometimes missing when entry is created
* Discrepancy with expenses on “Approvals” page for minus time zone
* Member of the private project not seeing the project on their side
* User can’t add Client Note by using API
* Client filter on Reports page not working properly

## September 2022

#### What’s new

* Scheduling: [Repeat assignments](https://clockify.me/help/projects/scheduling)
* Pomodoro: [Focus mode](https://clockify.me/help/track-time-and-expenses/idle-detection-reminders#pomodoro-timer)
* Allow half day and hourly time off across multiple days
* Resize columns on Detailed report and Projects page

#### What’s fixed

* Time zone mismatch when sending time entries to QuickBooks
* When you leave the Time tracker page open over night, the date picker doesn’t add time for today
* Clicking on a billable sign takes a second or two to register
* “Week already submitted” error when submitting expenses for approval
* Sorting by amount not working for specific grouping combinations
* When copying previous week’s timesheet, Monday isn’t copied
* Inconsistent heights of bar charts on the Dashboard
* Project missing on print preview of approved Timesheet week
* Team manager can’t see users without time in weekly report
* Indefinite load for summary reports with yearly date range
* First working day not Start day from Profile settings
* Time off requests not submitted properly after policy changes
* Admins, Team managers and Specific members don’t receive emails of withdrawn time off request
* Some users don’t receive weekly report

## August 2022

#### What’s new

* Invoicing improvements
	* Sent invoices with past due date get automatic overdue status
	* Filter invoices (by status, client, issue date, amount, bill from company, and ID)
	* Sort invoices (by ID, client, issue date, due date, status, and amount)
	* Add line break in invoice item description
	* Allow specific users to manage [invoices](https://clockify.me/help/projects/invoicing)
* Favorite projects and tasks (Windows app)
* Rearrange items in sidebar
* Mark assignment in [Schedule](https://clockify.me/help/projects/scheduling) as billable or nonbillable
* Set the amount of allowed negative balance for a time off policy
* Hide completed tasks on Project status page
* Hide weekends from Calendar page
* Choose rounding setting directly in reports

#### What’s fixed

* Filter weekly report removes users’ without time from view
* Recurring holidays are not displayed in Scheduling when viewing next year
* Admins and Team managers don’t receive some time off emails
* Change email flow doesn’t require password confirmation
* When creating entry from auto complete, billable status is inherited from that entry instead of the project/task
* Admin can’t change some team member’s name
* Missing progress indicator when timesheet template is activated
* Some users can’t approve timesheets
* User name is missing on print view of timesheet
* “Remind to submit” email is not sent when week only has expenses
* Expenses are shown in the approved request even though the user submitted only entries
* Group member unable to pull task list from the private project
* Title on PDF reports overlaps with logo
* Can’t create project template
* Google login doesn’t work when 2FA is enabled on workspace
* Reminders that a user didn’t track enough time are sent to admins even if the user has time off
* Login link in 2FA email is missing
* Approval emails show the wrong approver
* Regular users can’t see amount even if they have the permission
* GPS location is not shown when you click on a user’s entry
* Users who are not part of the group are getting reminders for other users
* Regular users can see button for creating limited members
* Old currency is displayed on Approvals page for expenses

## July 2022

#### What’s new

* [Kiosk mode](https://clockify.me/help/track-time-and-expenses/track-time-on-kiosk)
* [Reminders](https://clockify.me/help/apps/windows-desktop-app#reminders) (Windows)
* [SOC2 Type II compliance](https://cake.com/security)
* Add [custom text](https://clockify.me/help/reports/customize-exports) to report PDF exports
* Add line break to item description in [invoices](https://clockify.me/help/extra-features/invoicing)
* New [languages](https://clockify.me/help/administration/profile-settings): Japanese \& Korean

#### What’s fixed

* Create and edit popups are closed and you lose entered data if you accidentally click outside of popup
* Templates and Copy Last Week in Timesheet doesn’t copy breaks
* Bill from address isn’t displayed on some invoices
* Log in as user in Accounts tab not working chat is enabled
* Some users can’t see their tasks in project picker
* Approval emails don’t look good
* User agent sometimes saves wrong time zone during registration
* Some users do not receive weekly scheduled reports
* “Publish” button on Schedule disabled out after adding a new assignment
* Estimate in Summary report export are returned only when Project or Task is in the first or second grouping level
* Projects created via API don’t follow default billable setting from Workspace Settings
* Scheduled hours in timeline view and Edit assignment view don’t match
* Distorted Detailed report on Safari
* Error when adding company address on an invoice without a client

## June 2022

#### What’s new

* Improved [Scheduling](https://clockify.me/help/projects/scheduling)
	* Allow Project managers to create and publish assignments
	* Filter assignments by user and group
* Improved [Invoicing](https://clockify.me/help/projects/scheduling)
	* Customize “bill from” address for each invoice
	* Bulk delete items in an invoice

#### What’s fixed

* Approval column moved upfront in Excel report
* When activating timesheet, required project is disabled without checkmark
* Stop and discard are disabled on a running entry
* Assignment can be created for a private project that user has no access to
* Project manager can’t see Team filter in reports
* Time off timeline loading too long when This Year selected
* Time off calculates wrong dates after the winter time change

## May 2022

#### What’s new

* [Idle detection](https://clockify.me/help/apps/windows-desktop-app#idle-detection) (Windows app)
* [Global shortcuts](https://clockify.me/help/apps/windows-desktop-app#shortcuts) (Windows app)
* Approve [expenses](https://clockify.me/help/track-time-and-expenses/expenses)
* Allow Project managers to create new projects
* Client note
* See reports others shared with you
* Audio/video calls \& sound notifications (chat widget)

#### What’s fixed

* Missing 2FA for admin panel
* Day is added when a user selects one day and changes policy
* Project status disparity with Detailed report
* Customize reports shows blank pop\-up
* Duplicated assignments on Scheduling page
* Today’s running timer shows up on for each week in Calendar
* Can’t click on an item in Summary report to see it in Detailed report
* Time off requests is sometimes duplicated
* Alerts are sent twice
* Error when downloading a CSV report for Audit log
* Time off period shows incorrectly when people are in different time zones
* Unable to update who can see section for the shared reports

## April 2022

#### What’s new

* [User fields](https://clockify.me/help/track-time-and-expenses/user-fields)
* Scheduled [assignments in Calendar](https://clockify.me/help/projects/scheduling#publishing-assignments)
* Set working day per user
* Add profile photo for your teammates
* Two\-factor authentication (personal)
* Force 2FA
* Duplicate invoices
* Include [expenses](https://clockify.me/help/track-time-and-expenses/expenses) in project budget
* [Single sign\-on](https://clockify.me/help/getting-started/single-sign-on-sso) templates (Azure, Google, JumpCloud, Okta, OneLogin, Rippling)

#### What’s fixed

* Percentages are missing in Dashboard
* Tax in PDF invoices doesn’t show more than 2 decimals
* Some project status bars don’t show percentages for used hours
* Team manager can’t see time in the shared Weekly report they’ve created
* Regular users can’t see billable rate column on Team page (when they have the permission to see it)
* 2FA error when a user doesn’t have an active workspace selected
* Some users receive a running timer reminder even though they are not running any
* Team manager see more policies in the balance tab than they should
* Time in Timesheet is moved by one hours because of daylight saving time
* Time off request is sometimes duplicated
* Calendar Today view gets messed up when switching between days
* Some expenses are hidden when there’s a time zone mismatch
* Users receive time tracking reminders even if they have time off

## March 2022

#### What’s new

* Change Client/Project/Task label
* Improved Scheduling
	* [Publish assignments](https://clockify.me/help/projects/manage-scheduled-team-assignments)
	* Users can see their assignments
	* Copy assignment
	* Split assignment
	* Shift schedule by X days
	* See total assigned hours per user
	* See time off along assignments
	* Move milestones via drag\-n\-drop
	* Improved print view
* Improved Calendar
	* Discard or stop running timer
	* Stop timer for another user
	* Running timer is added to daily total
	* Events inherit color from external calendar
* API improvements
	* Get expense report
	* Update task rate (billable, cost)

#### What’s fixed

* Owner who also has manager role doesn’t receive other admin related reminders
* Users not able to access previously created shared reports
* Invoices, PDF, and CSV reports written in Hebrew export incorrectly
* Amount mismatch when creating Category in Expenses
* “Day” view in Calendar isn’t remembered when you return to the page
* Screenshot app is generating hundreds of screenshots
* “Without note” filter in Expense report doesn’t work
* Logo overlaps with title in PDF reports
* Bar charts in Summary report don’t match exact values
* Approvals page shows 0h on approved entries
* Accept invite page shows password when single sign\-on login is forced
* Project status page is not updated automatically each time it’s opened
* Admin who has Team Manager role can’t see groups in team filter in reports
* Add time for others and project bulk update is slow
* Error when creating approving timesheet for a user who is not registered
* When stopping timer with “select” type custom field, default value overrides user’s choice
* When cost rate is set, project status starts calculating workspace billable rate instead of its project rate

## February 2022

#### What’s new

* [Expense report](https://clockify.me/help/track-time-and-expenses/expenses#expense-report): download all receipts
* See [amount/cost/profit](https://clockify.me/help/reports/labor-cost) in reports at the same time
* Calendar view ([iOS](https://clockify.me/help/apps/iphone-app#calendar) \& [Android](https://clockify.me/help/apps/android-app#calendar))
* Pomodoro timer countdown ([extension](https://clockify.me/help/apps/chrome-extension))
* Choose at what time timesheets are [locked](https://clockify.me/help/track-time-and-expenses/lock-timesheets)
* Web app moved to app.clockify.me

#### **What’s fixed**

* Some regular users don’t receive timesheet reminder email
* Duration column on summary report is not vertically aligned
* Invoice logo low aspect ratio issue
* Difference in time duration when using compact duration format
* Scheduling is slow when there are a lot of assignments
* Work Log in JIRA isn’t updated when we have a running timer and start a new one
* Timesheet approval for last week is not working properly
* Can’t filter approval requests by group
* User’s address is not aligned with the Client’s address in invoices
* Custom field values are not visible in Timesheet when changing project’s default value
* Screenshots recording on Windows crashes the app
* Slow user load because user endpoints don’t have pagination
* Can’t upload file for SAML2 metadata in admin panel
* Logo in PDF invoices is cut off
* Removed signup link and password from self\-hosted login when forced single sign\-on
* When user clicks on a project in Summary report, it excludes them Detailed report
* Expense report and CSV export off by 1 day
* When joining a workspace or creating an account that has an invite, you’re not required to verify email
* “Approve all” takes a long time to finish when there are a lot of timesheets
* Custom fields don’t pick up default value from project settings in some cases
* User redirected to regular login page when clicking “Manage tracked time”
* Only “Without task” option available in the task picker when starting the JIRA integration and switching to manual mode
* Lists displays tags with empty tag IDs
* Time and project pickers are not being updated
* Slow update when bulk editing multiple projects
* Webhooks are disabled when a user has both admin and manager role
* Switching user in “Balance” tab doesn’t work
* “Requests” tab refresh sometimes doesn’t work
* Switching workspaces while user is in “Balance” tab doesn’t reload
* Filter in reports offers only only previously searched terms
* Wrong email subject for Time Off emails addressed to Team Managers
* Time off policies not properly displayed for Regular Users
* UI issues for Time Off and available time balance
* Pagination issue in Time Off tabs when user changes name
* Non\-rounded value is displayed on time off balance
* When tax value is zero, it isn’t displayed in downloaded PDFs
* Not able to select “Last week” on Calendar view
* User cannot accept workspace invitation due to “Internal server error”
* Cannot edit expense mileage rate to 0\.58 or from 0\.56 to 0\.57
* Print view on Calendar, Timesheet, and other page has unnecessary elements
* Changing time format in profile settings doesn’t automatically reflect in apps
* Can’t see non\-working days in Timesheet
* Unable to give assignment to owners on Scheduling page
* Progress bar on Projects page is not shown when billable hours are disabled

## January 2022

#### What’s new

* Calendar day view
* Submit timesheet for others
* Custom fields (Windows app)
* Improved admin panel (self\-hosted)
* API improvements
	* Get all invoices and get invoice by ID
	* Get time off requests and balance by user/policy
	* Get client by ID
	* Webhooks for invoicing (created/updated)
	* Webhooks for approval (submitted/approved/rejected/withdrawn)

#### What’s fixed

* Discard and export not working in Audit log
* User can withdraw their approved time off request
* Logo on invoices is too small
* When user tries to print scheduling page, the first project on the list isn’t visible
* “Remind to approve” is not working when the first submitted request is without team manager
* When tax or discount isn’t applied, subtotal is visible
* Can’t access holidays if there are no time off policies
* Can’t assign manager role to workspace owner
* Missing time off options in sidebar
* Time entries created after December 28th, 2021 are displayed in invoice as entries from December 2022
* Weekly report email doesn’t match the timesheet view hours
* JIRA project picker: can’t see or search by clients, and other issues
* Shared detailed report always shows USD currency icon
* Can’t see locations on mobile web view
* Weekend lines are messed up on PTO and Scheduling timelines
* Clicking arrows to change dates Weekly report doesn’t work
* Admin is unable to create an assignment for a private project in Schedule
* Columns on Team page get messed up when billable hours are turned OFF
* Missing translation in some places
* A user can’t stop the timer in some cases
* Day labels are missing on the calendar page
* LDAP email address validation doesn’t work
* Alert email is using project’s currency instead of workspace currency
* In some time zones, time entries are imported to QuickBooks with incorrect date and inconsistent rounding
* Various minor issues with Audit log
* When Admin edits user’s name, this isn’t reflected on Time Off page
* Project status calculation fails when owner changes their time zone
* Teammate’s timesheet is not displayed correctly when accessed from Unsubmitted tab in Approvals

## December 2021

#### What’s new

* [Scheduling (projects and team)](https://clockify.me/help/projects/scheduling)
* Team chat
* [New languages](https://clockify.me/help/administration/profile-settings#change-language): German and Russian
* [Exclude non\-billable time](https://clockify.me/help/projects/project-budget#define-project-budget) from project estimate and progress

#### What’s fixed

* Some users sometimes don’t get a weekly email report
* API v1 sometimes doesn’t return updated task duration
* Scheduled report is not sent when Day start is not a full hour
* Regular user can’t see amount on reports if they’re allowed to see it but aren’t allowed to see what’s billable
* Team filter is cleared when moving between reports
* Time for Sunday is not shown in Timesheet
* Some entries couldn’t be copied using template on Timesheet
* Webhook task duration returns PT0S
* Copy with time in Timesheet pastes templates even in locked time range
* User gets “Something went wrong message” even after connecting to a different network
* Various bugs and improvements for Time Off
* Toast “Export settings updated” showing even if the setting wasn’t updated
* User isn’t moved to default workspace when removed from active one
* Time off doesn’t return correct holidays for long overlapping period
* Various minor expense issues

## November 2021

#### What’s new

* [Audit log](https://clockify.me/help/administration/audit-log)
* [Timesheet: Copy last week with time](https://clockify.me/help/track-time-and-expenses/timesheet-view#create-new-timesheets-quickly)
* [Timesheet: Save template with time](https://clockify.me/help/track-time-and-expenses/timesheet-view#create-new-timesheets-quickly)
* Summary report: Group by week and month
* Remove billing and hourly rates from interface
* Hide billable status of time entries from regular users
* [Manage email preferences](https://clockify.me/help/administration/profile-settings#preferences)
* [Edit member profiles](https://clockify.me/help/administration/edit-profiles)
* [New languages](https://clockify.me/help/administration/profile-settings#change-language): Portuguese and Spanish
* [Windows app](https://clockify.me/help/apps/windows-desktop-app#preferences): Mini\-timer, always\-on\-top, and automatically start/stop timer
* Send notifications from Admin Panel (self\-hosted)
* API: [Expenses](https://docs.clockify.me/#tag-Expense) \& [Approvals](https://docs.clockify.me/#tag-Approvals)
* Improved [timesheet approval](https://clockify.me/help/track-time-and-expenses/approval)
	* See unsubmitted timesheets
	* Remind users to submit their timesheets
	* See who’s responsible for approving timesheets
	* Remind managers to approve their team members’ timesheets
	* Filter requests by member or group
	* Submit for approval (Android \& iOS)

#### What’s fixed

* Timer option appears in Calendar when tracker is turned off
* Description isn’t left aligned on PDF invoice
* Regular user can’t see amounts on reports when allowed
* Multiple clicks create multiple identical expenses
* Cost rate from workspace settings isn’t applied to non\-billable entries
* Project filter doesn’t remember active/archived filter when switching between reports
* When a shared report is filtered only by a deactivated user, the report shows everyone’s time
* When an expense is removed from an invoice, it remains marked as “invoiced”
* Users can’t see their team’s time off
* Item type column is too wide on invoice PDF
* New users aren’t added to a time off policy when Everyone is selected
* Expense isn’t updated when unit price is removed from its category
* Multiple time entries are created when double clicking on Add
* Owner unable to remove admin role if there are multiple roles
* Entries are added twice on double click
* Placeholder for custom field doesn’t inherit name
* Old expenses take new unit price in invoices
* Missing duration field on smaller screens when adding time for others
* Missing amount in tooltip on reports
* In Calendar, sometimes time popup doesn’t close

## October 2021

#### What’s new

* [Expense report](https://clockify.me/help/track-time-and-expenses/expenses#expense-report)
* [Record expenses](https://clockify.me/help/track-time-and-expenses/expenses#record-expenses-using-mobile-app) (Android \& iOS)
* [Custom fields](https://clockify.me/help/track-time-and-expenses/custom-fields) (Calendar view, Chrome \& Firefox extensions)
* [Group manager](https://clockify.me/help/administration/user-roles-and-permissions/manager-role)
* Give manager role to admins so they can receive team\-related emails
* Create [time off](https://clockify.me/help/track-time-and-expenses/create-manage-time-off-policy) for another user
* Automatic [time off](https://clockify.me/help/track-time-and-expenses/create-manage-time-off-policy#create-and-manage-policies) accrual
* Set password for users (self\-hosted)

#### What’s fixed

* Issue and due date of an invoice is incorrect in web app when in different time zone (but correct on PDF)
* Billable time entries showing zero amount
* Integrations tab in the workspace settings is not opening
* Unable to create invoices on Asian server
* Item type is null on an invoice
* Error while generating a Summary report
* Days and dates on Timesheet are not matching for all years
* Can’t sort by amount in Summary report
* Custom fields don’t inherit default value in some cases
* Error “File not uploaded” during import
* Customize export issues with unchecking all in the description column
* JIRA integration error “Entry failed to save” when time rolls over to another day
* When updating both time and billable status via Timesheet, one entry doesn’t get the new billable status
* When updating an entry’s non\-project field via Calendar, project’s new hourly rate is applied
* Can’t sync users with QuickBooks if the user already exists in QuickBooks employee list
* Reminders for different days are all sent together each day
* Can’t rename project in some cases when cost rate is not defined

## September 2021

#### **What’s new**

* [Expenses](https://clockify.me/help/track-time-and-expenses/expenses)
* Time off improvements
	* Allow regular users to see other people’s time off
	* Filter time off timeline by user and groups
	* Add and remove time off balance using decimals (e.g. 1\.75h)

#### **What’s fixed**

* Some admins can’t see pending approval requests
* Missing pagination on Team and Reminders
* In Time off Balance tab, Accrued number is same as Available
* Can’t share reports with fixed dates
* Missing client tooltip on hover
* Budget reset doesn’t reset in some cases
* Dashboard loads too long
* UI elements briefly show their system keys instead of UI text
* Issue with resetting password on subdomains
* Reminder emails not working properly for some team managers
* When adding time for past dates in JIRA via manual mode, it’s added for today
* Various minor UI and UX fixes for time off
* Task assignees dropdown not working properly

## August 2021

#### **What’s new**

* [Languages](https://clockify.me/help/administration/profile-settings#change-language)
* Improved [auto tracker](https://clockify.me/help/track-time-and-expenses/auto-tracker) on Windows (idle activity, URL tracking, bulk add)

#### **What’s fixed**

* Can’t see respective project’s client when scrolling in long lists
* Toast messages don’t have icon (colorblind accessibility)
* Can’t change project color due to unspecified cost rate
* Entries created via Calendar don’t follow project’s default billable state
* “This Year” date range in Dashboard returns error in some accounts
* Admin can’t see pending approval requests in some cases
* It’s possible to import time from one CSV file multiple times
* Confusing message when trying to import time from badly formatted CSV
* Can’t delete default subject from invoices
* Outlook Calendar connection fails in some cases
* Some projects are missing in the report’s project filter
* Time entry are not properly imported from Clockify to QuickBooks when there are project with same name but different clients
* Mismatch between reports and project status for some project
* Public shareable link doesn’t show entries if you’re not logged in
* Detailed report CSV export shows users as part of Admin group
* Internal server error when updating custom field on a time entry
* Time off requests is created for a day earlier in some cases
* Minor cosmetic and UI fixes

## July 2021

#### **What’s new**

* [Time off](https://clockify.me/help/track-time-and-expenses/create-manage-time-off-policy)
* Add inactive/invited users to projects
* Add time for inactive/invited users
* Weekends are visually distinct in Timesheet and Calendar
* Custom fields (Android)
* Invoicing improvements
	* Reorder items via drag\&drop
	* Set defaults for new invoices
	* Simple/compounded calculation of Tax 2
	* Hide quantity/unit price from invoices
	* Display text right\-to\-left
	* Sort invoices

#### **What’s fixed**

* Regular users can see clients in filter from private projects
* Selecting project is too slow
* Can’t import inactive users’ time into invoice
* Error when importing thousands of projects via CSV
* Can’t send to QuickBooks time entries that don’t have hourly rate
* Time entries don’t inherit custom field default value on some projects
* In Team filter in reports, “Select all” selects both active and inactive users
* Cosmetic and UI fixes

## June 2021

#### **What’s new**

* [Clockify for Windows](https://clockify.me/windows-time-tracking) (Beta)
* Send [reminder](https://clockify.me/help/administration/targets-reminders) emails just to admins or managers (when someone tracks too much or not enough time)

#### **What’s fixed**

* Weekly report isn’t displayed properly
* Billable entries made via continue button in apps doesn’t pick up hourly rate
* Adding a tag via bulk edit overwrites old hourly rate
* Continue button appears in Dashboard even though Time tracker is hidden
* “Copy last week” on Timesheet copies archived projects
* Various minor QuickBooks integration fixes
* Missing hourly rate for some time entries in Detailed report
* Wrong due date on invoices in some time zones
* Project manager can’t see project progress for budget estimate
* Outlook integration authorization error
* Amount for billable time entry on is set to 0 when timer is started via continue
* Admin can’t update project field for entries for multiple users via bulk edit
* Entry is left without user if no user is selected in bulk edit
* Project sorting doesn’t work on Projects page

## May 2021

#### **What’s new**

* [Outlook and Google Calendar integrations](https://clockify.me/help/track-time-and-expenses/calendar-view#connect-to-google-calendar-or-outlook)
* Allow Team managers to edit time for their team
* Assign groups to tasks
* Task favorites
* Default task (browser extensions)

#### **What’s fixed**

* Zapier trigger for “new time entry” is missing amount and hourly rate
* Regular user can duplicate entry and continue timer for task they no longer have access to (no longer assignee or task is marked as done)
* User who has been deactivated and then reactivated gets back their old Project manager role (if they had it)
* Deleted screenshot or location is removed after refresh
* Can’t import more than 100 customers from QuickBooks
* “Copy last week” in Timesheet adds projects multiple times
* Unvoiced filter shows invoiced entries (and vice versa)
* Invoice for archived clients allows other clients’ projects to be selected
* Deleting time in a timesheet cell doesn’t actually delete the time

## April 2021

#### **What’s new**

* [QuickBooks integration](https://clockify.me/help/integrations/tracking-integrations-integrations/quickbooks-integration)
* [Decimal format](https://clockify.me/help/track-time-and-expenses/duration-format)
* [Auto tracker](https://clockify.me/help/track-time-and-expenses/auto-tracker) (Windows, Mac, Linux)
* [Notify team manager/admins when users track under/over target](https://clockify.me/help/administration/targets-reminders#emails-for-admins-and-managers)
* Improved invoicing (group by project/user/date \& subgroup by project/user/date/description, get user in detailed time import, add Tax 2, enter negative value in quantity and price, more decimals for tax value)
* Get each user’s group in Detailed report’s CSV/Excel export via [customize export](https://clockify.me/help/reports/customize-exports)
* Add team member without triggering email invitation

#### **What’s fixed**

* When amount and user is disabled in Detailed report’s customize export, PDF still shows User in the column header
* Various Calendar bug fixes
* When creating time via Timesheet’s detail view, changing billable status isn’t remembered
* Timesheet import via CSV doesn’t work when if start/end misses seconds and displays wrong message
* Team managers can’t see Team Dashboard
* Team managers can’t see their team members without time in the Weekly report
* Team manager can’t filter report to get only their time
* Screenshots and locations aren’t automatically deleted when timer is canceled
* Admins can’t edit or delete rows in Timesheet for completed tasks or archived projects
* When a user is removed from a workspace, their timer for the workspace is not discarded
* Various visual fixes

## March 2021

#### **What’s new**

* [Estimates in reports](https://clockify.me/help/projects/project-budget#estimates-in-reports)
* [Edge browser extension](https://clockify.me/edge-time-tracking)
* [Add/edit time in Calendar](https://clockify.me/help/track-time-and-expenses/calendar-view#add-and-edit-time)
* [Translate invoices](https://clockify.me/help/projects/invoicing#additional-invoice-settings)
* [Customize report exports (PDF, CSV, Excel)](https://clockify.me/help/reports/customize-exports)
* API: Mark time entries as invoiced
* [Select default project/task for Pomodoro break](https://clockify.me/help/apps/chrome-extension#pomodoro) (browser extensions)
* [Auto tracker](https://clockify.me/help/apps/mac-desktop-app#auto-tracker) can recognize names of open documents across programs (Mac)
* Improved project picker (faster, “Task filter” personal setting, can create tasks directly from picker)

#### **What’s fixed**

* Amount in reports is barely visible
* Can’t move time entry to another workspace if current workspace doesn’t have any projects
* Timesheets rows for projects without time are lost when switching between weeks sometimes
* Project picker returns partial matches
* Some API endpoints cannot handle concurrency properly
* Not possible to remove favorite status from last project
* Missing loader when importing CSV file and
* Different values in reports when filtering just by client and by client and all tasks
* Editing archived project removes its archived client
* Projects page won’t filter by user group
* Team managers can’t see their team members in Dashboard Team
* Copy last week in Timesheet doesn’t carry over task’s billability
* Users receive “Screenshots Enabled” notification every time they go to the Activity page
* GET tasks API always returns duration 0
* Restored project gets archived again on its own
* “Copy last week” and “Template” in Timesheet don’t apply task’s billable status
* Minutes are not rounded up in invoices
* Duplicating entry in a group doesn’t instantly reflect in the group’s duration

## February 2021

#### **What’s new**

* [Customize report export](https://clockify.me/help/reports/customize-exports) (CSV and Excel)
* See [Calendar](https://clockify.me/help/track-time-and-expenses/calendar-view) of your team members
* [Who can see project status: Admins/Everyone](https://clockify.me/help/administration/hide-time)
* Post\-start popup for integrations ([browser extensions](https://clockify.me/help/apps/chrome-extension))
* [Screenshots](https://clockify.me/help/apps/screenshots) are now grouped by time
* Team managers now get email notification when their team member submits timesheet for [approval](https://clockify.me/help/track-time-and-expenses/approval)
* Team manager can no longer see Team or Projects pages if they’re hidden

#### **What’s fixed**

* Invited user can export reports on workspace
* Dashboard Billable view has no bars
* When adding users to a group, the sometimes show up twice
* Can’t load detailed report when there is invoiced time with deleted client or project
* Wrong project colors and uneven charts in Dashboard
* Project status sometimes doesn’t get updated in real time
* Missing thousands separators on invoice PDF
* Unrestricted file upload type
* Activity page doesn’t load if there’s a deleted user with a screenshot or a location
* Missing client name in Dashboard and detailed approval
* Team manager can see amount in detailed approval
* Custom fields not visible in Calendar on hover
* When task is over character limit but its project is not, project is not imported
* Various small Calendar bugs

## January 2021

#### **What’s new**

* Mark invoice as void
* Time rounding when invoicing time

#### **What’s fixed**

* Various Calendar view bugs and improvements
* Projects with non\-standard characters don’t get imported properly
* Improper access control in viewing custom fields
* It’s possible to have more than one active subscription
* Random order of time entries when imported into an invoice
* Next and previous date arrows in report skip only by one day
* Dashboard sometimes shows different results
* Dashboard takes too much system resources
* Entries on private projects where admin isn’t explicitly added doesn’t show up in autocomplete
* Can’t create a new custom field when old value is stuck in database
* Task amount doesn’t always show up

## December 2020

#### **What’s new**

* [Calendar view](https://clockify.me/help/track-time-and-expenses/calendar-view)
* [GPS tracking](https://clockify.me/help/track-time-and-expenses/gps-tracking)
* [Screenshots](https://clockify.me/help/apps/screenshots)
* [Project budget](https://clockify.me/help/projects/project-budget)
* [Invoicing](https://clockify.me/help/projects/invoicing)
* [Task rates](https://clockify.me/help/reports/task-rates)
* [Import timesheets](https://clockify.me/help/track-time-and-expenses/import-timesheets)
* [Reports (Android app)](https://clockify.me/help/apps/android-app#reports)
* [Timesheet (Android app)](https://clockify.me/help/apps/android-app#timesheet)
* Sort projects by tracked time, amount, and progress

#### **What’s fixed**

* Not all the groups and users are showing in project’s Access dropdown
* Can’t assign some users to tasks
* Can’t see more than 50 project templates
* Delay in listing users on Accounts tab
* Wrong error message when importing time entries with incorrect date format
* Can’t create reminders on new workspaces
* Project creation via API requires fields other than name
* Entries in the Timesheet are displayed a day back in some time zones
* Can’t remove 0 as default value from custom field number type
* Amount in project status and report don’t match sometimes
* Incorrect project progress percent
* Calendar view wrong when changing time zones
* Calendar view doesn’t take into account “Week starts” settings
* Calendar view puts a bunch of time entries into the same start slot
* Null can be entered as a tag via “Create time entry” API request
* When user is invited to workspace, “Resend invite” sends login link
* When decreasing time in one timesheet cell that has two different descriptions, one of them is deleted

## November 2020

#### **What’s new**

* [Force timer](https://clockify.me/help/track-time-and-expenses/force-timer)
* [Scheduled reports](https://clockify.me/help/reports/scheduled-reports)
* Collapse sidebar (web)
* Running timer notification (Android)
* [Bug bounty program](https://security.cake.com/)

#### **What’s fixed**

* Error when trying to generate a weekly report for last week (24\-30 Oct)
* Duplicated tags in Summary report
* Hourly rate not removed when workspace is deleted
* Admins appear as a group in Team filer
* Error on login form and redirect to localhost
* Issues with time zones and other time settings in shared reports
* Slow load on project status tab for some projects
* Start timer grayed out
* Issue when clicking on custom field for “select” type
* Projects and users are not displayed when hovering over dropdown in the manager options
* Team page doesn’t load for some users
* Project manager sees approval page in sidebar (but can’t access it)
* For relative range, PDF takes report’s creation date
* Cost rate isn’t calculated for some non\-billable entries

## October 2020

#### **What’s new**

* [Import projects, clients, tasks, and tags from a file](https://clockify.me/help/track-time-and-expenses/import-timesheets)
* Share a report with relative range (e.g. Yesterday, This Week, etc.)
* Improved [JIRA integration](https://clockify.me/help/integrations/tracking-integrations-integrations/jira-integration) (manual mode)
* Improved [Android app](https://clockify.me/help/apps/android-app#offline-mode) (improved offline mode, time grouping, autocomplete)
* Improved [Mac auto tracker](https://clockify.me/help/apps/mac-desktop-app#auto-tracker) (bulk add as time entries, delete and hide records; track MS Office, Photoshop, and Firefox,)

#### **What’s fixed**

* When removing project from an entry, its task remains in the database
* Sometimes reports with custom fields are not loading properly
* Dashboard is slow on workspaces with a lot of data
* Sometimes projects are missing in the project picker list that has a large number of projects
* Custom fields without values on approved time entries can be edited
* Admin can’t delete “not joined” users
* Sometimes a user can’t create a project from a template
* Admin can remove another admin’s role
* It was possible to send a workspace request containing null value
* Regular user and Project manager get 403 error when they change workspace when Approval is enabled

## September 2020

#### **What’s new**

* [Manager role](https://clockify.me/help/administration/user-roles-and-permissions/manager-role)
* Autocomplete on Time tracker
* New webhook events: Me/Anyone

#### **What’s fixed**

* Can’t delete a client
* Autojoin with OAuth and SAML doesn’t work properly
* Possible to add a default option that doesn’t exist to a custom field
* User value is null in Zapier
* When user changes email, the old invite remains
* Users don’t receive a confirmation email when their timesheets are approved
* User added via a group cannot create a task on the project
* Custom field switch type needs a refresh to show true value in the running timer
* Pagination doesn’t work on Detailed shared reports
* Clicking on Date group in the Summary report’s table doesn’t lead you to Detailed report for that date
* Can’t see a project in Timesheet when one task has some time
* Sometimes an extra entry is included in the Detailed report page\-2 via API
* Can’t add pending users to a group
* Can’t update payment information when 2FA is enabled

## August 2020

#### **What’s new**

* Dark theme (web)
* [See users without time](https://clockify.me/help/reports/weekly-report#users-without-time)
* Filter tasks, clients, tags on respective pages
* Resizable tag picker
* Projects page improvements
	* “Expand all” options on Projects page (mobile version)
	* Added “Without task” on project status
	* Completed tasks are visually marked on project status page
	* Added “Overage” on project status
	* Project name appears in browsers tab’s title

#### **What’s fixed**

* Timesheet template tasks not being saved
* Project cost rate is reset when project estimate is changed
* Regular users see dollar icon on Time tracker even if the workspace currency is different
* Sometimes “No client” in the project picker appears down the list
* Lazy loading
* Project templates list all projects
* Project managers can’t see status overview for any project
* Some entries without description are not grouped together
* Missing filter button on Projects page on smaller resolutions
* Color picker opens on Enter when saving manual estimation
* API pagination on Detailed report doesn’t work
* Alerts for task\-based estimates don’t come out right
* Sorting order in project picker is not good in some cases
* Can’t create more than 10 webhooks on a workspace
* It’s possible to approve time entry in progress
* Users from groups who have access to private shared report can’t open it
* Some users can’t seethe  workspace they are a part off
* Problem when submitting for approval in time zones affected by daylight saving time
* In Approval details, some billable entries are shown as non\-billable
* Can’t expand projects in timesheet
* On approval withdraw, “Review timesheet” link in emails doesn’t work
* When changing time zone through the “time zone mismatch” notifications, pending approval requests are not withdrawn
* Cost rate in Approval details are calculated only if a project is billable
* Admin cannot see some user added to a project
* API doesn’t send content\-type for PDF, CSV, and Excel reports
* Can’t select all users when bulk editing users to projects
* Sorting projects in project picker is not good in some cases
* When adding users to a project, all users are listed instead of just active ones
* When adding users to a project, changing filter resets the selected users
* Tooltip doesn’t display full project name on hover
* Deleted project doesn’t immediately disappear from the list
* Missing active/archived selector in client filter on Projects page
* Missing active filter indicator on Projects page
* Status page doesn’t show estimated tasks when there’s a new hourly rate (needs refresh)
* Missing “Restore” in project bulk edit
* Missing copy when there are no more members to add to a project

## July 2020

#### **What’s new**

* Time approval
* Prepay user seats for Enteprise plan
* Complete API documentation
* Sort Team page by group
* Week total on Time tracker
* Active filters on Project page are remembered
* Both members and groups are shown in project access tab immediately
* Dropdowns on Reports are open on hover

#### **What’s fixed**

* When Time tracker is left open overnight, date says “Today” even though it will add time to yesterday
* Admin cannot see a user added to a project
* Deleted client appears in project picker when collapse is turned on
* Sidebar glitch on iPhone and other visual issues
* Cost rate on project isn’t shown even though it’s saved and applied
* If Team page is hidden, regular users and managers can’t see their name in Team filters in reports and can’t click in table on user name to filter the report by the user
* Regular users can’t access get their time entries using /time\-entries endpoint in API
* Missing “content\-type” in Reports API’s header
* Changing duration in Timesheet doesn’t update end time incrementally, as according to profile settings
* Can’t create webhooks on subdomain
* Sort on Dashboard is not case\-insensitive
* Owner can remove their role from Group page
* It’s possible to create two projects with the same name and the same client via bulk edit
* Missing toast message when activating/deactivating users
* Missing total time in Weekly report PDF
* Tag filter is not working properly in some cases
* “Select all” in task filter selects only first 50 tasks
* “Copy invite link” on subdomains is not right
* High CPU usage on log in page
* Webhooks don’t return user’s name
* Selected tag doesn’t show up immediately
* Sometimes a user is both active and pending at the same time on subdomain workspace
* “Fix” link on Timesheet doesn’t apply proper filters in Detailed report

## June 2020

#### **What’s new**

* [Improved JIRA integration](https://clockify.me/jira-time-tracking)
* Improved Summary and Weekly report
	* Three levels of grouping
	* Works on smaller screens
	* Analyze cost and profit
	* Hide billable amount from exports
	* Remembers date range
	* Sort data (name, duration, amount)
	* PDF shows percents for pie charts
	* Active filters are transferred between reports
	* Click on an item in Summary table to see Detailed report for that item
	* New filters
* [Share reports](https://clockify.me/help/reports/sharing-reports)
	* Lock dates (prevent changing dates)
	* Only you can see links you create
	* Link shows all filtered data as you can see it
	* Click on report to open it
	* See applied filters in “Filter info”
	* Report name shows up when you open link and in PDF export
	* Settings are carried over (grouping, amount, rounding, sort)
* Webhooks and Reports API
* Faster app loading and report generation
* Encryption at rest for all accounts (improved security)

#### **What’s fixed**

* “Add tag” button is missing from Detailed report
* Summary Excel/CSV only exports two decimals
* Detailed Excel/CSV shows “Without X” instead of empty row
* Workspaces from subdomain don’t show up in the workspace picker on cloud
* Various Zapier issues
* Too strict URL validation for webhooks
* Bulk editing custom fields sometimes shows error
* Reminders don’t work when edited
* Task filter is no longer case insensitive
* Managers can’t see Team filter in reports
* Pin to top on Team Dashboard gets reset after logout
* Entry longer than 24h loses 24h when time is edited in Detailed report

## May 2020

#### **What’s new**

* API v1 returns custom fields on time entries

#### **What’s fixed**

* Reports don’t work if time is added via a group whose member has not yet joined
* Deleting user groups is slow
* Admins get a wrong email address of a user who fails to join their workspace on a subdomain
* “Select all” in client filter doesn’t always work

## April 2020

#### **What’s new**

* [Historic hourly rates](https://clockify.me/help/reports/hourly-rates#historic-rates)
* [Labor cost and profit](https://clockify.me/help/reports/labor-cost)
* Who can create and update tasks: Admins/Everyone
* New endpoints and params in API (v1\)
* Improved Detailed Report
	* Works on all screen sizes
	* More room for description and tags
	* Hide amount and export without hourly rates
	* Add time for multiple users in one action
	* Select all time entries, across pages
	* Bulk edit custom fields on time entries
	* See each time entry’s amount plus their hourly rate on hover
	* Right\-to\-left text support (Arab, Hebrew, Persian)
	* See 50/100/200 time entries at once
	* Page stays in place when editing
	* Improved project selector
* Improved filters (only for Detailed report, Summary report coming later)
	* Advanced tag filtering (contains, does not contain, contains exactly)
	* [Filter by custom fields](https://clockify.me/help/track-time-and-expenses/custom-fields#custom-fields-in-reports)
	* Choose which filters to see
	* Limited access to what regular users can see in filters
	* All time entries are displayed (regardless of archive status)
	* Filter clients, projects, tasks, tags, and users by status
	* Filter a list and select all that matches the criteria
	* Filter by “Without description”
	* Resize filter list
	* Filters in URL so you can bookmark reports
	* See selected filters on hover
	* Categorized project and task list
	* Selecting a client narrows down the project filter
	* “Past two weeks” date range option

#### **What’s fixed**

* Changing time in timesheet doesn’t change total time and project status
* Daylight saving time in some time zones move entries one day back
* Timesheet entries are changing after page refresh
* Incorrect calculation of task\-based estimates
* Links in emails don’t lead to subdomains
* Hourly rates on project templates are multiplied by 100
* It’s possible to save a reminder without selecting at least one day
* Link to project status in alerts for task\-based estimates isn’t correct
* Group by date in Summary report doesn’t handle well different time zones
* Full name isn’t visible in Accounts tab

## March 2020

#### **What’s new**

* Add tags, description, start/end, and custom fields via Timesheet
* Hide Time tracker from sidebar
* Description and tags can be required fields always (even while Timesheet is ON)
* Multiline description field in Timesheet
* Bulk edit custom field data
* New Android app supports custom domains, self\-hosted users, and single sign\-on login
* Timeline in Auto tracker (Mac)

#### **What’s fixed**

* Projects without time aren’t sorted alphabetically on Timesheet
* Time entries don’t pick up projects’ billability status on Timesheet
* Stable API (v1\) doesn’t return user memberships
* Wrong calculation in some saved reports
* Cannot remove task assignee
* Summary report breakdown by category does not show calculation for billable hours
* Inactive/pending users receive project alerts
* Automatic lock isn’t working on some workspaces
* Admins and users see different currency symbols
* Can’t remove task assignees when project visibility is changed
* Deleting tasks on page 2 makes completed tasks show up
* Users lose memberships on archived projects
* Editing days on reminders closes the dropdown
* Newsletter checkbox looks unchecked even if you decided to subscribe

## February 2020

#### **What’s new**

* [Custom fields](https://clockify.me/help/track-time-and-expenses/custom-fields) (track anything)

#### **What’s fixed**

* Various minor lock and automatic lock issue
* Updating workspace settings is slow when it has a lot of users
* Modals close by accident on mouse up
* Project hourly rate can’t be set to 8\.69
* Can’t edit day checkboxes in Reminders

## January 2020

#### **What’s new**

* New Android app (Beta)
* [Auto tracker (Mac)](https://forum.clockify.me/t/auto-tracker/26/2)

#### **What’s fixed**

* Favorites are always collapsed in compact project picker
* Updating workspace settings is very slow when some user has a lot of memberships
* Issues with project alerts
* Subscription isn’t cancelled when a workspace that has inactive members gets deleted
* Time entries without memberships are not returned when generating reports
* Manually changing date range in reports doesn’t work without pressing Enter
* “Workspace settings have been updated” toast is displayed on other pages
* Hourly rate set for an invited user resets to zero after accepting invite
* Invited users with a name are not sorted properly
* Company logo in PDF too small
* Print view of Timesheet doesn’t show specific dates and user name
* Tags are not sorted alphabetically on Time tracker
* In Timer mode, a border appears when hovering over duration, even though it’s not editable
* Some tooltips and popups don’t look good on smaller screens
* When changing date of time entries via bulk edit, duration is changed to zero
* Excel export of Detailed report doesn’t follow selected sorting logic
* Missing “expand all” option on mobile resolutions for Projects and Team pages
* Selecting the only available user group triggers the select all option
* Click on setting hourly rate doesn’t auto\-focus to input

## December 2019

#### **What’s new**

* Archive tags and clients
* Projects and Team pages work on mobile
* [Project note](https://clockify.me/help/projects/formatting-project-note)
* Assign multiple members to tasks
* Workspace settings: “New projects are by default: Public/Private”
* Sort projects by status
* Copy and send invite link to users manually
* Add tags and members to projects in bulk without overwriting the existing ones
* Removed “Created with Clockify” in branded PDF reports
* Print\-friendly timesheet, project list, and project status (can be saved as PDF)
* Auto\-start timer (Mac)

#### **What’s fixed**

* Can’t access more than 10 invoices
* Members added to projects via groups don’t receive project overage alerts
* When connection is slow, users can delete a workspace several times
* Wrong year for December 30/31 when exporting Detailed report
* Percentage not correct on task based estimates
* Profile settings/logout are not visible when there are a lot of workspaces
* Missing validation on some inputs
* Inactive users receive reminders
* Possible to move entries between workspaces even if the dates are locked
* There shouldn’t be change password option if a user don’t have password
* Request for SAML logout isn’t sent
* Timer isn’t always shown accurately in the sidebar
* Sometimes users delete active projects and members by accident
* When getting all users via API, paging doesn’t work
* Entries can be moved to another workspace even though the dates are locked
* Error when an inactive users is added with the same e\-mail address
* Reset password doesn’t work when a user doesn’t have a default workspace
* Project collapse list doesn’t work when a client is assigned via new project modal
* API doesn’t return full list of project tasks

## November 2019

#### **What’s new**

* New workspace settings, tags, and clients pages
* Timer widget (iOS)
* Long press options (iOS)

#### **What’s fixed**

* Trouble with some time zones due to updated daylight saving laws in some countries
* Redundant time zone options
* In entry list, the whole date or duration is always selected
* Sometimes, owner’s entries are locked too
* When a new user is invited, their name is prefilled on signup page (leading to confusing names)

## October 2019

#### **What’s new**

* [Single sign\-on](https://clockify.me/help/getting-started/single-sign-on-sso) (OAuth2, SAML2, LDAP/Active Directory)
* [Control user accounts](https://clockify.me/help/administration/manage-accounts)

#### **What’s fixed**

* Invitation link is displayed as expired (even though it’s valid)
* Invitation link sometimes creates two workspaces
* Issue with adding entries in Asia/Famagusta time zone
* Reports show one more day due to daylight savings switch
* In some time zones, Timesheet saves an entry under incorrect date
* Can’t create projects, clients, and tags as regular user via API, even though it’s allowed

## September 2019

#### **What’s new**

* Reassign entry to another user in Detailed report (part of “Add time for others” feature)
* Timesheet no longer splits a time entry if it’s the only one
* Auto\-update (Mac)

#### **What’s fixed**

* Excel export of the Detailed report combines project/client/description into one column, email and billability columns are missing
* Template lists where all items are named “No template”
* Group by date in Summary report doesn’t work in some time zones
* Projects are not sorted in Timesheet when using Copy last week
* CSV export shows total time in columns of Weekly report
* Exporting takes too long when there’s a large amount of data
* Some entries end up with invalid date
* Admins don’t get all the tasks via API
* Automatic lock sometimes locks more entries on Timesheet than it should
* When you select a task on some project, you can’t re\-select the project itself after that
* Entries on Timeshet for a project made from a template are not marked as billable
* When subgrouped by date in Summary report, entries are not ordered form first to last in exports

## August 2019

#### **What’s new**

* Improved CSV and Excel export
* Time tracker works completely without using a mouse
* Project alerts now work for public projects and task\-based estimates
* Dark mode (Mac, Windows, Linux, iOS, Android, Chrome, Firefox)
* Quicker workspace switching (Windows, Linux, Android, Chrome, Firefox)
* Create projects, clients, and tags (Windows, Linux, Android, Chrome, Firefox)
* Resize window (Windows, Mac)
* Auto\-update (Windows)
* Time grouping (Mac, iOS)
* Force offline mode (iOS)

#### **What’s fixed**

* Line breaks in description mess up CSV export
* Different start and end date of time entries from the same day in export
* Project and client name is missing in task alerts
* Favorite projects sometimes end up at the bottom of the list
* Time rounding causes problem on reports when subscription expires
* Projects missing in non\-collapsed project picker
* Input field for reminders, automatic lock, and task estimates accepts negative values
* Detailed report shows 50 time entries even on pages that should have less entries
* Chart in PDF export sometimes overlaps the time table
* Issues with having spaces in password
* Project managers and regular users can’t see tasks that are mark as done
* Project managers can see hourly rates if it’s set to admin only
* Project managers can’t see or edit their project’s manual estimate or switch between manual and task\-based estimate
* Hourly rate field on project is disabled when project is marked as non\-billable
* Group/subgroup by date in Summary report isn’t good in some time zones
* Team Dashboard doesn’t retain sorting preference when changing date range
* API: when getting users of workspace, the response gets all their memberships
* Workspace list page is not responsive
* Issue with task field in Zapier integration
* Zapier integration only sends project and tags IDs of a time entry instead of their names
* One trigger in Zapier integration for both time created and timer started (now they’re separate)
* Duplicated time entries omit seconds when using hh:mm duration format
* Project picker shows \-1 project under No client when one project is selected
* Issue when using a same account on two different workspaces and computers
* When the deleting account, can’t type a reason in text area
* Pagination dropdown isn’t closed after selecting some value
* Numbers in Summary report PDF export are not right\-aligned
* Wrong message when changing password but the old entered pass isn’t correct

## July 2019

#### **What’s new**

* [Pomodoro timer](https://clockify.me/pomodoro-timer) (Chrome/Firefox extensions)
* Resizable project picker
* Remember show/hide sidebar
* Change invoice recipient email
* Auto\-generated profile pictures based on initials
* Entity hydration (get names of project, task, and tags instead of IDs via API)
* Improved Timesheet
	* Works on mobile devices
	* Shows total by project/task
	* Improved project selector
	* Changing time through Timesheet preserves existing data (description and tag)
	* Start and end times for new entries are auto\-incremented (you can define when your days starts in a new “Day start” setting in your Profile settings)

#### **What’s fixed**

* Project picker won’t close after you close project creation modal
* Missing email validation when inviting new members
* Date picker sometimes won’t show on saved report
* Admin sees only public projects and not all projects (API v1\)
* Profile settings page is not optimized for mobile devices
* Modal in Dashboard isn’t displayed properly when printing
* Notifications aren’t open automatically on page load
* PDF doesn’t display currency in the right format
* Link for adding time in reminder email doesn’t set Time tracker mode to manual
* When manually setting date range in reports, one extra day is sometimes included
* Autofill doesn’t appear in description field in the Time tracker
* Onboarding tooltips sometimes won’t go away
* On slow connection it’s possible to click twice on “Create project” and “Start timer”
* When task is created on the Time tracker page, the modal won’t close
* When task is required, creating a project automatically selects it when it shouldn’t
* Canceling timer opens a popup across the whole page
* Command line tools don’t display CSV exports correctly
* Tags are not shown in PDF export of Detailed report
* Rounding to nearest number doesn’t take seconds into account
* Incorrect date formatting in PDF export when a report is grouped by date
* When grouped by project/entry, report shows client name instead of description
* Sometimes minus values appear on the Y axis on the PDF bar chart
* Exporting PDF of Detailed report doesn’t work if an entry in the report was edited before that
* Issue on Detailed report PDF when audit time filter is ON

## June 2019

#### **What’s new**

* [Idle detection](https://clockify.me/help/track-time-and-expenses/idle-detection-reminders#idle-detection) (Chrome \& Firefox extensions)
* [Time tracking reminders](https://clockify.me/help/track-time-and-expenses/idle-detection-reminders) (Chrome \& Firefox extensions)
* [Automatic clock\-in and clock\-out](https://clockify.me/help/track-time-and-expenses/idle-detection-reminders#automatic-start-and-stop) (Chrome extension)
* [Auto\-stop timer on sleep/lock/shut down](https://clockify.me/help/apps/mac-desktop-app#auto-stop-timer) (Mac)

#### **What’s fixed**

* Entries in Detailed report can’t be changed when filter is active or custom data range is selected
* Optimized performance (report loading, time update, etc.)
* Sidebar is not responsive
* Spaces in names (client, tag, projects…) are not trimmed
* Turning on Rounding resets selected filters
* Confusion when task filter is ON (don’t know why projects aren’t displayed)
* Clearing entered filter from the project picker doesn’t reset the filter
* Newly created project from a template sometimes duplicates team members
* Browser autofill sometimes updates fields of all time entries on a page
* Page paginator is displayed even if there are no multiple pages
* White spaces are not trimmed when creating a workspaces, clients, tags, tasks, projects, and user groups
* Can’t update invoice info sometimes
* User list is displayed multiple times in Team filter on reports
* Project picker on Detailed report not showing favorite projects
* When changing password, “Collapse project” field is affected
* When clicking on start or end time without entering a new value, seconds are removed
* Applied hourly rate on Summary report when subgrouped by anything but time entry is not displayed correctly
* Wrong error message while editing clients/tags/user group name
* Bug with pagination and bulk edit on projects page

## May 2019

#### **What’s new**

* Daily breakdown: Date is a new group/subgroup option in Summary report
* Increment date and time using Up and Down keys on your keyboard
* Improved project/task selector added to Timesheet
* [Browser extension open sourced](https://github.com/clockify/browser-extension) so others can add/fix/improve integrations

#### **What’s fixed**

* Project picker sometimes doesn’t display projects/tasks
* When there’s no project selected, project picker still offers “No project”
* Unclear copy when filtering primarily by task
* When adding users, captcha appears after entering emails
* Missing confirmation dialogues when deleting some stuff
* Time grouped by date isn’t sorted correctly in PDF export
* Summary report and PDF aren’t consistent when grouped by User/Task
* Reset password link should be expired after 2 hours
* When task is a required field, you can’t see projects that don’t have tasks
* When you open a link but you’re not logged in, after logging in you’re not redirected to the original page
* Sometimes you can’t see who is Project manager when you open Access tab on a project
* Admin can’t change hourly rate for users who have not joined yet
* Setting workspace hourly rate sets the same rate to users who don’t have an hourly rate
* In progress entries are not shown on Dashboard
* Can’t download PDF on Safari
* Project manager can change duration for others in Detailed report (but change is not saved, which is ok)
* Adding user group to a project requires refresh to display the change
* Summary report groups projects with the same name even if they have different clients
* Summary report groups tasks with the same name even if they are on different projects
* Entries admins add for others are not locked
* Editing start and end time in Detailed report doesn’t work like on Time tracker page
* Admin can’t modify user groups owners created
* Wrong time gets added in manual mode if you click on ADD immediately after typing end time
* Play button on locked entries is missing
* When you go to some other workspace’s settings, your active workspace is not changed
* Reset password link expires too soon
* Doesn’t show that you’ve removed admin role from someone until refreshing the page
* Can’t change project members’ hourly rates for projects made from templates
* In manual time entry mode, if you enter start or end time and click “ADD” without moving the focus away from the time field first, the row gets added with wrong time
* When you load more projects in Dashboard, new projects are sorted incorrectly
* Users can’t access a project if they’re added via a user group
* Clicking on sidebar doesn’t close the notification popup
* Time zone mismatch notification for some time zones doesn’t work properly
* Time zone label in Personal Settings is not accurate for some time zones
* When bulk editing projects, “Select client” becomes the name of the client
* When you signup but already have an account with that email, a new workspace with the same name is created
* Custom value of project grouping label isn’t reflected in Bulk Edit
* There’s no indicator to wait while Clockify is exporting a report

## April 2019

#### **What’s new**

* Brand new PDF exports (download samples)
* Brand new Time Tracker
	* Bulk edit in time tracker
	* Group same time entries
	* Responsive design (works on all screen sizes)
	* Create projects and tags from time tracker
	* Compact project list
	* Duplicate creates an identical entry
	* Move entries to a different workspace
	* Description field max length raised to 3,000 chars
	* Add time by duration in manual mode
	* Show 50/100/200 entries per page
	* Keyboard shortcuts (n, c, s, m)
	* Improved controls and performance
	* “Filter primarily by: Task” can now also search by client (task @client)
	* Create task and project from project picker by typing “task@project”
* Who can create tags: Admins/Everyone
* [Integrate Clockify with 1,400\+ apps via Zapier](https://clockify.me/zapier-time-tracking)
* Improved Dashboard (billability breakdownby project, tooltips on charts)
* Stable API v1
* Improved integrations via extension
	* Auto\-select project based on project in Trello/Asana/JIRA
	* Custom domain for self\-hosted tools
	* Turn off where you don’t want to see the button

#### **What’s fixed**

* Space not working on some keyboards
* User groups don’t appear in reports’ team filter
* Columns in CSV export of Detailed report are shifted if some value has a comma
* Inconsistent rounding between project status and reports
* Results in the project picker reloads twice after searching and scrolling
* When there are braces “()” in project search, search doesn’t work
* “Show only active tasks” is set to OFF when you open a project
* Hourly rate does not display well in CSV export of Summary report
* Password max length (50 chars) is enforced only on log\-in page
* Infinity% in reports tooltip
* Closing drop\-down menu in Summary report doesn’t work on click
* Project status not showing time spent on tasks

## March 2019

#### **What’s new**

* Brand new [Dashboard](https://clockify.me/help/reports/dashboard)
	* Choose between project and billability chart in Dashboard
	* See all running timers in workspace
	* See when was someone last active
* See your preferred currency symbol in charts
* Automatic update of lock dates

#### **What’s fixed**

* Continue timer button doesn’t pick up project/task field if a user is added on that project via user group
* Can’t scroll down user groups list when saving a report
* When you select an older date in manual mode and add time, the date reverts back to today but the calendar says it’s the same the same old date
* Yearly reports don’t work right in some time zones
* In templates, completed tasks are not copied

## February 2019

#### **What’s new**

* Active workspace is now displayed in sidebar under the user’s name
* Random project colors are now assigned when you create a new project
* On Projects page, Team column displays Anyone if a project is public
* Notification improvements (auto\-open, open/close on click, clear all, design, removed discarded notifications, new notification when you’re deleted from workspace, invite notifications always appears on top)
* Archived projects now appear crossed out on Projects page
* You can now open projects in a new tab from the Projects page (either via right\-click menu or on middle click)
* Print button automatically downloads print\-ready PDF
* Success message when updating billable/non\-billable time

#### **What’s fixed**

* Detailed report sends you to 1st page on edit and sorts the entry as soon as it gets a new value (so you lose track of the thing you’re editing)
* Long user name in sidebar isn’t shortened
* Entering time using space is not working (e.g. 4 am)
* Project picker doesn’t always properly sort by client name
* Total hours missing from saved reports
* Project page throws a lot of “Project updated” message when changing custom color
* When data is deleted form some project, Timesheet saves that project’s name
* Task’s row remains in Timesheet when you delete the task
* A project’s tracked time is different on the Projects page and on the project’s Status
* When you’re on Workspaces page and you create a new workspace, you’re not switched to the newly create workspace
* When deleting a “net joined yet” user,  message doesn’t display user’s email
* Project status’ billable/non\-billable chart has random colors
* When you create new time entries for others, entries don’t appear on top
* Time entries assigned to wrong client in the Detailed report if the project has the same name
* Project status is not updated after you delete time
* When changing password, there is no message that says that the old password is required
* Sometimes the start time resets to 9am
* Edit tag pop\-up opens up for locked time entry even if you can’t edit the entry
* Detailed report doesn’t sort well by duration when seconds are turned off
* Selecting a custom date makes the timesheet move entries by one day
* Label for Project manager sometimes doesn’t appear
* Entered hourly rate doesn’t recognize comma as a decimal separator (only point)
* Reminder with lots of users doesn’t display properly
* Exported report doesn’t reflect sorting
* Invalid date on web in manual mode when the timer starts running in apps/extensions
* Project manager permission is not removed when a user is removed from the project
* When you enter hourly rate or manual estimation, success message is missing
* Filters on Projects page are removed when you delete/archive a project
* When editing tasks on projects, “Show only active tasks” switch reverts to ON
* Can’t see completed tasks on Safari \& Edge
* “Without project” color in reports is always random
* Project colors in pie charts are randomized on hover

## January 2019

#### **What’s new**

* [Bulk edit time entries and projects](https://clockify.me/help/track-time-and-expenses/editing-time-entries#bulk-edit-in-time-tracker)
* Hide Team, Projects, Reports pages from non\-admins
* Free trial of Premium features
* Default project (mobile and desktop apps)
* Regular users can create clients (if “Who can create projects and clients” is set to Everyone)

#### **What’s fixed**

* Optimized performance and resource usage when timer is running
* When there’s only row in Timesheet and it’s empty, when the row is deleted, all entries without project that week get deleted too
* When custom date is selected in Timesheet, time entries made in next week delete entries for the project this week
* Bulk edit of project estimation produces error
* “Fix entries without project” link on Timesheet doesn’t apply filter
* Detailed report PDF doesn’t follow User Settings
* Clockify isn’t automatically refreshed when you accept a workspace invite
* Day of the week is not shown in Weekly report
* When you delete time, total in Timesheet doesn’t change until refresh
* Invited users disappear from the team page until they accept the invite
* Non\-admins can’t define templates
* When transferring ownership, the former owner doesn’t get admin role and the new owner doesn’t get the Owner label
* Editing sorted entries in Detailed report brakes selected sorting
* Saved Detailed report is missing duration column
* Workspace invitation link leads to log\-in page
* Entries in Detailed report are sorted by date of creation (not start time)
* Too many decimals in Project status
* Can’t apply template in Timesheet when a first row is deleted
* Missing entries in PDF export of Detailed report
* User who is part of a user group can’t use template in Timesheet
* When Team Dashboard is disabled for regular users, users still get Team Dashboard if it was their default view
* Greek characters are not shown well in PDF export
* Excel report contains extra row with column numbers
* “Stay logged in” is not checked after log out
* “Transfer owner role” option exists for inactive users

## December 2018

#### **What’s new**

* [Alerts](https://clockify.me/help/projects/alerts)
* Entries for the same activity are grouped in the Summary report
* Group Summary report by User Group
* Transfer workspace ownership

#### **What’s fixed**

* User that was deleted from their only workspace doesn’t get a new workspace
* Editing duration bugs in Detailed report
* Public branded reports can’t be downloaded as PDF if you’re not logged in
* “Add time for team” appears when you’re a regular user
* No indicator that billable filter is applied
* Hourly rate input field doesn’t support comma as a decimal separator (only dot)
* Description can be deleted even if it’s a required field
* Time zone issues
* Regular users can’t use templates
* Detailed report graph isn’t updated when you add time for others
* Project status doesn’t display properly when task\-based estimate is selected
* Workspace gets deleted even if there are other people in it
* Sometimes can’t see task assignee dropdown
* When entering task estimates, tasks are rearranged
* User is not automatically switched to the new workspace when they accept an invite
* Automatically refresh page when user accepts invite
* When you switch Me/Team Dashboard, selection isn’t remembered when you return
* Entries can be locked for future dates (they shouldn’t)
* Some users can’t see all projects they’ve been assigned to
* Admin can’t modify locked timesheets for teammates
* Can’t accept invite on second workspace when user doesn’t have an account

## November 2018

#### **What’s new**

* [Project templates](https://clockify.me/help/projects/project-templates)
* [Add time for others](https://clockify.me/help/track-time-and-expenses/add-time-for-others)
* Added DD.MM.YYYY time format
* Add multiple users at once using a comma (e.g. mail@domain.com, mail2@domain.com)

#### **What’s fixed**

* All items with the same project name are expanded in the Summary report
* Admin can set Owner as inactive
* Column for time entry’s description is too short in the Detailed report
* Team dropdown in a project sometimes doesn’t show user list
* When owner leaves, regular users remain in empty workspace
* Error when entering start/end time with a dot
* Editing time on the first try doesn’t do anything
* CSV export contains hourly rates
* Shifting by day using \<\> in Dashboard and Reports doesn’t work
* Whole date doesn’t show up in the PDF export, plus it doesn’t follow time format from User Settings
* Saved reports: user group filter doesn’t work
* Saved reports: export PDF in a saved report doesn’t work
* Saved reports: anyone with a link can see hourly rate in exported csv and xlsx
* Each new user group is automatically assigned to the owner
* Can’t add users whose email domain is too short (e.g. @qq.com, @t.co)
* Reminder emails are sent even when the paid subscription ends
* Time entries in Timesheet shift by a day when selecting a custom date range

## October 2018

#### **What’s new**

* [Windows](https://clockify.me/windows-time-tracking) and [Linux](https://clockify.me/linux-time-tracking) desktop apps
* Manual time entry mode and offline support for Android/Windows/Linux app
* Better start/end timer sync between all the apps
* You can now search by client name in project dropdown filter (not possible if [smart filter](https://clockify.me/help/projects/project-filter) is turned on)
* Project’s client is now shown in the Timesheet

#### **What’s fixed**

* Entries for a completed task disappear from the Timesheet
* Filtering by client on the Projects page doesn’t work
* Weekly report doesn’t list subgrouped properties properly
* Projects with the same names are combined in reports and timesheet
* When we add a new project in timer mode, and switch to the manual mode, the project disappears
* When we edit the time entry and use smart project filter, and after that use tag, the project disappears
* Every time we click on some project, “Project updated” message appears
* Create a new project from timer page doesn’t work well if we already have some time entry
* A non\-admin user can see time entries of another user if they choose to see archived projects in a report
* Other users see task which are assigned to someone else on public projects
* Can’t see who is workspace owner
* If project favorite is enabled, search bar shows all projects as favourite
* If Tag is a required field, “no tag” is allowed for editing old time entries
* Hourly rate for time entries without a project doesn’t show in Summary report
* Editing project in timesheet adds a new row
* Commas aren’t escaped in task names when exporting reports in CSV
* Play button doesn’t copy the project if you’re not part of the team
* “Without client” filter on Projects page doesn’t work when changed
* Dashboard chart does not match project colors
* Favorite projects don’t show client names
* Favorite projects don’t work well with project filter
* When you invite to workspace someone who already has an account, they don’t show up on the Team page until they accept the invite
* When a user is added to workspace, they are not shown until you refresh the page
* When a user is invited, they get a confusing page which only says Password
* Copy last week in Timesheet doesn’t work properly

## September 2018

#### What’s fixed:

* Project/Task filter is too finicky
* Weekly report email doesn’t follow “Week start” day defined in User Settings
* When adding a tag in the Detailed report, the tag popup freezes
* If a user has one workspace, every time they login or go to workspaces page it throws toast for default workspace change
* When we enter time in a timesheet for e.g. 4th and 5th September and in calendar chose those days, it will move hours for the next day. When we refresh the page it will be good again.
* Zero hours is showing in timesheet page (when a time entry with zero hours is added on Time tracker page)
* If we check Public on a project, then add an assignee to a task, and then check out the public, assign for that task will be empty
* When adding a time entry with a required field, the description is gone and tag can’t be added anymore
* Need to reload the page to see workspace invite notification
* Add Members in a project’s page doesn’t work properly
* Time entry can have a task which doesn’t belong to a specific project via API
* When the timer is running,  “Give manager rights” isn’t clickable in the project team page
* Favorite projects aren’t affected by the filter
* Estimate progress on a project are not shown until you have tracked some time
* Reminder coming for the day which isn’t checked in the days list
* Duplicated projects in the report filter when unchecking client filters

## August 2018

#### **What’s new:**

* [Targets and reminders](https://clockify.me/help/administration/targets-reminders)
* [Android app](https://clockify.me/android-time-tracking)
* Allow same project name if you have different clients

#### **What’s fixed:**

* Inactive/deleted user can’t track time because they have no other workspace
* The dashboard shows other users’ entries
* “Stay logged in” isn’t checked by default when using Google login
* End timer button is the same color as for starting the timer
* Targets block shows up in User Settings even when there are no targets
* Deleting locked entries in Timesheet causes some issues
* The whole week is locked in Timesheet if even a one day in the week is locked
* Entering a future date for the running timer results in bad calculation of duration
* No Project doesn’t show on some workspaces
* The project field remains a required field when Timesheet is disabled
* Invitation link doesn’t work properly if an account already exists
* The total time for that day is not entered after the timer stops (need to refresh the page)
* CSV export of a report is missing a column with time in decimal format
* Updating time entry in the Detailed report doesn’t work when “Do not allow saving time without project” is turned on
* In timesheet, you can add the same project more than once
* Adding project/task after adding durations on timesheet page is disabled
* When the timer is running, date picker doesn’t work
* Time from archived projects disappears from the Time tracker page
* When you add a time entry with a tag, the tag will stay in place for the next time entry
* Error message appears in the console after click on the “X” for the running timer
* Time entry end button doesn’t work properly in some cases
* When you write a description for a time entry and then click out of it, a new notification pops up in green “Successfully updated time entry. If you have clicked another time entry and are typing its description, the notification pops up and stops you from typing
* “\#access\_token” in tab title

## July 2018

#### **What’s new:**

* [Clockify Time Tracker extension for Chrome](https://chrome.google.com/webstore/detail/pmjeegjhjdlccodhacdgbgfagbpmccpe/)
* Chrome extension update: track from selected text, start/stop keyboard shortcut (ctrl\+shift\+x)
* [Integrations with 100\+ apps](https://clockify.me/integrations)
* Change the default “Client” project grouping label
* You can now remove seconds from interface (Workspace Settings \-\> Track time down to the second: Disable)
* Added client name next to project/task on the Timer Tracker page
* Added YYYY\-MM\-DD date format in User Settings

#### **What’s fixed:**

* Error while creating a new saved report
* In report’s filter drop\-down, long words are out of line
* Pixelized bar charts in report’s PDF export
* Client name isn’t included in a report’s PDF export
* Projects client dropdown in report in projects doesn’t contain clients
* If you add multiple entries, their date is changed back by one day
* Scrollbar is difficult to work with (too thin)
* Long decimal values when viewing earnings in the Summary report
* Entered data for a time entry sometimes disappears
* Clockify slows down if you have more than 50 time entries on the Time tracker page
* When changing date of some time entry in the Detailed report, chart doesn’t immediately reflect the change
* Duplicating a time entry, while the timer is on, stops the timer.
* When adding a project after an entry is made, the project’s billability status isn’t applied
* Saved report bugs (can’t save the Summary report, visual bugs when choosing a user group)
* Timesheet template doesn’t work any more
* Reports PDF displays “Without Client” next to client name
* Client label field accepts empty input
* Long decimals of earning in report PDF export
* Non\-billable filter on report page doesn’t work
* PDF report shows only the time for billable hours but not the earnings
* When changing start time while the timer is running, it calculates the correct amount of time when ending it, but does not recalculate while running
* When we duplicate some time entry, the top time entry is changed to that one also
* In the Detailed report, 3\-dots menu is covered and unusable

## June 2018

#### **What’s new:**

* API docs and API key in User Settings
* Improved project status (project and task progress bar, red color when tracked is greater than estimated)
* Projects that are past estimate are red
* Timesheet view compact option
* More apparent when something is editable on Time tracker page
* :30 becomes 30 minutes

#### **What’s fixed:**

* When changing the start time of the running timer, it’s not reflected in the duration (only after stopping the timer)
* Entering 2\.0 in timesheet give 2 minutes (instead of 2h)
* Non\-standard characters from non\-English languages aren’t displayed in PDF export
* Entries sometimes disappear from the timesheet (but are shown in the time tracker)
* Clockify doesn’t recognize space character when typing 1:00 AM in star/end time
* Start and end times disappear in the time tracker
* Project disappears temporarily when you start the timer
* Reports page sometimes doesn’t load
* Various Timesheet view bugs
* Sorting projects by estimate sorts them only using the first number instead of total
* Project name is shortened even when there’s enough of empty space
* Saved report (Public) doesn’t work if you’re not logged in
* Admin label shows twice for some users
* Can’t enter hourly rate for newly added project team members
* When adding time by duration in timer mode, button remains “Start” instead of “Add”
* When printing a weekly report, you get an incorrect display for portrait and landscape layout
* Clicking on time while the timer is running shows 00:00:00
* On Time tracker page, long descriptions in time entries overlap project
* Left side menu is not responsive
* When logo upload fails, there’s no message why
* “Without tag” filter doesn’t work
* Can’t scroll project status on smaller screens
* $ sign covers date on bar chart
* Changing user status sometimes results in an incorrect list of workspaces
* Project/task selections in the Timesheet don’t survive into the next session (unless time has been entered)
* When adding tags after selecting a project in the time tracker, tags disappear
* Entering 2\.0 doesn’t result in 2:00:00

## May 2018

#### **What’s new:**

* [Timesheet view (Beta)](https://clockify.me/help/track-time-and-expenses/timesheet-view)
* Favorite projects
* [Required fields](https://clockify.me/help/track-time-and-expenses/required-fields)
* [Smart project filter](https://clockify.me/help/projects/project-filter)
* [Time rounding](https://clockify.me/help/track-time-and-expenses/time-rounding)
* [Time audit](https://clockify.me/help/track-time-and-expenses/time-audit)
* Set currency as anything you want (e.g. $, ‎€, £)
* “Week starts on” from User Settings get applied to date picker and reports
* Limited what entries regular users can see (only their own entries and other people’s entries on public projects)
* New option in Workspace Settings: “Who can see all time entries: Admins or Everyone”
* New option in Workspace Settings when “Who can see all time entries” is set to Everyone: “Who can see public project’s entries: Admins or Everyone”
* Redirect from login page to tracker if a user is already logged in
* Pagination on Team and Projects pages
* Filter by name, e\-mail, or user access on the Team page

#### **What’s fixed:**

* Changing the filters in a report doesn’t work
* Can’t edit time entries in the Detailed report when audit by duration is on
* When adding time by duration, 0\.5 is converted to 5 seconds. Now it converts to 30min
* Members of user group can’t view project details they belong
* Task list breaks when switching between Team and Task tab
* Time zone alert shows up even when the time zone is right
* Tags, User Settings, Reports, and Projects pages are not displayed properly on smaller screens
* Long descriptions break UI

## April 2018

#### **What’s new:**

* [Lock timesheets](https://clockify.me/help/track-time-and-expenses/lock-timesheets)
* Branded reports with your logo
* [Mac desktop app](https://clockify.me/help/apps/mac-desktop-app)
* [Improved Weekly report](https://clockify.me/help/reports/weekly-report) (more details and breakdown, a total column for each day, client name next to project)
* Delete and manage invited users who didn’t accept the invite

#### **What’s fixed:**

* When you set user as inactive, their hourly rate is lost
* Delete inactive user doesn’t work
* Dropdowns are not closed when switched to another field using Tab
* Dashboard includes the time from the current running timer

## March 2018

#### **What’s new:**

* Mark tasks as done
* Remove a user from a workspace
* See timer running in the browser tab
* Change email
* Delete account
* Full export of Detailed report (clients, tasks, tags, and more)
* Task name character limit raised to 1000 characters
* Clockify automatically assigns you the correct time zone when you first sign up
* Added YYYY\-DD\-MM date format
* Only task assignee can select the task when tracking time
* Time tracker page now shows ALL the entries you’ve made in the last 7 days (not just 10 most recent ones as before). On each “Load more”, Clockify loads one more week. To see (and edit) time entries older than 1 month, you should use Detailed report.  
Use ENTER key to confirm dialogs.
* Time tracker page is much faster now ( even if you have hundreds of time entries)
* Stay logged in longer (no more having to log in each day)
* You can now delete time entries in Detailed report (admins can delete all and team members can delete entries that they made)
* You can now see date of each time entry in Detailed report
* Notification when the time zone is not set correctly
* Sorting is now case\-insensitive

#### **What’s fixed:**

* Clicking on \+ doesn’t fold back tasks in the time tracker
* Long time descriptions in PDF exports overlap duration and amount
* Team member can’t edit their time entries in Detailed report
* Tasks aren’t sorted alphabetically
* Support menu can’t be seen on smaller screen sizes
* Input box text is difficult to see
* Can’t export a saved report
* Completed tasks can’t be selected as filters in a report
* Time entries that start on one day and finish the next shows up in a report for both dates. Now, that time shows up only for the day it finished
* Sometimes, due to different time zones, reports show time entries for the day before
* User group members can’t access the project
* When you remove a user from a user group, time entries from that user on a project where that user group was assigned won’t show in reports
* Hover menu on Reports disappears too quickly
* Long workspace names aren’t displayed fully
* There’s no error message when 1\) adding a task with the same name 2\) task name is too long
* Error when updating task estimate for tasks that have the same name as tasks on other projects
* Users who are not owners can’t see saved reports, even if they saved one
* You can’t edit and select a different project in Detailed report
* Infinite scroll on project list on Time tracker page
* Filtering time entries by name is case\-sensitive (e.g. searching “Recording video” doesn’t return results for “recording video”)
* There’s no page when a password token expires and a user doesn’t know that they have to reset the password again
* When “Who can see Teams Dashboards” setting is set to everyone, some users still can’t see Team Dashboard
* Admin can’t change a user group when updating a saved report
* There are two users with the same email in the system
* Subscribe/unsubscribe button for newsletter doesn’t work

## February 2018

#### **What’s new:**

* [Archive projects](https://clockify.me/help/projects/creating-projects#archiving-projects)
* [Change start time while the timer is running](https://clockify.me/help/track-time-and-expenses/creating-a-time-entry#change-start-time-of-the-running-timer)
* You can now see when a filter is applied
* User group members are now seen on a project’s Team tab
* Continue recording button starts the timer even if you’re in manual time entry mode
* Increased length limit from 250 to 500 characters for time entry description

#### **What’s fixed:**

* Main menu items at the bottom can’t be accessed on smaller screens
* Project status uppers only at the top of the project page
* “Without project” filter doesn’t work
* The amount is always 0 USD in project status
* If a time entry lasts more than 24 hours, it shows just the hours of the last day (a time entry that lasts 25h will display as if it lasts 1h)
* When updating a saved report and clicking save, the dialog doesn’t close
* Dashboard looks bad on smaller screens
* Data in ‘Grouped by’ table should be separated with a space
* Different displays of charts in different time zones on Reports page
* Header is separated from the timetable in Weekly report
* Selecting Archived activity filter doesn’t get applied immediately and doesn’t reset other filters
* Two project dropdowns can be opened at the same time
* No warning message when an owner or a user tries to leave a workspace
* When changing or setting a password and clicking save, the dialog doesn’t close

## January 2018

#### **What’s new:**

* [Export reports to Excel (.xlsx)](https://clockify.me/help/reports/exporting-reports)
* Projects and Time tracker pages load faster

#### **What’s fixed:**

* Filter for summary reports does not work in some cases
* User is allowed to edit project even if he is not admin (when hitting endpoint, not through the application)
* User can’t set password if he first used Google login
* Summary report ignores workspace currency and defaults back to USD
* Time scale in reports have too many decimal points
* Play button in Manual mode not working

## December 2017

#### **What’s new:**

* Group time in Summary report by tags

#### **What’s fixed:**

* Rendering problems on Dashboard page
