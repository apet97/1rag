---
title: "Difference between userID and API key"
url: "https://clockify.me/help/troubleshooting/difference-between-userid-and-api-key"
category: "troubleshooting"
slug: "difference-between-userid-and-api-key"
---

# Difference between userID and API key

1 min read

* **API Key**: A unique key generated for your account to authenticate API calls
* **UserID**: A unique identifier for each user in the workspace

To retrieve the `userID`, use the endpoint:

```
GET [/v1/user](https://docs.clockify.me/#tag/User/operation/getLoggedUser)
```

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
