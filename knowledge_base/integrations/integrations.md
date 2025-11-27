---
title: "Overview of integrations"
url: "https://clockify.me/help/integrations/integrations"
category: "integrations"
slug: "integrations"
---

# Overview of integrations

* [Syncing projects and tasks](#syncing-projects-and-tasks)
* [Custom domains](#custom-domains)
* [Disable integrations](#disable-integrations)
* [List of Clockify integrations](#list-of-clockify-integrations)
* [FAQ](#faq)

# Overview of integrations

5 min read

Start Clockify timer from within other web tools, like [JIRA](https://clockify.me/jira-time-tracking), [Trello](https://clockify.me/trello-time-tracking), [Asana](https://clockify.me/asana-time-tracking), [Todoist](https://clockify.me/todoist-time-tracking), and others (see [integrations page](https://clockify.me/integrations) for the full list).

User interface displayed in this video may not correspond to the latest version of the app.

Simply install the [Chrome extension](https://chrome.google.com/webstore/detail/pmjeegjhjdlccodhacdgbgfagbpmccpe/) or [Firefox extension](https://addons.mozilla.org/en-US/firefox/addon/clockify-time-tracker/), and a timer button will appear in your favorite web app’s tasks, to\-dos, issues, leads, events, etc.

The [browser extension is open\-sourced](https://github.com/clockify/browser-extension), so feel free to create new integrations or improve existing ones.

To use JIRA integration, you need to install the [Clockify plugin for JIRA](https://marketplace.atlassian.com/apps/1222624/clockify-time-tracking-timesheets?tab=overview&hosting=cloud). Check out [this](https://clockify.me/help/integrations/tracking-integrations-integrations/jira-integration) Help Center page for detailed instructions.

## Syncing projects and tasks [\#](#syncing-projects-and-tasks)

The extension can also pick up project name from another app if there’s a project in Clockify with the same name (e.g. you have a **Project X** in both Clockify and Asana/JIRA/Trello/Todoist).

Clockify extension can also create and select projects, tasks, and tags based on the integration:

* If there’s a project or task with the same name in Clockify, it will be selected
* If there’s no project or task and you have the permission to create it (based on workspace settings), a new one will be automatically created and selected

To enable creation of projects/tasks/tags, you first need to enable it in the extension’s Settings.

Each integration is different. For example, task and project can be created from Asana, Gitlab will also pick up tags, but Gmail won’t do anything except pick up description.

If you need support for this in other integrations, feel free to [contribute code to the extension on Github](https://github.com/clockify/browser-extension/).

## Custom domains [\#](#custom-domains)

If you use a self\-hosted tool that you use on a custom URL (e.g. you use YouTrack on mydomain.com), you’ll need to add your domain and connect it to the corresponding tool:

1. Open extension
2. Open settings (hamburger menu in the upper left corner)
3. Click **Integrations**
4. Scroll down and under **Custom domains** enter your domain (e.g. mydomain.com)
5. Select the tool that’s on that domain
6. Click **Add**

## Disable integrations [\#](#disable-integrations)

If you don’t want the button to appear in certain web apps, you can disable it in **Integrations**. 

* Open the extension
* Click on the menu icon in the upper right corner
* Click on the **Integrations** button and you’ll jump to the integrations list
* Uncheck the apps in which you don’t want to see the **Start timer** button

If you use a self\-hosted / on\-premise version of some app (like JIRA or Gitlab), at the bottom of the **Integrations** page you can specify the domain where you have the app installed.

## List of Clockify integrations [\#](#list-of-clockify-integrations)

Complete list of all the integrations available in Clockify based on their type:

| **Project management \& collaboration**Airtable, Asana, Axosoft, Basecamp, Breeze, ClickUp, ConnectoHub, Fibery, Freedcamp, GetFlow, Group\&Work, Jira, Linear, MantisHub, Manuscript, Microsoft Planner, Monday, Notion, Pipefy, Pivotal Tracker, Placker, Podio, Redbooth, Redmine, TeamWave, Teamwork, Trello, Unfuddle, Way We Do, WeKan, Wrike, YouTrack, Zenkit. |
| --- |
| **Task management**Google Calendar, Infinity, MeisterTask, MyFocusSpace, Nozbe, Outlook, Plaky, Pyrus, TickTick, Todoist, Toodledo. |
| **Communication \& support**Cerb, Dixa, Freshdesk, Front, Google Mail, Helprace, Help Scout, Husky Marketing Planner, LiveAgent, Nela, Pixie, Pumble, Slack, Zammad, Zendesk, Zoho Connect. |
| **Development \& version control**Azure, Bitbucket, Gitea, GitHub, GitLab, Phabricator, Sentry, Visual Studio. |
| **CRM \& sales management**CapsuleCRM, HubSpot, Pipedrive, Salesforce Lightning, Zoho Desk. |
| **Document \& note\-taking**Coda, Evernote, Google Docs / Sheets, Google Keep, Microsoft Planner. |
| **Time tracking and source management**Clockify, Freshservice, LiquidPlanner, ManageEngine, Microsoft To Do, Plutio, Scoro. |
| **Agile \& Kanban**Kanbanize, Rally, Shortcut, Taiga. |
| **Design \& prototyping**Figma, Miro. |
| **Workflow automation**Zapier. |
| **Other**Ambra, Connecthub, Crowdin, Freshrelease, Hillia, JetBrains Space, Nifty, OpenProject, osTicker, Sprint. |

## FAQ [\#](#faq)

### I get an error about missing project when I try to stop the timer [\#](#i-get-an-error-about-missing-project-when-i-try-to-stop-the-timer)

If you have Timesheet enabled, project is automatically a [required field](https://clockify.me/help/track-time-and-expenses/required-fields). To stop the timer, you’ll have to open your timer and select a project.

Tip: You can set a default project, so each time you start a timer, project is selected automatically (you can enable it by opening the extension and going to Settings).

### I’m using an on\-premise version of some app [\#](#im-using-an-on-premise-version-of-some-app)

No problem. In the extension options, select **Integrations**, scroll down to the bottom, select the tool you’re using (e.g. Gitlab), and enter your custom domain.

### Help, I don’t see the button [\#](#help-i-dont-see-the-button)

If you don’t see the button, first make sure you’re logged in to the extension. If that doesn’t help, restart the browser. Also, make sure the integration is enabled in URL Permissions (when you open the extension, click on options icon in the upper right corner).

If you’re still experiencing the problem, try these troubleshooting steps:

1. Remove the extension from your browser
2. Clear cache and cookies (date range: all time)
3. Download the latest version of the extension and pin it to the browser
4. Log in to the extension and enable integration with the app
5. Check if the button appears in the app

If none of these worked, send us an email and we’ll look into the problem. Sometimes integrations break due to updates in other apps. If you don’t want to wait for us to fix the integration, feel free to help us out by [contributing to our codebase](https://github.com/clockify/browser-extension).

### How can I get my favorite tool added? [\#](#how-can-i-get-my-favorite-tool-added)

The [extension is open source](https://github.com/clockify/browser-extension) so anyone can contribute. If you’ve developed an integration, be sure to let us know so we can feature it on our [Integrations page](https://clockify.me/integrations).  
Adding your tool requires basic web programming skills (HTML, Javascript, Git) and can be done in a couple of hours.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
