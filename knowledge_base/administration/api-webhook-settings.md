---
title: "API & webhook settings"
url: "https://clockify.me/help/administration/api-webhook-settings"
category: "administration"
slug: "api-webhook-settings"
---

# API & webhook settings

* [API keys](#api-keys)
* [Webhooks](#webhooks)

# API \& webhook settings

4 min read

This feature is available to all users on all subscription plans.

Clockify allows you to manage and configure advanced settings for your profile such as **webhooks** and **API keys**. This way get more control over your account’s security and efficiency.

## API keys [\#](#api-keys)

It’s important to save your API keys in a secure place. If you lose a key, or don’t save it, generating a new one will deactivate the old key, potentially breaking existing setups and integrations.   
In Clockify, you can save your API keys and edit them, as needed.

Find your API key settings in the **Advanced** tab of your **Profile settings**.

![](https://clockify.me/help/wp-content/uploads/2018/01/Screenshot-2025-08-11-at-11.20.42-1024x590.png)
Click **Manage API keys** button and see a list of all the APIs you’ve generated on the page that opens. 

Here, you can manage your API keys in a few different ways. 

### **Generate API key**

To create a new key:

1. Click **Generate new** at the top right corner of the page
2. Generate API key window opens
3. Enter a name for your new API key  
**Give a descriptive name, so that you know what it is for.**
4. Click **Generate**

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcu3Y5tcuYCvKanG4aouAfmFlrUeXSJmPrEIoUB7yH9t9NyKqUbyTt1viLlphUf4D49_3AQpG3S1gqJSVNvrEsDetiXFUCK3b99DBkzim44a-RKmi8C8W_cDeyWP7XBkeK8RVeiwA?key=jdo3BnHEVYy3WcX3M-qUcQ)
Your new key will be automatically created and added to the list on the **Manage API keys** page.

### **Edit API key**

If you need to make some changes to the API key:

1. Click the **three\-dots menu** next to the API key you want to disable
2. Choose **Rename/Delete** option  
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeDQ7esHtbldMHImwoCuSQuFYBwvPUmQncmhnVm46ZuKOxNF5GBjrDqVMGV_hkVM3URCuUFUovf5bnTZ6MpOoWnOhDP8BYr1JlxaVWncNE6F3Q0FSkqTyHu7YCvYe_U51Xv6vv3Gg?key=jdo3BnHEVYy3WcX3M-qUcQ)
3. Enter new name or click **Delete** to confirm the action

New API key name is automatically updated on the **Manage API keys** page.  
After being deleted, that API key can no longer be used and is automatically removed from the **Manage API keys** page and the **Accounts** tab in the **Workspace settings**.

## Webhooks [\#](#webhooks)

Create webhooks to receive real\-time notifications and data updates.

This feature is available to workspace Owners and Admins. Webhooks section is not visible to other user roles.

Follow these steps:

1. Go to **Preferences**
2. Select the **Advanced** tab
3. In the **Webhooks** section, click on **Manage webhooks**
4. You will be redirected to the **Webhooks** page

If you are part of multiple workspaces, choose the relevant workspace.

![](https://clockify.me/help/wp-content/uploads/2024/05/Screenshot-2024-05-08-at-16.44.15-1024x261.png)
To create a new webhook:

1. Click on the **Create new** button at the top right corner
2. In the **Create webhook** window, provide the following details:  
![](https://clockify.me/help/wp-content/uploads/2018/01/Screenshot-2024-05-08-at-16.47.36.png)  
**Name**: Specify a name for your webhook  
**Endpoint**: Enter the webhook’s endpoint URL  
**Event**: Choose the event that will trigger the webhook
3. Click on **Create** to complete the process

If you are part of multiple workspaces, choose the relevant workspace.

Created webhook events are sorted in alphabetical order. 

Webhook event can be disabled while created, if Clockify workspace is not on the subscription plan that supports this feature.  

### Webhook details  [\#](#webhook-details)

If you’d like to see webhook details, you can do that by opening a three\-dots menu of that webhook. 

* Go to the webhook you’d like to examine
* Open **Details** in the three\-dots menu
* New page opens with the list of **Webhook attempts**

Here, you can see the attempt time and status of the event. 

**Tip: Attempt time follows the format set in the preferences.**  
Test webhook can also be displayed in the Webhook attempts with the appropriate status and payload. 

### Edit webhook [\#](#edit-webhook)

If you’d like to modify any data related to the webhooks, you can do that by choosing the editing option.

* Go to the webhook you’d like to edit
* Open **Edit** in the three\-dots menu
* New page opens with the list of **Webhook attempts**

Here you can modify all the elements of the created webhook: 

* Change webhook name
* Change endpoint URL
* Choose another event from the dropdown
* Change (reset) **Signing secret**

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdB2FZtFbQhJjC7ouCX1mz5HoDPub3zl_YlLudDX9MomnrQrejR7kCKehD5jmK9isy5Y4AR8v8dkdAbhu4-8Qi7UysH2533nmf9-oJZPoNqHlvZlOLC1WsMZhbDLlH5PQa1WHLo7w?key=ayWEdBbSRqLBF8m8bS__2Q)
### Delete webhook [\#](#delete-webhook)

If you’d like to delete webhook that is deprecated or you’re not using anymore, you can do that in the following way: 

* Go to the webhook you’d like to edit
* Choose **Delete** in the three\-dots menu
* Click **Delete** in the confirmation window

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcId1fNVOiKWbmeo-MSiSf2SpWQsEQvs6u0dnkvePCQRc1ANUwwt6ZcoSd-UICvUZkSCAP4Ky6Z4DBiEXuD6CI906_WdTQipVXo76KfaLrkaXHJgLK326VXigyKoVOsztTQMzcZSA?key=ayWEdBbSRqLBF8m8bS__2Q)
### Marketplace webhooks [\#](#marketplace-webhooks)

Add\-on users don’t have a **Resend** button in add\-on webhook attempts.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
