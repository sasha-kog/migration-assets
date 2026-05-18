---
title: Zendesk
updated: 2026-03-20T14:12
git_hash: c9a768b429ffd5d31f8293ed8100178f1e087608
description: Overview of the Zendesk integration.
icon: headset
---

# Zendesk

{% hint style="info" %}
The following documentation is for **Zendesk v3.3.0**.
{% endhint %}

## Overview

Zendesk integration that enables users to create, update, delete, and get tickets in Zendesk. This integration provides comprehensive ticket management capabilities including creating tickets with custom properties, updating ticket status and priority, deleting tickets, and retrieving tickets through search or direct ID lookup. It also supports comment management with optional file attachments and includes user search functionality for accessing Zendesk user information.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Zendesk**

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

Add a name for the connection. You'll be prompted for [**authentication**](zendesk.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using subdomain, email and token

Connects to Zendesk using email and API token authentication.

| Label     | Description                                     | Type   |
| --------- | ----------------------------------------------- | ------ |
| subdomain | The subdomain of your Zendesk account.          | `text` |
| email     | The email associated with your Zendesk account. | `text` |
| token     | The API token from Zendesk for authentication.  | `text` |

## Actions

The following actions are available in the **Zendesk** integration:

### 1. Add a comment to a ticket

Adds a comment to an existing ticket in Zendesk with an optional single file attachment.

### 2. Create a ticket in zendesk

Creates a new ticket in Zendesk with the specified properties.

### 3. Delete a ticket in zendesk

Deletes a specified ticket in Zendesk.

### 4. Download an attachment

Downloads an attachment from Zendesk.

### 5. Get a ticket in zendesk

Retrieves a specific ticket from Zendesk by its ID using direct API access.

### 6. Get a user in zendesk

Retrieves a specific user from Zendesk by their ID.

### 7. Get some ticket's audits in zendesk

Retrieves all audits for a specific ticket in Zendesk.

### 8. Get some ticket's comments in zendesk

Retrieves all comments for a specific ticket in Zendesk.

### 9. Get some users in zendesk

Retrieves users from Zendesk using search functionality with optional filter expressions.

### 10. Get ticket fields in zendesk

Retrieves all available ticket field definitions from Zendesk.

### 11. Search some tickets in zendesk

Retrieves tickets from Zendesk using search functionality with optional filter expressions.

### 12. Update a ticket in zendesk

Updates a specific ticket in Zendesk with the provided information.

## Concepts

### Zendesk ticket

A ticket in Zendesk.

| Field Name                   | Description                                                       | Type                     |
| ---------------------------- | ----------------------------------------------------------------- | ------------------------ |
| `id`                         | The ID of the ticket.                                             | `optional[number]`       |
| [`assignee`](#zendesk-user)  | The assignee of the ticket.                                       | `optional[zendesk user]` |
| `created_at`                 | The creation date of the ticket.                                  | `optional[datetime]`     |
| `custom_fields`              | List of custom fields as dictionaries with 'id' and 'value' keys. | `optional[list of json]` |
| `description`                | The description of the ticket.                                    | `optional[text]`         |
| `due_at`                     | The due date of the ticket.                                       | `optional[datetime]`     |
| `priority`                   | The priority of the ticket.                                       | `optional[text]`         |
| `requester_id`               | The ID of the requester.                                          | `optional[number]`       |
| [`submitter`](#zendesk-user) | The submitter of the ticket.                                      | `optional[zendesk user]` |
| `status`                     | The status of the ticket.                                         | `optional[text]`         |
| `subject`                    | The subject of the ticket.                                        | `optional[text]`         |
| `tags`                       | The tags of the ticket.                                           | `optional[list of text]` |
| `type`                       | The type of the ticket.                                           | `optional[text]`         |
| `url`                        | The URL of the ticket.                                            | `optional[text]`         |

### Zendesk user

A user in Zendesk.

| Field Name | Description            | Type               |
| ---------- | ---------------------- | ------------------ |
| `id`       | The ID of the user.    | `optional[number]` |
| `email`    | The email of the user. | `optional[text]`   |
| `name`     | The name of the user.  | `optional[text]`   |

### Zendesk comment

A comment in Zendesk.

| Field Name                           | Description                                                       | Type                                   |
| ------------------------------------ | ----------------------------------------------------------------- | -------------------------------------- |
| `id`                                 | The ID of the comment.                                            | `optional[number]`                     |
| `body`                               | The content/text of the comment.                                  | `optional[text]`                       |
| [`author`](#zendesk-user)            | The user who created the comment.                                 | `optional[zendesk user]`               |
| `created_at`                         | When the comment was created.                                     | `optional[datetime]`                   |
| `public`                             | Whether the comment is public (true) or an internal note (false). | `optional[boolean]`                    |
| `type`                               | The type of comment (Comment, VoiceComment, etc.).                | `optional[text]`                       |
| [`attachments`](#zendesk-attachment) | List of ZendeskAttachment objects.                                | `optional[list of zendesk attachment]` |

### Zendesk attachment

An attachment in Zendesk.

| Field Name     | Description                                 | Type               |
| -------------- | ------------------------------------------- | ------------------ |
| `id`           | The ID of the attachment.                   | `optional[number]` |
| `file_name`    | The name of the file.                       | `optional[text]`   |
| `content_url`  | The URL to download the attachment content. | `optional[text]`   |
| `content_type` | The MIME type of the attachment.            | `optional[text]`   |
| `size`         | The size of the attachment in bytes.        | `optional[number]` |

### Zendesk audit

An audit record for a ticket in Zendesk.

| Field Name   | Description                                             | Type                             |
| ------------ | ------------------------------------------------------- | -------------------------------- |
| `id`         | The ID of the audit.                                    | `optional[number]`               |
| `ticket_id`  | The ID of the ticket this audit belongs to.             | `optional[number]`               |
| `created_at` | When the audit was created.                             | `optional[datetime]`             |
| `author_id`  | The ID of the user who performed the action.            | `optional[number]`               |
| `metadata`   | Additional metadata about the audit.                    | `optional[json]`                 |
| `events`     | List of events in this audit (changes, comments, etc.). | `optional[list of list of any?]` |

### Zendesk ticket field

A custom field definition for Zendesk tickets.

| Field Name    | Description                                                       | Type             |
| ------------- | ----------------------------------------------------------------- | ---------------- |
| `id`          | The ID of the ticket field.                                       | `number`         |
| `title`       | The human-readable title of the field.                            | `optional[text]` |
| `type`        | The type of the field (text, textarea, checkbox, dropdown, etc.). | `optional[text]` |
| `description` | The description of the field.                                     | `optional[text]` |
| `value`       | The actual value for this field on a specific ticket.             | `optional[any?]` |
