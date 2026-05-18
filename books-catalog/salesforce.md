---
title: Salesforce
updated: 2026-03-20T13:44
git_hash: ae0521530c3a47cb2dafb8075ac9bfa71f9e24c5
description: Overview of the Salesforce integration.
icon: salesforce
---

# Salesforce

{% hint style="info" %}
The following documentation is for **Salesforce v2.0.4**.
{% endhint %}

## Overview

Salesforce is a CRM platform for managing sales, customer relationships, and business operations. This integration lets you create, update, and delete Salesforce objects, manage reports, and send emails directly from your Kognitos automations.

{% hint style="success" %}
The Salesforce integration supports **discovery**. Once connected, Kognitos automatically learns the object types in your Salesforce instance, including custom objects. You can then enable the specific actions your automations need. See [Custom Actions](README.md#custom-actions) for setup instructions.
{% endhint %}

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Salesforce**

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

Add a name for the connection. You'll be prompted for [**authentication**](salesforce.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

### Discovering Actions

After connecting, you can discover and enable the Salesforce objects and operations available in your instance:

{% stepper %}
{% step %}
#### Open the connection menu

Navigate to **Integrations**, find your Salesforce connection, and click the three-dot menu <kbd>**⋯**</kbd> next to the connection name. Select <kbd>**Configure Actions**</kbd>.
{% endstep %}

{% step %}
#### Browse and enable objects

Browse or search for the Salesforce objects you need (e.g., "Account", "Opportunity", "Custom\_Object\_\_c"). Toggle them on to enable them in your workspace.
{% endstep %}

{% step %}
#### Save and wait

Click <kbd>**Save**</kbd> to apply your configuration. Allow 1-2 minutes for Kognitos to complete the discovery process. Once finished, the enabled actions become available in your drafts and automations.
{% endstep %}
{% endstepper %}

## Credentials

This section explains how to obtain the credentials needed to connect Salesforce. You can choose from different authentication methods, each requiring different credentials.

### 1. Client Credentials

This connection method uses OAuth 2.0 through a Connected App. These steps walk you through obtaining a consumer key and secret.

{% hint style="success" %}
This is the most secure and recommended authentication method.
{% endhint %}

{% stepper %}
{% step %}
#### Create a Connected App

1. Log in to Salesforce
2. Click the **Setup** icon (gear icon in the top right)
3. In the Quick Find box, search for **"App Manager"**
4. Click **New Connected App**
{% endstep %}

{% step %}
#### Configure the Connected App

1. **Basic Information:**
   1. **Connected App Name:** Enter a name (e.g., "Kognitos Integration")
   2. **API Name:** Will auto-populate
   3. **Contact Email:** Enter your email address
2. **API (Enable OAuth Settings):**
   1. Check **Enable OAuth Settings**
   2. **Callback URL:** Enter `https://login.salesforce.com/services/oauth2/callback` (or your specific callback URL)
   3. **Selected OAuth Scopes:** Add the required scopes:
      1. Access and manage your data (api)
      2. Perform requests on your behalf at any time (refresh\_token, offline\_access)
      3. Full access (full) - if needed
   4. Click **Save**
{% endstep %}

{% step %}
#### Get Consumer Key and Consumer Secret

1. After saving, navigate back to **Setup** → **App Manager**
2. Find your Connected App and click **View**
3. In the **API (Enable OAuth Settings)** section:
   1. Copy the **Consumer Key** (also called Client ID)
   2. Click **"Click to reveal"** next to **Consumer Secret**
   3. Salesforce will ask you to verify your identity (via email or MFA)
   4. Copy the **Consumer Secret** (also called Client Secret)
{% endstep %}

{% step %}
#### Get Your Domain

Your Salesforce **domain** is the My Domain prefix from your Salesforce URL:

* **With My Domain:** `mycompany` (from `https://mycompany.my.salesforce.com`)
* **Without My Domain:** `na30` (from `https://na30.salesforce.com`, where "na30" is your instance)

Log into Salesforce and check your browser's address bar.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
For more information, check out the Salesforce documentation: [Create a Connected App](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create.htm\&type=5).
{% endhint %}

### 2. Username, Password, Security Token, and Domain

This method uses username-password authentication with an API security token.

{% stepper %}
{% step %}
#### Get Your Username

Your username is the email address you use to log into Salesforce (e.g., `yourname@yourcompany.com`).
{% endstep %}

{% step %}
#### Get Your Password

This is your standard Salesforce account password.
{% endstep %}

{% step %}
#### Get Your Security Token

1. Log in to Salesforce
2. Click your **profile icon** (top right)
3. Select **Settings**
4. In the Quick Find box, type **"Reset"**
5. Click **Reset My Security Token**
6. Click the **Reset Security Token** button
7. Check your email for the new security token
8. Copy the token from the email

{% hint style="info" %}
If you don't see the "Reset My Security Token" option, your organization may have IP restrictions enabled. Try this direct URL:

`https://[YourDomain].my.salesforce.com/_ui/system/security/ResetApiTokenEdit`
{% endhint %}
{% endstep %}

{% step %}
#### Get Your Domain

Use `login` for production, `test` for sandbox, or your My Domain prefix for custom domains.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect Using Consumer Key, Consumer Secret and Domain

Connect to Salesforce using the OAuth 2.0 Client Credentials flow.

| Label           | Description                                                                            | Type        |
| --------------- | -------------------------------------------------------------------------------------- | ----------- |
| Consumer Key    | The Consumer Key (also called Client ID) from your Connected App.                      | `sensitive` |
| Consumer Secret | The Consumer Secret (also called Client Secret) from your Connected App.               | `sensitive` |
| Domain          | Your Salesforce My Domain prefix (e.g., `mycompany` for mycompany.my.salesforce.com).  | `text`      |

### Connect Using Username, Password, Security Token and Domain

Connects to a Salesforce instance using username, password, security token, and domain.

| Label          | Description                                                                                                              | Type        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------- |
| Username       | The Salesforce login email (e.g., `user@company.com`).                                                                   | `text`      |
| Password       | The password associated with your Salesforce account.                                                                    | `sensitive` |
| Security Token | The security token emailed to you by Salesforce after a token reset. Appended to your password internally for API auth.  | `sensitive` |
| Domain         | Use `login` for production, `test` for sandbox, or your My Domain prefix for custom domains.                             | `text`      |

### Connect Using Username, Password and Security Token

Connects to a Salesforce instance using username, password, and security token.

| Label          | Description                                                                                                              | Type        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------- |
| Username       | The Salesforce login email (e.g., `user@company.com`).                                                                   | `text`      |
| Password       | The password associated with your Salesforce account.                                                                    | `sensitive` |
| Security Token | The security token emailed to you by Salesforce after a token reset. Appended to your password internally for API auth.  | `sensitive` |

## Actions

The following actions are available in the **Salesforce** integration:

### 1. Create a report

Creates a report in Salesforce using the provided report metadata (name, description, report type, and optional filters).

### 2. Export a report as Excel

Exports a Salesforce report as an Excel file.

### 3. Export a report as a table

Exports a Salesforce report as a table for use in automations.

### 4. Retrieve reports

Retrieves reports from Salesforce. Supports filtering by report name and other fields.

### 5. Send an email

Sends an email through Salesforce to one or more recipients with a subject and body.

{% hint style="info" %}
In addition to these built-in actions, the Salesforce integration supports **custom actions** discovered from your specific Salesforce instance. This includes operations on standard and custom objects (Accounts, Opportunities, Cases, custom objects, etc.). The actions available depend on which objects you enable through the [discovery process](salesforce.md#discovering-actions).
{% endhint %}

## Concepts

### Salesforce create report body

Information sent to Salesforce to create a report.

| Field Name        | Description                 | Type   |
| ----------------- | --------------------------- | ------ |
| `report_metadata` | The metadata of the report. | `json` |

### Salesforce report

A Salesforce report object representing a set of data that meets certain criteria, displayed in an organized format.

| Field Name             | Description                                                                                            | Type                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------ | -------------------- |
| `id`                   | The ID of the report.                                                                                  | `text`               |
| `owner_id`             | The ID of the owner of the report.                                                                     | `text`               |
| `name`                 | The name of the report.                                                                                | `text`               |
| `developer_name`       | The unique name of the object in the API.                                                              | `text`               |
| `description`          | The description of the report. Limit: 255 characters.                                                  | `optional[text]`     |
| `folder_name`          | The name of the folder that contains the report.                                                       | `optional[text]`     |
| `namespace_prefix`     | The namespace prefix of the report.                                                                    | `optional[text]`     |
| `format`               | The format of the report: Tabular, Summary, Matrix, or Joined.                                         | `optional[text]`     |
| `is_deleted`           | Whether the report is deleted.                                                                         | `optional[boolean]`  |
| `created_date`         | The date and time when the report was created.                                                         | `optional[datetime]` |
| `created_by_id`        | The ID of the user who created the report.                                                             | `optional[text]`     |
| `last_modified_date`   | The date and time when the report was last modified.                                                   | `optional[datetime]` |
| `last_modified_by_id`  | The ID of the user who last modified the report.                                                       | `optional[text]`     |
| `last_referenced_date` | The date and time when the report was last referenced.                                                 | `optional[datetime]` |
| `last_run_date`        | The date and time when the report was last run.                                                        | `optional[datetime]` |
| `last_viewed_date`     | The date and time when the report was last viewed.                                                     | `optional[datetime]` |
