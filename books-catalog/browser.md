---
title: Browser
description: Overview of the Browser integration for step-by-step web automation.
icon: browser
---

# Browser

## Overview

The **Browser** integration lets you automate web interactions through **precise, individual actions** — navigating to a page, clicking buttons, filling forms, verifying content, and more.

Each run uses:

* **Live view** to watch the browser in real time.
* **Agent step stream** to track what the agent is doing step-by-step.
* **Restricted tools** so the agent is limited to approved browser actions (not arbitrary code execution).

Use the Browser integration when you need:

* **Fine-grained control** over each interaction on a web page.
* **Secure credential handling** where passwords and secrets are injected without being exposed to the agent or logs.
* **Verification** that specific content or values are present before continuing.
* **File downloads and uploads** as part of a web workflow.
* **Data extraction** from pages using AI-powered reading. For visual extraction workflows, connect **Intelligent Document Processing (IDP)**.

## How It Works

Browser automation follows this workflow:

1. You describe the task in natural language.
2. The agent explores the page and authors a deterministic automation.
3. The automation is run and a verification pass checks stability.
4. You review progress in live view and the step stream.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Browser**

### Steps

Follow these steps to connect the integration in Kognitos:

{% stepper %}
{% step %}
#### Navigate

Using the left navigation menu, go to **Integrations** → **Explore Integrations**.
{% endstep %}

{% step %}
#### Find

Search for **Browser** and click on it.
{% endstep %}

{% step %}
#### Connect

Click on <kbd>**Connect**</kbd> to add a connection to the integration.
{% endstep %}

{% step %}
#### Configure

Add a name for the connection. You'll be prompted for [**authentication**](browser.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

The **Browser** book can be used **with or without credentials**.

To automate workflows that require login or sensitive input, connect with **Browser Credentials**.

Credentials are stored as named key-value pairs and injected securely at runtime. Credential values are not exposed to the agent and are not shown in your automation outputs.

### Credential key naming rules

Credential **key names** (the left-hand side of each pair) must contain only:

* Alphanumeric characters (`A–Z`, `a–z`, `0–9`)
* Hyphens (`-`)
* Underscores (`_`)

Characters such as `@`, `.`, and spaces are **not allowed** in key names.

{% hint style="warning" %}
Do not put your actual email address (or any value containing `@`) in the key name field. The key is just a label you choose to reference the credential — the value is where the actual secret goes.
{% endhint %}

**Example — email-based login:**

| Key | Value |
| --- | ----- |
| `email_address` | `you@example.com` |
| `email_password` | `your_password` |

You can optionally reference credentials by key name in your prompt — for example, `"type the 'email_address' credential in the Email field"` — though the agent will also discover and use the right credential automatically.

## Getting Started

A typical Browser automation follows this pattern:

1. **Provision** a browser.
2. **Navigate** to a website.
3. **Interact** with the page — click buttons, fill out forms, select options.
4. **Verify** that the expected content appeared.
5. **Extract** information if needed.
6. **Close** the browser.

Describe each step in plain English in your prompt. For example:

> Provision a browser. Navigate to https://example.com/login. Type "admin" in the Username field. Type the "password" credential in the Password field. Click the Log In button. Verify that "Welcome" is visible on the page. Then close the browser.

## Best Practices

* **Provision first.** Every browser interaction requires a provisioned browser, so always start by provisioning one.
* **Prompt with clear intent.** Describe the business outcome first, then the key page steps.
* **Be specific about elements.** Instead of "click the button," say "click the **Submit Order** button" or "type in the **Email** field."
* **Use scope when elements share the same name.** If a page has two sections with a "Street" field, specify which one: "type '123 Main St' in the Street field in the **Billing Address** section."
* **Use credentials for sensitive data.** Reference credentials by name rather than typing secrets directly.
* **Add explicit verification steps.** Confirm expected state after key transitions (for example, "verify that 'Order confirmed' is visible").

## Actions

The following capabilities are available in the **Browser** integration:

### Lifecycle

| Action | Description |
| ------ | ----------- |
| Provision a browser | Start a new remote browser session. Returns a live view URL you can use to watch in real time. |
| Close a browser | End the browser session and release resources. |
| Get downloaded files | Retrieve any files the browser downloaded during the session. |

### Navigation

| Action | Description |
| ------ | ----------- |
| Navigate to a URL | Open a web page in the browser. |
| Go back | Navigate to the previous page in browser history. |
| Go forward | Navigate to the next page in browser history. |
| Scroll the page | Scroll up, down, left, or right on the current page. |

### Clicking and Hovering

| Action | Description |
| ------ | ----------- |
| Click an element | Click a button, link, or other interactive element on the page. |
| Hover an element | Move the cursor over an element without clicking. |
| Drag an element | Drag one element to another location on the page. |

### Typing and Selection

| Action | Description |
| ------ | ----------- |
| Type text | Type into an input field. Can optionally press Enter after typing. |
| Type a credential | Securely type a credential value (e.g., a password) into a field. Requires Browser Credentials. |
| Select a dropdown option | Choose an option from a dropdown or combobox. |
| Press a key | Press a keyboard key or combination (e.g., Enter, Tab, Ctrl+A). |

### Forms and File Upload

| Action | Description |
| ------ | ----------- |
| Fill a form | Fill multiple fields in a single step. |
| Fill a form using credentials | Fill a form where some fields use securely stored credential values. Requires Browser Credentials. |
| Upload a file | Upload a file to a file input on the page. |

### Dialogs and Tabs

| Action | Description |
| ------ | ----------- |
| Handle a dialog | Accept or dismiss the next browser dialog (alert, confirm, prompt). Must be called before the action that triggers the dialog. |
| List tabs | See all open browser tabs with their titles and URLs. |
| Switch tab | Switch focus to a different browser tab. |

### Waiting

| Action | Description |
| ------ | ----------- |
| Await text | Wait until specific text appears on the page (up to a timeout). |
| Await a specified time | Pause for a set number of seconds. |

### Verification

| Action | Description |
| ------ | ----------- |
| Verify text is visible | Confirm that specific text is visible on the page. |
| Verify an element is visible | Confirm that a specific element is present and visible. |
| Verify a value | Confirm that a form field contains an expected value. |
| Verify a list | Confirm that all items in a list of text strings are visible on the page. |

### Observation and Extraction

| Action | Description |
| ------ | ----------- |
| Take a snapshot | Get a structured, text-based view of all elements on the page. Useful for inspecting page content. |
| Take a screenshot | Capture a visual image of the current page. |
| Extract from a screenshot | Use AI to answer a question about the visual content of the page. |
| Extract from a snapshot | Use AI to answer a question about the structured content of the page. |

{% hint style="info" %}
Extraction actions use AI and are best suited for one-off reads. Avoid requesting them repeatedly in tight loops.
{% endhint %}

## Concepts

### Browser instance

Represents a provisioned browser session.

| Field Name      | Description                                    | Type   |
| --------------- | ---------------------------------------------- | ------ |
| `session_id`    | Unique identifier for the browser session.     | `text` |
| `live_view_url` | URL to watch the browser session in real time. | `text` |

### Browser action result

The result returned after each browser action.

| Field Name    | Description                                                          | Type             |
| ------------- | -------------------------------------------------------------------- | ---------------- |
| `success`     | Whether the action completed successfully.                           | `boolean`        |
| `result`      | The action's output (for example, snapshot content, extracted data, PASS/FAIL). | `text`       |
| `action_type` | The type of action that was performed.                               | `text`           |
| `snapshot`    | A structured view of the page after the action (when available).     | `optional[text]` |
