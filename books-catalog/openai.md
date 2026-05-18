---
title: OpenAI
description: Overview of the OpenAI integration.
icon: grid-2
updated: 2026-03-20T14:12
git_hash: aeda732800547d0bcaa500dfee10e4ad2534a677
---

{% hint style="info" %}
The following documentation is for **OpenAI v1.1.4**.
{% endhint %}

# Overview

This integration connects to OpenAI's GPT models, enabling you to leverage advanced AI capabilities for text generation, analysis, and intelligent automation workflows.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **OpenAI**


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

#### 1. OpenAI API Key

Follow these steps to obtain your OpenAI API key:

{% stepper %}
{% step %}
#### Log In to OpenAI

Navigate to the [**OpenAI Platform**](https://auth.openai.com/log-in) and log in with your credentials.
{% endstep %}

{% step %}
#### API Keys

Open **Account Settings**, then navigate to [**API Keys**](https://platform.openai.com/account/api-keys)**.**&#x20;
{% endstep %}

{% step %}
#### Generate a New API Key

Click **Create new secret key**. Copy the key immediately — it will only be shown once.
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

The following actions are available in the **OpenAI** integration:

### 1. Prompt openai

Send a prompt to the OpenAI LLM and get a response.
