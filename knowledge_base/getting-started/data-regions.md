---
title: "Data regions for Clockify"
url: "https://clockify.me/help/getting-started/data-regions"
category: "getting-started"
slug: "data-regions"
---

# Data regions for Clockify

* [Data regions](#data-regions)
* [How it works](#how-it-works)
* [Log in to workspace on region](#log-in-to-workspace-on-region)
* [Change region](#change-region)
* [Data residency and API](#data-residency-and-api)

# Data regions for Clockify

4 min read

With data regions, Clockify users can choose the specific region where their workspace data is stored. 

Only the workspace Owner can enable or change data residency for a workspace

This feature is available on [PRO](https://clockify.me/help/administration/subscription-plans#pro) and [ENTERPRISE](https://clockify.me/help/administration/subscription-plans#enterprise) plans. 

Choosing data regions (residency) mainly changes where your data is stored when it’s not being used. It doesn’t change how Clockify handles your data otherwise, or where other types of data are stored. If you don’t choose a specific data region, your workspace data will be stored in the global region by default.

## Data regions [\#](#data-regions)

Clockify offers data regions in the following locations:

* USA (United States)
* EU (Germany)
* UK (United Kingdom)
* AU (Australia)

## How it works [\#](#how-it-works)

### **Data stored in your chosen region**

Once data residency is enabled, the following categories of user data will be stored in a data center within your selected region:

* Time entries (tasks, projects, clients, tags)
* User activity data (e.g. auto\-tracked programs, URLs)
* Invoice details and related financial records
* Workspace configurations specific to your data
* Search indexes of your workspace data

### **Data stored outside your chosen region**

Some categories of data may be stored in regions outside of your selected data region in your [CAKE.com](http://cake.com) account, for operational purposes such as:

* Clockify member profiles (basic user account information: email, name, profile picture)
* Organization/workspace details (Org name, status, membership information)
* Data used for internal metrics (e.g. seat count, usage)
* Logs and analytics for quality of service
* System\-generated IDs (e.g. workspace, kiosk)

## Log in to workspace on region [\#](#log-in-to-workspace-on-region)

When you [log in](https://app.clockify.me/login) to Clockify, all of your workspaces, including those hosted on region, will appear in your workspace list.   
To access a workspace on **region**, click on its name and you’ll be redirected to it.

## Change region [\#](#change-region)

You can change data hosting region for your workspace: 

1. Go to the **[Workspace settings](https://clockify.me/help/track-time-and-expenses/workspaces#workspace-settings)**
2. Choose the **Authentication** tab
3. Click on **Change region** in the **Data region** section  
![](https://clockify.me/help/wp-content/uploads/2022/09/Screenshot-2024-12-23-at-11.03.58.png)
4. Choose the region from the dropdown  
![](https://clockify.me/help/wp-content/uploads/2022/09/Screenshot-2024-04-26-at-09.54.30.png)

You’ll see information about what this data region change may affect. Click **Continue** and **Start data transfer** to begin the process.  
If all conditions for the region change are met, the transfer will start. 

During the transfer, you and all workspace users will be logged out and cannot access the workspace or track time. Transfers can take up to 12 hours.

### Workspace data transfer [\#](#workspace-data-transfer)

All active workspace users will be notified when the transfer starts, when it’s completed, or if it fails. If the transfer fails, your workspace will remain on its original server.

**During transfer**:

* The workspace is locked and unavailable. (If you’re a member of another workspace, you can switch to it)
* Any installed add\-ons are automatically uninstalled
* API operations are locked

Backup copy of your transferred workspace remains in the source region for 7 days. This backup is locked and will be deleted after that period. 

Transfer won’t occur if any user in your workspace already has an account on the destination region’s server.

### Global vs. regional data transfers [\#](#global-vs-regional-data-transfers)

* Owners can transfer data from a global server to a regional server
* Transfers from a regional server back to global are **not possible**
* If you prefer regional hosting but started globally, follow the instructions above to transfer
* By default, when creating your workspace, your data will be hosted on a global server, regardless of your physical location
* While you can’t go from a regional server to a global one, you **can** choose to transfer your data from one regional server to another (e.g. from EU to AU)

## Data residency and API [\#](#data-residency-and-api)

If your workspace data is hosted on a regional server, you must use a region\-specific URL for your API calls to ensure requests reach your data’s correct destination.

| Global API – base URL | Regional API – base URL |
| --- | --- |
| <https://clockify.me/api/v1/> | EU:[https://euc1\.clockify.me/api/v1/](https://euc1.clockify.me/api/v1/) |
| USA:[https://use2\.clockify.me/api/v1/](https://use2.clockify.me/api/v1/) |
| UK:[https://euw2\.clockify.me/api/v1/](https://euw2.clockify.me/api/v1/) |
| AU:[https://apse2\.clockify.me/api/v1/](https://apse2.clockify.me/api/v1/) |

To get data from the workspace in the EU region, use [https://euc1\.clockify.me/api/v1/get/workspaces](https://euc1.clockify.me/api/v1/get/workspaces) instead of the default <https://clockify.me/api/v1/get/workspaces>.

Also, if you create a custom subdomain on a regional server, your API URL will follow the format \[subdomainname.clockify.me].  
For example https://subdomainname.clockify.me/api/v1/get/workspaces.

After a regional transfer, new API keys are generated. This way your API requests are correctly routed to your new data region.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
