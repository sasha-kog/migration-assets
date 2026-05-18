---
title: Postgres
updated: 2026-03-20T14:12
git_hash: d659480432bc3482c681c99a4e9fff3f682344b7
description: Overview of the Postgres integration.
icon: database
---

# Postgres

{% hint style="info" %}
The following documentation is for **Postgres v2.1.0**.
{% endhint %}

## Overview

Enables connecting to, querying, and managing PostgreSQL databases.

{% hint style="success" %}
The Postgres integration supports **discovery**. Once connected, you can browse available services and entities directly from Kognitos, then enable the specific actions your automations need. See [Custom Actions](README.md#custom-actions) for setup instructions.
{% endhint %}

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Postgres**

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

Add a name for the connection. You'll be prompted for [**authentication**](postgres.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

### Discovering Actions

After connecting, you can discover and enable the specific services and entities available in your system:

{% stepper %}
{% step %}
#### Open the connection menu

Navigate to **Integrations**, find your Postgres connection, and click the three-dot menu <kbd>**⋯**</kbd> next to the connection name. Select <kbd>**Configure Actions**</kbd>.
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

### Connect using Host, Port, Username, Password and Database Name

Connect to a PostgreSQL database using the provided connection parameters.

| Label         | Description   | Type        |
| ------------- | ------------- | ----------- |
| Host          | Host          | `text`      |
| Port          | Port          | `text`      |
| Username      | Username      | `text`      |
| Password      | Password      | `sensitive` |
| Database Name | Database Name | `text`      |
