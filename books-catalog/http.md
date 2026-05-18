---
title: HTTP
updated: 2026-02-06T18:35
git_hash: b2e0063ff35ab0b63f3ba76c2534fbf21d9d79bc
description: Overview of the HTTP integration.
icon: globe
---

# HTTP

{% hint style="info" %}
The following documentation is for **HTTP v1.8.0**.
{% endhint %}

## Overview

HTTP integration provides fundamental web communication capabilities for API interactions and web service calls. This integration supports GET, POST, PUT, DELETE, and other HTTP methods for seamless API integration. Enable your workflows to communicate with any REST API or web service.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **HTTP**

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

Add a name for the connection. You'll be prompted for [**authentication**](http.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using API Key

Connect to the HTTP server using an API key. The API key will be sent as a x-api-key header in every request.

| Label   | Description        | Type        |
| ------- | ------------------ | ----------- |
| API Key | The API key value. | `sensitive` |

### Connect using Username and Password

Connect to the HTTP server using basic authentication. Note: If connect is set, "Authorization" header will be added automatically to the request and manually set "Authorization" header will be ignored.

| Label    | Description                            | Type        |
| -------- | -------------------------------------- | ----------- |
| Username | The username for basic authentication. | `text`      |
| Password | The password for basic authentication. | `sensitive` |

### Connect using Token URL, Client ID and Client Secret

Connect to the HTTP server using client credentials method. Note: If connect is set, "Authorization" header will be added automatically to the request and manually set "Authorization" header will be ignored.

| Label         | Description                               | Type        |
| ------------- | ----------------------------------------- | ----------- |
| Token URL     | The token URL for client credentials.     | `text`      |
| Client ID     | The client ID for client credentials.     | `text`      |
| Client Secret | The client secret for client credentials. | `sensitive` |

### Connect using Username and Password

Connect to the HTTP server using digest authentication. Note: If connect is set, "Authorization" header will be added automatically to the request and manually set "Authorization" header will be ignored.

| Label    | Description                             | Type        |
| -------- | --------------------------------------- | ----------- |
| Username | The username for digest authentication. | `text`      |
| Password | The password for digest authentication. | `sensitive` |

### Connect using Token URL, Username, Password, Client ID and Client Secret

Connect to the HTTP server using password grant method. Note: If connect is set, "Authorization" header will be added automatically to the request and manually set "Authorization" header will be ignored.

| Label         | Description                           | Type        |
| ------------- | ------------------------------------- | ----------- |
| Token URL     | The token URL for password grant.     | `text`      |
| Username      | The username for password grant.      | `text`      |
| Password      | The password for password grant.      | `sensitive` |
| Client ID     | The client ID for password grant.     | `text`      |
| Client Secret | The client secret for password grant. | `sensitive` |

## Actions

The following actions are available in the **HTTP** integration:

### 1. Delete a url

Make a DELETE request to the specified url.

### 2. Head a url

Make a HEAD request to the specified url.

### 3. Patch payload on a url

Make a PATCH request to the specified url.

### 4. Post payload to a url

Make a POST request to the specified url.

### 5. Put payload on a url

Make a PUT request to the specified url.

### 6. Retrieve a url

Make a GET request to the specified url.
