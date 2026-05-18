---
title: OpenSearch
updated: 2026-02-06T18:35
git_hash: dd9c81379eb3b70a8b2fa540b62373ead10bf10f
description: Overview of the OpenSearch integration.
icon: magnifying-glass
---

# OpenSearch

{% hint style="info" %}
The following documentation is for **OpenSearch v2.0.1**.
{% endhint %}

## Overview

OpenSearch is a distributed, open-source search and analytics suite used for a broad set of use cases like real-time application monitoring, log analytics, and website search. This integration enables automated index management, document indexing, search operations, and data analytics workflows. Leverage powerful search capabilities and streamline data discovery processes.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **OpenSearch**

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

Add a name for the connection. You'll be prompted for [**authentication**](opensearch.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Hosts, Username and Password

Connect via http credentials

| Label    | Description                | Type        |
| -------- | -------------------------- | ----------- |
| Hosts    | comma-separated hosts      | `text`      |
| Username | the username for http auth | `text`      |
| Password | The password for http auth | `sensitive` |

## Actions

The following actions are available in the **OpenSearch** integration:

### 1. Create a document in opensearch

Create a document in opensearch

### 2. Delete a document from opensearch

Delete a document from opensearch

### 3. Get a document from opensearch

Get a document from opensearch by its ID

### 4. Query some documents from opensearch

Query documents from Opensearch

### 5. Update a document in opensearch

Update a document in opensearch

## Concepts

### Opensearch document

Represents an Document in Opensearch.

| Field Name   | Description                                    | Type   |
| ------------ | ---------------------------------------------- | ------ |
| `id`         | The ID of the document.                        | `text` |
| `index_name` | The name of the index the document belongs to. | `text` |
| `source`     | The document values.                           | `json` |
