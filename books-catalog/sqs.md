---
title: SQS
updated: 2026-03-20T14:12
git_hash: 762df59a5bfc7003fadf2a12494d6ef9de3ff4a5
description: Overview of the SQS integration.
icon: aws
---

# SQS

{% hint style="info" %}
The following documentation is for **SQS v1.6.4**.
{% endhint %}

## Overview

Manages message queues by storing and delivering messages between systems.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **SQS**

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

Add a name for the connection. You'll be prompted for [**authentication**](sqs.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using AWS Access key ID, AWS Secret Access Key, AWS Region, AWS Role ARN and AWS External ID

Assumes a role using the provided AWS credentials.

| Label                 | Description                                                                | Type        |
| --------------------- | -------------------------------------------------------------------------- | ----------- |
| AWS Access key ID     | The AWS Access Key ID for the initial authentication.                      | `text`      |
| AWS Secret Access Key | The AWS Secret Access Key for the initial authentication.                  | `sensitive` |
| AWS Region            | The AWS Region for the initial authentication.                             | `text`      |
| AWS Role ARN          | The ARN of the role to assume.                                             | `text`      |
| AWS External ID       | An optional external ID that might be required by the role's trust policy. | `sensitive` |

### Connect using AWS Access key ID, AWS Secret Access Key and AWS Region

Connects to an API using the provided API key.

| Label                 | Description               | Type        |
| --------------------- | ------------------------- | ----------- |
| AWS Access key ID     | The AWS Access Key ID     | `text`      |
| AWS Secret Access Key | The AWS Secret Access Key | `sensitive` |
| AWS Region            | The AWS Region            | `text`      |

## Actions

The following actions are available in the **SQS** integration:

### 1. Delete a message from a queue

Delete a message from an SQS queue.

### 2. Get queues from sqs

Get queues available in SQS.

### 3. Receive messages from a queue

Get messages from an SQS queue.

### 4. Send a message to a queue

Create a message in an SQS queue.

## Concepts

### Sqs message

Represents a message from an Amazon SQS queue.

| Field Name           | Description                                        | Type             |
| -------------------- | -------------------------------------------------- | ---------------- |
| `message_id`         | The unique identifier for the message              | `text`           |
| `receipt_handle`     | The receipt handle used to delete the message      | `text`           |
| `queue_url`          | The URL of the queue the message was received from | `text`           |
| `body`               | The message body                                   | `text`           |
| `attributes`         | System attributes of the message                   | `optional[json]` |
| `message_attributes` | Custom attributes of the message                   | `optional[json]` |
