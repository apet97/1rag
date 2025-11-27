---
title: "Time entries aren\u2019t syncing to QuickBooks"
url: "https://clockify.me/help/troubleshooting/entries-not-syncing-to-quickbooks"
category: "troubleshooting"
slug: "entries-not-syncing-to-quickbooks"
---

# Time entries aren’t syncing to QuickBooks

* [QuickBooks plan may not be supported](#quickbooks-plan-may-not-be-supported)
* [Client and project mapping don’t match](#client-and-project-mapping-don’t-match)
* [Check for new users and customers](#check-for-new-users-and-customers)
* [Reconnect the integration](#reconnect-the-integration)
* [Only billable time entries will sync](#only-billable-time-entries-will-sync)

# Time entries aren’t syncing to QuickBooks

3 min read

If time entries aren’t syncing to QuickBooks, it could be due to how the integration is set up, plan compatibility, or how projects and clients are structured. Here’s how the connection works and what to check if syncing fails. 

## QuickBooks plan may not be supported [\#](#quickbooks-plan-may-not-be-supported)

Clockify QuickBooks integration works only with:

* QuickBooks Online Essentials
* QuickBooks Online Plus

  
If you’re using QBO Simple Start, Advanced with Payroll, or any plan with Payroll enabled, the integration will not work due to compatibility issues. 

To check your plan:

1. Open QuickBooks Online
2. Go to Account and Settings \-\> Billing and Subscription
3. Review your current plan and features

## Client and project mapping don’t match [\#](#client-and-project-mapping-dont-match)

Mapping between Clockify and QuickBooks happens based on matching names and structure. 

* The user name from Clockify must match an Employee name in QuickBooks

* If using only projects in Clockify, project names must be identical to Customer names in QBO
* If using both clients and projects in Clockify:
	* Clockify clients must have the same name as the parent customers in QBO
	* Clockfy projects must have the same name as sub\-customers in QBO

If you only have projects in Clockify, in that case, you would sync them with customers in QuickBooks; however, if projects also have clients in Clockify, then your project will actually be a sub\-customer and the client a parent customer in QBO.

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXcM2FtvQ5C9xbwDO7axJ7cbmZNU0Qszf4lkcnDKqVtamJuxpHcTHz_ORHKM8_X6t4YLBd0mhcByRTT6Oyt9zwohLI4n8txj9m2BHrjDFoWwY3KmzqoVLg4LQhRK0oNa3Y16osgN.png)
## Check for new users and customers [\#](#check-for-new-users-and-customers)

If everything has been set following the data mapping rules, make sure to resync your QBO data with Clockify. 

1. Click on the three dots next to your Workspace name
2. Select “Workspace settings.”
3. Click on the Integrations tab
4. Click on the “Check for new users and customers” button

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXeTqh7nwagWv5FZx9A_LNG_m5ZpF6Bzo9aVlhte9bG_rp8LhUfkfFycZhk2FPoWrnqgGrKw2bmIV7vHC9nZKT2OrwgogYofMdUibqrSFJqgHvoh2xgbM7hadWuUpm_bWxidXp7y.png)
## Reconnect the integration [\#](#reconnect-the-integration)

If data sync was unsuccessful, try disconnecting the integration. 

1. Navigate to the Workspace settings by clicking on the three dots next to the Workspace name
2. Open the Integrations tab
3. Select the dropdown arrow next to QuickBooks
4. Click Disconnect
5. Reconnect your QuickBooks account and follow the prompts

## Only billable time entries will sync [\#](#only-billable-time-entries-will-sync)

Make sure your time entries meet these criteria:

* Marked as billable (represented by blue dollar icon in Clockify)
* Assigned to a project (and client, if applicable)
* Tracked by a mapped user

You can check all of this via the Detailed report in Clockify. 

Still having issues? The Clockify Support Team will be happy to look into it and assist you further. Please contact us at support@clockify.me and include the following details:

1. Information about your current QBO plan and whether you have a Payroll feature enabled
2. A screenshot of any error messages you might have received when sending time to QBO
3. A screenshot of your projects, clients, and users from both Clockify and QuickBooks

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
