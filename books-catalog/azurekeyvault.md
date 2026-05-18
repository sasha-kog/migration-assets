---
title: Azure Key Vault
updated: 2026-03-31T14:46
git_hash: ce079737338ca07ae306d11a1cd9d047ef69e961
description: Overview of the Azure Key Vault integration.
icon: microsoft
---

# Azure Key Vault

{% hint style="info" %}
The following documentation is for **Azure Key Vault v1.3.4**.
{% endhint %}

## Overview

Azure Key Vault securely stores and manages cryptographic keys, secrets, and certificates in the cloud. This integration enables automated secret management, key rotation, and secure credential workflows. Strengthen security posture and automate sensitive data protection in Azure environments.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Azure Key Vault**

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

Add a name for the connection. You'll be prompted for [**authentication**](azurekeyvault.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Azure tenant ID, Azure client ID, Azure client secret and Azure subscription ID

Connect to Microsoft Graph API using client credentials.

| Label                 | Description                 | Type        |
| --------------------- | --------------------------- | ----------- |
| Azure tenant ID       | The Azure tenant ID         | `text`      |
| Azure client ID       | The client (application) ID | `text`      |
| Azure client secret   | The client secret           | `sensitive` |
| Azure subscription ID | The Azure subscription ID   | `text`      |

## Actions

The following actions are available in the **Azure Key Vault** integration:

### 1. Get key vaults

Retrieve all Key Vaults accessible to the authenticated principal in your Azure subscription.

### 2. Get a secret from a key vault

Retrieve a specific secret from a Key Vault by name.

### 3. List secrets in a key vault

List all secrets stored in a specific Key Vault.

## Concepts

### Azure key vault reference

Represents a reference to an Azure Key Vault.

| Field Name        | Description                                      | Type             |
| ----------------- | ------------------------------------------------ | ---------------- |
| `id`              | The ID of the key vault.                         | `text`           |
| `name`            | The name of the key vault.                       | `text`           |
| `url`             | The URL of the key vault.                        | `text`           |
| `location`        | The Azure region where the key vault is located. | `optional[text]` |
| `resource_group`  | The resource group containing the key vault.     | `optional[text]` |
| `subscription_id` | The subscription ID containing the key vault.    | `optional[text]` |
