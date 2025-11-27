---
title: "Common errors and issues"
url: "https://clockify.me/help/troubleshooting/common-errors-and-issues"
category: "troubleshooting"
slug: "common-errors-and-issues"
---

# Common errors and issues

* [Start time is greater than end time](#start-time-is-greater-than-end-time )
* [403 \- Forbidden](#403---forbidden)
* [401 \- Unauthorized](#401---unauthorized)
* [400 \- Required token or API key and 1000 \- Full authentication required](#400---required-token-or-api-key-and-1000---full-authentication-required)

# Common errors and issues

4 min read

## Start time is greater than end time  [\#](#start-time-is-greater-than-end-time)

This error occurs when the start time in your API request is after the end time, often due to a mismatch between local time zones and UTC, which is what the Clockify API expects. 

Why this happens: 

* The Clockify API uses UTC time for all time\-based values
* Sending a start time in local time (e.g., Brussels \+1\) without converting it to UTC may result in a start time that appears later than the end time.

How to fix it: 

* Make sure both start and end times in your request are converted to UTC.
* Double\-check the full API request:
	* Endpoint used
	* Request body and time fields
	* Headers (especially Content\-Type and authentication)
	* Time zone settings on the server or script generating the request

Even if a non\-UTC start time is accepted, the timer might begin with a negative duration, which can affect calculations and reporting. Converting to UTC resolves this issue completely.

## 403 – Forbidden [\#](#403-forbidden)

This error means your request is understood by the server, but you’re not authorized to perform the action due to missing permissions or feature restrictions. 

Why this happens:

* The API key being used doesn’t have permission for the requested operation
* The user’s role (e.g., Project Manager or a Team Manager) has limited access
* The subscription plan doesn’t include the requested feature
* You’re requesting a report with amounts, but you don’t have permission to view amounts

How to fix it: 

* Check user role and permissions:

Make sure the API key belongs to a user with the correct role and access to the resource.

* Verify subscription:

Some endpoints and features require a paid plan, like “Add time for others”, for example. 

* Regenerate your API key:

1. Click on your Profile picture and select Preferences
2. Open the Advanced tab
3. Click Generate next to the API key field

* If generating a report as a Project or a Team Manager:

If amounts are restricted and you don’t have access, use the following parameter in your request:

“amountShown”: “HIDE\_AMOUNT”

This will generate the report without including financial data. 

## 401 – Unauthorized [\#](#401-unauthorized)

This error means authentication failed, usually because the API key is missing, invalid, or not authorized to access the requested source. 

Why this happens:

* API key is missing, invalid, or incorrectly passed in the header
* API key is associated with a user who doesn’t have access to the endpoint
* The current subscription plan doesn’t support the requested feature

How to fix it: 

* Verify that the API key is included correctly

X\-Api\-Key: your\_api\_key

* Check that the API key is valid:

1. Click on your profile picture and select Preferences
2. Open the Advanced tab
3. Click Generate to create a new API key

* Ensure correct permissions

The user tied to the API key must have access to the requested workspace, project, or feature. 

* Double\-check your plan:

Some API endpoints are only available on paid plans, like “Add time for others”, for example.

## 400 – Required token or API key and 1000 – Full authentication required [\#](#400-required-token-or-api-key-and-1000-full-authentication-required)

This error appears when the request is missing an authentication header, meaning the system doesn’t know who is making the request.

Why this happens: 

* The API call is missing the X\-Api\-Key in the headers
* The request might be sent from a script or tool that didn’t properly include authentication info

How to fix it:

Include the following header in your request:

X\-Api\-Key: your\_api\_key 

Still having issues? The Clockify Support Team will be happy to look into it and assist you further. Please contact us at support@clockify.me and include the following details:

1. A screenshot of the request and response you’re getting
2. Information about your role in the workspace
3. A screenshot of the error message you see in the response

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
