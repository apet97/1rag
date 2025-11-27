---
title: "Roles and Permissions"
url: "https://cake.com/help/administration/roles-and-permissions"
category: "administration"
slug: "roles-and-permissions"
---

# Roles and Permissions

* [Organization\-level roles](#organization-level-roles )
* [Product\-level roles](#product-level-roles)

# Roles and Permissions

As a platform designed to improve team collaboration, CAKE.com Productivity Suite offers various user roles and access permissions tailored to meet the needs of organizational structures of different business solutions. 

User roles are organized in two main levels: 

* Organization level
* Product level

## Organization\-level roles

At the organization level, there are two primary roles:

1\. **Owner**: The owner is the highest level role within the CAKE.com organization. They have the authority to manage organizations, access all information, and grant permissions for all features and actions. While an organization can only have one owner, that owner can create multiple organizations. Also, ownership can be transferred from one organization member to another.

2\. **Member**: Members are regular users within the organization. They have permissions limited to modifying content in the workspaces they are in and modifying their account.

Please note that while there **isn’t** a specific role called **Organization admin**, certain workspace roles, like a **Workspace admin**, may have additional permissions on the organization level, such as managing bundle payments. Multiple workspace admins from different workspaces can exist within one organization.

Workspace owner role has the same permissions as Organization owner, though individual Help centers may refer to it as the Workspace owner. Only a Workspace owner can create a new workspace. If a Workspace admin wishes to create one, new organization must be created, with the Workspace admin assuming the Workspace owner role in that organization.

To help you understand these roles better, check out the table below with comprehensive list of access permissions within the [CAKE.com](http://cake.com/) organization, categorized based on user roles and levels.

You can find this list in the table below:

| **Organization** | | | |
| --- | --- | --- | --- |
|  | **Owner** | **WS Admin** | **Member** |
| Create | Yes | No | No |
| Edit | Yes | No | No |
| Delete | Yes | No | No |

| **Workspace** | | | |
| --- | --- | --- | --- |
|  | **Owner** | **WS Admin** | **Member** |
| Create | Yes | Yes | No |
| Edit | Yes | Yes | No |
| Delete product ws | Yes | No | No |
| Transfer ws between org | Yes | No | No |
| View ws data | Yes | Yes | Yes\* |
| Edit ws data | Yes | Yes | Yes\* |

| **Users** | | | |
| --- | --- | --- | --- |
|  | **Owner** | **WS Admin** | **Member** |
| Assign admin | Yes | Yes | No |
| Remove admin | Yes | No | No |
| Remove ws admin role from org | Yes | No | No |
| Transfer ownership | Yes | No | No |
| Invite members to ws | Yes | Yes | Yes\* |
| Revoke user invite | Yes | Yes | No |
| Deactivate members from ws | Yes | Yes | No |
| Deactivate yourself from ws | No | Yes | Yes |
| Edit other user profile info | No | No | No |
| Delete user profile info | Yes | No | No |
| Edit your user profile info | Yes | Yes | Yes |

| **Subscription** | | | |
| --- | --- | --- | --- |
|  | **Owner** | **WS Admin** | **Member** |
| **Individual** | | | |
| Create subscription | Yes | Yes | No |
| Cancel subscription | Yes | Yes | No |
| Add seats | Yes | Yes | No |
| Remove seats | Yes | Yes | No |
| Upgrade | Yes | Yes | No |
| Downgrade | Yes | Yes | No |
| Edit customer payment info | Yes | No | No |
| Edit payment info | Yes | Yes | No |
| **Bundle** | | | |
| Create subscription | Yes | Yes | No |
| Cancel subscription | Yes | Yes | No |
| Add seats | Yes | Yes | No |
| Remove seats | Yes | Yes | No |
| Upgrade | Yes | Yes | No |
| Downgrade | Yes | Yes | No |
| Edit customer payment info | Yes | No | No |
| Edit payment info | Yes | Yes | No |

\*Product specific 

Transfer ownership: Only a member with active memberships of all workspaces under the organization can become a new owner of that organization. 

## Product\-level roles

User roles defined for each product in the CAKE.com Suite can be found here:

* [Clockify](https://clockify.me/help/administration/user-roles-and-permissions/who-can-do-what)
* [Pumble](https://pumble.com/help/getting-started/pumble-basics/roles-permissions/)
* [Plaky](https://plaky.com/help/administration/roles-and-permissions/overview-4/)

The majority of user roles are the same on all three products. These are: Workspace Owner, Workspace Admin, Regular member.  

However, there are also some product\-specific roles: 

* Clockify:
	* [Team manager](https://clockify.me/help/administration/user-roles-and-permissions/manager-role#team-manager)
	* [Project manager](https://clockify.me/help/administration/user-roles-and-permissions/manager-role#project-manager)
	* [Limited member](https://clockify.me/help/track-time-and-expenses/limited-users)
* Pumble:
	* [Multi\-channel guest](https://pumble.com/help/getting-started/pumble-basics/guest-role-permissions/)
	* [Single\-channel guest](https://pumble.com/help/getting-started/pumble-basics/guest-role-permissions/)
* Plaky:
	* [Viewer](https://plaky.com/help/administration/roles-and-permissions/overview-4/#viewer)

### Was this article helpful?

Submit
Cancel

Thanks for your feedback!
