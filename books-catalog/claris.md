---
title: FileMaker
updated: 2026-03-20T14:12
git_hash: 4d645d0768b7ec15a50fbec8091bee7e610edbdf
description: Overview of the FileMaker integration.
icon: database
---

# FileMaker

{% hint style="info" %}
The following documentation is for **FileMaker v1.1.4**.
{% endhint %}

## Overview

Integrate with Claris services to build custom apps and manage data

{% hint style="success" %}
The FileMaker integration supports **discovery**. Once connected, you can browse available services and entities directly from Kognitos, then enable the specific actions your automations need. See [Custom Actions](README.md#custom-actions) for setup instructions.
{% endhint %}

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **FileMaker**

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

Add a name for the connection. You'll be prompted for [**authentication**](claris.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

### Discovering Actions

After connecting, you can discover and enable the specific services and entities available in your system:

{% stepper %}
{% step %}
#### Open the connection menu

Navigate to **Integrations**, find your FileMaker connection, and click the three-dot menu <kbd>**⋯**</kbd> next to the connection name. Select <kbd>**Configure Actions**</kbd>.
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

### Connect using URL, Username and Password

Connects to the FileMaker API using basic authentication.

| Label    | Description                                      | Type        |
| -------- | ------------------------------------------------ | ----------- |
| URL      | The base URL of the FileMaker OData API endpoint | `text`      |
| Username | The username for authentication                  | `text`      |
| Password | The password for authentication                  | `sensitive` |
