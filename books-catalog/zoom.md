---
title: Zoom
updated: 2026-04-15T14:56
git_hash: 6a9746ea1bd5933ba89c5941c235473f3c3730ae
description: Overview of the Zoom integration.
icon: video
---

# Zoom

{% hint style="info" %}
The following documentation is for **Zoom v1.0.1**.
{% endhint %}

## Overview

Zoom is a video communications platform for meetings, webinars, and team collaboration. This integration lets you create and manage meetings, list users, access recordings, and work with webinars from Kognitos.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Zoom**

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

Add a name for the connection. You'll be prompted for [**authentication**](zoom.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos.

### OAuth Authorization Code

Connect to Zoom with your own OAuth client.

| Label | Description | Type |
| --- | --- | --- |
| Client ID | OAuth client identifier | `text` |
| Client Secret | OAuth client secret | `sensitive` |

### Server-to-Server OAuth

Connect to Zoom using Server-to-Server OAuth credentials.

| Label | Description | Type |
| --- | --- | --- |
| Account ID | The Zoom Account ID, found on the Server-to-Server OAuth app page under **App Credentials**. | `text` |
| Client ID | The Client ID of your Server-to-Server OAuth app, found under **App Credentials**. | `text` |
| Client Secret | The Client Secret of your Server-to-Server OAuth app, found under **App Credentials**. | `sensitive` |

## Actions

The following actions are available in the **Zoom** integration:

### 1. Create a meeting

Create a Zoom meeting.

### 2. Create a webinar

Create a Zoom webinar.

### 3. Delete a meeting

Delete a Zoom meeting.

### 4. Delete a webinar

Delete a Zoom webinar.

### 5. End a meeting

End an active Zoom meeting.

### 6. Get the current user

Retrieve the current Zoom user.

### 7. Get a meeting

Retrieve a Zoom meeting.

### 8. Get meeting participants

Retrieve participants for a Zoom meeting.

### 9. Get meeting recordings

Retrieve recordings for a Zoom meeting.

### 10. Get meetings

Retrieve Zoom meetings.

### 11. Get recordings

Retrieve Zoom cloud recordings.

### 12. Get users

Retrieve Zoom users.

### 13. Get a webinar

Retrieve a Zoom webinar.

### 14. Get webinars

Retrieve Zoom webinars.

### 15. Update a meeting

Update an existing Zoom meeting.
