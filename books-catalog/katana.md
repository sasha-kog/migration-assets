---
title: Katana
updated: 2026-02-06T18:35
git_hash: 96195c60c5366f05041871be6887a9d4e88097b6
description: Overview of the Katana integration.
icon: k
---

# Katana

{% hint style="info" %}
The following documentation is for **Katana v2.0.0**.
{% endhint %}

## Overview

Katana is a comprehensive manufacturing resource planning (MRP) software designed for modern manufacturers. This integration enables automated inventory management, production scheduling, order processing, and supply chain optimization workflows. Streamline manufacturing operations and improve production efficiency through automated processes.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Katana**

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

Add a name for the connection. You'll be prompted for [**authentication**](katana.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using api key

Connects to an API using the provided API key.

| Label   | Description                           | Type   |
| ------- | ------------------------------------- | ------ |
| api key | The API key to be used for connecting | `text` |

## Actions

The following actions are available in the **Katana** integration:

### 1. Retrieve some customers

Fetch the customers with optional filtering.

### 2. Retrieve some purchase orders

Fetch the purchase orders with optional filtering.

### 3. Retrieve some sales orders

Fetch the sales orders with optional filtering.

### 4. Update a sales order

Update an existing sales order.

## Concepts

### Katana customer

Customer represents a customer within the Katana system, serving as a comprehensive record of customer information, contact details, and associated addresses. It provides essential information to manage customer relationships and process orders.

| Field Name                                         | Description                                                              | Type                     |
| -------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------ |
| `id`                                               | Unique identifier for the customer.                                      | `text`                   |
| `name`                                             | Customer's full name or business name.                                   | `text`                   |
| [`addresses`](katana.md#addresses-katana-customer) | An array of shipping and billing addresses associated with the customer. | `optional[list of json]` |
| `first_name`                                       | Customer's first name.                                                   | `optional[text]`         |
| `last_name`                                        | Customer's last name.                                                    | `optional[text]`         |
| `company`                                          | Company name associated with the customer.                               | `optional[text]`         |
| `email`                                            | Customer's email address for communication.                              | `optional[text]`         |
| `phone`                                            | Customer's phone number for contact.                                     | `optional[text]`         |
| `comment`                                          | Additional comments or notes about the customer.                         | `optional[text]`         |
| `currency`                                         | Default currency code used for the customer's transactions.              | `optional[text]`         |
| `reference_id`                                     | External reference identifier for integration purposes.                  | `optional[text]`         |
| `category`                                         | Customer category or classification for grouping.                        | `optional[text]`         |
| `discount_rate`                                    | Default discount rate applied to the customer's orders.                  | `optional[number]`       |
| `created_at`                                       | The timestamp when the customer was created.                             | `optional[datetime]`     |
| `updated_at`                                       | The timestamp when the customer was last updated.                        | `optional[datetime]`     |
| `default_billing_id`                               | ID of the default billing address from the addresses array.              | `optional[text]`         |
| `default_shipping_id`                              | ID of the default shipping address from the addresses array.             | `optional[text]`         |

### Katana purchase order

PurchaseOrder represents a supplier order within the Katana system, serving as a comprehensive record of all order details, receiving status, and associated metadata. It provides essential information to track and manage supplier orders throughout their lifecycle.

| Field Name                                                                   | Description                                                                | Type                     |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------ |
| `id`                                                                         | Unique identifier for the object.                                          | `text`                   |
| `order_no`                                                                   | A unique, identifying string used in the UI and controlled by the user.    | `text`                   |
| [`purchase_order_rows`](katana.md#purchase_order_rows-katana-purchase-order) | An array of purchase order rows.                                           | `optional[list of json]` |
| `status`                                                                     | Status of the order.                                                       | `optional[text]`         |
| `billing_status`                                                             | Status of generating the bill through accounting integration.              | `optional[text]`         |
| `last_document_status`                                                       | Status of the last e-mail sent from (O)PO card.                            | `optional[text]`         |
| `entity_type`                                                                | Either "regular" or "outsourced", depending on the purchase order type.    | `optional[text]`         |
| `supplier_id`                                                                | ID of the supplier who this order belongs to.                              | `optional[text]`         |
| `currency`                                                                   | Currency of the purchase order.                                            | `optional[text]`         |
| `expected_arrival_date`                                                      | The timestamp when the items are expected to arrive.                       | `optional[datetime]`     |
| `order_created_date`                                                         | The timestamp of creating the document.                                    | `optional[datetime]`     |
| `location_id`                                                                | The ID of the location to which items are received.                        | `optional[text]`         |
| `total`                                                                      | The total value of the order (including taxes) in purchase order currency. | `optional[number]`       |
| `total_in_base_currency`                                                     | The total value of the order (including taxes) in base currency.           | `optional[number]`       |
| `created_at`                                                                 | The timestamp when the purchase order was created.                         | `optional[datetime]`     |
| `updated_at`                                                                 | The timestamp when the purchase order was last updated.                    | `optional[datetime]`     |
| `additional_info`                                                            | Internal comments, links to external files, additional instructions.       | `optional[text]`         |
| `ingredient_availability`                                                    | Status of ingredients for outsourced purchase orders.                      | `optional[text]`         |
| `ingredient_expected_date`                                                   | Latest date for required ingredients on outsourced orders.                 | `optional[datetime]`     |
| `tracking_location_id`                                                       | Location where ingredients are processed for outsourced orders.            | `optional[text]`         |

### Katana sales order

SalesOrder represents a customer order within the Katana system, serving as a comprehensive record of all order details, fulfillment status, and associated metadata. It provides essential information to track and manage customer orders throughout their lifecycle.

| Field Name                                                          | Description                                                                                         | Type                     |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------ |
| `id`                                                                | Unique identifier for the object.                                                                   | `text`                   |
| `order_no`                                                          | A unique, identifying string used in the UI and controlled by the user.                             | `text`                   |
| [`sales_order_rows`](katana.md#sales_order_rows-katana-sales-order) | An array of sales order rows.                                                                       | `optional[list of json]` |
| [`addresses`](katana.md#addresses-katana-sales-order)               | An array of shipping and billing addresses.                                                         | `optional[list of json]` |
| `customer_id`                                                       | ID of the customer who this order belongs to.                                                       | `optional[text]`         |
| `source`                                                            | Indication of whether the sales order was created manually, by API or imported from somewhere else. | `optional[text]`         |
| `location_id`                                                       | ID of the location from which the order is shipped by default.                                      | `optional[text]`         |
| `status`                                                            | Status of the order.                                                                                | `optional[text]`         |
| `currency`                                                          | Currency of the sales order.                                                                        | `optional[text]`         |
| `invoicing_status`                                                  | Status of generating the invoice through accounting integration.                                    | `optional[text]`         |
| `product_availability`                                              | Stock status for the products required by the sales order.                                          | `optional[text]`         |
| `ingredient_availability`                                           | Stock status for ingredients required to produce the products.                                      | `optional[text]`         |
| `production_status`                                                 | Production status of the manufacturing order.                                                       | `optional[text]`         |
| `billing_address_id`                                                | The ID of the billing address of the sales order.                                                   | `optional[text]`         |
| `shipping_address_id`                                               | The ID of the shipping address of the sales order.                                                  | `optional[text]`         |
| `order_created_date`                                                | The timestamp of creating the document.                                                             | `optional[datetime]`     |
| `delivery_date`                                                     | A timestamp when the items are required to be delivered to the customer.                            | `optional[datetime]`     |
| `conversion_date`                                                   | The date of the conversion rate used.                                                               | `optional[datetime]`     |
| `conversion_rate`                                                   | Currency rate used to convert from sales order currency into factory base currency.                 | `optional[number]`       |
| `created_at`                                                        | The timestamp when the sales order was created.                                                     | `optional[datetime]`     |
| `updated_at`                                                        | The timestamp when the sales order was last updated.                                                | `optional[datetime]`     |
| `total_in_base_currency`                                            | The total value of the order (including taxes) in base currency.                                    | `optional[number]`       |
| `total`                                                             | The total value of the order (including taxes) in sales order currency.                             | `optional[number]`       |
| `picked_date`                                                       | The timestamp when delivery status was marked as "PACKED" or "DELIVERED".                           | `optional[datetime]`     |
| `additional_info`                                                   | Internal comments, links to external files, additional instructions.                                | `optional[text]`         |
| `customer_ref`                                                      | An identifier to reference the customer associated with the sales order.                            | `optional[text]`         |
| `ecommerce_order_type`                                              | Name of the ecommerce platform if imported from one.                                                | `optional[text]`         |
| `ecommerce_store_name`                                              | Name of the ecommerce store if imported from ecommerce platform.                                    | `optional[text]`         |
| `ecommerce_order_id`                                                | ID of the order in the source system if imported.                                                   | `optional[text]`         |
| `product_expected_date`                                             | Latest date of manufacturing/purchasing deadline for required products.                             | `optional[datetime]`     |
| `ingredient_expected_date`                                          | Latest date of manufacturing/purchasing deadline for required ingredients.                          | `optional[datetime]`     |
| `tracking_number`                                                   | Deprecated - use tracking\_number from sales order fulfillment instead.                             | `optional[text]`         |
| `tracking_number_url`                                               | Deprecated - use tracking\_number\_url from sales order fulfillment instead.                        | `optional[text]`         |

#### Concept attribute specifications

**addresses (katana customer)**

| Name          | Type                 |
| ------------- | -------------------- |
| `id`          | `text`               |
| `customer_id` | `optional[text]`     |
| `entity_type` | `optional[text]`     |
| `default`     | `optional[boolean]`  |
| `first_name`  | `optional[text]`     |
| `last_name`   | `optional[text]`     |
| `company`     | `optional[text]`     |
| `phone`       | `optional[text]`     |
| `line_1`      | `optional[text]`     |
| `line_2`      | `optional[text]`     |
| `city`        | `optional[text]`     |
| `state`       | `optional[text]`     |
| `zip`         | `optional[text]`     |
| `country`     | `optional[text]`     |
| `created_at`  | `optional[datetime]` |
| `updated_at`  | `optional[datetime]` |

**purchase\_order\_rows (katana purchase order)**

| Name                           | Type                 |
| ------------------------------ | -------------------- |
| `id`                           | `text`               |
| `variant_id`                   | `optional[text]`     |
| `quantity`                     | `optional[number]`   |
| `price_per_unit`               | `optional[number]`   |
| `purchase_uom`                 | `optional[text]`     |
| `purchase_uom_conversion_rate` | `optional[number]`   |
| `total`                        | `optional[number]`   |
| `total_in_base_currency`       | `optional[number]`   |
| `conversion_rate`              | `optional[number]`   |
| `conversion_date`              | `optional[datetime]` |
| `created_at`                   | `optional[datetime]` |
| `updated_at`                   | `optional[datetime]` |
| `tax_rate_id`                  | `optional[text]`     |
| `batch_transactions`           | `optional[json]`     |
| `received_date`                | `optional[datetime]` |
| `arrival_date`                 | `optional[datetime]` |

**sales\_order\_rows (katana sales order)**

| Name                              | Type                 |
| --------------------------------- | -------------------- |
| `id`                              | `text`               |
| `variant_id`                      | `optional[text]`     |
| `conversion_rate`                 | `optional[text]`     |
| `conversion_date`                 | `optional[datetime]` |
| `created_at`                      | `optional[datetime]` |
| `updated_at`                      | `optional[datetime]` |
| `quantity`                        | `optional[number]`   |
| `price_per_unit`                  | `optional[number]`   |
| `price_per_unit_in_base_currency` | `optional[number]`   |
| `total_in_base_currency`          | `optional[number]`   |
| `total`                           | `optional[number]`   |
| `tax_rate_id`                     | `optional[text]`     |
| `location_id`                     | `optional[text]`     |
| `product_availability`            | `optional[text]`     |
| `product_expected_date`           | `optional[datetime]` |
| `cogs_value`                      | `optional[number]`   |
| `attributes`                      | `optional[json]`     |
| `batch_transactions`              | `optional[json]`     |
| `serial_numbers`                  | `optional[text]`     |
| `linked_manufacturing_order_id`   | `optional[text]`     |

**addresses (katana sales order)**

| Name             | Type                 |
| ---------------- | -------------------- |
| `id`             | `text`               |
| `sales_order_id` | `optional[text]`     |
| `entity_type`    | `optional[text]`     |
| `line_1`         | `optional[text]`     |
| `city`           | `optional[text]`     |
| `zip`            | `optional[text]`     |
| `country`        | `optional[text]`     |
| `created_at`     | `optional[datetime]` |
| `updated_at`     | `optional[datetime]` |
| `first_name`     | `optional[text]`     |
| `last_name`      | `optional[text]`     |
| `company`        | `optional[text]`     |
| `phone`          | `optional[text]`     |
| `line_2`         | `optional[text]`     |
| `state`          | `optional[text]`     |
