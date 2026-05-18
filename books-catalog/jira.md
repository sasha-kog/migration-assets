---
title: Jira
updated: 2026-03-20T13:30
git_hash: 013edb71dca2660c8e68413286ed48acf984c803
description: Overview of the Jira integration.
icon: jira
---

# Jira

{% hint style="info" %}
The following documentation is for **Jira v1.2.0**.
{% endhint %}

## Overview

Jira is Atlassian's project management and issue tracking platform. This integration lets you create, search, edit, assign, and delete Jira issues, and retrieve Jira labels directly from your Kognitos automations.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Jira**

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

Add a name for the connection. You'll be prompted for [**authentication**](jira.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### OAuth Authorization Code

Best for personal accounts. Click <kbd>Continue with Atlassian</kbd> to sign in through Atlassian's secure authentication page and authorize the connection.

### Connect Using Email, Domain and API Token

Connects to Jira using your Atlassian email and an API token.

| Label     | Description                                                                                                            | Type        |
| --------- | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| Email     | Your Atlassian account email, the one you use to log in. Example: `john@company.com`                                   | `text`      |
| Domain    | Your Jira Cloud site domain (the host part of your Jira URL). Example: `mycompany.atlassian.net`                       | `text`      |
| API Token | An API token generated from your Atlassian account settings.                                                            | `sensitive` |

{% hint style="info" %}
To generate an API token, go to [**Atlassian API Tokens**](https://id.atlassian.com/manage-profile/security/api-tokens), click <kbd>Create API token</kbd>, give it a label, and copy the value.
{% endhint %}

## Actions

The following actions are available in the **Jira** integration:

### 1. Assign an issue

Assigns a Jira issue to a user. Looks up the user by email and assigns the issue to them.

### 2. Create an issue

Creates a new issue in a Jira project. You can specify the project key, summary, and issue type (defaults to "Task").

### 3. Create multiple issues

Creates multiple issues in a Jira project in a single operation. Each issue in the list needs at least a summary.

### 4. Delete an issue

Permanently deletes an issue from Jira. This action cannot be undone.

### 5. Edit an issue

Edits an existing issue in Jira. Compares the provided issue against its current state and updates only the fields that have changed. Supports updating summary, status, issue type, priority, and assignee.

### 6. Get labels

Retrieves labels from Jira.

### 7. Search issues

Searches for issues in Jira. If no filter is provided, returns all issues. Supports filtering by any Jira field: project, status, assignee, priority, issue type, summary, created, updated, labels, reporter, and resolution.

## Concepts

### Jira issue

An issue in Jira.

| Field Name   | Description                                    | Type   |
| ------------ | ---------------------------------------------- | ------ |
| `id`         | The unique identifier of the issue.            | `text` |
| `key`        | The issue key (e.g., PROJ-123).                | `text` |
| `summary`    | The summary/title of the issue.                | `text` |
| `status`     | The current status of the issue.               | `text` |
| `issue_type` | The type of the issue (e.g., Bug, Story, Task).| `text` |
| `priority`   | The priority level of the issue.               | `text` |
| `assignee`   | The display name of the assignee.              | `text` |
| `created`    | The creation date of the issue.                | `text` |
| `updated`    | The last updated date of the issue.            | `text` |
