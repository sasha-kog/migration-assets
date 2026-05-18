---
title: Asana
updated: 2026-04-15T14:56
git_hash: a7121ae374a2499a64123a0c7640bc7305e9f13e
description: Overview of the Asana integration.
icon: list-check
---

# Asana

{% hint style="info" %}
The following documentation is for **Asana v1.1.1**.
{% endhint %}

## Overview

Asana is a project management platform for organizing work, tracking tasks, and coordinating teams. This integration lets you create and update tasks, assign work, add comments, and retrieve projects, sections, and users from Asana.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Asana**

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

Add a name for the connection. You'll be prompted for [**authentication**](asana.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos.

### Sign in with Asana

To connect to the **Asana** integration, click on <kbd>Sign in with Asana</kbd>. This redirects you to Asana so you can sign in and authorize the connection.

### OAuth Authorization Code

Connect to Asana with your own OAuth client.

| Label | Description | Type |
| --- | --- | --- |
| Client ID | OAuth client identifier | `text` |
| Client Secret | OAuth client secret | `sensitive` |

### API Key

Connect to Asana with a Personal Access Token.

| Label | Description | Type |
| --- | --- | --- |
| Personal Access Token | The Asana Personal Access Token (PAT). Found under **My Settings** → **Apps** → **Personal Access Tokens** in Asana. | `sensitive` |

## Actions

The following actions are available in the **Asana** integration:

### 1. Add a comment to a task

Add a comment to an existing Asana task.

### 2. Assign a task to a user

Assign an Asana task to a user.

### 3. Complete a task

Mark an Asana task as complete.

### 4. Create a task in a project

Create a new task in an Asana project.

### 5. Delete a task

Delete an Asana task.

### 6. Get comments from a task

Retrieve comments for a task.

### 7. Get projects

Retrieve projects from Asana.

### 8. Get sections from a project

Retrieve sections from an Asana project.

### 9. Get tasks from a project

Retrieve tasks from an Asana project.

### 10. Get users

Retrieve users from Asana.

### 11. Update a task

Update an existing Asana task.
