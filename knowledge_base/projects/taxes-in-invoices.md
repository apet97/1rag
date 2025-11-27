---
title: "Invoice taxes"
url: "https://clockify.me/help/projects/taxes-in-invoices"
category: "projects"
slug: "taxes-in-invoices"
---

# Invoice taxes

4 min read

**Tax** fields in an invoice form shows the amount of tax added to the total price of a product or a service. Tax can either be a general amount added to the total, or broken down by the item, depending on the tax system used. Clockify uses item\-based tax system.

### Item\-based taxes [\#](#item-based-taxes)

Item\-based taxes are used to apply taxes individually to each item on an invoice. This way you can have a better control over your taxes, making sure that taxes are applied only to relevant items.  

This feature is available to users on [Standard](https://clockify.me/help/administration/subscription-plans#standard) and higher subscription plans and on [Free trial](https://clockify.me/help/administration/free-trial). 

In order to use it, the Invoicing feature needs to be enabled in the **[Workspace settings](https://clockify.me/help/track-time-and-expenses/workspaces#workspace-settings)**: 

1. Navigate to the workspace name at the top left corner of the page
2. Open the three\-dot menu and choose **Workspace settings**
3. Navigate to the **Invoicing** section in the **General** settings and toggle the switch to enable it

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfTgQRth161qt7YFj7ONKUfZfgJD7DUHBHbGxR1P7C4t434aRR2hUrKmTZvI5HGWhrAcO19phzm7GmfWaB3TE_K37ifXRMEVxFB0gNXea67rjROpCe5SZWXtiwI8Oz-gPDcgMgvUyrhZCp56TA5TrEq3V0?key=om-QeMoD2lNvGTlhUn5IiA)
User permissions for this feature depend on the settings in the Permissions tab, in the Workspace settings. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdaH5AgGxun999Ns1wvzxDsikVdA-pKDC6cJwi0H0HolO2ZE6NZmZtc3ltt6-k00aTV_48xiI_IvkzDeGNN4-dxordtZ5PVtyOKWJpyKbRF6VQAdEuZn0rM5a9Fxvd9LzN_T7js5OIsThmg0B2NHaKx1mRO?key=om-QeMoD2lNvGTlhUn5IiA)
#### How item\-based taxes work [\#](#how-item-based-taxes-work)

 When you create a new invoice, you will see two columns after the **AMOUNT** column:  

* **TAX** (if only one tax is enabled)
* **TAX 2** (if a second tax is enabled in the settings)

Each item on the invoice has checkboxes next to the **TAX** and **TAX 2** columns. By default, these checkboxes are checked (blue with a white tick), indicating that the taxes are applied. Unchecking them means that taxes will **not** be applied to that particular item.

Taxes are calculated in the following way:

* **TAX**: This is calculated based on the percentage defined in the **Invoice Settings**
* **TAX 2**: If enabled, this is also calculated as a percentage of the item amount

#### Taxation mode [\#](#taxation-mode)

Taxation mode can be:

* **Simple**: Both taxes are applied to the total amount of the item
	* E.g.: For an item priced at $100, with **Tax 1** at 10% and **Tax 2** at 10%, the calculated taxes will be $10 for each, making the total $120\.
* **Compound**: The second tax is applied on the taxed amount, not the item amount.
	* E.g.: For an item priced at $100, with **Tax 1** at 10% and **Tax 2** at 10%, **Tax 1** is $10, and **Tax 2** is calculated on the taxed amount, resulting in $11 for **Tax 2**, making the total $121\.

The **checkboxes** for **TAX** and **TAX 2** are remembered for each item on the invoice, meaning that the selected state is retained until the invoice is manually edited or changes are made to the tax settings. If you change the tax percentage during invoice creation, the totals will update automatically to reflect the new tax rates.  
If you switch from **Simple** to **Compound** or vice versa, all **Unsent invoices** will automatically update to match the new taxation settings.

For example:

* **Simple to Compound mode**: The **Apply tax** checkbox will appear next to each item
* **Compound to simple mode**: The **Tax** and **Tax 2** checkboxes will reappear

![](https://clockify.me/help/wp-content/uploads/2020/11/Screenshot-2025-07-18-at-12.57.34-1024x608.png)
If you remove one of the taxes from an invoice, then selected taxation mode will also be removed.   
If you add a previously removed tax, the system will remember the last selected taxation mode for that invoice. 

#### Set taxation mode on individual invoices [\#](#set-taxation-mode-on-individual-invoices)

If you’re using two taxes (**TAX** and **TAX 2**) you can set a default taxation mode in the **Invoice settings** that will be applied to all new invoices. However, you can override these default settings for individual invoices when creating or editing.

To do that: 

1. Open the invoice you’re working on
2. Scroll down to the **Taxation mode** section
3. Choose whether **Simple** or **Compound** taxation mode should be applied to that specific invoice

![](https://clockify.me/help/wp-content/uploads/2020/11/Screenshot-2025-07-18-at-13.06.13-1024x328.png)
Taxation mode for a new invoice will not affect any invoices that are already **Partially paid**, **Paid** or **Void**.

### Was this article helpful?

Submit
Cancel

Thank you! If you’d like a member of our support team to respond to you, please drop us a note at support@clockify.me
