---
title: "Browser extension"
url: "https://clockify.me/help/apps/chrome-extension"
category: "apps"
slug: "chrome-extension"
---

# Browser extension

* [How it works](#how-it-works)
* [Dark mode](#dark-mode)
* [Track time from selected text](#track-time-from-selected-text)
* [Track time from web app Projects page](#track-time-from-web-app-projects-page)
* [Default project and task](#default-project-and-task)
* [Idle detection](#idle-detection)
* [Pomodoro](#pomodoro)
* [Start/stop automatically](#start-stop-automatically)
* [Notifications](#notifications)
* [Reminders](#reminders)
* [Integrations](#integrations)

# Browser extension

10 min read

Clockify Time Tracker for browser lets you track time from anywhere on the web, without opening Clockify.

[Get Chrome extension →](https://chrome.google.com/webstore/detail/pmjeegjhjdlccodhacdgbgfagbpmccpe/)

[Get Firefox extension →](https://addons.mozilla.org/en-US/firefox/addon/clockify-time-tracker/)

For step\-by\-step guidance on using Clockify in your browser, watch the video and follow the instructions below.

User interface displayed in this video may not correspond to the latest version of the app.  

## How it works [\#](#how-it-works)

### Log in [\#](#log-in)

To start tracking time, you’ll first need to log in to the browser extension.

To log in:

1. Click the **Login** button
2. You’ll be redirected to the web app **Login** screen  
![](https://clockify.me/help/wp-content/uploads/2018/07/Screenshot-2024-01-31-at-09.57.18.png)
3. Continue the process by entering and verifying your email

After you complete the login process, you can start using the extension and tracking time.    

If you’re already logged in, the extension will automatically open Clockify.  
If you don’t have a Clockify account yet, you can create it by clicking the New here? **Create an account** button.

### Logging in with custom domain and subdomain [\#](#logging-in-with-custom-domain-and-subdomain)

Users on custom domain or subdomain can also use the Chrome browser extension:

1. Open the extension
2. Find the **Log in to custom domain** or **Log in to subdomain** (Pro plan users on subdomain) link at the bottom of the extension screen

If you’re logging in with a **custom domain**, choose your custom address.   
If you’re logging in with a **subdomain**, enter subdomain name in the field (e.g. https://acme.clockify.me).

Click **Submit** and log in with your email or SSO.

### Time tracking [\#](#time-tracking)

Once you’ve logged in to the extension, type what you’re working on and start the timer.

To edit the running time, click on the running entry to bring up its details. There you can change the description, change running time, mark time as billable, and add project and tags.

You can also edit past time entries by clicking on them, or add time manually (once you switch to manual mode in the settings).

To quickly continue tracking time, click on the play icon for the time entry you wish to continue, and the timer will start ticking again for that entry.

Clockify also supports tracking holidays and time off on the web app. Time off and holiday entries are distinctly displayed in the tracker. 

For more information on how to time off and holiday entries, check out [Track holidays \& time off](https://clockify.me/help/track-time-and-expenses/track-holidays-time-off).

## Dark mode [\#](#dark-mode)

You can enable dark mode for the extension (as well as desktop and mobile app) in the app’s Settings.

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-25-at-09.19.39-611x1024.png)
## Track time from selected text [\#](#track-time-from-selected-text)

1. Go to **Settings**
2. Check **Enable context menu** option  
![](https://clockify.me/help/wp-content/uploads/2018/07/Screenshot-2024-03-26-at-12.13.04.png)
3. Select any text in the browser (e.g. task name in Trello, email subject in Gmail, issue in Github)
4. Right\-click on the selected text
5. Click **Start timer with description** in the right\-click menu

![](https://clockify.me/help/wp-content/uploads/2024/03/track_time_from_selected_text-1024x429.png)
## Track time from web app Projects page [\#](#track-time-from-web-app-projects-page)

If you’re involved in an extensive project and task planning but would like to easily navigate through the Clockify web app, you have the option to start the timer from the created projects and tasks on the **Projects** page. 

In order to use this feature, you need to be logged in to the Clockify browser extension and the Clockify web app with the same account. 

Once you’re logged in:

1. Navigate to the **Projects** page
2. Find the project you’d like to track time for
3. Hover over the project and the start button will appear
4. Click the button
5. Timer will start running and the time entry details window will appear  
![](https://clockify.me/help/wp-content/uploads/2018/07/Screenshot-2024-03-25-at-09.52.53.png)
6. Choose project task, make some other modifications, or stop the timer

To start the timer for a project task: 

1. Click on the project in the **Projects** page
2. Go to the **Task** tab
3. Hover over the task and the start button will appear
4. Click on the button
5. Timer will start running and the time entry details window will appear
6. The extension will pick up project and task name from the web app  
Task name will be additionally in the description

If you stop the timer in the extension, that entry will be added in the time tracker with all other info related to that entry.

Start time button is not available for archived projects and tasks.

## Default project and task [\#](#default-project-and-task)

If you work on the same project every day, set a default project or task. Then, all you have to do is type what you’re working on, start the timer, and the project will be selected automatically.

You can select:

* **Fixed project** to always use when you start a timer for an entry without project
* **Fixed task** to always use when you start a timer for an entry without project/task
* **Last used project** to pick up most recently used available project (if task is required, task will also be picked up)

Enable default project in the Settings.

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-25-at-09.56.59-612x1024.png)

![](https://clockify.me/help/wp-content/uploads/2024/03/chrome_extension_default_project-640x1024.png)

## Idle detection [\#](#idle-detection)

While tracking time, Clockify browser extension can detect when you’re away from your computer so you don’t accidentally log that time. The extension detects when you’re inactive based on your mouse and keyboard movements.

If there’s no mouse movement or keyboard strokes for X minutes, the timer will enter into idle mode. It will continue running, but it will treat those X minutes (and the time after that) as idle. When you become active, a notification will pop up, asking what you want to do with the idle time.

You can choose to:

* **Discard idle time** – The timer will be stopped and the detected idle time will be removed from its total.
* **Discard and continue** – The current timer will be stopped, the detected idle time will be removed from its total, and a new timer will immediately start for the same activity.
* **Keep idle time** – The timer will keep running as it is. In order to keep idle time in the extension, simply close or dismiss the notification.

[Can’t see idle notification?](https://clockify.me/help/track-time-and-expenses/idle-detection-reminders#cant-see-notifications)

**To set up idle time detection in the extension:**

1. Click on the **Clockify timer button** located in the upper right\-hand corner of your browser
2. Open the extension settings by clicking on the **hamburger icon**
3. Go to **Settings**
4. Select **Idle detection** checkbox
5. Specify the number of minutes of inactivity after which the idle time will be detected
6. Click **Done**

Idle detection will work only if you started the timer from the extension (it won’t work if you started the timer from the web but have the extension installed).

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-25-at-10.08.12-623x1024.png)
## Pomodoro [\#](#pomodoro)

With the Pomodoro timer, set up notifications to let you know when it’s time to take a short break.

To enable Pomodoro:

1. Open the extension settings by clicking on the hamburger icon
2. Go to **Settings**
3. Check the **Enable Pomodoro timer**

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-25-at-10.14.51.png)
**Timer interval** – set how long will your Pomodoro session last.

**Short break** – set how long will your short break last.

**Long break** – set how long will your long break last and after how many short breaks it will occur. For example, if you set Long break starts after 3 short breaks your fourth break will be the long break.

For Long Break to work you would need to start/stop the timer from the notification popup. If you stop the timer manually, it will reset the count sessions and will start over.

If you have built\-in notification sound enabled in Windows already, the notification will play both sounds so it’s best to have just one option enabled.

Disable/enable notification sound on Windows by going to **Settings**\>**System**\>**Notifications \& actions** then click on the **Google Chrome** icon (note: this switch should still be set to ON) and switch off or on **Play sound when the notification arrives**.

**Default break project** – Select the default project on which the break timer will be logged (**Last used project** will take the project/task from the timer just before the break).

**Automatic** **breaks** – You can choose to automatically start/stop the timer when the Pomodoro period or break ends.

**Focus mode** – When enabled, your time logs will be hidden while you have the timer running and you’ll just see a visual representation of time left.

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-25-at-10.17.32-625x1024.png)
## Start/stop automatically [\#](#start-stop-automatically)

You can automatically start/stop the timer when you open/close the browser so you don’t have to worry about clocking in when you start working or clocking out when you finish with your work. 

1. Open the extension settings by clicking on the hamburger icon
2. Go to **Settings**
3. Check the **Start timer when browser starts** and/or **Stop timer when browser closes**

![](https://clockify.me/help/wp-content/uploads/2024/02/Screenshot-2024-02-08-at-14.31.52.png)
If you shut down your PC and leave the browser open the timer will continue working. You would have to close the browser first and then turn off the computer in order for the timer to stop.

In case you have both idle detection and auto\-stop enabled, if the timer is stopped automatically, idle detection will not trigger (meaning idle time will be kept).

To see more about how it works, follow [this](https://clockify.me/help/track-time-and-expenses/idle-detection-reminders#automatic-start-stop) link.

## Notifications [\#](#notifications)

Notifications are located under the bell icon at the top\-right corner of the screen.

**Synchronization across platforms** 

Notifications in the extensions sync with those on the web app. If you’ve read notifications on the web app, they’re marked as read in the Clockify extension.

**Visual indicators for new notifications**

New notifications are marked with an orange dot and a count. Click the bell to read them.

## Reminders [\#](#reminders)

Simply check **Remind to track time** box in the Clockify browser extension settings, specify the interval (e.g. 10 minutes), and you will receive a notification from Clockify every 10 minutes, reminding you to use the timer.

You can also set **reminder start and end time**, and the reminder notification will only appear during this time period (e.g. from 08:00 to 16:00\).

And, you can also set **days for which you want to enable/disable reminders**. If you don’t want to receive reminders on Sundays for example, leave it unchecked.

To see more about how it works, follow [this link](https://clockify.me/help/track-time-and-expenses/idle-detection-reminders#reminders).

![](https://clockify.me/help/wp-content/uploads/2024/02/Screenshot-2024-02-08-at-14.39.18.png)
## Integrations [\#](#integrations)

Start Clockify timer in other web tools, like [Jira](https://clockify.me/jira-time-tracking), [Trello](https://clockify.me/trello-time-tracking), [Asana](https://clockify.me/asana-time-tracking), [Gitlab](https://clockify.me/gitlab-time-tracking), [Basecamp](https://clockify.me/basecamp-time-tracking), Slack, [Github](https://clockify.me/github-time-tracking), [Pumble](https://pumble.com/), [Google Calendar](https://clockify.me/google-calendar-time-tracking), Xero…

If you try to stop the timer from another website and you get an error, it means that project is a [required field](https://clockify.me/help/track-time-and-expenses/required-fields). You’ll either have to add the project manually from extension, enable the creation of projects/tasks/tags in the extension’s settings, or disable required field (if you have Timesheet enabled, project field is automatically required).

The extension can also pick up project name from another app if there’s a project in Clockify with the same name, and create and select projects, tasks, and tags based on the integration. [Here’s how](https://clockify.me/help/integrations/integrations#syncing-projects-and-tasks).

You can also make Clockify work with self\-hosted instances of software (like JIRA, Redmine, etc.), here’s [how](https://clockify.me/help/integrations/integrations#faq).

When you start a timer via a **Start timer** button, a popup will appear where you can add a project and edit other information for the time entry. You can disable this in the extension’s Settings \> **Show post\-start** **popup**.

![](https://clockify.me/help/wp-content/uploads/2024/03/browser_extension_start_timer-1-1024x441.png)

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
