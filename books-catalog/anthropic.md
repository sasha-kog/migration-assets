---
title: Anthropic
description: Overview of the Anthropic integration.
icon: grid-2
updated: 2026-03-20T14:12
git_hash: aeda732800547d0bcaa500dfee10e4ad2534a677
---

{% hint style="info" %}
The following documentation is for **Anthropic v1.1.4**.
{% endhint %}

# Overview

This integration provides LLM functionality by connecting to the Anthropic API, enabling you to send prompts and receive AI-generated responses for natural language processing workflows.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Anthropic**


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

Add a name for the connection. You'll be prompted for [**authentication**](#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

### Credentials

#### 1. Anthropic API Key

Follow these steps to obtain your Anthropic API key:

{% stepper %}
{% step %}
#### Log in to the Anthropic Console

Go to the [**Anthropic Console**](https://console.anthropic.com) and log in with your credentials.
{% endstep %}

{% step %}
#### Navigate to API Keys

Go to **Settings** > **API Keys**. Then click **+ Create Key** in the top right.
{% endstep %}

{% step %}
#### Configuration

Select a workspace and give your key a descriptive name (e.g., "Development Key" or "Production App"). Then, click **Add** to generate your API key.
{% endstep %}

{% step %}
#### Copy and Store Your Key

Copy your API key immediately and store it securely. You won't be able to view it again after closing the dialog.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using API Key

Connect using an API key.

| Label   | Description                     | Type        |
| ------- | ------------------------------- | ----------- |
| API Key | The API key for authentication. | `sensitive` |


## Actions

The following actions are available in the **Anthropic** integration:

### 1. Prompt anthropic

Send a prompt to the Anthropic Claude LLM and get a response.
