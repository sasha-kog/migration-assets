---
title: Oracle Fusion
updated: 2026-03-20T14:12
git_hash: e76dadc33873fe0631d2c14516d320d2dafa33f1
description: Overview of the Oracle Fusion integration.
icon: building
---

# Oracle Fusion

{% hint style="info" %}
The following documentation is for **Oracle Fusion v1.0.5**.
{% endhint %}

## Overview

Access and organize enterprise data in Oracle Fusion. Oracle Fusion provides a centralized way to access and organize Oracle Fusion data such as financials, supply chain, and human capital information. It can be used to create, retrieve, update and delete Oracle Fusion resources, as well as perform certain supported actions on them.

{% hint style="success" %}
The Oracle Fusion integration supports **discovery**. Once connected, you can browse available services and entities directly from Kognitos, then enable the specific actions your automations need. See [Custom Actions](README.md#custom-actions) for setup instructions.
{% endhint %}

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Oracle Fusion**

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

Add a name for the connection. You'll be prompted for [**authentication**](oracle-fusion.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

### Discovering Actions

After connecting, you can discover and enable the specific services and entities available in your system:

{% stepper %}
{% step %}
#### Open the connection menu

Navigate to **Integrations**, find your Oracle Fusion connection, and click the three-dot menu <kbd>**⋯**</kbd> next to the connection name. Select <kbd>**Configure Actions**</kbd>.
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

### Connect using Instance URL, Username and Password

Connects to Oracle Fusion using the username and password.

| Label        | Description                        | Type        |
| ------------ | ---------------------------------- | ----------- |
| Instance URL | The URL for the Oracle instance    | `text`      |
| Username     | The username of the Oracle account | `text`      |
| Password     | The password of the Oracle account | `sensitive` |
