---
title: "Troubleshooting SSO Login Issues in Clockify (SAML 2.0 & OAuth2)"
url: "https://clockify.me/help/troubleshooting/troubleshooting-sso"
category: "troubleshooting"
slug: "troubleshooting-sso"
---

# Troubleshooting SSO Login Issues in Clockify (SAML 2.0 & OAuth2)

* [Troubleshooting SAML 2\.0 Issues](#troubleshooting-saml-2-0-issues)
* [Troubleshooting OAuth2 Issues (e.g., Google, Microsoft)](#troubleshooting-oauth2-issues-e-g--google-microsoft)
* [Best Practices for Admins](#best-practices-for-admins)
* [Need More Help?](#need-more-help)

# Troubleshooting SSO Login Issues in Clockify (SAML 2\.0 \& OAuth2\)

2 min read

If you or your team encounter issues while logging into Clockify using SSO (via SAML 2\.0 or OAuth2\), use this guide to quickly identify and resolve the most common problems.

## Troubleshooting SAML 2\.0 Issues [\#](#troubleshooting-saml-2-0-issues)

### **“You don’t have permission to access this workspace”**

Clockify can’t authenticate the user because they haven’t been added to the workspace.

 **Fix**:

* Invite the user manually from **Team → Invite**
* Or enable **Auto\-provisioning** under **SSO settings**

---

### **Incorrect or Incomplete SAML Setup**

**Verify the following in both Clockify and your IdP:**

* **Entity ID**, **SAML SSO URL**, **Metadata URL**, **Relay State** and **X.509 Certificate** are correct
* The **email** attribute is included in the SAML assertion
* Clockify workspace domain matches what’s configured in IdP
* **NameID Format** is set to emailAddress

---

### **Missing Email Claim**

**Fix (Azure AD example)**:

* Go to **Enterprise applications → your app → Single sign\-on**
* Under **Attributes \& Claims**, add a claim:
	* Name: email
	* Source attribute: user.mail

---

### **User Belongs to a Different Workspace**

**Fix**:

* Confirm the user is invited to the correct workspace
* Workspace SSO settings only apply to that specific workspace

---

### **“SAML Authentication Failed” or “Invalid Response”**

* Check if the signature is valid
* NameID is set to email
* Response is within valid time range (NotBefore, NotOnOrAfter)

---

## Troubleshooting OAuth2 Issues (e.g., Google, Microsoft) [\#](#troubleshooting-oauth2-issues-e-g-google-microsoft)

### **User can’t log in via Oauth2**

* Check that the email used with OAuth2 matches the one in Clockify

---

### **Redirect URI Mismatch**

If you’re using a custom OAuth2 app (e.g., for enterprise Microsoft login), the redirect URI might not be correctly set.

**Fix**:

* Go to your OAuth2 provider’s app settings
* Make sure to add relevant redirect URI is:

https://yoursubdomain.clockify.me/login

https://app.clockify.me/login

<https://app.clockify.me/login/android/oauth2> For Android

<https://clockify.me/login/ios/oauth2> For iOS app

---

### **Invalid Token / Expired Session**

Tokens issued by the provider may expire or become invalid.

**Fix**:

* Try logging out and back in again
* If using Microsoft, ensure consent has been granted for required scopes (like openid, email, profile)

## Best Practices for Admins [\#](#best-practices-for-admins)

* Regularly check for **certificate expiration**
* Always match users by email address across all platforms

---

## Need More Help? [\#](#need-more-help)

If you’re still having trouble, reach out to **Clockify Support** with:

* A screenshot of the error
* A screenshot from Developer tools Console
* The user’s email address
* Timestamp of the login attempt
* (For SAML) A copy of the SAML response or debug log

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
