---
title: Linear
updated: 2026-03-20T14:12
git_hash: 8d5d421e29995c97b048822713cf7b552122ec70
description: Overview of the Linear integration.
icon: diagram-project
---

# Linear

{% hint style="info" %}
The following documentation is for **Linear v1.2.0**.
{% endhint %}

## Overview

Streamline your team's project management and issue tracking with Linear integration. Linear is a modern project management platform that helps teams organize work, track progress, and deliver projects efficiently. This integration enables you to seamlessly manage your Linear workspace directly through natural language commands.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Linear**

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

Add a name for the connection. You'll be prompted for [**authentication**](linear.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Actions

The following actions are available in the **Linear** integration:

### 1. Create an issue

Create an issue in Linear.

### 2. Get the issues

Fetch the issues matching the filters (if any).

### 3. Get the labels

Fetch all available issue label names in the workspace.

### 4. Get the teams

Fetch the teams matching the filters (if any).

### 5. Get the users from a team

Get the users from a team.

## Concepts

### Linear team

A team in Linear

| Field Name | Description                         | Type   |
| ---------- | ----------------------------------- | ------ |
| `id`       | The unique identifier for the team. | `text` |
| `name`     | The name of the team.               | `text` |
| `key`      | The short identifier for the team.  | `text` |

### Linear user

A user in Linear

| Field Name | Description                                  | Type      |
| ---------- | -------------------------------------------- | --------- |
| `id`       | The unique identifier for the user.          | `text`    |
| `email`    | The email address of the user.               | `text`    |
| `name`     | The name of the user.                        | `text`    |
| `is_me`    | Whether this user is the authenticated user. | `boolean` |
