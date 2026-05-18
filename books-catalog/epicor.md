---
title: Epicor
updated: 2026-03-20T14:12
git_hash: ddb55bcb60518379cdfdc413bc5952f706d9d00e
description: Overview of the Epicor integration.
icon: industry
---

# Epicor

{% hint style="info" %}
The following documentation is for **Epicor v1.2.0**.
{% endhint %}

## Overview

Discover business entities and automate ERP workflows within Epicor.

{% hint style="success" %}
The Epicor integration supports **discovery**. Once connected, you can browse available services and entities directly from Kognitos, then enable the specific actions your automations need. See [Custom Actions](README.md#custom-actions) for setup instructions.
{% endhint %}

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Epicor**

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

Add a name for the connection. You'll be prompted for [**authentication**](epicor.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

### Discovering Actions

After connecting, you can discover and enable the specific services and entities available in your system:

{% stepper %}
{% step %}
#### Open the connection menu

Navigate to **Integrations**, find your Epicor connection, and click the three-dot menu <kbd>**⋯**</kbd> next to the connection name. Select <kbd>**Configure Actions**</kbd>.
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

### Connect using Host, Environment, Company, Username, Password and API Key

Connects to an API using the provided API key.

| Label       | Description                           | Type   |
| ----------- | ------------------------------------- | ------ |
| Host        | The Epicor server URL                 | `text` |
| Environment | The Epicor environment                | `text` |
| Company     | The Epicor company ID                 | `text` |
| Username    | The username for authentication       | `text` |
| Password    | The password for authentication       | `text` |
| API Key     | The API key to be used for connecting | `text` |

## Actions

The following actions are available in the **Epicor** integration:

### 1. Get method info from epicor

Gets the parameter info for a custom method on an Epicor service.

### 2. Invoke a method on epicor

Invokes a custom method on an Epicor Business Object service.

### 3. Retrieve some baqs from epicor

Retrieves the list of available Business Activity Queries (BAQs).

### 4. Retrieve some entities from epicor

Retrieves the list of available Epicor entities for a given service.

{% hint style="info" %}
In addition to these built-in actions, the Epicor integration supports **custom actions** that are discovered from your specific system. The actions available depend on which services you enable through the [discovery process](epicor.md#discovering-actions).
{% endhint %}

## Concepts

### Epicor entity

Represents an Epicor entity with its metadata.This includes both regular entities and Business Activity Queries (BAQs).

| Field Name      | Description                                        | Type   |
| --------------- | -------------------------------------------------- | ------ |
| `name`          | The name of the entity or BAQ.                     | `text` |
| `kind`          | The kind of the entity (e.g., "EntitySet", "BAQ"). | `text` |
| `url`           | The URL of the entity or BAQ.                      | `text` |
| `discover_call` | The discovery call for the entity or BAQ.          | `text` |
