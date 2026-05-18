---
title: Browser Use
updated: 2026-03-20T14:12
git_hash: 732184d8924eaa8caa67fc7b9e99cf018742f1b5
description: Overview of the Browser Use integration.
icon: browser
---

# Browser Use

{% hint style="info" %}
The following documentation is for **Browser Use v3.0.0**.
{% endhint %}

## Overview

The **Browser Use** book enables you to perform **web automation** using natural language. Use plain English to describe a task, and a remote browser agent will execute it.

The browser agent can perform a range of web automation tasks, including navigating pages, filling out forms, and extracting structured data, all with full traceability. Every action is logged with detailed step plans and unique session IDs. Take a look at this quick example:

{% embed url="https://app.supademo.com/demo/cmfrasdf107h810k8ggp5fqyk" %}

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Browser Use**

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

Add a name for the connection. You'll be prompted for [**authentication**](browser-use.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

The **Browser Use** book can be used with or without credentials.

## Getting Started

## Best Practices

## Actions

The following actions are available in the **Browser Use** integration:

### 1. Close a browser

Close a browser instance.

### 2. Perform a task on a browser and get the visual log, the detailed plan, the result, the browser run id and the browser files

Execute a browser-based web automation task.

### 3. Provision a browser

Provision a new K8s browser instance for a web automation task.

### 4. Provision an aws browser

Provision a new AWS AgentCore browser instance for a web automation task.

### 5. Run a playwright script on a browser and get the result, the browser run id and the browser files

Execute a custom Playwright script on the provisioned browser.

## Concepts

### Browser instance

Represents attributes of an instance with browser support.

| Field Name     | Description                                                    | Type             |
| -------------- | -------------------------------------------------------------- | ---------------- |
| `browser_name` | The name of the browser instance (pod name or AWS session ID). | `text`           |
| `vnc`          | The Virtual Network Computing (VNC) URL to access the browser. | `text`           |
| `browser_type` | The type of browser backend ("k8s" or "aws").                  | `optional[text]` |

### Browser task

Represents a browser automation task.

| Field Name             | Description                                                                                                                                                                                | Type                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| `instructions`         | A natural language description of the task for the browser agent to perform (e.g., "Log into my account on example.com and check for new messages").                                       | `text`                   |
| `browser_task_id`      | Identifier for the browser task.                                                                                                                                                           | `text`                   |
| `output`               | The desired structure or format of the results. It is recommended to use key-value pairs for clarity (e.g., {"key": "value"}). If specified, the agent will format the result accordingly. | `optional[text]`         |
| `worker_id`            | Identifier for the Kognitos worker executing the task.                                                                                                                                     | `text`                   |
| `line_id`              | Identifier for the specific line/step in the Kognitos automation.                                                                                                                          | `text`                   |
| `browser_task_version` | Version of the browser task.                                                                                                                                                               | `text`                   |
| `task_context`         | Optional additional context or data to assist in completing the task. Contains the resolved reference facts for the task.                                                                  | `optional[json]`         |
| `credential_names`     | The names of the authentication credentials needed for the task.                                                                                                                           | `optional[list of text]` |
| `files`                | The files to be uploaded to the browser.                                                                                                                                                   | `optional[list of text]` |
