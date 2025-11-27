---
title: "Single sign-on (SSO)"
url: "https://clockify.me/help/getting-started/single-sign-on-sso"
category: "getting-started"
slug: "single-sign-on-sso"
---

# Single sign-on (SSO)

* [Setting up custom subdomain](#setting-up-custom-subdomain)
* [Inviting new users](#inviting-new-users)
* [Configuring SSO](#configuring-sso)
* [SAML 2\.0 with Okta](#saml-2-0-with-okta)
* [SAML 2\.0 with OneLogin](#saml-2-0-with-onelogin)
* [SAML 2\.0 with Google](#saml-2-0-with-google)
* [SAML 2\.0 with Rippling](#saml-2-0-with-rippling)
* [SAML 2\.0 with JumpCloud](#saml-2-0-with-jumpcloud)
* [OAuth 2\.0 (OIDC) with Google](#oauth-2-0-oidc-with-google)
* [OAuth 2\.0 (OIDC) with Microsoft Azure](#oauth-2-0-oidc-with-microsoft-azure)
* [SAML 2\.0 with Microsoft Azure](#saml-2-0-with-microsoft-azure)
* [OAuth 2\.0 (OIDC) with Okta](#oauth-2-0-oidc-with-okta)

# Single sign\-on (SSO)

22 min read

Single sign\-on feature (hereafter SSO) provides security at scale by controlling access and managing login credentials while using your company’s IdP via both SAML 2\.0 and OAuth 2\.0 (OIDC) (Office 365, Okta, Azure, Active Directory, Google, OneLogin…).

This is a paid feature, which you can enable by [upgrading](https://clockify.me/pricing) your workspace to **Enterprise plan**.

In order to use SSO, you first need to move your workspace to subdomain. Once you do that, you can configure SSO settings and disable other login methods.

## Setting up custom subdomain [\#](#setting-up-custom-subdomain)

### Moving to subdomain [\#](#moving-to-subdomain)

Before you can configure and start using SSO for authorization, you need to move your Clockify app domain to a **custom subdomain**.

When you upgrade your Clockify subscription to **Enterprise plan**, you will get **Authentication** tab in the **Workspace** **settings**. There, you can enter the subdomain you’d like to use and move your workspace there.

To set up subdomain:

1. Navigate to the **Authentication** tab in the **[Workspace settings](https://clockify.me/help/track-time-and-expenses/workspaces#workspace-settings)**
2. Enter your custom subdomain in the provided field
3. Click **Create subdomain** and **Create** to confirm the action

![](https://clockify.me/help/wp-content/uploads/2022/11/Screenshot-2024-12-23-at-10.47.02-1024x381.png)
After you created your subdomain and moved your workspace there, Google login will no longer work for you and your users. 

If you’d, however, like to use Google login, you need to set it up manually by configuring **OAuth 2\.0 (OIDC)** for **SSO**. 

For more information, check out the [OAuth 2\.0 (OIDC) with Google](https://clockify.me/help/getting-started/single-sign-on-sso#oauth-2-0-oidc-with-google) section below.

### Accessing Clockify from subdomain [\#](#accessing-clockify-from-subdomain)

After you create your subdomain, you’ll automatically be logged out of any apps you were logged in with your Clockify account. You’ll have access to them only through the subdomain you created (e.g. https://yourcompanysubdomain.clockify.me/login).

### Workspaces on subdomain [\#](#workspaces-on-subdomain)

Subdomain is tied to only one workspace. Users on subdomain can’t have multiple workspaces: there is no workspace switcher, no workspaces in the sidebar, and no access to subdomain workspace from the main domain.

To access multiple workspaces, log in to the main Clockify domain. 

### Changing subdomain [\#](#changing-subdomain)

You can change subdomain URL at any time. 

Once you change your URL, your Users will be logged out and will have to use the workspace through the new URL.

If you cancel the subscription to the Enterprise plan: 

* you’ll move back to the main domain when the subscription expires
* your subdomain will become available for others to use
* your users will have to log in with their email

### API keys on subdomain [\#](#api-keys-on-subdomain)

For security reasons, each user on subdomain gets a separate API key that works only for that workspace – meaning, no one can access your data on your subdomain unless they have the right authorization.

If, for example, there is a user with two separate Enterprise workspaces, workspace owners can’t see, or access data from each others accounts.

## Inviting new users [\#](#inviting-new-users)

Once you’re in the subdomain workspace, you can invite users one by one **using email** (like before), or let anyone join without you having to manually invite them.

To let anyone join, check the **Users can join without an invite** checkbox.

If you use SSO and someone without an account tries to log in, the account will be automatically created for them and they’ll log in.

If you allow **Log in with email**, people will be able to create an account and automatically join your workspace.

## Configuring SSO [\#](#configuring-sso)

If you’d like to use SSO via your mobile devices (android or iOS) all the SSO configurations supported by Clockify should contain **\[yourcompany subdomain].clockify.me** links. For example, in the **Redirect URL** section add **https://yourcompanysubdomain.clockify.me/login/android/oauth2** or **https://yourcompanysubdomain.clockify.me/login/ios/oauth2** link.

Clockify supports all major SSO identity providers:

* SAML 2\.0 ([Google](https://clockify.me/help/getting-started/single-sign-on-sso#saml-2-0-with-google), [OneLogin](https://clockify.me/help/getting-started/single-sign-on-sso#saml-2-0-with-onelogin), [Okta](https://clockify.me/help/getting-started/single-sign-on-sso#saml-2-0-with-okta), [Azure](https://clockify.me/help/getting-started/single-sign-on-sso#saml-2-0-with-microsoft-azure), [Rippling](https://clockify.me/help/getting-started/single-sign-on-sso#saml-2-0-with-rippling), [JumpCloud](https://clockify.me/help/getting-started/single-sign-on-sso#saml-2-0-with-jumpcloud))
* OAuth 2\.0 (OIDC) ([Google](https://clockify.me/help/getting-started/single-sign-on-sso#oauth-2-0-oidc-with-google), [Azure](https://clockify.me/help/getting-started/single-sign-on-sso#oauth-2-0-oidc-with-microsoft-azure), [Okta](https://clockify.me/help/getting-started/single-sign-on-sso#oauth-2-0-oidc-with-okta))

Only workspace owner can see **Authorization** tab, manage subdomain, configure SSO, and turn SSO on/off.

If you wish to force everyone to log in with SSO, simply turn off the **Log in with email** option. Once this change has been saved, your workspace members accounts will be required to use SSO to log in.

Data in the SSO configuration can always be edited or deleted. If deleted, your users will have to switch back to logging in by using email.

Owner can always log in using the original credentials at **https://mysubdomain.clockify.me/login\-owner**

To add **Default Relay State**, use the parameters below.

Make sure to use curly brackets and straight quotes instead of the curly ones, otherwise it won’t work.

Example of Default Relay State:

```
{"location":"https://yourcompanysubdomain.clockify.me", "organizationName":"yourcompanysubdomain"}
```

## SAML 2\.0 with Okta [\#](#saml-2-0-with-okta)

User interface displayed in this video may not correspond to the latest version of the app.

show more

### Step 1: Create subdomain in Clockify [\#](#step-1-create-subdomain-in-clockify)

For more information on this, check out [Setting up custom subdomain](https://clockify.me/help/getting-started/single-sign-on-sso#setting-up-custom-subdomain) section.

### Step 2: Create application in Okta [\#](#step-2-create-application-in-okta)

1. Navigate to **Applications** in the sidebar
2. Click **Create App Integration** button
3. Choose **SAML 2\.0** in modal
4. Click **Next**

#### Create SAML 2\.0 integration [\#](#create-saml-2-0-integration)

In **General Settings** form, enter the following information and click **Next**

* **App name**: e.g. Clockify
* **Logo**: e.g. upload Clockify logo

In **Configure SAML** form, enter the following information:

* **Single sign on URL** (or ACS): Specific URL that SAML assertions from Okta should be sent to (e.g. https://global.api.clockify.me/auth/saml2\)
* **Audience URI** (Entity ID in your app): Unique identifier of your custom application; same as **Entity Id** in SAML authentication field (e.g. https://yourcompanysubdomain.clockify.me)
* **Default Relay State**: IdP\-initiated authentication so that users can log in to Clockify straight from the Okta dashboard

Example of **Default Relay State**:

```
{"location":"https://yourcompanysubdomain.clockify.me", "organizationName":"yourcompanysubdomain"}
```

Make sure you put straight quotes instead of the curly ones, or it won’t work.

Leave everything else as is and click **Next**.

In **Feedback** check **I’m an Okta customer adding an internal app** and click **Finish**.

You should get the screen that looks something like this:

![](https://clockify.me/help/wp-content/uploads/2022/04/image_17.png)
As the final step in this section, click **View Setup Instructions** button seen in the screenshot above.

In **How to Configure SAML 2\.0 for Clockify Application**, you’ll get the list of data you need in order to configure your Clockify application.

### Step 3: Add SSO configuration in Clockify [\#](#step-3-add-sso-configuration-in-clockify)

Now, in Clockify, in the **Authentication** screen:

1. Click **Add SSO Configuration** at the bottom of the screen
2. Choose **SAML2** as authentication type
3. Choose **Okta** as **IdP Template**

**SAML2 authentication** form appears:

![](https://clockify.me/help/wp-content/uploads/2024/06/sso_okta_initial_screen.png)
Enter the following:

* **Entity Id (Audience URI in Okta):** e.g. https://yourcompanysubdomain.clockify.me
* **Metadata Url**:
	* Navigate back to Okta
	* Copy the **Identity Provider metadata** link from the **Settings** section in Okta
	* **Save it as an .xml file and upload it to Clockify**
* **SAML SSO URL**: Copy/paste **Identity Provider Single Sign\-On URL** from Okta’s **How to configure SAML 2\.0 for Clockify Application**

For example:

```
https://okta.ops.clockify.me/app/dev05335506_clockifytempsaml2_1/exk4erumfseHaalgs5d7/sso/saml
```

* **Advanced**: Copy/paste **X.509 Certificate** from Okta

Finally, your screen in Clockify should look something like this:

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-12-at-16.14.31-672x1024.png)
and

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-12-at-16.41.42.png)
After entering all required data, you can choose to verify your configuration by clicking the **Test configuration** button. This action ensures the accuracy of the provided information. If everything is correct, the **Test configuration** button will be replaced with a **Finish configuration** button.

Click **Finish configuration** to complete the process and enable **Log in with SAML2**. Optionally, disable **Log in with email and password**.

### Step 4: Assign application in Okta [\#](#step-4-assign-application-in-okta)

In Okta:

1. Navigate to **Applications**
2. Choose **Clockify**
3. In **Assignments** tab click **Assign**
4. Choose **Assign to People/Groups** depending on who from your Okta account you’d like to be able to access Clockify

And that’s it! Now you, and your workspace users are able to log in to your workspace with SAML2\.

![](https://clockify.me/help/wp-content/uploads/2022/04/image_6.png)
show less

## SAML 2\.0 with OneLogin [\#](#saml-2-0-with-onelogin)

User interface displayed in this video may not correspond to the latest version of the app.

show more

### Step 1: Create subdomain in Clockify [\#](#step-1-create-subdomain-in-clockify)

For more information on this, check out [Setting up custom subdomain](https://clockify.me/help/getting-started/single-sign-on-sso#setting-up-custom-subdomain) section.

### Step 2: Create application in OneLogin [\#](#step-2-create-application-in-onelogin)

1. Navigate to **Applications**
2. Click **Add App**
3. Search and choose **SAML Custom Connector** (Advanced)
4. Info:
	* **Display Name**: Clockify
	* Logo: e.g. upload Clockify logo

Click **Save** and fill out the **Configuration**:

* **Audience**: Clockify
* **Recipient**: https://global.api.clockify.me/auth/saml2
* **ACS (Consumer) URL Validator**\*: ^https:\\/\\/global.api.clockify\\.me\\/auth\\/saml2\\/$
* **ACS (Consumer) URL**\*: https://global.api.clockify.me/auth/saml2
* **Login URL**: https://yourcompanysubdomain.clockify.me/
* **SAML initiator**: Service Provider
* Click **Save** to complete the process

### Step 3: Add SSO configuration in Clockify [\#](#step-3-add-sso-configuration-in-clockify)

1. Click **Add SSO Configuration**
2. Choose **SAML2** as authentication type
3. Choose **OneLogin** as **IdP Template** and fill out the following fields
	* **Audience** (**Entity Id**): Clockify
	* **Metadata Url**: Go to OneLogin \> SSO and copy Issuer URL then paste it in Metadata Url in Clockify
	* **Login Url**: Copy/paste SAML 2\.0 Endpoint (HTTP) from SSO section in OneLogin

In **Advanced** section, enter:

* **Certificate**: Copy/paste the **X.509 Certificate** from View Details, SSO in OneLogin

### Step 4: Assign application in OneLogin [\#](#step-4-assign-application-in-onelogin)

In OneLogin:

1. Navigate to **Users** (this is where you choose which users from your OneLogin account will be able to access Clockify)
2. Click on the specific User
3. In **Applications**, click the **\+** sign to add an app
4. Choose **Clockify**
5. Click **Continue** and **Save**

In Clockify, after entering all required data, you can choose to verify your configuration by clicking the **Test configuration** button. This action ensures the accuracy of the provided information. If everything is correct, the **Test configuration** button will be replaced with a **Finish configuration** button.

Click **Finish configuration** to complete the process and enable **Log in with SAML 2\.0**. Optionally, you can disable **Log in with email and password**.

And that’s it! Now you, and your workspace users are able to log in to your workspace with SAML 2\.0\.

show less

## SAML 2\.0 with Google [\#](#saml-2-0-with-google)

show more

### Step 1: Create subdomain in Clockify

For more information, check out [Setting up custom subdomain](https://clockify.me/help/getting-started/single-sign-on-sso#setting-up-custom-subdomain) section.

Clockify: 

1. Navigate to the **Authentication** tab
2. Choose **Add SSO Configuration**
3. Choose **SAML2** as identity provider In **Authentication type** window
4. Click **Next**
5. Choose **Google** as **IdP template**

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-13-at-09.22.56.png)
### Step 2: Create application in Google  [\#](#step-2-create-application-in-google)

Google:

1. Create Google account and go to the **Admin** page
2. Choose **Add custom SAML** app in **Add app**  
![](https://lh7-us.googleusercontent.com/b4om5Xv5tczNS2oGUhBSVrVhwE7kUE7y31kEZACuxkegYDWcIMinrjkyD0idTsuRyXrMlcnTr3Ft1JFvpP6SKthN0BMcsnX3mF5JwvSZ2tSQso3MxGMQM0QTpVmGuQLdvnMCR2Ur8lDUYntRGUMLdhM)
3. Insert the following  
– **App name**: e.g. <https://yourcompanysubdomain.clockify.me/>– **Description**: e.g. Clockify SAML2 demo app  
– **App icon**: optionally add icon  
![](https://lh7-us.googleusercontent.com/1kD5Pg67QD_nxFpxVRAnjgOb8ZUl3QeGGGQm--_LLi7rtgGj5Azz2HY80nbjzOVqKy47P5RImPMC6Fggab5X46OqO4n0WUiqWH40K_2yQYqPY5oMiJUAW8cY8qbKDU3O20DBHiXO5oeWbI8ImS5xbEc)
4. Click **Continue**
5. You’ll proceed to the **Google Identity Provider details** screen  
Google side:  
![](https://lh7-us.googleusercontent.com/yw8oM_741-dq3O2mzU4Ctsx_miJVRapDewYVQxQER0l6bY46YpbW01I6GbTkRIq1fyujuHdRvy7TYI38RBJO_cBzUjm0Y6-Lo3fV639SiHkjR29U4EfEdFd_tob6mclQ9XDJZIhT_iJmkRR7DA80OKE)
6. Download **IdP metadata URL** and upload it to **Clockify/IdP Metadata URL** field
7. Copy **SSO URL** and paste it to **Login URL** field in Clockify  
Clockify side:  
![](https://clockify.me/help/wp-content/uploads/2022/11/Screenshot-2024-06-13-at-09.26.30.png)
8. Click **Continue**  
Google side:
9. You’ll proceed to **Service provider details**
10. Insert the following:  
– ACS URL: Copy/paste **Reply URL** from Clockify, e.g. https://global.api.clockify.me/auth/saml2  
– Entity ID: Unique identifier of your custom application, e.g. Clockify  
– Start URL: Copy/paste **Default Relay State** from Clockify, e.g.

{“location”:”https://yourcompanysubdomain.clockify.me”,”organizationName”:”yourcompanysubdomain”}  
  
  
![](https://lh7-us.googleusercontent.com/LK7SMMSCoo7XKMVL5Ibxndpxi19UPtm9X3bR9H4D93SVaOKvCMQ2F3alutDy9RLIwfQNMvfAM-OgLutRyLbQkczZiwQOiS79WvszLiI8WhXg92i4P1OquUkD_F7CvWJ9WP4XIxAgmX7lQFZEX8EeUbo)

11. Click **Continue**
12. You’ll proceed to the **Attribute mapping** screen  
![](https://lh7-us.googleusercontent.com/9L__Wp9Wnt0HR_Mnw4E_Whoqb72v8lFikCet_Uoh7U-V7JjDC1Wa-emmtotb9zBYiK9HQu3YzDP3PsWCn-OLZokPC3jZIuJyWy87wMqL8rBakfEoHFIrIzdVx4xMWpJQTfjbnCEvlRR9Hn2VoVsHfHM)
13. Click **Finish** to complete the process

After entering all required data, on the Clockify side, you can choose to verify your configuration by clicking the **Test configuration** button. This action ensures the accuracy of the provided information. If everything is correct, the **Test configuration** button will be replaced with a **Finish configuration** button.

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-13-at-11.17.10.png)
Now that you’ve completed all the steps and created the app, open the app’s settings and in **Service status** enable the app for everyone.  

![](https://lh7-us.googleusercontent.com/8l96nQWaaDJOZDOyZCcEbF0TKAF4cGern4ePDpe_aiEjUcbngFlQJlUhv3vC8Mj_w3GZuNsBE3ayqksq2N6idy2qukwUvQtai7oMTPLitATRAHibbOU7P4C_nkUaZpfR1qZawnhAW3A0cvhHH6KGJ5s)
The app you created will appear in the Google workspace for all the users of that workspace.   

show less

## SAML 2\.0 with Rippling [\#](#saml-2-0-with-rippling)

show more

### Step 1: Create subdomain in Clockify [\#](#step-1-create-subdomain-in-clockify)

For more information on this, check out the [Setting up custom subdomain](https://clockify.me/help/getting-started/single-sign-on-sso#setting-up-custom-subdomain) section.

### Step 2: Create application in Rippling [\#](#step-2-create-application-in-rippling)

1. Log in to Rippling as Administrator
2. Select **IT management**
3. Select **Custom app**
4. Give app a descriptive name, select category and upload a logo
5. Check **Single Sign\-on (SAML)**
6. Click **Continue**
7. Confirm that you are Application Admin

New page with SSO instructions opens and you can proceed with the next step. The page contains **SSO Setup instructions** which include the IdP Metadata XML file.

Download IDP Metadata from Rippling.

### Step 3: Add SSO configuration in Clockify [\#](#step-3-add-sso-configuration-in-clockify)

In the **Authentication** tab in which you created your subdomain:

1. Click **Add SSO Configuration**
2. Choose **SAML2** as authentication type and click **Next**
3. Choose **Rippling** as **IdP Template**

In **SAML2 authentication** form that appears enter the following information:

* **Entity Id** (**Service Provider Entity ID** in Rippling)**:** e.g. <https://yourcompanysubdomain.clockify.me>
* **Metadata Url**:
	* Upload IdP Metadata XML file you downloaded in Step 2   
	or
	* Copy/paste **IdP Metadata URL** from Rippling
* **Login Url:** Copy/paste **Single Sign\-on URL**/**Target URL** from Rippling

After entering all required data, you can choose to verify your configuration by clicking the **Test configuration** button. This action ensures the accuracy of the provided information. If everything is correct, the **Test configuration** button will be replaced with a **Finish configuration** button.

Click **Finish configuration** to complete the process and enable **Log in with SAML2**. Optionally, disable **Log in with email and password**.

### Step 4: Assign application in Rippling [\#](#step-4-assign-application-in-rippling)

Navigate back to Rippling:

On SSO Instructions page scroll down and enter the following: 

* **ACS URL**: Copy/paste **Reply URL** from Clockify
* **Service Provider Entity ID**: Copy/paste **Entity ID** from Clockify

1. Click **Move to Next Step**
2. Choose **Access Rules** you want
3. Choose **Provision Time** you want
4. Configure SSO for Admins if necessary
5. Configure Group Attributes if necessary
6. Click **Connect via Rippling** if you’d like to check the connection between apps or simply **Continue**

And that’s it! You’ve successfully installed your application in rippling and you and your users are now able to log in to your workspace with SAML 2\.0\.

show less

## SAML 2\.0 with JumpCloud [\#](#saml-2-0-with-jumpcloud)

show more

### Step 1: Create subdomain in Clockify [\#](#step-1-create-subdomain-in-clockify)

For more information on this, check out the [Setting up custom subdomain](https://clockify.me/help/getting-started/single-sign-on-sso#setting-up-custom-subdomain) section.

### Step 2: Add SSO Configuration in Clockify  [\#](#step-2-add-sso-configuration-in-clockify)

In the **Authentication** tab in which you created your subdomain:

1. Click **Add SSO Configuration**
2. Choose **SAML2** as authentication type and click **Next**
3. Choose **JumpCloud** as **IdP Template**

### Step 3: Create application in JumpCloud [\#](#step-3-create-application-in-jumpcloud)

1. Navigate to **SSO** in the sidebar on the left
2. Click **\+** to add new app
3. Choose **Custom SAML App**
4. In **Application Information** enter the following:

* **Display Label**: Application name e.g. Clockify
* **Logo**: e.g. upload Clockify logo

In SSO tab you can proceed with the next step. The page contains **SSO Setup instructions** which include the IdP Metadata XML file. Download IDP Metadata from JumpCloud and save it for later.

Continue by populating the following fields.

* **IdP Entity ID**: e.g. <https://yourcompanysubdomain.clockify.me>
* **SP Entity ID**: Copy/paste **Default Relay State** from **Clockify**

Example of Default Relay State:

```
{"location":"https://yourcompanysubdomain.clockify.me", "organizationName":"yourcompanysubdomain"}
```

Make sure you put straight quotes instead of curly ones, or it won’t work.

* **ACS URL:** Copy/paste **Reply URL** from Clockify, e.g. <https://global.api.clockify.me/auth/saml2>

5. In **User attribute mapping** add attributes mapping **Service Provider Attribute Name** to **JumpCloud Attribute Name**
6. Click **Activate**
7. Open the application you created
8. Click on **IDP Certificate Valid** on the left and download the certificate
9. Click **Save**

You’ve successfully created your application in JumpCloud. Now you can decide which users from your JumpCloud account will be able to access Clockify and finish the configuration in Clockify.

### Step 4: Finish SSO configuration in Clockify [\#](#step-4-finish-sso-configuration-in-clockify)

1. Navigate back to Clockify
2. In **SAML2 authentication** form enter the following information:

* **IdP Entity ID**: e.g. <https://yourcompanysubdomain.clockify.me>
* **Metadata Url**: Upload IdP Metadata XML file you downloaded in Step 3
* **IdP Url**: Copy/paste IDP URL from JumpCloud
* **Advanced**: Copy/paste IDP Certificate from JumpCloud

After entering all required data, you can choose to verify your configuration by clicking the **Test configuration** button. This action ensures the accuracy of the provided information. If everything is correct, the **Test configuration** button will be replaced with a **Finish configuration** button.

Click **Finish configuration** to complete the process and enable **Log in with SAML2**. Optionally, disable **Log in with email and password**.

show less

## OAuth 2\.0 (OIDC) with Google [\#](#oauth-2-0-oidc-with-google)

show more

Once you move to subdomain, the default Google log\-in will stop working and you’ll have to configure it manually to continue using it.

Setting up Google log\-in is quick and easy. 

You’ll need to have a **G Suite** or **Cloud Identity** account in order to do this. 

You need to [Set up OAuth 2\.0](https://support.google.com/cloud/answer/6158849?ref_topic=6262490) in your Google account, create a project and get OAuth 2\.0 client ID for a web application.

In **Google Cloud Platform** navigate to **API \& Services** and choose **Credentials**. Open the project/application you’ve created and paste **https://yoursubdomain.clockify.me/login** under the **Authorized redirect URIs**.

You should also add the following URIs in order for the OAuth login to work on Clockify mobile apps:

* https://yourcompanysubdomain.clockify.me/login
* https://yourcompanysubdomain.clockify.me/login/android/oauth2
* https://yourcompanysubdomain.clockify.me/login/ios/oauth2

If you’re using one of the **regional servers** for hosting, please note that the URLs for workspaces that are on subdomain won’t contain the indicator of the region in question, although they are hosted on a regional server.

1. In Clockify, go to **Authentication** tab
2. Click **Add SSO Configiuration**
3. Choose **OAuth2** authentication type
4. Choose **Google** in **IdP Templates** modal
5. Click **Next**
6. Copy/paste **Client ID** and **Client Secret** from your **Google app** as seen in the example below (fields in the **Advanced** section will be pre\-populated)

Your screen in Clockify should look something like this:

![](https://clockify.me/help/wp-content/uploads/2024/06/oauth_with_goodle_1.png)
and

![](https://clockify.me/help/wp-content/uploads/2024/06/oauth_with_google_2.png)
After entering all required data, you can choose to verify your configuration by clicking the **Test configuration** button. This action ensures the accuracy of the provided information. If everything is correct, the **Test configuration** button will be replaced with a **Finish configuration** button.

Click **Finish configuration** to complete the process. Check the **Log in with OAuth** checkbox to start using Google login. Optionally, you can force everyone to use your company’s Google identity for logging in by disabling **Log in with email and password**.

show less

## OAuth 2\.0 (OIDC) with Microsoft Azure [\#](#oauth-2-0-oidc-with-microsoft-azure)

User interface displayed in this video may not correspond to the latest version of the app.

show more

You can connect Azure to Clockify by setting up OAuth.

### Step 1: Create subdomain in Clockify [\#](#step-1-create-subdomain-in-clockify)

For more information on this, check out [Setting up custom subdomain](https://clockify.me/help/getting-started/single-sign-on-sso#setting-up-custom-subdomain) section.

### Step 2: Add SSO configuration in Clockify [\#](#step-2-add-sso-configuration-in-clockify)

1. Click **Add SSO Configuration**
2. Choose **OAuth2** as authentication type
3. Choose **Azure** in **IdP Templates** modal
4. Copy **Redirect URL**

### Step 3: Register application in AzureAD [\#](#step-3-register-application-in-azuread)

1. Navigate to **App registrations**
2. Click **New Registration**
3. Enter the following information:
	* Info:
		* **Name**: Clockify
		* **Supported account types**: Choose what you prefer; in our case it’s **Accounts in this organizational directory only** (**Default Directory only – Single tenant**)
		* **Redirect URI**: Paste **Redirect URL** you copied from Step 2; https://yourcompanysubdomain.clockify.me/login (it can also be: https://yourcompanysubdomain.clockify.me/login/ios/oauth2 or https://yourcompanysubdomain.clockify.me/login/android/oauth2\) and click **Register** to continue

Or, if you’re using one of the regional servers, you should add one of the [regional URLs](https://clockify.me/help/getting-started/single-sign-on-sso#regional-redirection).

### Step 4: Configure (Clockify \& Azure) [\#](#step-4-configure-clockify-azure)

#### Configure AzureAD:  [\#](#configure-azuread)

* **Certificates \& Secrets**:
	* Choose **New client secret**
		* Description: Clockify
		* Expires: Never
	* Click **Add**
* **Client Secret**: Copy/paste the value of this client secret
* **API permissions**:
	* Add a permission
		* Microsoft Graph
		* Check openid in **Delegated permissions**
		* Add permissions (you can also check other permissions such as **email** and **profile**)
* Refresh the page
* Go back to **Overview**

#### Configure Clockify: [\#](#configure-clockify)

* **OAuth2 authentication**:
	* **Client Id**: Go to Azure — Overview — Application (client) ID: copy the value and paste it back in Clockify
	* **Client Secret**: this should already be pasted from previous steps (Certificates \& Secrets)
	* **Directory (tenant) ID**: Go to Azure — Overview — Directory (tenant) ID copy the value and paste it back in Clockify

Fields in the **Advanced** section will be pre\-populated.

Your screen in Clockify should look something like this:

![](https://clockify.me/help/wp-content/uploads/2024/06/oauth_azure_1.png)
and

![](https://clockify.me/help/wp-content/uploads/2024/06/oauth_azure_2.png)
After entering all required data, you can choose to verify your configuration by clicking the **Test configuration** button. This action ensures the accuracy of the provided information. If everything is correct, the **Test configuration** button will be replaced with a **Finish configuration** button.

Click **Finish configuration** to complete the process. Check the **Log in with OAuth** checkbox (and optionally disable **Log in with email and password**).

Alternatively, you can connect Azure using the SAML2 authentication protocol, first by [adding an unlisted (non\-gallery) application](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/add-non-gallery-app) to your Azure AD organization and then [configuring SAML\-based single sign\-on](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-single-sign-on-non-gallery-applications) to this non\-gallery application.

show less

## SAML 2\.0 with Microsoft Azure [\#](#saml-2-0-with-microsoft-azure)

User interface displayed in this video may not correspond to the latest version of the app.

show more

### Step 1: Create subdomain in Clockify [\#](#step-1-create-subdomain-in-clockify)

For more information on this, check out [Setting up custom subdomain](https://clockify.me/help/getting-started/single-sign-on-sso#setting-up-custom-subdomain) section.

### Step 2: Add application in Azure [\#](#step-2-add-application-in-azure)

1. Navigate to **Enterprise Applications**
2. **New application** (then make sure you’re on the new gallery view)
3. Choose **Create your own application**
4. Enter the following:
	* Name: **Clockify**
	* Integrate any other application you don’t find in the gallery

Click **Create** and navigate to **Properties** and fill out the fields:

* Logo: e.g. upload Clockify logo
* Optionally change **User assignment required** and **Visible to users** if necessary

Click **Save** to complete the process.

### Step 3: Clockify [\#](#step-3-clockify)

1. Click **Add SSO Configuration**
2. Choose **SAML2** as authentication type
3. Click **Next**

Once you get the **SAML2 authentication** template, go back to Azure.

### Step 4: Azure SSO configuration [\#](#step-4-azure-sso-configuration)

1. Navigate to **Single sign\-on** in the sidebar
2. Choose **SAML**
3. **Basic SAML Configuration** (click the pencil to edit):
	* **Identifier** (**Entity ID**): This is where you put your subdomain address, e.g. https://yourcompanysubdomain.clockify.me/
	* **Reply URL** (**Assertion Consumer Service URL**): go back to Clockify and copy pre\-generated **Reply URL**, e.g. https://global.api.clockify.me/auth/saml2

Click **Save** and continue with **SAML Certificate**: (click the pencil to edit):

* New certificate

Save the changes and click **the 3 dots** on the **Inactive** certificate, choose **Make certificate active** and click **Yes**.

Now, reload the page to see the changes.

### Step 5: Clockify [\#](#step-5-clockify)

1. **Entity Id**: (this is where you put your subdomain address, in our case it’s https://yourcompanysubdomain.clockify.me/)
2. **Federation Metadata**: Navigate to Azure, under **SAML Certificates** copy/paste **App Federation Metadata Url** in Clockify

**Login Url**: Navigate to Azure, under **Set up Clockify** find **Login URL** and copy/paste it in Clockify

Your screen should look like this:

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-13-at-10.40.06.png)
and like this: 

![](https://clockify.me/help/wp-content/uploads/2024/06/Screenshot-2024-06-13-at-10.40.28.png)
After entering all required data, you can choose to verify your configuration by clicking the **Test configuration** button. This action ensures the accuracy of the provided information. If everything is correct, the **Test configuration** button will be replaced with a **Finish configuration** button.

Click **Finish configuration** and enable **Log in with SAML2** (and optionally disable **Log in with email and password**).

### Step 6: Assign application in Azure [\#](#step-6-assign-application-in-azure)

1. Navigate to **Users and Groups** in the sidebar (where you choose which users from your Azure account will be able to access Clockify)
2. Click **Add user**/group
3. In **Users and groups** choose users you want
4. Click **Select** and **Assign**

show less

## OAuth 2\.0 (OIDC) with Okta [\#](#oauth-2-0-oidc-with-okta)

show more

### Step 1: Create subdomain in Clockify [\#](#step-1-create-subdomain-in-clockify)

For more information on this, check out [Setting up custom subdomain](https://clockify.me/help/getting-started/single-sign-on-sso#setting-up-custom-subdomain) section.

### Step 2: Create application in Okta [\#](#step-2-create-application-in-okta)

1. Navigate to **Applications** in the sidebar
2. Click **Create App Integration** button
3. Choose **OIDC – OpenID Connect** in **Sign\-in** **method** section
4. Choose **Web application** in **Application type** section
5. Click **Next**

#### Create OIDC Integration [\#](#create-oidc-integration)

In **New Web App Integration**, **General Settings** form enter the following information and click **Save**.

1. **App integration name:** e.g. Clockify
2. **Logo** (optional): e.g. upload Clockify logo
3. **Sign\-in redirect URIs**: Copy/paste URL from **Redirect URL** (**Advanced** section) in Clockify SSO configuration

You should also add the following URIs in order for the OAuth 2\.0 (OIDC) login to work on Clockify mobile apps:

* https://yourcompanysubdomain.clockify.me/login/android/oauth2
* https://yourcompanysubdomain.clockify.me/login/ios/oauth2

or, if you’re using one of the regional servers, you should add one of the [regional URLs](https://clockify.me/help/getting-started/data-regions).

Then, scroll down and in the **Assignments** section check **Allow everyone in your organization to access** option. Click **Save** to complete the action. 

You should get the screen that looks like this:

![](https://clockify.me/help/wp-content/uploads/2022/04/image_7_blur.png)
### Step 3: Add SSO configuration in Clockify [\#](#step-3-add-sso-configuration-in-clockify)

Now, in Clockify, in **Authentication** screen where you created your subdomain:

1. Click **Add SSO Configuration** at the bottom of the screen
2. Choose **OAuth2** as authentication type
3. Choose **Okta** as **IdP Template**
4. Click **Next**

In OAuth 2\.0 (OIDC) authentication form enter the following information:

* **Client ID**: Generated in Okta in the previous step; copy it from the **Client Credentials** section
* **Client Secret**: Same as Client ID; copy it from the **Client Credentials** section
* **Okta Domain**: Copy it from Okta, **General Settings**, **Okta domain** field (Note: Okta Domain requires a **domain name only**, for example: doamin\_name.okta.com instead of: https://domain\_name.okta.com)
* **Logout Url**: Optionally add a logout URL to set up redirection after logging out
* **Advanced** section is pre\-populated (automatically generated)

The screen should look something like this:

![](https://clockify.me/help/wp-content/uploads/2022/11/sso_oauth_sample_url-1-1.png)
and

![](https://clockify.me/help/wp-content/uploads/2022/11/Screenshot-2025-02-05-at-16.48.59.png)
### Step 4: Assign application in Okta [\#](#step-4-assign-application-in-okta)

In Okta:

1. Navigate to **Applications**
2. Choose **Clockify**
3. In **Assignments** tab click **Assign**
4. Choose **Assign to People/Groups** depending on who from your Okta account you’d like to be able to access Clockify

After entering all required data, on the Clockify side, you can choose to verify your configuration by clicking the **Test configuration** button. This action ensures the accuracy of the provided information. If everything is correct, the **Test configuration** button will be replaced with a **Finish configuration** button.

Click **Finish configuration** to complete the process and enable **Log in with OAuth**. Optionally, you can disable **Log in with email and password**.

Finally, your screen in Clockify should look something like this:

![](https://clockify.me/help/wp-content/uploads/2022/04/image_blur_33.png)
![](https://clockify.me/help/wp-content/uploads/2022/04/image_34.png)
And that’s it! Now you, and your workspace users are able to log in to your workspace with OAuth 2\.0 (OIDC).

![](https://clockify.me/help/wp-content/uploads/2022/04/image_9.png)
show less

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
