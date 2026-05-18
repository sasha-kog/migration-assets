---
title: Google Docs
updated: 2026-03-20T14:12
git_hash: c6315027c750fa201441f805c497f198193e31d6
description: Overview of the Google Docs integration.
icon: google
---

# Google Docs

{% hint style="info" %}
The following documentation is for **Google Docs v2.2.0**.
{% endhint %}

## Overview

Google Docs provides collaborative document creation and editing with real-time synchronization across teams. This integration enables automated document generation, content management, and collaborative writing workflows. Enhance documentation processes and improve team collaboration on shared documents.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Google Docs**

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

Add a name for the connection. You'll be prompted for [**authentication**](googledocs.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos.

{% hint style="info" %}
If you want to connect Google Docs with OAuth, follow [Google Authentication](google-authentication.md). You can reuse the same Client ID and Client Secret for Gmail, Google Calendar, Google Chat, Google Docs, Google Drive, and Google Sheets.
{% endhint %}

{% hint style="info" %}
If you want to connect Google Docs with a service account, follow [Google Service Account Authentication](google-service-account-authentication.md). You can reuse the same service account for Google Docs, Google Drive, and Google Sheets.
{% endhint %}

### Connect using Client Email, Token URI and Private Key

Gets the credentials from the service account keys.

| Label        | Description                                                                     | Type        |
| ------------ | ------------------------------------------------------------------------------- | ----------- |
| Client Email | The client email of the service account registered in the Google Cloud Console. | `text`      |
| Token URI    | The token URI of the Google Cloud Console.                                      | `text`      |
| Private Key  | The private key of the service account registered in the Google Cloud Console.  | `sensitive` |

### Continue with Google

To connect to the **Google Docs** integration, click on <kbd>Continue with Google</kbd>. This redirects you to Google's secure authentication page, where you can sign in with your Google account and authorize the application. Once connected, Kognitos can access your Google Docs without storing your Google credentials directly.

## Actions

The following actions are available in the **Google Docs** integration:

### 1. Add a paragraph to a document

Adds a new paragraph to the document.

### 2. Create a google document in a folder

Creates a new Google Docs document.

## Concepts

### Google drive file reference

Contains all information required to identify a file in Google Drive.

| Field Name                              | Description                   | Type           |
| --------------------------------------- | ----------------------------- | -------------- |
| `id`                                    | The id of the file            | `text`         |
| `file_name`                             | The name of the file          | `text`         |
| [`parents`](googledocs.md#list-of-text) | The ids of the parent folders | `list of text` |

### Google drive folder reference

Contains all information required to identify a folder in Google Drive.

| Field Name                              | Description                   | Type           |
| --------------------------------------- | ----------------------------- | -------------- |
| `id`                                    | The id of the folder          | `text`         |
| `folder_name`                           | The name of the folder        | `text`         |
| [`parents`](googledocs.md#list-of-text) | The ids of the parent folders | `list of text` |
