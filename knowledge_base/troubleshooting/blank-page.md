---
title: "Blank page or \u2018something went wrong\u2019 message"
url: "https://clockify.me/help/troubleshooting/blank-page"
category: "troubleshooting"
slug: "blank-page"
---

# Blank page or ‘something went wrong’ message

* [Check your firewall and VPN settings](#check-your-firewall-and-vpn-settings)
* [Your network connection is not stable](#your-network-connection-is-not-stable)
* [Whitelist Clockify domains and IP addresses](#whitelist-clockify-domains-and-ip-addresses)

# Blank page or ‘something went wrong’ message

3 min read

If you are experiencing a blank page or you’re getting the message ‘something went wrong’ on the login screen, this issue is often related to your network connection.

![](https://clockify.me/help/wp-content/uploads/2025/06/Screenshot-2025-06-25-at-11.55.03-1024x533.png)
## Check your firewall and VPN settings [\#](#check-your-firewall-and-vpn-settings)

Your firewall or VPN might be blocking access to our site, and therefore, it’s advisable to check whether the Clockify app is allowed access.

## Your network connection is not stable [\#](#your-network-connection-is-not-stable)

Try connecting to a different network, such as a mobile hotspot or a different WiFi connection, to see whether the issue persists. 

**Browser issues**

Make sure that your browser is up to date and that you’re running the latest version. Additionally, clearing the cache and cookies might also help resolve the issue. 

Here’s how to clear the cache on different browsers:

* **Google Chrome**

1. Click the three\-dot menu in the top\-right corner
2. Go to Settings
3. Click Privacy and security on the left sidebar
4. Select Delete browser data
5. Select “all time” under the time range
6. Delete

* **Safari**

1. Launch the Safari browser on your Mac.
2. Select Safari → Preferences
3. Click the Privacy tab and select **Manage Website Data**
4. Select a website that is listed, then click Remove. To remove all website data from Safari, click Remove All.

* **Firefox**

1. Click the menu button to open the menu panel.
2. Click *History* → select **Clear Recent History**
3. Next to Time range to clear, choose Everything from the drop\-down menu, select Cache in the items list, make sure other items you want to keep are not selected, and then click the OK button.

* **Microsoft Edge**

1. In Edge, select More (three horizontal dots in the upper right corner).
2. Select Settings → Open the Settings on the left\-side menu → Privacy, search, and services.
3. Select **Choose what to clear** under Clear browsing data.
4. Under Time range, choose a time range “All time”.
5. Select Cookies and other site data, and then select Clear now.

To ensure that all data is deleted and that your browser is running properly, make sure to select ‘all time’ when clearing the cache. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe6Eny6MQnw_DnqC64nga43ZRhhSw0K3ToZ11qIBC5pRor_nqwvTjpQypBlnyUzWZb27AMqExtUsDD2s38-o65O5p0M0TzQRGO42NT_LtJ_i0HeMVnYyShBhP2Fje7rHa-PVOqw?key=XZmssafXgdhlV2XB9mRUkEGN)
## Whitelist Clockify domains and IP addresses [\#](#whitelist-clockify-domains-and-ip-addresses)

If you’re using a restricted network (e.g., corporate or secure office network), you may need to whitelist specific Clockify domains to allow the login page to load properly.

Make sure the following domains and IPs are allowed in your firewall or network settings:

* img.clockify.me
* api.clockify.me
* global.api.clockify.me
* reports.api.clockify.me
* stomp.clockify.me
* IP address: 198\.2\.128\.220

**How to whitelist**

1. Identify where to manage network access (firewall, proxy, security software, etc.)
2. Add the domains and IP addresses listed above to your allowed list
3. Save the changes and refresh the login page

Still having issues? The Clockify Support Team will be happy to look into it and assist you further. Please contact us at [support@clockify.me](mailto:support@clockify.me) and provide us with the following information:

1. Browser and browser version
2. Whether you’re using a VPN or a Firewall

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
