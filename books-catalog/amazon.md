---
title: Amazon Selling Partner
updated: 2026-02-06T18:35
git_hash: e0353ed04907ed85c17c3ed6f21f363f3d49f293
description: Overview of the Amazon Selling Partner integration.
icon: amazon
---

# Amazon Selling Partner

{% hint style="info" %}
The following documentation is for **Amazon Selling Partner v2.0.1**.
{% endhint %}

## Overview

Amazon Selling Partner connects you to Amazon's marketplace to automate order retrieval and processing. This integration allows you to pull order data from your Amazon seller account and integrate it seamlessly into your workflows.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Amazon Selling Partner**

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

Add a name for the connection. You'll be prompted for [**authentication**](amazon.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Refresh Token, Client ID and Client Secret

Connect to Amazon Selling Partner API using LWA OAuth credentials.

| Label         | Description                                              | Type        |
| ------------- | -------------------------------------------------------- | ----------- |
| Refresh Token | LWA refresh token from Seller Central                    | `sensitive` |
| Client ID     | LWA client ID (starts with amzn1.application-oa2-client) | `text`      |
| Client Secret | LWA client secret                                        | `sensitive` |

## Actions

The following actions are available in the **Amazon Selling Partner** integration:

### 1. Retrieve orders

Retrieve orders from Amazon Selling Partner API.

### 2. Retrieve an order from amazon selling partner

Retrieve order details from Amazon Selling Partner API.

## Concepts

### Amazon order

Amazon Selling Partner order information.

| Field Name                                                                                        | Description                               | Type                     |
| ------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------------------ |
| `amazon_order_id`                                                                                 | The unique Amazon order identifier.       | `text`                   |
| `order_status`                                                                                    | The current status of the order.          | `text`                   |
| `purchase_date`                                                                                   | The date when the order was purchased.    | `text`                   |
| `last_update_date`                                                                                | The date when the order was last updated. | `text`                   |
| `marketplace_id`                                                                                  | The Amazon marketplace identifier.        | `optional[text]`         |
| `fulfillment_channel`                                                                             | The fulfillment channel (e.g., MFN, AFN). | `optional[text]`         |
| `order_type`                                                                                      | The type of order.                        | `optional[text]`         |
| `shipment_service_level_category`                                                                 | The shipment service level category.      | `optional[text]`         |
| `earliest_ship_date`                                                                              | The earliest ship date.                   | `optional[text]`         |
| `latest_ship_date`                                                                                | The latest ship date.                     | `optional[text]`         |
| `earliest_delivery_date`                                                                          | The earliest delivery date.               | `optional[text]`         |
| `latest_delivery_date`                                                                            | The latest delivery date.                 | `optional[text]`         |
| [`shipping_address`](amazon.md#shipping_address-amazon-order)                                     | The shipping address.                     | `optional[json]`         |
| [`default_ship_from_location_address`](amazon.md#default_ship_from_location_address-amazon-order) | The default ship from location address.   | `optional[json]`         |
| `number_of_items_shipped`                                                                         | The number of items shipped.              | `optional[number]`       |
| `number_of_items_unshipped`                                                                       | The number of items unshipped.            | `optional[number]`       |
| `payment_method`                                                                                  | The payment method.                       | `optional[text]`         |
| `payment_method_details`                                                                          | List of payment method details.           | `optional[list of text]` |
| [`buyer_info`](amazon.md#buyer_info-amazon-order)                                                 | Buyer information.                        | `optional[json]`         |
| `is_business_order`                                                                               | Whether this is a business order.         | `optional[boolean]`      |
| `is_prime`                                                                                        | Whether this is a Prime order.            | `optional[boolean]`      |
| `is_global_express_enabled`                                                                       | Whether global express is enabled.        | `optional[boolean]`      |
| `is_premium_order`                                                                                | Whether this is a premium order.          | `optional[boolean]`      |
| `is_sold_by_ab`                                                                                   | Whether sold by Amazon Business.          | `optional[boolean]`      |
| `is_iba`                                                                                          | Whether this is an IBA order.             | `optional[boolean]`      |
| `is_ispu`                                                                                         | Whether this is an ISPU order.            | `optional[boolean]`      |
| `is_access_point_order`                                                                           | Whether this is an access point order.    | `optional[boolean]`      |
| [`fulfillment_instruction`](amazon.md#fulfillment_instruction-amazon-order)                       | Fulfillment instructions.                 | `optional[json]`         |
| [`automated_shipping_settings`](amazon.md#automated_shipping_settings-amazon-order)               | Automated shipping settings.              | `optional[json]`         |
| `sales_channel`                                                                                   | The sales channel.                        | `optional[text]`         |
| `order_channel`                                                                                   | The order channel.                        | `optional[text]`         |
| `ship_service_level`                                                                              | The ship service level.                   | `optional[text]`         |
| `order_total`                                                                                     | The order total amount.                   | `optional[json]`         |
| `payment_execution_detail`                                                                        | Payment execution details.                | `optional[list of json]` |

#### Concept attribute specifications

**shipping\_address (amazon order)**

| Name              | Type             |
| ----------------- | ---------------- |
| `name`            | `optional[text]` |
| `address_line1`   | `optional[text]` |
| `address_line2`   | `optional[text]` |
| `address_line3`   | `optional[text]` |
| `city`            | `optional[text]` |
| `county`          | `optional[text]` |
| `district`        | `optional[text]` |
| `state_or_region` | `optional[text]` |
| `municipality`    | `optional[text]` |
| `postal_code`     | `optional[text]` |
| `country_code`    | `optional[text]` |
| `phone`           | `optional[text]` |
| `address_type`    | `optional[text]` |

**default\_ship\_from\_location\_address (amazon order)**

| Name              | Type             |
| ----------------- | ---------------- |
| `name`            | `optional[text]` |
| `address_line1`   | `optional[text]` |
| `address_line2`   | `optional[text]` |
| `address_line3`   | `optional[text]` |
| `city`            | `optional[text]` |
| `county`          | `optional[text]` |
| `district`        | `optional[text]` |
| `state_or_region` | `optional[text]` |
| `municipality`    | `optional[text]` |
| `postal_code`     | `optional[text]` |
| `country_code`    | `optional[text]` |
| `phone`           | `optional[text]` |
| `address_type`    | `optional[text]` |

**buyer\_info (amazon order)**

| Name                    | Type             |
| ----------------------- | ---------------- |
| `buyer_email`           | `optional[text]` |
| `buyer_name`            | `optional[text]` |
| `buyer_county`          | `optional[text]` |
| `buyer_tax_info`        | `optional[json]` |
| `purchase_order_number` | `optional[text]` |

**fulfillment\_instruction (amazon order)**

| Name                           | Type             |
| ------------------------------ | ---------------- |
| `fulfillment_supply_source_id` | `optional[text]` |

**automated\_shipping\_settings (amazon order)**

| Name                              | Type                |
| --------------------------------- | ------------------- |
| `has_automated_shipping_settings` | `optional[boolean]` |
| `automated_carrier`               | `optional[text]`    |
| `automated_ship_method`           | `optional[text]`    |
