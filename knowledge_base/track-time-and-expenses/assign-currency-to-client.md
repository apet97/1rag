---
title: "Assign currency to client"
url: "https://clockify.me/help/track-time-and-expenses/assign-currency-to-client"
category: "track-time-and-expenses"
slug: "assign-currency-to-client"
---

# Assign currency to client

* [Assign currency](#assign-currency)
* [Client currency in Clockify](#client-currency-in-clockify)

# Assign currency to client

4 min read

In case you’re working on projects for clients that use various currencies, instead of using one currency on a workspace level for all your projects, you can assign different currencies to different clients.   
  
For example: *Client A is using US dollars as a currency and Client B euros. You can record project\-related expenses in US dollars for Client A and in euros for Client B.*  

The currency assigned on a workspace level is assigned by default to all the clients available in the workspace. To assign currency to a client, you need to be an admin and your workspace needs to be on a **PRO** or higher subscription plan.

## Assign currency [\#](#assign-currency)

To assign currency to client:

1. Go to the **Clients** page in your workspace
2. In the list of **Clients,** locatetheclient you wish to edit
3. Click on the **Edit** button next to their name
4. Choose the currency from the search bar that appears with all available currencies in the workspace

![](https://clockify.me/help/wp-content/uploads/2023/11/Screenshot-2023-11-06-at-16.27.18-10-658x1024.png)
Currency assigned to a client will be referred to as **client currency** hereafter.

## Client currency in Clockify [\#](#client-currency-in-clockify)

#### Trial [\#](#trial)

* After downgrade or the end of a trial period, all currencies are changed back to the default currency
* Subscription restores currency settings that were in place before the trial period

Currency is present in all client\-related actions, from the client creation or editing, to the amount overview in the dashboard, project status and so on. If other than default currency is assigned to a client, it affects **adding time entries** throughout the app and **Clients**, **Expenses**, **Reports**, **Projects** and **Invoices** pages.

#### Clients [\#](#clients)

By default, every default client gets a default workspace currency. 

Whenever the currency related to the client changes, updated currency values will be presented with the new one being marked as updated.

#### Adding time entries in Time tracker, Timesheet, Calendar, Detailed report [\#](#adding-time-entries-in-time-tracker-timesheet-calendar-detailed-report)

Entry’s billable and cost amounts are calculated in **default currency** if: 

* entry doesn’t have a project
* entry’s project doesn’t have a client

Entry’s billable and cost amounts are calculated in **client currency** if: 

* entry’s project has a client with assigned specific currency

For imported entries, currency is derived from the project. 

Currency is related to the client, not entry, so if the currency is changed on a client level, all entries assigned to those client’s projects will get a new currency. Also, if a project or a client related to that project is deleted, all time entries related to that project get the default currency.

#### Expenses [\#](#expenses)

In case currency is assigned to client,the **default currency** is still used when:

* adding a new expense category that has a unit price
* expense’s project is deleted from the workspace
* project’s client is deleted from the workspace

If client currency, or default currency changes, those changes will not impact the already existing records, only the future ones. 

#### Report [\#](#report)

You can filter out reports by currencies, or find a currency in the search bar at the top of the page.

Different client currencies are displayed in summary report, time and expense reports and exported formats. 

#### Project [\#](#project)

The currency displayed in projects is the one related to the client. If there is no client on the project, the default currency is displayed.  

#### Invoices  [\#](#invoices)

Since all invoices are made for a specific client, the amount is displayed in client currency. If the client’s invoice is updated, the existing invoice is updated to that currency, as well.

For more information on how to create multiple currencies in a workspace, check out [Set up multiple currencies](https://clockify.me/help/track-time-and-expenses/multiple-currencies). 

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
