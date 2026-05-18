---
title: EC2
updated: 2026-03-20T14:12
git_hash: 762df59a5bfc7003fadf2a12494d6ef9de3ff4a5
description: Overview of the EC2 integration.
icon: aws
---

# EC2

{% hint style="info" %}
The following documentation is for **EC2 v1.6.4**.
{% endhint %}

## Overview

Manages network security for EC2 by controlling access to resources.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **EC2**

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

Add a name for the connection. You'll be prompted for [**authentication**](ec2.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
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

The following actions are available in the **EC2** integration:

### 1. Attach a rule to a security group

Create an ingress or egress rule in a security group.

### 2. Get security groups from ec2

Get security groups from EC2.

### 3. Get some security group's rules

Get security group rules for a security group in EC2.

### 4. Revoke a security group rule

Delete a security group rule from a security group.

## Concepts

### Ec2 security group

Represents an EC2 security group.

| Field Name         | Description                                            | Type              |
| ------------------ | ------------------------------------------------------ | ----------------- |
| `id`               | The ID of the security group.                          | `text`            |
| `name`             | The name of the security group.                        | `text`            |
| `description`      | The description of the security group.                 | `text`            |
| `vpc_id`           | The ID of the VPC to which the security group belongs. | `text`            |
| [`tags`](#aws-tag) | A list of tags associated with the security group.     | `list of aws tag` |

### Aws tag

Represents an AWS tag.

| Field Name | Description           | Type   |
| ---------- | --------------------- | ------ |
| `key`      | The key of the tag.   | `text` |
| `value`    | The value of the tag. | `text` |

### Ec2 ip permission

Represents an IP permission for an EC2 security group.

| Field Name                                              | Description                                     | Type                     |
| ------------------------------------------------------- | ----------------------------------------------- | ------------------------ |
| `ip_protocol`                                           | The IP protocol for the permission.             | `text`                   |
| `from_port`                                             | The start port for the permission.              | `number`                 |
| `to_port`                                               | The end port for the permission.                | `number`                 |
| [`ip_ranges`](#ip_ranges-ec2-ip-permission)             | The list of IP ranges for the permission.       | `optional[list of json]` |
| [`ipv6_ranges`](#ipv6_ranges-ec2-ip-permission)         | The list of IPv6 ranges for the permission.     | `optional[list of json]` |
| [`prefix_list_ids`](#prefix_list_ids-ec2-ip-permission) | The list of prefix list IDs for the permission. | `optional[list of json]` |

### Ec2 security group rule

Represents an EC2 security group rule.

| Field Name         | Description                                                        | Type              |
| ------------------ | ------------------------------------------------------------------ | ----------------- |
| `rule_id`          | The ID of the security group rule.                                 | `text`            |
| `group_id`         | The ID of the security group.                                      | `text`            |
| `group_owner_id`   | The AWS account ID of the security group owner.                    | `text`            |
| `is_egress`        | Whether the rule is an egress rule (True) or ingress rule (False). | `boolean`         |
| `ip_protocol`      | The IP protocol for the rule.                                      | `text`            |
| `from_port`        | The start port (or ICMP type) for the rule.                        | `number`          |
| `to_port`          | The end port (or ICMP code) for the rule.                          | `number`          |
| [`tags`](#aws-tag) | A list of tags associated with the security group rule.            | `list of aws tag` |
| `rule_arn`         | The ARN of the security group rule.                                | `text`            |
| `cidr_ipv4`        | The IPv4 CIDR range for the rule, if applicable.                   | `optional[text]`  |
| Name          | Type             |
| ------------- | ---------------- |
| `description` | `optional[text]` |
| `cidr_ip`     | `optional[text]` |
| Name          | Type             |
| ------------- | ---------------- |
| `description` | `optional[text]` |
| `cidr_ipv6`   | `optional[text]` |
| Name             | Type             |
| ---------------- | ---------------- |
| `description`    | `optional[text]` |
| `prefix_list_id` | `optional[text]` |
