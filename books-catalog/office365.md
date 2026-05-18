---
title: Microsoft Office 365
description: Overview of the Microsoft Office 365 integration.
icon: microsoft
updated: 2026-03-20T14:12
git_hash: f3d697f0b32f65eb46ce7316539f730dac957813
---

{% hint style="info" %}
The following documentation is for **Microsoft Office 365 v2.6.0**.
{% endhint %}

# Overview

Microsoft Office 365 provides comprehensive productivity suite with cloud-based collaboration and communication tools. This integration enables automated workflow management across Word, Excel, PowerPoint, and other Office applications. Enhance productivity and streamline business processes through integrated Microsoft ecosystem automation.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Microsoft Office 365**


### Steps

Follow these steps to connect the integration in Kognitos:

{% stepper %}
{% step %}
#### Navigate

Using the left navigation menu, go to **Integrations** → **Explore Integrations**.
{% endstep %}

{% step %}
#### Find

Search for the integration and click on it.
{% endstep %}

{% step %}
#### Connect

Click on <kbd>**Connect**</kbd> to add a connection to the integration.
{% endstep %}

{% step %}
#### Configure

Add a name for the connection. You'll be prompted for [**authentication**](#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Permissions

When using **client credentials** authentication, you need to have the following **application permissions** in Microsoft Graph:

{% hint style="info" %}
Application permissions are used when an app runs without a signed-in user _(such as with a client credentials flow)_.
These permissions give the app organization-wide access and must be granted by an administrator in your Microsoft organization.
For additional details, refer to Microsoft's [**guides**](https://learn.microsoft.com/en-us/graph/security-authorization#grant-permissions-to-an-application).
{% endhint %}

#### User and Directory Access

* `User.Read.All`
* `User.ReadWrite.All`
* `Directory.Read.All`
* `Directory.ReadWrite.All`

#### Mail Operations

* `Mail.Read`
* `Mail.ReadWrite`
* `Mail.ReadBasic`
* `Mail.ReadBasic.All`
* `Mail.ReadWrite.Shared`
* `Mail.Send`

#### Calendar Operations

* `Calendars.ReadBasic`
* `Calendars.Read`
* `Calendars.ReadWrite`

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Client ID, Client Secret and Tenant ID

Connect to the Microsoft Graph API using the provided client credentials.

| Label         | Description                                                  | Type        |
| ------------- | ------------------------------------------------------------ | ----------- |
| Client ID     | The client ID of the application registered in Azure AD.     | `text`      |
| Client Secret | The client secret of the application registered in Azure AD. | `sensitive` |
| Tenant ID     | The tenant ID of the Azure AD directory.                     | `text`      |

### Connect using Client ID, Certificate and Tenant ID

Connect to the Microsoft Graph API using certificate credentials.

| Label       | Description                                                                           | Type        |
| ----------- | ------------------------------------------------------------------------------------- | ----------- |
| Client ID   | The client ID of the application registered in Azure AD.                              | `text`      |
| Certificate | PEM-encoded X.509 certificate string containing both the certificate and private key. | `sensitive` |
| Tenant ID   | The tenant ID of the Azure AD directory.                                              | `text`      |

### Connect using Client ID, Certificate, Private Key and Tenant ID

Connect to the Microsoft Graph API using certificate and private key.

| Label       | Description                                              | Type        |
| ----------- | -------------------------------------------------------- | ----------- |
| Client ID   | The client ID of the application registered in Azure AD. | `text`      |
| Certificate | PEM-encoded certificate string.                          | `sensitive` |
| Private Key | PEM-encoded private key string.                          | `sensitive` |
| Tenant ID   | The tenant ID of the Azure AD directory.                 | `text`      |


## Actions

The following actions are available in the **Microsoft Office 365** integration:

### 1. Get a group's members from office365

Retrieves members of an Office 365 group accessible via the Microsoft Graph API.

### 2. Get some groups from office365

Get Office 365 groups accessible via the Microsoft Graph API.

### 3. Get some users from office365

Get Office 365 users accessible via the Microsoft Graph API.



## Concepts

### Office group

An Office Group represents a group in the Microsoft Graph. It includes key user details such as display name,and email address.

| Field Name      | Description                                           | Type             |
| --------------- | ----------------------------------------------------- | ---------------- |
| `id`            | The unique identifier for the group.                  | `text`           |
| `display_name`  | The name displayed in the address book for the group. | `optional[text]` |
| `email_address` | The group's email address.                            | `optional[text]` |

### Office user

An Office User represents a user in the Microsoft Graph. It includes key user details such as display name,email address, and job title.

| Field Name      | Description                                                   | Type             |
| --------------- | ------------------------------------------------------------- | ---------------- |
| `id`            | The unique identifier for the user.                           | `text`           |
| `display_name`  | The name displayed in the address book for the user.          | `optional[text]` |
| `email_address` | The user's email address (usually their user principal name). | `optional[text]` |
| `job_title`     | The user's job title.                                         | `optional[text]` |
