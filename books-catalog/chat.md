---
title: Google Chat
updated: 2026-04-15T14:56
git_hash: 83523946c92acbf8b6e138bb8ab83a63560ec6ca
description: Overview of the Google Chat integration.
icon: google
---

# Google Chat

{% hint style="info" %}
The following documentation is for **Google Chat v2.2.0**.
{% endhint %}

## Overview

Google Chat provides messaging and collaboration inside Google Workspace. This integration lets you list spaces, read and send messages, reply in threads, manage reactions, and check read state information.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Google Chat**

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

Add a name for the connection. You'll be prompted for [**authentication**](chat.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use Google OAuth to connect this integration in Kognitos.

{% hint style="info" %}
If your organization uses its own Google OAuth app, follow [Google Authentication](google-authentication.md). You can reuse the same Client ID and Client Secret for Gmail, Google Calendar, Google Chat, Google Docs, Google Drive, and Google Sheets.
{% endhint %}

### Continue with Google

To connect to the **Google Chat** integration, choose **OAuth Authorization Code**, enter your Google OAuth client details if prompted, and continue with Google sign-in to authorize the connection.

## Actions

The following actions are available in the **Google Chat** integration:

### 1. Add a reaction to a chat message

Add a reaction to a Google Chat message.

### 2. Create a direct message space

Create a direct message space in Google Chat.

### 3. Find a direct message space

Find an existing direct message space in Google Chat.

### 4. Get a chat message

Retrieve a specific Google Chat message.

### 5. Get a chat space

Retrieve a specific Google Chat space.

### 6. Get a chat space's read state

Retrieve read state information for a Google Chat space.

### 7. Get chat members from a space

Retrieve members from a Google Chat space.

### 8. Get chat messages from a space

Retrieve messages from a Google Chat space.

### 9. Get reactions from a chat message

Retrieve reactions for a Google Chat message.

### 10. Get chat spaces

Retrieve Google Chat spaces.

### 11. Get thread messages from a chat message

Retrieve replies in a Google Chat thread.

### 12. Send a thread reply

Send a reply in a Google Chat thread.

### 13. Send a chat message

Send a message in Google Chat.

### 14. Update a chat message

Update an existing Google Chat message.
