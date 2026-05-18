---
title: Databricks
updated: 2026-02-06T18:35
git_hash: e74d4c1fb5758205aba6ea760360dc20f28288bd
description: Overview of the Databricks integration.
icon: database
---

# Databricks

{% hint style="info" %}
The following documentation is for **Databricks v1.1.0**.
{% endhint %}

## Overview

Databricks is a unified analytics platform for data engineering, data science, and machine learning. This integration enables automated data pipeline management, notebook execution, and analytics workflows within your Databricks workspace.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Databricks**

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

Add a name for the connection. You'll be prompted for [**authentication**](databricks.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Cluster URL and Access Token

Connects to Databricks using the provided access token.

| Label        | Description                                | Type        |
| ------------ | ------------------------------------------ | ----------- |
| Cluster URL  | The Databricks cluster URL                 | `text`      |
| Access Token | The access token to be used for connecting | `sensitive` |

## Actions

The following actions are available in the **Databricks** integration:

### 1. Append a file to a table

Append data from a file to an existing table.

### 2. Append a table to a databricks table

Append data from a Kognitos table to an existing Databricks table.

### 3. Create a databricks table from a table

Create a table in Databricks from a Kognitos table.

### 4. Create databricks table from a file

Create a table from an uploaded file.

### 5. Get a catalog

Get a catalog by its name.

### 6. Get file at a path

Get file metadata for a file at the given path.

### 7. Get some catalog's schema

Get a schema from a catalog by its name.

### 8. Get some warehouses

List all warehouses in the workspace.

### 9. Upload a file to databricks

Upload a file to a catalog volume.

## Concepts

### Databricks warehouse

Warehouse in Databricks.

| Field Name | Description                            | Type   |
| ---------- | -------------------------------------- | ------ |
| `id`       | The unique identifier of the warehouse | `text` |
| `name`     | The name of the warehouse              | `text` |

### Databricks file

File in Databricks.

| Field Name    | Description                                          | Type   |
| ------------- | ---------------------------------------------------- | ------ |
| `schema`      | The schema containing the file                       | `json` |
| `path`        | The path to the file                                 | `text` |
| `file_type`   | The MIME type of the file                            | `text` |
| `file_format` | The file format extension (e.g., csv, json, parquet) | `text` |

### Databricks schema

Schema in Databricks.

| Field Name | Description                        | Type   |
| ---------- | ---------------------------------- | ------ |
| `name`     | The name of the schema             | `text` |
| `catalog`  | The catalog containing this schema | `json` |

### Databricks catalog

Catalog in Databricks.

| Field Name | Description             | Type   |
| ---------- | ----------------------- | ------ |
| `name`     | The name of the catalog | `text` |
