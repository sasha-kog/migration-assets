---
title: SNS
updated: 2026-03-20T14:12
git_hash: 762df59a5bfc7003fadf2a12494d6ef9de3ff4a5
description: Overview of the SNS integration.
icon: aws
---

# SNS

{% hint style="info" %}
The following documentation is for **SNS v1.6.4**.
{% endhint %}

## Overview

Manages notifications and alerts by delivering event messages to people, applications, or systems.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **SNS**

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

Add a name for the connection. You'll be prompted for [**authentication**](sns.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
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

The following actions are available in the **SNS** integration:

### 1. Get a topic

Get an SNS topic by its ARN.

### 2. List topics

Get SNS topics in the AWS account that match the filter (if any).

### 3. Publish a message to a topic

Create a message in an SNS topic.

## Concepts

### Sns topic

Represents an Amazon SNS topic.

| Field Name     | Description                                     | Type             |
| -------------- | ----------------------------------------------- | ---------------- |
| `arn`          | The Amazon Resource Name (ARN) of the topic     | `text`           |
| `name`         | The unique name of the topic within the account | `text`           |
| `display_name` | The display name of the topic                   | `optional[text]` |
