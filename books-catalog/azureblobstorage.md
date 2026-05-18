---
title: Azure Blob Storage
updated: 2026-03-31T14:46
git_hash: ce079737338ca07ae306d11a1cd9d047ef69e961
description: Overview of the Azure Blob Storage integration.
icon: microsoft
---

# Azure Blob Storage

{% hint style="info" %}
The following documentation is for **Azure Blob Storage v1.3.4**.
{% endhint %}

## Overview

Azure Blob Storage provides massively scalable object storage for unstructured data in the cloud. This integration enables automated file management, data archiving, and cloud storage workflows within Microsoft Azure. Leverage enterprise-grade cloud storage for secure and scalable data operations.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Azure Blob Storage**

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

Add a name for the connection. You'll be prompted for [**authentication**](azureblobstorage.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Azure account name and Azure account Key

Connect to a Blob Storage account using the provided account key.

| Label              | Description            | Type        |
| ------------------ | ---------------------- | ----------- |
| Azure account name | The Azure account name | `text`      |
| Azure account Key  | The Azure account Key  | `sensitive` |

### Connect using Azure Account Name, SAS Token and Container Name

Connect to an API using the provided API key.

| Label              | Description            | Type        |
| ------------------ | ---------------------- | ----------- |
| Azure Account Name | The Azure account name | `text`      |
| SAS Token          | The SAS token          | `sensitive` |
| Container Name     | The container name     | `text`      |

## Actions

The following actions are available in the **Azure Blob Storage** integration:

### 1. Copy an item to a folder

Copy a file or folder to a specified destination folder within the container.

### 2. Create a folder in another folder

Create a new subfolder inside an existing folder.

### 3. Delete an item

Delete a file or folder from the storage container.

### 4. Download a file

Download a file from Azure Blob Storage to use in your automation.

### 5. Get a folder at a path

Get a reference to a folder at a specific path within the container.

### 6. Get a root folder from a container

Get a reference to the root folder of a storage container.

### 7. Get some folder's items

List the files and subfolders contained within a folder.

### 8. Move an item to a folder

Move a file or folder to a different destination folder within the container.

### 9. Rename an item to a name

Rename a file or folder to a new name.

### 10. Sign a blob

Generate a signed URL for a blob, providing temporary access to the resource.

### 11. Upload a file to a folder

Upload a file to a specified folder in Azure Blob Storage.

## Concepts

### Azure file reference

Represents a reference to a file in an Azure Storage.

| Field Name       | Description                                                                            | Type             |
| ---------------- | -------------------------------------------------------------------------------------- | ---------------- |
| `container_name` | The name of the container.                                                             | `text`           |
| `blob_name`      | The full path of the file within the container, including the file name and extension. | `text`           |
| `account_name`   | The name of the account.                                                               | `optional[text]` |
| `etag`           | Entity tag.                                                                            | `optional[text]` |
| `sas_token`      | SAS token.                                                                             | `optional[text]` |

### Azure folder reference

Represents a reference to a folder in an Azure Storage

| Field Name       | Description                                                                                                    | Type             |
| ---------------- | -------------------------------------------------------------------------------------------------------------- | ---------------- |
| `container_name` | The name of the container.                                                                                     | `text`           |
| `path`           | The path of the folder within the container. Should end with a trailing slash ('/') to indicate it's a folder. | `text`           |
| `account_name`   | The name of the account.                                                                                       | `optional[text]` |
| `etag`           | Entity tag                                                                                                     | `optional[text]` |
| `sas_token`      | SAS token.                                                                                                     | `optional[text]` |
