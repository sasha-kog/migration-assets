---
title: Google Calendar
updated: 2026-03-20T14:12
git_hash: c6315027c750fa201441f805c497f198193e31d6
description: Overview of the Google Calendar integration.
icon: google
---

# Google Calendar

{% hint style="info" %}
The following documentation is for **Google Calendar v2.2.0**.
{% endhint %}

## Overview

Google Calendar provides intelligent scheduling and calendar management with smart automation features. This integration enables automated event creation, scheduling workflows, and calendar synchronization processes. Improve time management and automate scheduling coordination across teams and organizations.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Google Calendar**

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

Add a name for the connection. You'll be prompted for [**authentication**](googlecalendar.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use Google OAuth to connect this integration in Kognitos.

{% hint style="info" %}
If your organization uses its own Google OAuth app, follow [Google Authentication](google-authentication.md). You can reuse the same Client ID and Client Secret for Gmail, Google Calendar, Google Chat, Google Docs, Google Drive, and Google Sheets.
{% endhint %}

### Continue with Google

To connect to the **Google Calendar** integration, click on <kbd>Continue with Google</kbd>. This redirects you to Google's secure authentication page, where you can sign in with your Google account and authorize the application. Once connected, Kognitos can access your Google Calendar without storing your Google credentials directly.

## Actions

The following actions are available in the **Google Calendar** integration:

### 1. Create an event

Create a new Google Calendar event.

### 2. Get some events

Get events from Google Calendar, optionally filtered by time range.

## Concepts

### Google calendar event

A Google Calendar event representation.

| Field Name            | Description                                                             | Type                     |
| --------------------- | ----------------------------------------------------------------------- | ------------------------ |
| `summary`             | The title/summary of the event                                          | `text`                   |
| `start`               | The start time of the event                                             | `datetime`               |
| `end`                 | The end time of the event                                               | `datetime`               |
| `id`                  | The unique identifier for the event (set by Google Calendar)            | `optional[text]`         |
| `description`         | Optional description of the event                                       | `optional[text]`         |
| `location`            | Optional location of the event                                          | `optional[text]`         |
| `attendees`           | Optional list of all invited email addresses                            | `optional[list of text]` |
| `confirmed_attendees` | Optional list of confirmed attendee email addresses                     | `optional[list of text]` |
| `potential_attendees` | Optional list of potential attendee email addresses (not yet confirmed) | `optional[list of text]` |
| `creator`             | Optional email of the event creator                                     | `optional[text]`         |
| `created`             | Optional creation timestamp                                             | `optional[datetime]`     |
| `updated`             | Optional last update timestamp                                          | `optional[datetime]`     |
| `status`              | Optional status of the event (confirmed, tentative, cancelled)          | `optional[text]`         |
| `html_link`           | Optional URL to the event in Google Calendar                            | `optional[text]`         |
