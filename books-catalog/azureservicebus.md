---
title: Azure Service Bus
updated: 2026-03-31T14:46
git_hash: ce079737338ca07ae306d11a1cd9d047ef69e961
description: Overview of the Azure Service Bus integration.
icon: microsoft
---

# Azure Service Bus

{% hint style="info" %}
The following documentation is for **Azure Service Bus v1.3.4**.
{% endhint %}

## Overview

Azure Service Bus provides reliable cloud messaging as a service (MaaS) and simple hybrid integration. This integration enables automated message queuing, publish-subscribe messaging, and enterprise messaging workflows. Enhance application reliability and enable scalable communication between distributed applications and services.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Azure Service Bus**

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

Add a name for the connection. You'll be prompted for [**authentication**](azureservicebus.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Connection String

Connect to Azure Service Bus using connection string parameters.

| Label             | Description                                         | Type        |
| ----------------- | --------------------------------------------------- | ----------- |
| Connection String | The connection string for the Service Bus namespace | `sensitive` |

## Actions

The following actions are available in the **Azure Service Bus** integration:

### 1. Receive a message from a queue

Retrieve the latest message from an Azure Service Bus queue for processing in your automation.

### 2. Send a message to a queue

Send a message to an Azure Service Bus queue to trigger downstream processes or communicate with other services.
