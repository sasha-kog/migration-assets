---
title: SFTP
updated: 2026-02-06T18:35
git_hash: 4b92f0db2c8d2d3fe5bc6a78280bed28bac67430
description: Overview of the SFTP integration.
icon: server
---

# SFTP

{% hint style="info" %}
The following documentation is for **SFTP v1.4.11**.
{% endhint %}

## Overview

SFTP (Secure File Transfer Protocol) provides secure file transfer capabilities for safe data exchange. This integration enables automated file uploads, downloads, directory management, and secure data transmission workflows. Ensure secure file operations and maintain data integrity during transfers.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **SFTP**

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

Add a name for the connection. You'll be prompted for [**authentication**](sftp.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Hostname, Port, Username and Password

Connect to an SFTP server.

| Label    | Description                      | Type        |
| -------- | -------------------------------- | ----------- |
| Hostname | The hostname of the SFTP server. | `text`      |
| Port     | The port of the SFTP server.     | `text`      |
| Username | The username for authentication. | `text`      |
| Password | The password for authentication. | `sensitive` |

## Actions

The following actions are available in the **SFTP** integration:

### 1. Copy an item to a folder

Copy an item to a folder

### 2. Create a folder in another folder

Create a (folder) in another folder

### 3. Delete an item

Delete an item (file or folder)

### 4. Download a file

Download a file

### 5. Get a folder at a path

Get a reference to a folder.

### 6. Get a root folder

Get a reference to the root folder.

### 7. Get some folder's items

Get items from a folder.

### 8. Move an item to a folder

Move an item to a folder

### 9. Rename an item to a name

Rename an item (file or folder) to a given name

### 10. Upload a file to a folder

Upload a file to a folder

## Concepts

### Sftp file reference

Contains all information required to identify a file within a storage system

| Field Name  | Description                   | Type               |
| ----------- | ----------------------------- | ------------------ |
| `path`      | The path of the file          | `text`             |
| `file_name` | The name of the file          | `text`             |
| `size`      | The size of the file in bytes | `optional[number]` |
| `extension` | The file extension            | `optional[text]`   |
| `type`      | The type of the SftpItem      | `optional[text]`   |
| `name`      | The name of the item          | `optional[text]`   |

### Sftp folder reference

Contains all information required to identify a folder within a storage system

| Field Name    | Description              | Type             |
| ------------- | ------------------------ | ---------------- |
| `path`        | The path of the folder   | `text`           |
| `folder_name` | The name of the folder   | `text`           |
| `type`        | The type of the SftpItem | `optional[text]` |
| `name`        | The name of the item     | `optional[text]` |
