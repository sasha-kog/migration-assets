---
title: Slack
updated: 2026-03-31T14:46
git_hash: da3e95ec5a95c55749b48cf8b0a54c18eacb2baa
description: Overview of the Slack integration.
icon: slack
---

# Slack

{% hint style="info" %}
The following documentation is for **Slack v2.1.1**.
{% endhint %}

## Overview

The Slack integration allows users to retrieve information about Users and Channels and send messages to them.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Slack**

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

Add a name for the connection. You'll be prompted for [**authentication**](slack.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Token

Connect to an API using the provided API key.

| Label | Description                    | Type        |
| ----- | ------------------------------ | ----------- |
| Token | The Slack Bot User OAuth Token | `sensitive` |

## Actions

The following actions are available in the **Slack** integration:

### 1. List channels from slack

List all channels from Slack.

### 2. List users from slack

List all users from Slack.

### 3. Read the item's messages

Read messages from a channel.

### 4. Retrieve a channel from slack

Retrieve a channel from Slack.

### 5. Retrieve a user from slack

Retrieve a user from Slack.

### 6. Send message to an item

Send a message to a channel or user.

## Concepts

### Slack channel

Represents a reference to a channel in Slack.

| Field Name     | Description              | Type   |
| -------------- | ------------------------ | ------ |
| `channel_id`   | The ID of the channel.   | `text` |
| `channel_name` | The name of the channel. | `text` |

### Slack user

Represents a reference to a channel in Slack.

| Field Name   | Description                                         | Type             |
| ------------ | --------------------------------------------------- | ---------------- |
| `user_id`    | The ID of the user.                                 | `text`           |
| `user_name`  | The name of the user.                               | `text`           |
| `channel_id` | The ID of the IM channel with the current user/bot. | `optional[text]` |

### Slack message

Represents a reference to a message in the Slack

| Field Name  | Description                   | Type     |
| ----------- | ----------------------------- | -------- |
| `text`      | The message.                  | `text`   |
| `timestamp` | The timestamp of the message. | `number` |
| `meta`      | Metadata of the message       | `json`   |

### Slack action block

Represents an action block in Slack.

| Field Name | Description                 | Type                                                                                                                                                                                                                           |
| ---------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `block_id` | The ID of the block.        | `optional[text]`                                                                                                                                                                                                               |
| `elements` | The elements of the action. | `optional[list of list of slack button element` or `slack checkbox element` or `slack date picker element` or `slack image element` or `slack markdown element?` or `slack overflow element` or `slack static select element]` |

### Slack button element

Represents a button element in Slack.

| Field Name | Description                           | Type             |
| ---------- | ------------------------------------- | ---------------- |
| `action_id` | The ID of the button.                | `text`           |
| `text`      | The text of the button.              | `text`           |
| `confirm`   | The confirmation dialog for the button. | `optional[text]` |

### Slack static select element

Represents a static select element in Slack.

| Field Name    | Description                               | Type           |
| ------------- | ----------------------------------------- | -------------- |
| `action_id`   | The ID of the select element.             | `text`         |
| `placeholder` | The placeholder text for the select element. | `text`      |
| `options`     | The options for the select element.       | `list of text` |

### Slack date picker element

Represents a date picker element in Slack.

| Field Name    | Description                             | Type   |
| ------------- | --------------------------------------- | ------ |
| `action_id`   | The ID of the date picker.              | `text` |
| `placeholder` | The placeholder text for the date picker. | `text` |

### Slack overflow element

Represents an overflow element in Slack.

| Field Name  | Description                        | Type           |
| ----------- | ---------------------------------- | -------------- |
| `action_id` | The ID of the overflow element.    | `text`         |
| `options`   | The options for the overflow element. | `list of text` |

### Slack checkbox element

Represents a checkbox element in Slack.

| Field Name  | Description                        | Type           |
| ----------- | ---------------------------------- | -------------- |
| `action_id` | The ID of the checkbox element.    | `text`         |
| `options`   | The options for the checkbox element. | `list of text` |

### Slack image element

Represents an image element in Slack.

| Field Name  | Description                 | Type   |
| ----------- | --------------------------- | ------ |
| `image_url` | The URL of the image.       | `text` |
| `alt_text`  | The alt text of the image.  | `text` |

### Slack markdown element

Represents a markdown element in Slack.

| Field Name | Description                  | Type   |
| ---------- | ---------------------------- | ------ |
| `text`     | The text of the markdown element. | `text` |

### Slack context block

Represents a context block in Slack.

| Field Name | Description                        | Type                                                                                                                                                                                                                           |
| ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `block_id` | The ID of the block.               | `optional[text]`                                                                                                                                                                                                               |
| `elements` | The elements of the context block. | `optional[list of list of slack button element` or `slack checkbox element` or `slack date picker element` or `slack image element` or `slack markdown element?` or `slack overflow element` or `slack static select element]` |

### Slack divider block

Represents a divider block in Slack.

| Field Name | Description          | Type             |
| ---------- | -------------------- | ---------------- |
| `block_id` | The ID of the block. | `optional[text]` |

### Slack header block

Represents a header block in Slack.

| Field Name | Description             | Type             |
| ---------- | ----------------------- | ---------------- |
| `text`     | The text of the header. | `text`           |
| `block_id` | The ID of the block.    | `optional[text]` |

### Slack image block

Represents an image block in Slack.

| Field Name  | Description                 | Type             |
| ----------- | --------------------------- | ---------------- |
| `image_url` | The URL of the image.       | `text`           |
| `alt_text`  | The alt text for the image. | `text`           |
| `block_id`  | The ID of the block.        | `optional[text]` |

### Slack markdown block

Represents a markdown block in Slack.

| Field Name | Description                     | Type             |
| ---------- | ------------------------------- | ---------------- |
| `text`     | The text of the markdown block. | `text`           |
| `block_id` | The ID of the block.            | `optional[text]` |

### Slack section block

Represents a section block in Slack.

| Field Name  | Description                   | Type                                                                                                                                                                                                           |
| ----------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `text`      | The text of the section.      | `optional[text]`                                                                                                                                                                                               |
| `fields`    | The fields of the section.    | `optional[slack markdown element?` or `text]`                                                                                                                                                                  |
| `accessory` | The accessory of the section. | `optional[slack button element` or `slack checkbox element` or `slack date picker element` or `slack image element` or `slack markdown element?` or `slack overflow element` or `slack static select element]` |
| `block_id`  | The ID of the block.          | `optional[text]`                                                                                                                                                                                               |

### Slack attachment

Represents a reference to an attachment in the Slack

| Field Name  | Description                 | Type   |
| ----------- | --------------------------- | ------ |
| `file_name` | The name of the attachment. | `text` |
| `data`      | The File object             | `file` |
