---
title: "How to import time off balance for multiple users via API"
url: "https://clockify.me/help/troubleshooting/how-to-import-time-off-balance-for-multiple-users-via-api"
category: "troubleshooting"
slug: "how-to-import-time-off-balance-for-multiple-users-via-api"
---

# How to import time off balance for multiple users via API

* [Steps](#steps)

# How to import time off balance for multiple users via API

1 min read

To import time\-off balances for multiple users, you can use the API to update the balance for each user.

## Steps [\#](#steps)

1. **Create a `PATCH` request** to update user balances:  
Endpoint: `PATCH`   
[`/v1/workspaces/{workspaceId}/time-off/balance/policy/{policyId}/`](https://docs.clockify.me/#tag/Balance/operation/updateBalance)
2. **Prepare your CSV file**:  
Extract user IDs from Clockify and prepare a CSV file with user IDs and corresponding balance data
3. **Run collection in Postman**:  
Upload your CSV and execute the request

The users’ time\-off balances will be updated successfully, and you will receive a `204 No Content` response.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
