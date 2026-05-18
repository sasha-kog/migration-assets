---
title: Open Weather
updated: 2026-03-31T14:46
git_hash: 657221afc6f2de5181944b7812cdd082df229f28
description: Overview of the Open Weather integration.
icon: cloud-sun
---

# Open Weather

{% hint style="info" %}
The following documentation is for **Open Weather v1.6.2**.
{% endhint %}

## Overview

OpenWeather provides comprehensive weather data and forecasting services through robust APIs. This integration enables real-time weather information retrieval, forecast data access, and weather-based automation triggers. Incorporate weather intelligence into your decision-making and operational workflows.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Open Weather**

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

Add a name for the connection. You'll be prompted for [**authentication**](openweather.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using API Key

Authenticate to Open Weather API using the specified API key.

| Label   | Description                           | Type        |
| ------- | ------------------------------------- | ----------- |
| API Key | The API key to be used for connecting | `sensitive` |

## Actions

The following actions are available in the **Open Weather** integration:

### 1. Get the current temperature at a city

Get the current temperature for a specified city.
