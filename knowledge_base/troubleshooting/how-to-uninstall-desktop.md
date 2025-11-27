---
title: "How to uninstall desktop apps (Windows and MacOS)"
url: "https://clockify.me/help/troubleshooting/how-to-uninstall-desktop"
category: "troubleshooting"
slug: "how-to-uninstall-desktop"
---

# How to uninstall desktop apps (Windows and MacOS)

* [Uninstall Clockify on Windows](#uninstall-clockify-on-windows)
* [Uninstall Clockify on MacOS](#uninstall-clockify-on-macos)

# How to uninstall desktop apps (Windows and MacOS)

2 min read

In some cases, uninstalling and reinstalling the Clockify desktop app can help resolve unexpected issues, performance issues, or update problems. Here’s how to fully remove the app from your system based on your operating system.

## Uninstall Clockify on Windows [\#](#uninstall-clockify-on-windows)

 1\. Uninstall Clockify:   
  
Begin by uninstalling Clockify from your system through the standard uninstallation process (e.g., via “Add or remove programs” in Windows Settings).  
  
 2\. Delete Residual Files (User Data):

* Navigate to the following directory: C:\\Users\\\<Your Username\>\\AppData\\Local\\
* **Note:** The AppData folder is often hidden by default. If you cannot see it, open File Explorer, go to the “View” tab, and check the “Hidden items” box in the “Show/hide” section.
* Locate and delete any folders named “Clockify” within the Local folder.  
  
3\. Delete Residual Files (Program Data):
* Go to the root of your C: drive.
* Navigate to the ProgramData folder.
* **Note:** The ProgramData folder may also be hidden by default. If so, follow the same steps as above to reveal hidden items.
* Locate and delete any folders named “Clockify” within the ProgramData folder.  
  
4\. Reinstall Clockify:
* Visit the official Clockify website for Windows: https://clockify.me/windows\-time\-tracking
* Download the Clockify application.
* Install the application following the on\-screen instructions.

![](https://clockify.me/help/wp-content/uploads/2025/06/AD_4nXdCeevp0DQZL0EupUtrgLLAqk4ESHgz6M02SWsmyyqngaePneaN2OyQf1MgVaelnZBLSY7wZUt7o22r-d1-JIDAT0kBIrORxYp-SsRWCLjWG3zNGjS4AjEHSoYP4n-IDk94_JyG.png)

## Uninstall Clockify on MacOS [\#](#uninstall-clockify-on-macos)

Before attempting a clean install of the app, you can reset it without deleting the files:

1. Open the Clockify app and bring it to the front
2. Click on the “Help” option in the menu bar
3. Select “Reset Clockify”

This will reset your app completely and might help resolve issues you’re facing.

To manually reinstall the app and delete files:

1. Log out of Clockify.
2. Open Terminal and execute the command: defaults delete coing.ClockifyDesktop
3. In Terminal, execute the command: tccutil reset All coing.ClockifyDesktop
4. Open Finder, navigate to your home folder, then to the Library (this is a hidden folder), then Application Support, then coing.ClockifyDesktop. Delete the files named default.realm and default.realm.lock.
5. Delete the ClockifyDesktop application from your computer.
6. Download the new version from our website here

The clean reinstall will delete all of your Auto Tracker data. If you wish to save it, you can click on the “Add as a time entry” option on the right side of the Auto Tracker sessions to save them to your Clockify reports. 

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
