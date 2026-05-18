---
title: Confluence
updated: 2026-03-20T14:12
git_hash: 013edb71dca2660c8e68413286ed48acf984c803
description: Overview of the Confluence integration.
icon: confluence
---

# Confluence

{% hint style="info" %}
The following documentation is for **Confluence v1.2.0**.
{% endhint %}

## Overview

Connect to Atlassian Confluence to retrieve and publish content in your team’s collaborative space

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Confluence**

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

Add a name for the connection. You'll be prompted for [**authentication**](confluence.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Email, Domain and Token

Connects to an API using the provided email and Atlassian token.

| Label  | Description                                | Type        |
| ------ | ------------------------------------------ | ----------- |
| Email  | The email address for authentication       | `text`      |
| Domain | The domain of the Atlassian account        | `text`      |
| Token  | The Atlassian API token for authentication | `sensitive` |

## Actions

The following actions are available in the **Confluence** integration:

### 1. Create a page in a space

Creates a page in Confluence

### 2. Retrieve some pages from confluence

Retrieves pages from Confluence

### 3. Retrieve some spaces from confluence

Retrieves spaces from Confluence

## Concepts

### Confluence space

A Space in Confluence

| Field Name | Description                        | Type   |
| ---------- | ---------------------------------- | ------ |
| `id`       | The unique identifier of the space | `text` |
| `name`     | The name of the space              | `text` |

### Confluence page

A Page in Confluence

| Field Name | Description                       | Type   |
| ---------- | --------------------------------- | ------ |
| `id`       | The unique identifier of the page | `text` |
| `title`    | The title of the page             | `text` |
| `content`  | The content of the page           | `text` |
