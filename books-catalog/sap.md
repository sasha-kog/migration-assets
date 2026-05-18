---
title: SAP
updated: 2026-03-20T13:39
git_hash: 5bc439f59a3a6c4f504e341de79d53d630c3f443
description: Overview of the SAP integration.
icon: building-columns
---

# SAP

{% hint style="info" %}
The following documentation is for **SAP v2.6.0**.
{% endhint %}

## Overview

SAP is an enterprise resource planning (ERP) platform used to manage business operations across finance, logistics, and supply chain. This integration lets you discover SAP entities in your system and interact with them by reading, creating, and updating records.

{% hint style="success" %}
The SAP integration supports **discovery**. Once connected, you can browse available SAP services and entities directly from Kognitos, then enable the specific actions your automations need. See [Custom Actions](README.md#custom-actions) for setup instructions.
{% endhint %}

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **SAP**

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

Add a name for the connection. You'll be prompted for [**authentication**](sap.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

### Discovering Actions

After connecting, you can discover and enable the specific SAP services and entities available in your system:

{% stepper %}
{% step %}
#### Open the connection menu

Navigate to **Integrations**, find your SAP connection, and click the three-dot menu <kbd>**⋯**</kbd> next to the connection name. Select <kbd>**Configure Actions**</kbd>.
{% endstep %}

{% step %}
#### Browse and enable services

Browse or search for the SAP services you need (e.g., "Material Document API", "Purchase Order"). Toggle them on to enable them in your workspace.
{% endstep %}

{% step %}
#### Save and wait

Click <kbd>**Save**</kbd> to apply your configuration. Allow 1-2 minutes for Kognitos to complete the discovery process. Once finished, the enabled actions become available in your drafts and automations.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect Using Base URL, Username and Password

Connects to the SAP OData API.

| Label    | Description                        | Type        |
| -------- | ---------------------------------- | ----------- |
| Base URL | The base URL of the SAP OData API. | `text`      |
| Username | The username to authenticate with. | `text`      |
| Password | The password to authenticate with. | `sensitive` |

## Actions

The following actions are available in the **SAP** integration:

### 1. Retrieve services

Retrieves the list of available SAP services. Use this to see what services are accessible through your connection before enabling specific actions.

### 2. Retrieve entities

Retrieves the list of available SAP entities for a given API service. Provide the service name to see all entities you can interact with.

### 3. Upload an attachment

Uploads a file attachment to a SAP business object. Requires the file, a file name, the business object type, and the linked SAP object key.

{% hint style="info" %}
In addition to these built-in actions, the SAP integration supports **custom actions** that are discovered from your specific SAP system. The actions available to you depend on which services you enable through the [discovery process](sap.md#discovering-actions).
{% endhint %}
