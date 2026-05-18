---
title: Secrets Manager
updated: 2026-03-20T14:12
git_hash: 762df59a5bfc7003fadf2a12494d6ef9de3ff4a5
description: Overview of the Secrets Manager integration.
icon: aws
---

# Secrets Manager

{% hint style="info" %}
The following documentation is for **Secrets Manager v1.6.4**.
{% endhint %}

## Overview

Provides secure storage and management of sensitive business information like passwords, API keys, and certificates.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Secrets Manager**

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

Add a name for the connection. You'll be prompted for [**authentication**](secrets-manager.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
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

The following actions are available in the **Secrets Manager** integration:

### 1. Get a secret from secrets manager

Get a secret from AWS Secrets Manager.

### 2. List secrets from secrets manager

Get secrets available in AWS Secrets Manager.

## Concepts

### Aws secret information

Represents the information of an AWS Secret.

| Field Name    | Description                                | Type                     |
| ------------- | ------------------------------------------ | ------------------------ |
| `name`        | The name of the secret.                    | `text`                   |
| `arn`         | The ARN of the secret.                     | `text`                   |
| `description` | The description of the secret.             | `text`                   |
| `tags`        | A list of tags associated with the secret. | `optional[list of json]` |
