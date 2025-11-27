---
title: "JIRA integration"
url: "https://clockify.me/help/integrations/tracking-integrations-integrations/jira-integration"
category: "integrations"
slug: "jira-integration"
---

# JIRA integration

* [Install the Clockify JIRA app](#install-the-clockify-jira-app)
* [Track time](#track-time)

# JIRA integration

7 min read

Our free JIRA app enables you to track time on issues directly from Atlassian JIRA with just one click. 

Clockify plugin for JIRA is available in the JIRA web app, JIRA mobile app for Android and iOS, as well as JIRA macOS desktop app.

User interface displayed in this video may not correspond to the latest version of the app.

## Install the Clockify JIRA app [\#](#install-the-clockify-jira-app)

To start tracking the time, you’ll need to install the Clockify app in JIRA. 

**JIRA Cloud \+ Clockify Cloud** 

1. [Get the app](https://marketplace.atlassian.com/apps/1222624/clockify-time-tracking-timesheet?hosting=cloud&tab=overview) from the Atlassian Marketplace (make sure you installed the app developed by CAKE.com)
2. Click **Get it now** button and select **Cloud**
3. Choose a site from the dropdown list where you want to install the app and click the **Install app** button

****JIRA ****Server**** \+ Clockify**** ****Cloud****

1. Log in to your JIRA instance and go to **Manage apps**
2. On the Administration page, search the Atlassian Marketplace for JIRA and find Clockify app
3. Click **Install** (make sure you’re installing the app developed by CAKE.com) and confirm installation by clicking **Accept \& Install**

![](https://clockify.me/help/wp-content/uploads/2020/07/JiraAdministrationMarketplace.png)
You should receive a notification once the installation is complete and the Clockify timer button will appear in all JIRA issues so you can start tracking time. 

Only JIRA admins can manage apps in JIRA and install the Clockify app.

******JIRA ****Cloud**** \+ Clockify** Server****

Since this plugin is not being installed via the JIRA marketplace, you will first have to **Enable development mode** in your cloud JIRA by going to **Manage Apps**/**Settings**. (After the installation is complete, this setting can be turned off).  
After **Enable development mode** is turned on, you can install your custom JIRA plugin by selecting the **Upload URL** option, and providing a previously created public URL.

**JIRA Data Center (JIRA Server) \+ Clockify Cloud/Server**

1. Go to **Administration** \> **Manage apps**
2. Click **Upload app**
3. Enter URL https://clockify\-resources.s3\.eu\-central\-1\.amazonaws.com/downloads/clockify\-jira\-plugin.jar
4. Click **Upload** and install

If you’re using Clockify Server, you need to specify in the plugin’s Settings the URL to your Clockify Server account.

### API Key [\#](#api-key)

The first time you click on Clockify timer button, you will be asked for the Clockify API key. This key is used to connect your Clockify account to your JIRA account. 

1. Log in to your Clockify account and go to the **Profile settings** \> **Preferences** page \> **Advanced** tab (or click on the [Get API key](https://app.clockify.me/user/settings) link in your JIRA issue and you’ll be automatically redirected to your Clockify Profile settings).
2. At the bottom of this page click the **Generate** button to generate your API key
3. Copy your key to the API key field in your JIRA issue

![](https://clockify.me/help/wp-content/uploads/2020/07/apijira.jpg)
Once you enter the key, you will not be asked for it again. However, if you, at some point, generate a new API key for your Clockify account, you will need to update it to match the one in JIRA as well, by resetting it. 

### Regional server hosting [\#](#regional-server-hosting)

If you’re using regional server, follow the instructions below to successfully integrate Clockify with JIRA. 

******JIRA ****Cloud**** \+** Clockify on Regional Server****

After you turn on **Enable development mode**, depending on the region you’re hosting your data in, you need to insert one of the following JSON files in the **Upload URL** field:

[https://jira.use2\.clockify.me/atlassian\-connect.json](https://jira.use2.clockify.me/atlassian-connect.json) – USA (United States)

[https://jira.euc1\.clockify.me/atlassian\-connect.json](https://jira.euc1.clockify.me/atlassian-connect.json) – EU (European Union)

[https://jira.euw2\.clockify.me/atlassian\-connect.json](https://jira.euw2.clockify.me/atlassian-connect.json) – UK (United Kingdom)

[https://jira.apse2\.clockify.me/atlassian\-connect.json](https://jira.apse2.clockify.me/atlassian-connect.json) – AU (Australia)

**JIRA Data Center (JIRA Server) \+ Clockify on Regional Server**

1. Go to **Administration**
2. Choose **Manage apps**
3. Click **Upload app**
4. Enter URL https://clockify\-resources.s3\.eu\-central\-1\.amazonaws.com/downloads/clockify\-jira\-plugin.jar
5. Click **Upload** and install

After installation is completed, select the installed app and click **Configure** to proceed.

Depending on the region you’re hosting your data in, you need to insert one of the following JSON files in the URL field:

[https://jira.use2\.clockify.me](https://jira.use2.clockify.me/atlassian-connect.json) – USA (United States of America)

[https://jira.euc1\.clockify.me](https://jira.euc1.clockify.me/atlassian-connect.json) – EU (European Union)

[https://jira.euw2\.clockify.me](https://jira.euw2.clockify.me/atlassian-connect.json) – UK (United Kingdom)

[https://jira.apse2\.clockify.me](https://jira.apse2.clockify.me/atlassian-connect.json) – AU (Australia)

## Track time [\#](#track-time)

When you click on the Clockify timer button you will be able to choose between the Timer and Manual mode you can use to track your time.

### Timer mode [\#](#timer-mode)

Make sure you’re in the Timer tab and then start the timer. When you are done, click the **Stop** button and your time entry will be recorded. 

If you have multiple workspaces in Clockify, you can select the desired workspace before starting the timer in JIRA.

![](https://clockify.me/help/wp-content/uploads/2020/07/jiratimers.jpg)
The timer is synced to your Clockify account across all devices and can be stopped in JIRA or from any of the Clockify apps (browser, mobile, or desktop). 

If you start tracking time in another JIRA issue without stopping the previous timer, the timer on the first issue will be automatically stopped and saved, and a new timer on the second issue will start. 

### Manual mode [\#](#manual-mode)

If you forgot to start the timer, or you prefer to fill in all your work hours in one go, you can use manual mode. 

Make sure you’re in the Manual tab and then enter the time you have worked on the time entry. When you are done, click the Add time button and your time entry will be recorded. 

If you have multiple workspaces in Clockify, you can select the desired workspace before adding the time entry.

![](https://clockify.me/help/wp-content/uploads/2020/10/Screenshot-at-11-00-48.png)
Please note that the current limitation for projects shown in the Project picker on Plug\-in is 790\.

### What gets recorded in Clockify [\#](#what-gets-recorded-in-clockify)

When the timer starts, Clockify will automatically pick up the issue title, task, project, and label (tag) from JIRA if the corresponding project, task, etc. already exists in Clockify. 

If there is no corresponding JIRA project, task, or tag in Clockify, the integration can automatically create it in Clockify. To make this possible, a user must have permission to create projects, tasks, and tags in Clockify. These permissions can be set in the Workspace settings.

* **Description –** Clockify will pick up the JIRA issue key number and issue title as a time entry description.
* **Project –** your project in JIRA will be picked up as a Project in Clockify.
* **Task –** the JIRA issue key where you started the timer will be picked up as a task (subproject) in Clockify. You can manually change the task you are working on directly from JIRA by clicking on the task name and selecting the one you want from the dropdown.   
Tracking time on a Child issue in JIRA will be picked up as a task in Clockify with a tag **Subtask**.
* **Tags** – correspond to issue types (bug/task/story) and labels in JIRA. You can add more tags to your time entry directly from JIRA.

Information about an Epic or a Sprint will not be recorded, however, if you track time directly on an Epic in JIRA it will create a time entry in Clockify with a tag **Epic**. 

In order for the integration to pick up the right project/task/tag, it either has to already exist in Clockify, or you need to set the right permissions in Clockify’s Workspace settings and make sure all users can create new projects/tasks/tags.

![](https://clockify.me/help/wp-content/uploads/2020/07/jiraclockify.png)
### Work log [\#](#work-log)

When you stop the timer, the entry will be saved in Clockify and a time log will be created in the JIRA work log (time spent field). Work log shows a timeline of each time entry recorded by everyone for that issue.

If you edit/delete a time log entry from JIRA work log, note that this will not be synced with Clockify, meaning that a time entry in Clockify will not be updated/deleted. Likewise, if you edit/delete a time entry in Clockify, it will not be reflected in JIRA. 

Only time entries **stopped in JIRA issues** are going to be added to the work log. 

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
