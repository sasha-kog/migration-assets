---
title: ServiceNow
updated: 2026-02-06T18:35
git_hash: ff86c337460f64deffcd118d2b71ee27e28dadf2
description: Overview of the ServiceNow integration.
icon: ticket
---

# ServiceNow

{% hint style="info" %}
The following documentation is for **ServiceNow v2.0.0**.
{% endhint %}

## Overview

ServiceNow is an enterprise IT service management platform that automates and streamlines business processes. This integration enables automated ticket creation, incident management, change requests, and IT workflow automation. Improve service delivery and operational efficiency through automated IT processes.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **ServiceNow**

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

Add a name for the connection. You'll be prompted for [**authentication**](servicenow.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Instance, Username and Password

Connects to a ServiceNow instance using the provided credentials.

| Label    | Description                                       | Type        |
| -------- | ------------------------------------------------- | ----------- |
| Instance | The instance ID for the ServiceNow instance.      | `text`      |
| Username | The username to log in to the ServiceNow account. | `text`      |
| Password | The password to log in to the ServiceNow account. | `sensitive` |

## Actions

The following actions are available in the **ServiceNow** integration:

### 1. Create a record in a table name

Creates a new record in a ServiceNow account.

### 2. Delete some records

Deletes records from ServiceNow using batch processing.

### 3. Retrieve some records from servicenow

Retrieves a list of ServiceNow records based on the specified filters.

### 4. Update a record

Updates a record in ServiceNow, identified by its incident number, with specified attributes and their new values.

## Concepts

### Servicenow record

A dataclass for ServiceNow record.

| Field Name                 | Description                                 | Type                     |
| -------------------------- | ------------------------------------------- | ------------------------ |
| `short_description`        | The short description of the record.        | `optional[text]`         |
| `description`              | The description of the record.              | `optional[text]`         |
| `caller_id`                | The caller ID of the record.                | `optional[text]`         |
| `category`                 | The category of the record.                 | `optional[text]`         |
| `subcategory`              | The subcategory of the record.              | `optional[text]`         |
| `contact_type`             | The contact type of the record.             | `optional[text]`         |
| `assignment_group`         | The assignment group of the record.         | `optional[text]`         |
| `assigned_to`              | The assigned to of the record.              | `optional[text]`         |
| `priority`                 | The priority of the record.                 | `optional[text]`         |
| `severity`                 | The severity of the record.                 | `optional[text]`         |
| `impact`                   | The impact of the record.                   | `optional[text]`         |
| `urgency`                  | The urgency of the record.                  | `optional[text]`         |
| `location`                 | The location of the record.                 | `optional[text]`         |
| `business_service`         | The business service of the record.         | `optional[text]`         |
| `cmdb_ci`                  | The CMDB CI of the record.                  | `optional[text]`         |
| `comments`                 | The comments of the record.                 | `optional[text]`         |
| `additional_comments`      | The additional comments of the record.      | `optional[text]`         |
| `watch_list`               | The watch list of the record.               | `optional[list of text]` |
| `upon_reject`              | The upon reject of the record.              | `optional[text]`         |
| `notify`                   | The notify of the record.                   | `optional[text]`         |
| `number`                   | The number of the record.                   | `optional[text]`         |
| `sys_id`                   | The sys ID of the record.                   | `optional[text]`         |
| `sys_created_on`           | The sys created on of the record.           | `optional[text]`         |
| `table_name`               | The table name of the record.               | `optional[text]`         |
| `parent`                   | The parent of the record.                   | `optional[text]`         |
| `made_sla`                 | The made SLA of the record.                 | `optional[text]`         |
| `sys_updated_on`           | The sys updated on of the record.           | `optional[text]`         |
| `sys_updated_by`           | The sys updated by of the record.           | `optional[text]`         |
| `approval_history`         | The approval history of the record.         | `optional[text]`         |
| `opened_by`                | The opened by of the record.                | `optional[text]`         |
| `work_end`                 | The work end of the record.                 | `optional[text]`         |
| `approval_set`             | The approval set of the record.             | `optional[text]`         |
| `wf_activity`              | The workflow activity of the record.        | `optional[text]`         |
| `work_notes`               | The work notes of the record.               | `optional[text]`         |
| `correlation_display`      | The correlation display of the record.      | `optional[text]`         |
| `delivery_task`            | The delivery task of the record.            | `optional[text]`         |
| `work_start`               | The work start of the record.               | `optional[text]`         |
| `additional_assignee_list` | The additional assignee list of the record. | `optional[text]`         |
| `calendar_duration`        | The calendar duration of the record.        | `optional[text]`         |
| `close_notes`              | The close notes of the record.              | `optional[text]`         |
| `sys_class_name`           | The sys class name of the record.           | `optional[text]`         |
| `closed_by`                | The closed by of the record.                | `optional[text]`         |
| `follow_up`                | The follow up of the record.                | `optional[text]`         |
| `company`                  | The company of the record.                  | `optional[text]`         |
| `reassignment_count`       | The reassignment count of the record.       | `optional[text]`         |
| `activity_due`             | The activity due of the record.             | `optional[text]`         |
| `approval`                 | The approval of the record.                 | `optional[text]`         |
| `sla_due`                  | The SLA due of the record.                  | `optional[text]`         |
| `comments_and_work_notes`  | The comments and work notes of the record.  | `optional[text]`         |
| `due_date`                 | The due date of the record.                 | `optional[text]`         |
| `sys_mod_count`            | The sys mod count of the record.            | `optional[text]`         |
| `sys_tags`                 | The sys tags of the record.                 | `optional[text]`         |
| `escalation`               | The escalation of the record.               | `optional[text]`         |
| `upon_approval`            | The upon approval of the record.            | `optional[text]`         |
| `correlation_id`           | The correlation ID of the record.           | `optional[text]`         |
| `other_fields`             | Additional fields not explicitly mapped.    | `optional[json]`         |
