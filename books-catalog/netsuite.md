---
title: Netsuite
updated: 2026-03-20T14:12
git_hash: 317abba5f619529f8039c0b3e631c7bc5e5337cd
description: Overview of the Netsuite integration.
icon: n
---

# Netsuite

{% hint style="info" %}
The following documentation is for **Netsuite v2.1.8**.
{% endhint %}

## Overview

The Netsuite BDK integration connects to Oracle NetSuite ERP systems and automatically discovers all your business entities. From customers and employees to transactions and custom records, the Netsuite integration allows you to seamlessly read, create, and update any business entities in your NetSuite instance.

{% hint style="success" %}
The Netsuite integration supports **discovery**. Once connected, you can browse available services and entities directly from Kognitos, then enable the specific actions your automations need. See [Custom Actions](README.md#custom-actions) for setup instructions.
{% endhint %}

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Netsuite**

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

Add a name for the connection. You'll be prompted for [**authentication**](netsuite.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

### Discovering Actions

After connecting, you can discover and enable the specific services and entities available in your system:

{% stepper %}
{% step %}
#### Open the connection menu

Navigate to **Integrations**, find your Netsuite connection, and click the three-dot menu <kbd>**⋯**</kbd> next to the connection name. Select <kbd>**Configure Actions**</kbd>.
{% endstep %}

{% step %}
#### Browse and enable services

Browse or search for the services you need. Toggle them on to enable them in your workspace.
{% endstep %}

{% step %}
#### Save and wait

Click <kbd>**Save**</kbd> to apply your configuration. Allow 1-2 minutes for Kognitos to complete the discovery process. Once finished, the enabled actions become available in your drafts and automations.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Consumer key, Consumer secret, Token ID, Token secret and Account ID

Connects to Netsuite using token based authentication (TBA).

| Label           | Description                                  | Type        |
| --------------- | -------------------------------------------- | ----------- |
| Consumer key    | The consumer key for the Netsuite account    | `sensitive` |
| Consumer secret | The consumer secret for the Netsuite account | `sensitive` |
| Token ID        | The token ID for the Netsuite account        | `sensitive` |
| Token secret    | The token secret for the Netsuite account    | `sensitive` |
| Account ID      | The account ID for the Netsuite account      | `text`      |

## Actions

The following actions are available in the **Netsuite** integration:

### 1. Retrieve a file's information from netsuite

Get a file's information from NetSuite's File Cabinet, using the SOAP API.

### 2. Retrieve a schema from netsuite

Get the JSON schema for an entity

### 3. Retrieve an attachment from netsuite

Get an attachment from NetSuite's File Cabinet, using the SOAP API.

{% hint style="info" %}
In addition to these built-in actions, the Netsuite integration supports **custom actions** that are discovered from your specific system. The actions available depend on which services you enable through the [discovery process](netsuite.md#discovering-actions).
{% endhint %}
