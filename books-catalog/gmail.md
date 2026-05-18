---
title: Gmail
updated: 2026-03-20T14:12
git_hash: f71952747a136684c5925223e41b7705dd2b3c2f
description: Overview of the Gmail integration.
icon: google
---

# Gmail

{% hint style="info" %}
The following documentation is for **Gmail v2.2.0**.
{% endhint %}

## Overview

Gmail is Google's comprehensive email service providing powerful messaging, organization, and collaboration features. This integration enables automated email sending, inbox management, message filtering, and email workflow automation. Streamline communication processes and enhance productivity through intelligent email automation.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Gmail**

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

Add a name for the connection. You'll be prompted for [**authentication**](gmail.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use Google OAuth to connect this integration in Kognitos.

{% hint style="info" %}
If your organization uses its own Google OAuth app, follow [Google Authentication](google-authentication.md). You can reuse the same Client ID and Client Secret for Gmail, Google Calendar, Google Chat, Google Docs, Google Drive, and Google Sheets.
{% endhint %}

### Continue with Google

To connect to the **Gmail** integration, click on <kbd>Continue with Google</kbd>. This redirects you to Google's secure authentication page, where you can sign in with your Google account and authorize the application. Once connected, Kognitos can access your Gmail account without storing your Google credentials directly.

## Actions

The following actions are available in the **Gmail** integration:

### 1. Add a label to an email

Add a label to one or more emails.

### 2. Download an email's attachments

Get an email attachment as an IO object.

### 3. Forward an email

Forward an email to new recipients.

### 4. Get some label's emails

Get emails from a specified label in Gmail.

### 5. List labels

Get all labels from the user's Gmail account.

### 6. Remove a label from an email

Remove a label from one or more emails.

### 7. Reply an email

Reply to an email.

### 8. Send an email

Send an email using Gmail API.

## Concepts

### Gmail email

A Gmail Email represents an email message in Gmail.

| Field Name                                           | Description                                                | Type                                           |
| ---------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------- |
| `id`                                                 | The unique identifier for the email.                       | `text`                                         |
| `thread_id`                                          | The unique identifier for the thread containing the email. | `text`                                         |
| [`labels`](gmail.md#list-of-text)                    | The list of labels applied to the email.                   | `list of text`                                 |
| `state`                                              | The state of the email (draft, unread, or read).           | `text`                                         |
| `sender`                                             | The sender of the email.                                   | `text`                                         |
| [`recipients`](gmail.md#list-of-text)                | The recipients of the email.                               | `list of text`                                 |
| `message_id`                                         | The unique identifier for the message.                     | `optional[text]`                               |
| `cc_recipients`                                      | The cc recipients of the email.                            | `optional[list of text]`                       |
| `bcc_recipients`                                     | The bcc recipients of the email.                           | `optional[list of text]`                       |
| [`attachments`](gmail.md#gmail-attachment-reference) | The attachments of the email.                              | `optional[list of gmail attachment reference]` |
| `subject`                                            | The subject of the email.                                  | `optional[text]`                               |
| `plain_body`                                         | The plain text body of the email.                          | `optional[text]`                               |
| `html_body`                                          | The html body of the email.                                | `optional[text]`                               |
| `sent_date_time`                                     | The date and time the email was sent.                      | `optional[datetime]`                           |
| `received_date_time`                                 | The date and time the email was received.                  | `optional[datetime]`                           |

### Gmail attachment reference

A Gmail Attachment Reference represents a reference to a file attached to an email in Gmail.

| Field Name  | Description                               | Type     |
| ----------- | ----------------------------------------- | -------- |
| `id`        | The unique identifier for the attachment. | `text`   |
| `email_id`  | The unique identifier for the email.      | `text`   |
| `file_name` | The name of the attachment.               | `text`   |
| `file_size` | The size of the file in bytes.            | `number` |

### Gmail attachment

A Gmail Attachment represents a file with name.

| Field Name  | Description                    | Type   |
| ----------- | ------------------------------ | ------ |
| `file_name` | The name of the attachment.    | `text` |
| `content`   | The content of the attachment. | `file` |
