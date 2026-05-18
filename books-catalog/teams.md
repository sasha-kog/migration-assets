---
title: Teams
updated: 2026-03-20T14:12
git_hash: ab47ecf822fbbe886b79fda31fd83fa5ef1f5997
description: Overview of the Teams integration.
icon: microsoft
---

# Teams

{% hint style="info" %}
The following documentation is for **Teams v2.6.0**.
{% endhint %}

## Overview

Enables interacting with and managing Microsoft Teams workspaces, channels, and communications via the Microsoft Graph API. Teams provides a collaborative platform for team communication, file sharing, and integrated applications. Ideal for businesses and developers seeking efficient team collaboration, virtual meetings, and workspace organization. This integration ensures secure and seamless access to these collaboration services.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Teams**

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

Add a name for the connection. You'll be prompted for [**authentication**](teams.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Actions

The following actions are available in the **Teams** integration:

### 1. Add a member to a channel

Adds a member to a Teams channel.

### 2. Create a channel in a team

Creates a new channel in a Microsoft Team.

### 3. Get some channels from a team

Retrieves channels within a Microsoft Team.

### 4. Get some messages from a channel

Retrieves messages from a Teams channel.

### 5. Get some teams from teams

Retrieves Microsoft Teams accessible via the Microsoft Graph API.

### 6. Send a message to a channel

Sends a message to a Teams channel.

### 7. Send a message to a user

Sends a direct message to a user via Teams chat.

## Concepts

### Teams channel

A Teams Channel represents a channel in Microsoft Teams. It includes key details such as display name,description, and membership type.

| Field Name        | Description                                                         | Type                                         |
| ----------------- | ------------------------------------------------------------------- | -------------------------------------------- |
| `display_name`    | The name displayed for the channel.                                 | `text`                                       |
| `description`     | The description of the channel.                                     | `optional[text]`                             |
| `membership_type` | The type of membership for the channel (standard, private, shared). | `optional[enum[private, shared, standard]?]` |
| `team_id`         | The ID of the team that contains this channel.                      | `optional[text]`                             |
| `id`              | The unique identifier for the channel (optional for creation).      | `optional[text]`                             |
| `web_url`         | The web URL for the channel.                                        | `optional[text]`                             |

### Office user

An Office User represents a user in the Microsoft Graph. It includes key user details such as display name,email address, and job title.

| Field Name      | Description                                                   | Type             |
| --------------- | ------------------------------------------------------------- | ---------------- |
| `id`            | The unique identifier for the user.                           | `text`           |
| `display_name`  | The name displayed in the address book for the user.          | `optional[text]` |
| `email_address` | The user's email address (usually their user principal name). | `optional[text]` |
| `job_title`     | The user's job title.                                         | `optional[text]` |

### Teams team

A Teams Team represents a team in Microsoft Teams. It includes key details such as display name,description, and visibility settings.

| Field Name     | Description                                   | Type             |
| -------------- | --------------------------------------------- | ---------------- |
| `id`           | The unique identifier for the team.           | `text`           |
| `display_name` | The name displayed for the team.              | `optional[text]` |
| `description`  | The description of the team.                  | `optional[text]` |
| `visibility`   | The visibility of the team (private, public). | `optional[text]` |
| `web_url`      | The web URL for the team.                     | `optional[text]` |

### Teams message

A Teams Message represents a message in a Microsoft Teams channel or chat. It includes key details such as content,sender, and creation time.

| Field Name               | Description                                                              | Type             |
| ------------------------ | ------------------------------------------------------------------------ | ---------------- |
| `id`                     | The unique identifier for the message.                                   | `text`           |
| `content`                | The content of the message.                                              | `optional[text]` |
| `created_datetime`       | The datetime when the message was created.                               | `optional[text]` |
| `last_modified_datetime` | The datetime when the message was last modified.                         | `optional[text]` |
| `from_user`              | The user who sent the message.                                           | `optional[text]` |
| `channel_id`             | The ID of the channel where the message was sent (for channel messages). | `optional[text]` |
| `team_id`                | The ID of the team that contains the channel (for channel messages).     | `optional[text]` |
| `chat_id`                | The ID of the chat where the message was sent (for chat messages).       | `optional[text]` |
| `web_url`                | The web URL for the message.                                             | `optional[text]` |
