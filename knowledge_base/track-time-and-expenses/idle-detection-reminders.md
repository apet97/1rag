---
title: "Pomodoro, idle detection, reminders"
url: "https://clockify.me/help/track-time-and-expenses/idle-detection-reminders"
category: "track-time-and-expenses"
slug: "idle-detection-reminders"
---

# Pomodoro, idle detection, reminders

* [Can't see notifications?](#cant-see-notifications)
* [Idle detection](#idle-detection)
* [Pomodoro timer](#pomodoro-timer)
* [Automatic start and stop](#automatic-start-and-stop)
* [Reminders](#reminders)

# Pomodoro, idle detection, reminders

5 min read

Track time with greater accuracy so you can have a more accurate insight into how you really spend time with the help of idle detection, Pomodoro, automatic clock\-in/clock\-out, and reminders. You can enable them in: Preferences ([Mac desktop app](https://clockify.me/mac-time-tracking) and [Windows desktop app](https://clockify.me/windows-time-tracking)) / Settings ([Chrome/Firefox extension](https://clockify.me/chrome-time-tracking)).

## Can’t see notifications? [\#](#cant-see-notifications)

If you can’t see notifications for idle time, reminders, or Pomodoro, you’ll have to allow the browser to send notifications.

To enable notifications on Windows:

1. Go to **Notifications \& actions**
2. Turn ON the **Get notifications from apps and senders**
3. Make sure your browser (Chrome or Firefox) in the app list is also set to **ON**
4. [Turn on notifications](https://support.google.com/chrome/answer/3220216?co=GENIE.Platform%3DDesktop&hl=en) from Clockify in Chrome

![](https://clockify.me/help/wp-content/uploads/2019/06/notifications-see.jpg)
## Idle detection [\#](#idle-detection)

Away from the computer but forgot to stop the timer? Clockify can detect if you accidentally leave a timer running when you leave your desk, and let you remove the idle time so your timesheets stay accurate.

![](https://clockify.me/help/wp-content/uploads/2024/07/idle_detection_new.png)
#### How idle detection works [\#](#how-idle-detection-works)

If there’s no mouse movement or keyboard strokes for X minutes, the timer will enter into idle mode. It will continue running, but it will treat those X minutes (and the time after that) as idle. When you become active, a notification will pop up, asking what you want to do with the idle time.

You can choose to:

* **Discard idle time** – The timer will be stopped and the detected idle time will be removed from its total.
* **Discard and continue** – The current timer will be stopped, the detected idle time will be removed from its total, and a new timer will immediately start for the same activity.
* **Keep idle time** – The timer will keep running as it is. In order to keep idle time in the Chrome extension, simply close or dismiss the notification.

**What will be discarded**:  If you’ve been active for 1h, inactive for 30m, and idle time is triggered after 15m, Clockify will discard 30m (time needed for the idle time to trigger and the time after that), leaving you with a 1h time entry.

If you’ve been away from the computer but stopped the timer via another device in the meantime, idle detection popup won’t appear.

Note: idle detection can’t differentiate accidental mouse movements from normal activity. For example, if someone accidentally bumps into your desk while you’re away, idle detection will register the accidental movement as a normal activity.

**How to set up idle detection on:**

* [MacOS desktop app](https://clockify.me/help/apps/mac-desktop-app#detect-idle-time) (Note: if you’ve downloaded Clockify for Mac from the App Store, idle detection is not available. You can [download the version with idle detection here](https://clockify.me/mac-time-tracking).)
* [Windows desktop app](https://clockify.me/help/apps/windows-desktop-app#idle-detection)
* [Chrome/Firefox extension](https://clockify.me/help/apps/chrome-extension#idle-detection)

## Pomodoro timer [\#](#pomodoro-timer)

If you’re using a [browser extension](https://clockify.me/help/apps/chrome-extension#pomodoro), or desktop app for [Windows](https://clockify.me/help/apps/windows-desktop-app) or [Mac](https://clockify.me/help/apps/mac-desktop-app), you can set up notifications to let you know when it’s time to take a short break with the Pomodoro timer.

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-20-at-14.14.36.png)
Once you’re done with your break you can select to continue the last entry or start a new one.

There is also an option to set a **Long Break** where you can simply choose after how many short breaks you take a longer break to help recover from intense burst sessions.

For Long Break to work you would need to start/stop the timer from the notification pop up. If you stop the timer manually, it will reset the count sessions and start over.

If you don’t want to bother starting/stopping the timer, you can choose to do this **automatically** when the Pomodoro period or break ends.

You can also enable **Focus mode** in Settings. Focus mode hides your time log and just shows you a visual representation of time left.

![](https://clockify.me/help/wp-content/uploads/2024/03/Screenshot-2024-03-29-at-11.53.18-622x1024.png)
You can also find a slightly different version of Pomodoro on our [Mac desktop app](https://clockify.me/help/apps/mac-desktop-app#pomodoro-timer).

User interface displayed in this video may not correspond to the latest version of the app.

## Automatic start and stop [\#](#automatic-start-and-stop)

If you’re using the [browser extension](https://clockify.me/help/apps/chrome-extension#start-stop-automatically), Clockify can automatically start/stop the timer when the browser is opened/closed.

If you forget to stop the timer at the end of the workday, you can enable automatic stop and when the computer is locked/goes to sleep/shut down, the timer will also stop (currently available only for [Mac](https://clockify.me/help/apps/mac-desktop-app#auto-stop-timer)).

In case you have both idle detection and auto\-stop enabled, if the timer is stopped automatically, idle detection will not trigger (meaning idle time will be kept).

![auto-stop timer](https://clockify.me/help/wp-content/uploads/2019/06/auto-stop.png)

You can also automatically start/stop the timer at a certain time of the day using [Zapier](https://clockify.me/zapier-time-tracking) (e.g. automatically start the timer at 9 am and end any currently running timer at 5 pm).

## Reminders [\#](#reminders)

If you keep forgetting to start a timer, Clockify can send you reminders to do that.

Choose your working days, working hours, and after how much time you wish to be reminded.

For example, if it’s Monday – Friday between 9 am – 5 pm and you haven’t started the timer for 30 minutes, you’ll get the notification. You can start a new timer from there, or continue the latest one.

In addition to the time tracking reminder notifications, Clockify can also send your team [daily and weekly reminders](https://clockify.me/help/administration/targets-reminders) via email (e.g. if someone doesn’t log their target of 40h/week).

Weekly reminders will be sent on the day you set as the first day of the week in the [Profile settings](https://clockify.me/help/administration/profile-settings#preferences).

E.g. *If Monday is set as the first day in a weekly reminder and my first working day is Wednesday, a reminder will start counting from Wednesday (my first day).*

Reminder always picks up user’s information. If possible, check with users to set the same day, time and timezone.

**How to set up reminders on:**

* [MacOS desktop app](https://clockify.me/help/apps/mac-desktop-app#reminders)
* [Windows desktop app](https://clockify.me/help/apps/windows-desktop-app#reminders)
* [Chrome/Firefox extension](https://clockify.me/help/apps/chrome-extension#reminders)

![reminders screenshot](https://clockify.me/help/wp-content/uploads/2019/06/reminders-screnshot.png)

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
