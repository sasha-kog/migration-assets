---
title: Aspire
updated: 2026-03-20T14:12
git_hash: 0bb4122c50008bea166a71401f6742cd1b52672f
description: Overview of the Aspire integration.
icon: grid-2
---

# Aspire

{% hint style="info" %}
The following documentation is for **Aspire v1.1.1**.
{% endhint %}

## Overview

An integration with aspire

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Aspire**

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

Add a name for the connection. You'll be prompted for [**authentication**](aspire.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Base URL, Client ID and Client Secret

Connects to the Aspire API using client credentials.

| Label         | Description                                                               | Type        |
| ------------- | ------------------------------------------------------------------------- | ----------- |
| Base URL      | The base URL of the Aspire API (e.g. "https://cloud-api.youraspire.com"). | `text`      |
| Client ID     | The client ID for the Aspire API.                                         | `text`      |
| Client Secret | The client secret for the Aspire API.                                     | `sensitive` |

## Actions

The following actions are available in the **Aspire** integration:

### 1. Create an opportunity for a property

Create an opportunity in Aspire for a given property.

### 2. Get the branches

Fetch the list of branches from Aspire.

### 3. Get the catalog items

Fetch the list of catalog items from Aspire.

### 4. Get the opportunities

Fetch the list of opportunities from Aspire.

### 5. Get the opportunity statuses

Fetch the list of opportunity statuses from Aspire.

### 6. Get the properties

Fetch the list of properties from Aspire.

### 7. Get the regions

Fetch the list of regions from Aspire.

### 8. Update a catalog item

Update an existing catalog item in Aspire.

## Concepts

### Aspire opportunity

An opportunity in Aspire

| Field Name                | Description                                                                                                                                                                                                                                                        | Type                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| `opportunity_name`        | The name of the opportunity.                                                                                                                                                                                                                                       | `text`               |
| `opportunity_id`          | The unique identifier (read-only, assigned by API).                                                                                                                                                                                                                | `optional[number]`   |
| `opportunity_type`        | The type (e.g. "Contract", "Work Order").                                                                                                                                                                                                                          | `optional[text]`     |
| `opportunity_status`      | The current status (read-only).                                                                                                                                                                                                                                    | `optional[text]`     |
| `opportunity_status_id`   | The status ID. Use ``get_opportunity_statuses()`` to discover valid IDs (e.g. the "1-New" status).                                                                                                                                                                 | `optional[number]`   |
| `property_id`             | The property to associate. Use ``get_properties()`` to list.                                                                                                                                                                                                       | `optional[number]`   |
| `property_name`           | The associated property name (read-only).                                                                                                                                                                                                                          | `optional[text]`     |
| `branch_name`             | The branch name (read-only).                                                                                                                                                                                                                                       | `optional[text]`     |
| `division_id`             | The division ID. Typically copied from a template opportunity or chosen to match the property's branch.                                                                                                                                                            | `optional[number]`   |
| `division_name`           | The division name (read-only).                                                                                                                                                                                                                                     | `optional[text]`     |
| `sales_rep_id`            | The sales-rep contact ID. Use the ``AccountOwnerContactID`` from the target property, or look up a known sales-rep from an existing opportunity's ``SalesRepContactID``. **Note:** the API write field is ``SalesRepID``; the read field is ``SalesRepContactID``. | `optional[number]`   |
| `sales_rep`               | The sales rep contact name (read-only).                                                                                                                                                                                                                            | `optional[text]`     |
| `template_opportunity_id` | An existing opportunity whose services / line items will be copied into the new one. Use ``get_opportunities()`` with a filter to find a suitable template.                                                                                                        | `optional[number]`   |
| `start_date`              | The start date.                                                                                                                                                                                                                                                    | `optional[datetime]` |
| `end_date`                | The end date.                                                                                                                                                                                                                                                      | `optional[datetime]` |
| `estimated_dollars`       | The estimated dollar amount (read-only).                                                                                                                                                                                                                           | `optional[number]`   |
| `opportunity_number`      | The opportunity number (read-only).                                                                                                                                                                                                                                | `optional[number]`   |

### Aspire branch

A branch in Aspire.Branches belong to regions and are useful for mapping properties to their region. Use ``get_branches()`` alongside ``get_regions()`` to build the full region-to-branch hierarchy.

| Field Name                | Description                                         | Type                |
| ------------------------- | --------------------------------------------------- | ------------------- |
| `branch_id`               | The unique identifier for the branch.               | `number`            |
| `branch_name`             | The name of the branch.                             | `text`              |
| `active`                  | Whether the branch is active.                       | `optional[boolean]` |
| `internal_property_id`    | The ID of the internal property for this branch.    | `optional[number]`  |
| `internal_property_name`  | The name of the internal property.                  | `optional[text]`    |
| `catalog_price_list_name` | The catalog price list associated with this branch. | `optional[text]`    |
| `branch_address_id`       | The ID of the branch address.                       | `optional[number]`  |
| `region_id`               | The ID of the region this branch belongs to.        | `optional[number]`  |
| `region_name`             | The name of the region this branch belongs to.      | `optional[text]`    |

### Aspire catalog item

A catalog item in Aspire

| Field Name                  | Description                                 | Type                 |
| --------------------------- | ------------------------------------------- | -------------------- |
| `catalog_item_id`           | The unique identifier for the catalog item. | `number`             |
| `item_name`                 | The name of the item.                       | `text`               |
| `catalog_item_category_id`  | The category ID of the catalog item.        | `optional[number]`   |
| `item_type`                 | The type of the item.                       | `optional[text]`     |
| `item_description`          | The description of the item.                | `optional[text]`     |
| `item_code`                 | The code of the item.                       | `optional[text]`     |
| `item_cost`                 | The cost of the item.                       | `optional[number]`   |
| `purchase_unit_cost`        | The purchase unit cost.                     | `optional[number]`   |
| `purchase_unit_type_name`   | The purchase unit type name.                | `optional[text]`     |
| `allocation_unit_type_name` | The allocation unit type name.              | `optional[text]`     |
| `available_to_bid`          | Whether the item is available to bid.       | `optional[boolean]`  |
| `active`                    | Whether the item is active.                 | `optional[boolean]`  |
| `catalog_name`              | The name of the catalog.                    | `optional[text]`     |
| `last_updated`              | The last updated date and time.             | `optional[datetime]` |

### Aspire opportunity status

An opportunity status in Aspire

| Field Name              | Description                                       | Type      |
| ----------------------- | ------------------------------------------------- | --------- |
| `opportunity_status_id` | The unique identifier for the opportunity status. | `number`  |
| `status`                | The status label.                                 | `text`    |
| `status_name`           | The display name of the status.                   | `text`    |
| `stage`                 | The stage label.                                  | `text`    |
| `stage_name`            | The display name of the stage.                    | `text`    |
| `active`                | Whether the status is active.                     | `boolean` |
| `required`              | Whether the status is required.                   | `boolean` |

### Aspire property

A property in Aspire

| Field Name                                                | Description                                                                                | Type                                             |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| `property_id`                                             | The unique identifier for the property.                                                    | `number`                                         |
| `property_name`                                           | The name of the property.                                                                  | `text`                                           |
| `property_status`                                         | The status of the property.                                                                | `optional[text]`                                 |
| `branch_id`                                               | The ID of the branch this property belongs to.                                             | `optional[number]`                               |
| `branch_name`                                             | The branch this property belongs to.                                                       | `optional[text]`                                 |
| `branch_code`                                             | The short code for the branch.                                                             | `optional[text]`                                 |
| `account_owner_contact_id`                                | The account owner contact ID. Can be used as ``sales_rep_id`` when creating opportunities. | `optional[number]`                               |
| `account_owner`                                           | The account owner contact name.                                                            | `optional[text]`                                 |
| `address_line_1`                                          | The first line of the property address.                                                    | `optional[text]`                                 |
| `city`                                                    | The city of the property.                                                                  | `optional[text]`                                 |
| `state`                                                   | The state/province code.                                                                   | `optional[text]`                                 |
| `zip_code`                                                | The zip code of the property.                                                              | `optional[text]`                                 |
| `active`                                                  | Whether the property is active.                                                            | `optional[boolean]`                              |
| `modified_date`                                           | The last modified date.                                                                    | `optional[datetime]`                             |
| `modified_by_user_name`                                   | The name of the user who last modified.                                                    | `optional[text]`                                 |
| `property_type_id`                                        | The property type ID.                                                                      | `optional[number]`                               |
| `property_type`                                           | The property type name.                                                                    | `optional[text]`                                 |
| [`property_takeoff_items`](#aspire-property-takeoff-item) | Measured quantities for this property (e.g. total bed area, snow lots).                    | `optional[list of aspire property takeoff item]` |

### Aspire property takeoff item

A takeoff item associated with a property in Aspire.Takeoff items capture measured quantities for a property (e.g. total bed area, number of snow lots).

| Field Name                 | Description                                 | Type               |
| -------------------------- | ------------------------------------------- | ------------------ |
| `property_takeoff_item_id` | The unique identifier for this association. | `number`           |
| `takeoff_item_id`          | The ID of the takeoff item definition.      | `number`           |
| `takeoff_item_name`        | The name of the takeoff item.               | `text`             |
| `takeoff_item_value`       | The measured value.                         | `optional[number]` |

### Aspire region

A region in Aspire

| Field Name         | Description                           | Type             |
| ------------------ | ------------------------------------- | ---------------- |
| `region_id`        | The unique identifier for the region. | `number`         |
| `region_name`      | The name of the region.               | `text`           |
| `legal_name`       | The legal name of the region.         | `optional[text]` |
| `address_line_1`   | The first line of the region address. | `optional[text]` |
| `address_city`     | The city of the region.               | `optional[text]` |
| `address_state`    | The state/province code.              | `optional[text]` |
| `address_zip_code` | The zip code of the region.           | `optional[text]` |
| `manager_name`     | The manager of the region.            | `optional[text]` |
| `district_name`    | The district the region belongs to.   | `optional[text]` |
| `phone_number`     | The phone number of the region.       | `optional[text]` |
