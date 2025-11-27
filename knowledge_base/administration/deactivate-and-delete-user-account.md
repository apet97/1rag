---
title: "Deactivate and Delete User Account"
url: "https://cake.com/help/administration/deactivate-and-delete-user-account"
category: "administration"
slug: "deactivate-and-delete-user-account"
---

# Deactivate and Delete User Account

* [Key concepts](#key-concepts)
* [Deactivate user from workspace](#deactivate-user-from-workspace)
* [Deactivate user from organization](#deactivate-user-from-organization)
* [Reactivate deactivated user](#reactivate-deactivated-user)
* [Revoke user invite](#revoke-user-invite)
* [Delete user profile from organization](#delete-user-profile-from-organization)

# Deactivate and Delete User Account

This guide explains how to deactivate and delete a user from your organization. You’ll find step\-by\-step instructions for managing user accounts, including how to handle deactivating and deleting user accounts, and what effects these actions have on user data across CAKE.com applications.

## Key concepts

* **Deactivation** removes user from organization, but their data is still there
* **Deletion** permanently removes user’s personal data from the organization
* **Revoking an invite** cancels access for users who were invited, but haven’t joined yet

**Users** can deactivate themselves from workspaces and organizations.  
**Owners** can delete organization members’ personal data while those members’ workspace data remains.

User must be **deactivated** before they can be deleted from the workspace/organization.

## Deactivate user from workspace

When a user is a member of only one workspace within an organization and is deactivated from that workspace, they are also deactivated from the organization. User can be deactivated from the **Workspace management** page.

Each organization needs to have at least one workspace, and every user account is associated with an organization. 

**To deactivate user at workspace\-level:**

1. Go to Workspace
2. Click on specific Workspace where you want to manage the user
3. Click on the **Manage in \[Clockify/Pumble/Plaky]** to manage user in that specific workspace
4. Select the user and follow the instructions to deactivate them

The user will immediately lose access and receive a notification about being removed from the workspace (and the organization, if that’s the case).

## Deactivate user from organization

In the **Organization** page, users can deactivate themselves from an organization. 

To do that:

1. Navigate to the **Organization** page
2. Choose to **Leave Organization**  
![](https://cake.com/help/wp-content/uploads/2024/11/Screenshot-2025-03-21-at-16.10.41.png)  
A prompt will inform you that deactivation will result in losing access to all associated workspaces and data. If you wish to rejoin, you’ll need to contact the workspace owner.
3. You can:
	* Cancel the action
	* Leave and deactivate yourself

Organization owners can also deactivate other users from an organization. 

To do that:

1. Navigate to the **Members page**
2. Find the user you want to deactivate and open their **Member details**
3. Choose to **deactivate** user from all workspaces individually

![](https://cake.com/help/wp-content/uploads/2024/11/Screenshot-2024-12-30-at-11.09.38.png)
After deactivation:

* User receives a confirmation message
* Their status is updated to **deactivated**
* They are removed from all organization\-level access
* They are redirected to any other organizations they belong to

If the user deactivates themselves from their only organization, their account will be deleted and they must create a new organization to use CAKE.com apps.

**Reactivation**: Deactivated users can be reactivated and rejoin workspaces or organizations. 

Deactivation/reactivation and any other changes to user’s account information will be reflected across all workspaces of all apps with their account.

## Reactivate deactivated user

If a user is deactivated from all workspaces and organizations they are a member of, they won’t have any access to them, but they are still in the CAKE.com database. Therefore, when that user is reactivated, their account and associated data will be restored, allowing them to regain access to the workspaces and organizations they were previously a part of.

## Revoke user invite

Cancel a pending invitation before a user joins your workspace.

This action is available to **workspace admins** and **organization owners** directly from the CAKE.com account.

### Organization owner

To revoke an invite as an owner:

1. Go to the **Members** page
2. Find and click on the invited user
3. Choose **Revoke invite** option

![](https://cake.com/help/wp-content/uploads/2024/11/Screenshot-2025-06-24-at-10.47.00.png)
### Workspace admin

To revoke an invite as a workspace admin:

1. Go to the **Workspaces** page
2. Choose the workspace you invited the user to
3. Find the invitee in the list of members
4. Click the **three\-dots menu** next to user status
5. Choose **Revoke invite** option

![](https://cake.com/help/wp-content/uploads/2024/11/Screenshot-2025-06-25-at-14.56.12.png)
After revoking, the invitee is removed from the **Members** list.

## Delete user profile from organization

Owners can delete a user’s personal data from an organization via the **Members** page.

User must be **deactivated** before they can be deleted from the workspace/organization.

To delete user profile:

1. Navigate to the **Members** page
2. Select the **Delete user** option
3. Confirm the deletion

After deletion:

* User receives confirmation email
* User’s personal data is permanently removed
* User’s workspace data remains available
* User’s name is replaced with an alias ‘deleteduser’
* User is removed from all pages containing their data
* If this was their only organization, their account is fully deleted

Deleted user loses access to the organization and their deleted profile. If re\-invited, they are treated as new users.

If a deleted user belongs to other organizations, they will remain in those organizations unless specifically deleted. 

### Was this article helpful?

Submit
Cancel

Thanks for your feedback!
