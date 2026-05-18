---
title: Smartsheet
updated: 2026-02-06T18:35
git_hash: a34f64e6e8607e1786df7731b132be2e808e9f0d
description: Overview of the Smartsheet integration.
icon: table-cells
---

# Smartsheet

{% hint style="info" %}
The following documentation is for **Smartsheet v2.0.0**.
{% endhint %}

## Overview

Smartsheet is a dynamic work management platform that combines spreadsheet functionality with project management features. This integration enables automated sheet updates, project tracking, resource management, and collaborative workflow automation. Improve project organization and team productivity.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Smartsheet**

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

Add a name for the connection. You'll be prompted for [**authentication**](smartsheet.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Credentials

### 1. API Token

These steps outline how to create a secure Smartsheet API token for accessing and interacting with the [Smartsheet API](https://developers.smartsheet.com/api/smartsheet/introduction).

{% stepper %}
{% step %}
#### Open Personal Settings

Select your account profile image at the bottom of the left navigation bar, then choose **Personal Settings**.
{% endstep %}

{% step %}
#### Go to API Access

In the Personal Settings window, navigate to the **API Access** tab. Then click on **Generate new access token**.

<div data-with-frame="true"><figure><img src="../../.gitbook/assets/generate-smartsheet-api-token.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
#### Name the Token

Enter a descriptive name for the token and select **OK**.
{% endstep %}

{% step %}
#### Copy and Save the Token

Copy the generated token value and store it securely (e.g., in a password manager).\
&#xNAN;_&#x4E;ote: This is the only time the token will be visible._
{% endstep %}

{% step %}
#### Finish Setup

Select **OK** to return to the Manage API Access Tokens page, where your new token will appear by name.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
For more information, check out Smartsheet's documentation [**here**](https://help.smartsheet.com/articles/2482389-generate-API-key)**.**
{% endhint %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using token

Authenticate with the provided token.

| Label | Description                                  | Type        |
| ----- | -------------------------------------------- | ----------- |
| token | Smartsheet API token used for authentication | `sensitive` |

## Actions

The following actions are available in the **Smartsheet** integration:

### 1. Add some content to a sheet

Append the contents of a table into an existing sheet.

### 2. Get some sheet's columns

Get a sheet's columns.

### 3. Get some sheet's rows

Get a sheet's rows.

### 4. Get some sheets

Gets all sheets.

### 5. Get some workspaces

Gets all workspaces.

### 6. Insert a new column in a sheet

Inserts a column in a sheet.

### 7. Insert a new row in a sheet

Append a row in a sheet.

### 8. Write the content in a workspace

Set the contents of a table to a new sheet.

## Concepts

### Smartsheet sheet

A Sheet in Smartsheet

| Field Name | Description           | Type     |
| ---------- | --------------------- | -------- |
| `id`       | The id of the sheet   | `number` |
| `name`     | The name of the sheet | `text`   |

### Smartsheet column

A column from a sheet.

| Field Name    | Description             | Type                                                                                                                                      |
| ------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `id`          | The id of the column    | `optional[number]`                                                                                                                        |
| `title`       | The name of the column  | `text`                                                                                                                                    |
| `column_type` | The type of the column  | `enum[abstract_datetime, checkbox, contact_list, date, datetime, multi_contact_list, multi_picklist, picklist, predecessor, text_number]` |
| `index`       | The index of the column | `number`                                                                                                                                  |

### Smartsheet row

A row from a sheet.

| Field Name                               | Description                                              | Type                      |
| ---------------------------------------- | -------------------------------------------------------- | ------------------------- |
| `id`                                     | The id of the row                                        | `optional[number]`        |
| `row_number`                             | The number of the row                                    | `optional[number]`        |
| [`cells`](smartsheet.md#smartsheet-cell) | list of the cells from the row                           | `list of smartsheet cell` |
| `content`                                | a dictionary of column name to cell value in that column | `optional[json]`          |
| `parent_row_id`                          | the id of the parent row if this row is indented         | `optional[number]`        |

### Smartsheet cell

A cell from a sheet.

| Field Name     | Description                          | Type               |
| -------------- | ------------------------------------ | ------------------ |
| `column_id`    | The id of the column for the cell    | `number`           |
| `column_title` | The title of the column for the cell | `text`             |
| `row_id`       | The id of the row for the cell       | `optional[number]` |
| `value`        | The value of the cell                | `any`              |

### Smartsheet workspace

A Workspace in Smartsheet

| Field Name | Description               | Type     |
| ---------- | ------------------------- | -------- |
| `id`       | The id of the workspace   | `number` |
| `name`     | The name of the workspace | `text`   |
