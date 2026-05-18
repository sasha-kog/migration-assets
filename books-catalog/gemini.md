---
title: Gemini
updated: 2026-03-20T14:12
git_hash: 600024e21f436f744dcbd7a2b6989d3a521ccd9b
description: Overview of the Gemini integration.
icon: grid-2
---

# Gemini

{% hint style="info" %}
The following documentation is for **Gemini v1.1.4**.
{% endhint %}

## Overview

A Gemini integration for interacting with Google's Gemini models. This integration provides LLM functionality by connecting to the Google AI or Vertex AI API. It supports both API key authentication (Google AI) and service account authentication (Vertex AI).

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Gemini**

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

Add a name for the connection. You'll be prompted for [**authentication**](gemini.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using API Key

Connect using an API key.

| Label   | Description                     | Type        |
| ------- | ------------------------------- | ----------- |
| API Key | The API key for authentication. | `sensitive` |

### Connect using Service Account JSON and Location

Connect to Gemini using a Google Cloud service account (Vertex AI).

| Label                | Description                                      | Type        |
| -------------------- | ------------------------------------------------ | ----------- |
| Service Account JSON | The complete service account JSON.               | `sensitive` |
| Location             | The Google Cloud location (e.g., 'us-central1'). | `text`      |

## Actions

The following actions are available in the **Gemini** integration:

### 1. Prompt gemini

Send a prompt to the Gemini LLM and get a response.
