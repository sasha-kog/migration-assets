---
title: Airtable
updated: 2026-02-06T18:35
git_hash: 88f63168a991c4ef28e70e2d959e83d17a857116
description: Overview of the Airtable integration.
icon: table-cells
---

# Airtable

{% hint style="info" %}
The following documentation is for **Airtable v2.0.0**.
{% endhint %}

## Overview

Airtable is a database platform that works like a spreadsheet. This integration allows you to create records, sync data, and manage workflows in your Airtable bases.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Airtable**

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

Add a name for the connection. You'll be prompted for [**authentication**](airtable.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using personal access token

Connects using a Personal Access Token from Airtable.

| Label                 | Description                | Type        |
| --------------------- | -------------------------- | ----------- |
| personal access token | The Personal Access Token. | `sensitive` |

## Actions

The following actions are available in the **Airtable** integration:

### 1. Create a record in a table

Creates a new record in a table

### 2. Get some base's tables

Gets a list of all tables from a specific base

### 3. Get some bases

Gets a list of all bases

### 4. Get some table's records

Gets a list of all records from a specific table

## Concepts

### Airtable table

Represents an Airtable table.

| Field Name    | Description                                              | Type             |
| ------------- | -------------------------------------------------------- | ---------------- |
| `id`          | The unique identifier of the table.                      | `text`           |
| `base_id`     | The unique identifier of the base containing this table. | `text`           |
| `name`        | The name of the table.                                   | `optional[text]` |
| `description` | Optional description of the table.                       | `optional[text]` |

### Airtable record

Represents an Airtable record. A record is a row of a table.

| Field Name | Description                                         | Type   |
| ---------- | --------------------------------------------------- | ------ |
| `id`       | The unique identifier of the record.                | `text` |
| `fields`   | Dictionary containing the field data of the record. | `json` |

### Airtable base

Represents an Airtable base. A base is a collection of tables.

| Field Name | Description                        | Type             |
| ---------- | ---------------------------------- | ---------------- |
| `id`       | The unique identifier of the base. | `text`           |
| `name`     | The name of the base.              | `optional[text]` |
