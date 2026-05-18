---
title: Google Sheets
updated: 2026-03-20T14:12
git_hash: f71952747a136684c5925223e41b7705dd2b3c2f
description: Overview of the Google Sheets integration.
icon: google
---

# Google Sheets

{% hint style="info" %}
The following documentation is for **Google Sheets v2.2.0**.
{% endhint %}

## Overview

Google Sheets is a powerful cloud-based spreadsheet application with real-time collaboration capabilities. This integration enables automated data entry, spreadsheet management, and collaborative workflow automation. Streamline data analysis and enhance team productivity through automated spreadsheet operations.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Google Sheets**

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

Add a name for the connection. You'll be prompted for [**authentication**](googlesheets.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos.

{% hint style="info" %}
If you want to connect Google Sheets with OAuth, follow [Google Authentication](google-authentication.md). You can reuse the same Client ID and Client Secret for Gmail, Google Calendar, Google Chat, Google Docs, Google Drive, and Google Sheets.
{% endhint %}

{% hint style="info" %}
If you want to connect Google Sheets with a service account, follow [Google Service Account Authentication](google-service-account-authentication.md). You can reuse the same service account for Google Docs, Google Drive, and Google Sheets.
{% endhint %}

### Connect using Client Email, Token URI and Private Key

Gets the credentials from the service account keys.

| Label        | Description                                                                     | Type        |
| ------------ | ------------------------------------------------------------------------------- | ----------- |
| Client Email | The client email of the service account registered in the Google Cloud Console. | `text`      |
| Token URI    | The token URI of the Google Cloud Console.                                      | `text`      |
| Private Key  | The private key of the service account registered in the Google Cloud Console.  | `sensitive` |

### Continue with Google

To connect to the **Google Sheets** integration, click on <kbd>Continue with Google</kbd>. This redirects you to Google's secure authentication page, where you can sign in with your Google account and authorize the application. Once connected, Kognitos can access your Google Sheets without storing your Google credentials directly.

## Actions

The following actions are available in the **Google Sheets** integration:

### 1. Add some content to a table

Append content to a Google Sheets table.

### 2. Create a table in a sheet

Create a table in a spreadsheet's sheet.

### 3. Create a google spreadsheet in a folder

Create a new Google Sheets spreadsheet.

### 4. Get the file's sheets

Get the sheets from a Google Sheets file.

### 5. Get the sheet's tables

Get the tables from a Google Sheets sheet.

### 6. Insert a new column in the table

Create a new column in a Google Sheets table.

### 7. Insert a new row in the table

Create a new row in a Google Sheets table.

### 8. Read the content from a table

Get the contents of a Google Sheets table.

### 9. Retrieve the columns from the table

Get the columns from a Google Sheets table.

### 10. Retrieve the rows from the table

Get the rows from a Google Sheets table.

### 11. Write the content in a table

Update the contents of a Google Sheets table.

## Concepts

### Google sheet table reference

Reference to a table inside a Google Sheets spreadsheet's sheet.

| Field Name        | Description                | Type   |
| ----------------- | -------------------------- | ------ |
| `id`              | Id of the table            | `text` |
| `name`            | Name of the table          | `text` |
| `sheet_reference` | Sheet the table belongs to | `json` |

### Google sheet reference

Reference to a sheet inside a Google Sheets spreadsheet file.

| Field Name | Description                           | Type     |
| ---------- | ------------------------------------- | -------- |
| `id`       | Id of the sheet                       | `number` |
| `name`     | Name of the sheet                     | `text`   |
| `file`     | spreadsheet file the sheet belongs to | `json`   |

### Google drive folder reference

Contains all information required to identify a folder in Google Drive.

| Field Name                                | Description                   | Type           |
| ----------------------------------------- | ----------------------------- | -------------- |
| `id`                                      | The id of the folder          | `text`         |
| `folder_name`                             | The name of the folder        | `text`         |
| [`parents`](googlesheets.md#list-of-text) | The ids of the parent folders | `list of text` |

### Google drive file reference

Contains all information required to identify a file in Google Drive.

| Field Name                                | Description                   | Type           |
| ----------------------------------------- | ----------------------------- | -------------- |
| `id`                                      | The id of the file            | `text`         |
| `file_name`                               | The name of the file          | `text`         |
| [`parents`](googlesheets.md#list-of-text) | The ids of the parent folders | `list of text` |

### Google sheet column reference

Reference to a column inside a Google Sheets spreadsheet's sheet.

| Field Name | Description                 | Type     |
| ---------- | --------------------------- | -------- |
| `index`    | Index of the column         | `number` |
| `name`     | Name of the column          | `text`   |
| `table`    | Table the column belongs to | `json`   |

### Google sheet row reference

Reference to a row inside a Google Sheets spreadsheet's sheet.

| Field Name                              | Description              | Type                  |
| --------------------------------------- | ------------------------ | --------------------- |
| `index`                                 | Index of the row         | `number`              |
| [`values`](googlesheets.md#list-of-any) | Values in that row       | `list of list of any` |
| `table`                                 | Table the row belongs to | `json`                |
