---
title: Azure Translator
updated: 2026-03-31T14:46
git_hash: ce079737338ca07ae306d11a1cd9d047ef69e961
description: Overview of the Azure Translator integration.
icon: microsoft
---

# Azure Translator

{% hint style="info" %}
The following documentation is for **Azure Translator v1.3.4**.
{% endhint %}

## Overview

Azure Translator provides AI-powered language translation services for global communication and localization. This integration enables automated text translation, language detection, and multilingual content workflows. Break down language barriers and automate international communication processes.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Azure Translator**

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

Add a name for the connection. You'll be prompted for [**authentication**](azuretranslator.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Azure translator instance ID and Azure translator instance key

Connect to an API using the provided API key.

| Label                         | Description                       | Type   |
| ----------------------------- | --------------------------------- | ------ |
| Azure translator instance ID  | The Azure translator instance ID  | `text` |
| Azure translator instance key | The Azure translator instance key | `text` |

## Actions

The following actions are available in the **Azure Translator** integration:

### 1. Translate a document to a language

Translate an entire document to a specified target language using Azure's AI-powered translation service.

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
