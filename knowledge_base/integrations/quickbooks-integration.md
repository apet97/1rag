---
title: "QuickBooks"
url: "https://clockify.me/help/integrations/tracking-integrations-integrations/quickbooks-integration"
category: "integrations"
slug: "quickbooks-integration"
---

# QuickBooks

* [Connect QuickBooks Online](#connect-quickbooks-online)
* [Set up Clockify for the first time](#set-up-clockify-for-the-first-time)
* [Data mapping](#data-mapping)
* [Send time to QuickBooks](#send-time-to-quickbooks)
* [Disconnect QuickBooks Online](#disconnect-quickbooks-online)

# QuickBooks

6 min read

Connect Clockify to your QuickBooks Online account and send time entries.

QuickBooks integration is a paid feature, which you can enable by [upgrading](https://clockify.me/pricing) your workspace to Clockify’s Standard, Pro, or Enterprise plan and QuickBooks’ Essentials, Plus, or Advanced plan.

User interface displayed in this video may not correspond to the latest version of the app.

Integration supports **QuickBooks Online (Essentials or Plus plan).** Doesn’t work with QuickBooks Desktop or QuickBooks Online Simple Start plan. 

If you have Payroll feature enabled in QuickBooks, Clockify integration won’t work due to system’s capabilities.

## Connect QuickBooks Online [\#](#connect-quickbooks-online)

1. Log in to your Clockify account
2. Go to the **three dots** menu next to the workspace name
3. Choose **Workspace settings**, then **Integrations** tab
4. Expand QuickBooks section and click **Connect to QuickBooks**
5. Authorize Clockify to access QuickBooks (you’ll need to be logged in to QuickBooks)
6. Sync Clockify with QuickBooks
7. Create missing users from Clockify and missing customers from QuickBooks

**Before connecting to QuickBooks**, make sure you have invited all users in Clockify, they have accepted the invite, and their names in Clockify (in [Profile settings](https://clockify.me/help/administration/profile-settings)) and QuickBooks (their display name) are the same.

If you don’t have any projects in Clockify, everything will be pulled from QuickBooks so you don’t have to create anything manually. 

**If you add new user in Clockify, or new customer in QuickBooks**, you’ll have to perform the sync again manually in the Integrations tabs before trying to send time to QuickBooks (Clockify won’t make any changes to your QuickBooks account unless you do it explicitly).

Please note that if you can’t sync certain time entries, you should check the settings on the QuickBooks side and whether [Close the Books](https://quickbooks.intuit.com/learn-support/en-us/help-article/close-books/close-books-quickbooks-online/L59LelyPM_US_en_US) option is turned on for that year. 

**If you want to connect just one or several specific projects** (e.g. to test the integration):

1. Create a project with the same name as the customer (or project) in QuickBooks
2. Create employee(s) in QuickBooks with same name as they have in Clockify
3. Connect Clockify with QuickBooks
4. After you’ve connected, DON’T create missing users and project (at this point, users and projects between Clockify and QuickBooks with the same name are connected to each other)
5. Go to Detailed report, [filter](https://clockify.me/help/reports/filtering-reports) the report by the project/user you need, and send to QuickBooks

![](https://clockify.me/help/wp-content/uploads/2024/03/quickbooks-connect-11.png)
## Set up Clockify for the first time [\#](#set-up-clockify-for-the-first-time)

1. Invite team members to track time
2. Make sure their names in Clockify and QuickBooks are the same
3. Connect QuickBooks with Clockify
4. Sync users and customers (this will create a project in Clockify for each QuickBooks project/customer)
5. Track time on projects in Clockify
6. Send tracked time to QuickBooks using Detailed report

## Data mapping [\#](#data-mapping)

* **User Name in Clockify** and **Employee Display Name in QuickBooks** have to be identical in order to sync
* If user doesn’t exist in QuickBooks as an employee, you’ll perform sync in Settings \> Integrations \> QuickBooks
* **Project Name in Clockify** and **Customer (or Project) Name in QuickBooks** have to be identical in order to sync
* If you have parent customers in QuickBooks, **Sub\-customer** in QuickBooks will be treated as **Project** in Clockify and its **Parent** in QuickBooks will be treated as **Client** in Clockify
* If a project doesn’t exist in QuickBooks as a customer (or project), you’ll first have to create it manually in QuickBooks using the exact same name as in Clockify, and perform sync in Settings \> Integrations \> QuickBooks

![](https://clockify.me/help/wp-content/uploads/2024/03/quickbooks-user-employee-mapping11.png)

Employee name in QuickBooks and user name in Clockify (editable in CAKE.com account [Profile settings](https://cake.com/help/administration/profile-settings/)) must match

![](https://clockify.me/help/wp-content/uploads/2024/03/quickbooks-customer-project-mapping11.png)

Customer name in QuickBooks and project name in Clockify must match   
(or Customer\>Sub\-Customer in QuickBooks with Client\>Project in Clockify

Also, keep in mind that QuickBooks has a robust structure with the hierarchy going up to four levels in depth: 

* QuickBooks Customer ———\> Clockify Client
	* QuickBooks Sub\-customer 1————\> Clockify Client and Project (same name)
		* QuickBooks Sub\-customer 2 ———–\> Clockify Client and Project (same name)
			* QuickBooks Sub\-customer 3 ————\> Clockify Project

  
This means that you can have customers that are both, a **Parent** customer and a **Child** customer (**Sub\-customer**) at the same time (e.g. Sub\-customer 2\). In that case, when mapping it into Clockify, it will be mapped both, as a **Client** (since it’s a **Parent** of Sub\-customer 3\) and a **Project** (since it’s a **Child** of Sub\-customer 1\) with the same name.

QuickBooks also has a **Project** in their system. Depending on its position in the hierarchy, QuickBooks Project can be mapped either as Project or Client in Clockify as presented in the scheme above.

## Send time to QuickBooks [\#](#send-time-to-quickbooks)

Once you’ve connected Clockify and QuickBooks, and synced users and customers/projects, you’ll see the QuickBooks button in the [Detailed report](https://clockify.me/help/reports/detailed-report).

1. Go to the Detailed report
2. Click QuickBooks button to see all time entries that haven’t been sent to QuickBooks
3. Review if you wish to send all the data you see and apply filters if necessary
4. Click **Send to QuickBooks**

Clockify sends the following information to QuickBooks: 

* User
* Description
* Project
* Date
* Duration
* Billable status
* Billable rate

Once all the entries have been sent successfully, the system will mark them as sent. To see time entries that have been sent, click on the QuickBooks dropdown (next to **Showing not sent entries**), and choose **Show sent entries**.

Once an entry has been sent, it can’t be sent again. If you make changes to an entry, the change won’t be reflected in QuickBooks (meaning you’ll have to manually update time in QuickBooks too). To avoid this, it’s best to send only [approved time](https://clockify.me/help/track-time-and-expenses/approval) to QuickBooks.

![](https://clockify.me/help/wp-content/uploads/2024/03/quickbooks-send11.png)
**Notes**

* It’s not possible to send billable entry without a project to QuickBooks
* If you turn rounding ON, Clockify will send rounded values
* Only Admins can send time to QuickBooks
* Individual time entries longer than 23h55m won’t be sent
* Clockify sends user’s name, date, project (i.e. customer in QB), billable status, hourly rate (if billable), duration, description
* Clockify also sends time entries of inactive and deleted users that were previously synced

![](https://clockify.me/help/wp-content/uploads/2024/03/quickbooks-sent-time11.png)

Time sent from Clockify will be available as time data in QuickBooks, so you can run reports and invoice 

## Disconnect QuickBooks Online [\#](#disconnect-quickbooks-online)

To disconnect your QuickBooks account:

1. Log in to your Clockify account
2. Go to the **three dots** menu next to the workspace name
3. Choose **Workspace settings**, then **Integrations** tab
4. Expand QuickBooks section and click **Disconnect**
5. Confirm the action

Once you’ve disconnected QuickBooks, you’ll no longer see the QuickBooks button in Detailed report and Clockify won’t have access to your QuickBooks account.

You can reconnect to QuickBooks on the same page by clicking **Connect to QuickBooks**.

![](https://clockify.me/help/wp-content/uploads/2024/03/disconnect-qb11.png)

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
