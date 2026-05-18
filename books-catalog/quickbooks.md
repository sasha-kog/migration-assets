---
title: Quickbooks
updated: 2026-03-20T14:12
git_hash: d1d2993d48687cf1cad29adecc4effcc73ad9c8c
description: Overview of the Quickbooks integration.
icon: book-copy
---

# Quickbooks

{% hint style="info" %}
The following documentation is for **Quickbooks v2.6.0**.
{% endhint %}

## Overview

Automate accounting workflows by managing bills and records in QuickBooks.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Quickbooks**

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

Add a name for the connection. You'll be prompted for [**authentication**](quickbooks.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using token

Connects to QuickBooks using OAuth access token.

| Label | Description                                           | Type   |
| ----- | ----------------------------------------------------- | ------ |
| token | The OAuth access token for QuickBooks authentication. | `text` |

## Actions

The following actions are available in the **Quickbooks** integration:

### 1. Attach a file to the bill and get the attachment

Upload an attachment to an existing bill in QuickBooks.

### 2. Create a bill

Create a new bill in QuickBooks from the provided bill details.

### 3. Create a bill from a purchase order

Create a new bill in QuickBooks based on an existing purchase order.

### 4. Create an invoice

Create a new invoice in QuickBooks from the provided invoice details.

### 5. Delete an invoice

Delete/void an invoice in QuickBooks.

### 6. Delete an invoice by id

Delete/void an invoice in QuickBooks by invoice ID.

### 7. Edit a bill

Edit an existing bill in QuickBooks by updating it with new information.

### 8. Edit an invoice

Edit an existing invoice in QuickBooks by updating it with new information.

### 9. Retrieve bills

Retrieve bills in QuickBooks from the company.

### 10. Retrieve customers

Retrieve customers in QuickBooks from the company.

### 11. Retrieve invoices

Retrieve invoices in QuickBooks from the company.

### 12. Retrieve items

Retrieve items in QuickBooks from the company.

### 13. Retrieve purchase orders

Retrieve purchase orders in QuickBooks from the company.

### 14. Retrieve vendors

Retrieve vendors in QuickBooks from the company.

### 15. Retrieve a report

Retrieve a specific report from QuickBooks.

### 16. Update an item

Update an existing item in QuickBooks.

## Concepts

### Quickbooks bill input

Input data for creating a QuickBooks Bill with mixed line item types.

| Field Name              | Description                                              | Type                  |
| ----------------------- | -------------------------------------------------------- | --------------------- |
| `vendor`                | The vendor in QuickBooks.                                | `json`                |
| [`items`](#list-of-any) | List of line items (can be item-based or account-based). | `list of list of any` |
| `terms`                 | Optional sales terms name.                               | `optional[text]`      |
| `bill_date`             | The bill date in YYYY-MM-DD format.                      | `optional[text]`      |
| `due_date`              | The due date in YYYY-MM-DD format.                       | `optional[text]`      |
| `bill_no`               | Optional bill number.                                    | `optional[text]`      |

### Quickbooks vendor

A comprehensive representation of a QuickBooks Vendor.

| Field Name                               | Description                                  | Type                           |
| ---------------------------------------- | -------------------------------------------- | ------------------------------ |
| `id`                                     | The unique identifier for the vendor.        | `text`                         |
| `display_name`                           | The display name of the vendor.              | `text`                         |
| `company_name`                           | The company name of the vendor.              | `optional[text]`               |
| `first_name`                             | The first name of the vendor contact person. | `optional[text]`               |
| `last_name`                              | The last name of the vendor contact person.  | `optional[text]`               |
| `print_on_check_name`                    | The name to print on checks.                 | `optional[text]`               |
| `email`                                  | The primary email address of the vendor.     | `optional[text]`               |
| `phone`                                  | The primary phone number of the vendor.      | `optional[text]`               |
| `website`                                | The vendor's website URL.                    | `optional[text]`               |
| [`billing_address`](#quickbooks-address) | The billing address of the vendor.           | `optional[quickbooks address]` |
| `account_number`                         | The vendor's account number.                 | `optional[text]`               |
| `balance`                                | The current balance owed to the vendor.      | `optional[number]`             |
| `default_terms`                          | The default payment terms for the vendor.    | `optional[text]`               |
| `is_1099_contractor`                     | Whether the vendor is a 1099 contractor.     | `optional[boolean]`            |
| `is_active`                              | Whether the vendor is currently active.      | `optional[boolean]`            |

### Quickbooks bill

A created QuickBooks Bill.

| Field Name                                  | Description                                             | Type                                                                            |
| ------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`                                        | The unique identifier of the bill in QuickBooks.        | `text`                                                                          |
| `doc_number`                                | The document number of the bill.                        | `text`                                                                          |
| `vendor_name`                               | The name of the vendor.                                 | `text`                                                                          |
| `total_amount`                              | The total amount of the bill.                           | `number`                                                                        |
| `balance`                                   | The current balance of the bill from QuickBooks.        | `number`                                                                        |
| `bill_date`                                 | The bill date.                                          | `optional[text]`                                                                |
| `due_date`                                  | The due date.                                           | `optional[text]`                                                                |
| [`terms`](#terms-quickbooks-bill)           | The payment terms reference with id and name.           | `optional[json]`                                                                |
| [`location`](#location-quickbooks-bill)     | The department/location reference with id and name.     | `optional[json]`                                                                |
| `items`                                     | List of bill line items.                                | `optional[list of list of quickbooks item` or `quickbooks account based line?]` |
| [`custom_fields`](#quickbooks-custom-field) | List of custom fields associated with the bill.         | `optional[list of quickbooks custom field]`                                     |
| [`attachment_ref`](#quickbooks-attachment)  | The attachment reference if an attachment was uploaded. | `optional[quickbooks attachment]`                                               |
| `created_time`                              | When the bill was created.                              | `optional[text]`                                                                |
| `last_updated`                              | When the bill was last updated                          | `optional[text]`                                                                |

### Quickbooks custom field

Represents a custom field in QuickBooks.

| Field Name      | Description                                            | Type             |
| --------------- | ------------------------------------------------------ | ---------------- |
| `definition_id` | The unique identifier for the custom field definition. | `text`           |
| `name`          | The name of the custom field.                          | `text`           |
| `field_type`    | The type of the custom field (e.g., 'StringType').     | `text`           |
| `string_value`  | The string value of the custom field.                  | `optional[text]` |

### Quickbooks attachment

An attachment to a QuickBooks bill.

| Field Name     | Description                                            | Type               |
| -------------- | ------------------------------------------------------ | ------------------ |
| `id`           | The unique identifier of the attachment in QuickBooks. | `text`             |
| `file_name`    | The name of the attached file.                         | `text`             |
| `note`         | Optional note associated with the attachment.          | `optional[text]`   |
| `content_type` | The MIME type of the attachment.                       | `optional[text]`   |
| `size`         | The size of the attachment in bytes.                   | `optional[number]` |

### Quickbooks purchase order

A created QuickBooks Purchase Order.

| Field Name                                        | Description                                                | Type                                        |
| ------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------- |
| `id`                                              | The unique identifier of the purchase order in QuickBooks. | `text`                                      |
| `doc_number`                                      | The document number of the purchase order.                 | `text`                                      |
| `vendor_name`                                     | The name of the vendor.                                    | `text`                                      |
| `total_amount`                                    | The total amount of the purchase order.                    | `number`                                    |
| `po_status`                                       | The status of the purchase order (e.g., "Open", "Closed"). | `optional[text]`                            |
| `po_date`                                         | The purchase order date.                                   | `optional[text]`                            |
| `due_date`                                        | The due date.                                              | `optional[text]`                            |
| `memo`                                            | Memo or notes for the purchase order.                      | `optional[text]`                            |
| `private_note`                                    | Private note for the purchase order.                       | `optional[text]`                            |
| [`terms`](#terms-quickbooks-purchase-order)       | The payment terms reference.                               | `optional[json]`                            |
| [`location`](#location-quickbooks-purchase-order) | The department/location.                                   | `optional[json]`                            |
| `ship_method`                                     | The shipping method.                                       | `optional[text]`                            |
| `vendor_address`                                  | The vendor address for the purchase order.                 | `optional[text]`                            |
| `ship_address`                                    | The shipping address.                                      | `optional[text]`                            |
| `exchange_rate`                                   | The exchange rate used.                                    | `optional[number]`                          |
| `global_tax_calculation`                          | The tax calculation method.                                | `optional[text]`                            |
| `items`                                           | List of purchase order line items.                         | `optional[list of list of any?]`            |
| [`custom_fields`](#quickbooks-custom-field)       | List of custom fields associated with the purchase order.  | `optional[list of quickbooks custom field]` |
| `created_time`                                    | When the purchase order was created.                       | `optional[text]`                            |
| `last_updated`                                    | When the purchase order was last updated.                  | `optional[text]`                            |

### Quickbooks invoice input

Input data for creating a QuickBooks Invoice with mixed line item types.

| Field Name                                  | Description                                                 | Type                                        |
| ------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------- |
| `customer`                                  | The customer in QuickBooks.                                 | `json`                                      |
| [`items`](#list-of-any)                     | List of line items (can be sales-item or description-only). | `list of list of any`                       |
| [`custom_fields`](#quickbooks-custom-field) | Optional list of custom fields for the invoice.             | `optional[list of quickbooks custom field]` |
| `terms`                                     | Optional sales terms name.                                  | `optional[text]`                            |
| `invoice_date`                              | The invoice date in YYYY-MM-DD format.                      | `optional[text]`                            |
| `due_date`                                  | The due date in YYYY-MM-DD format.                          | `optional[text]`                            |
| `invoice_no`                                | Optional invoice number.                                    | `optional[text]`                            |

### Quickbooks customer

A comprehensive representation of a QuickBooks Customer.

| Field Name                                | Description                                    | Type                           |
| ----------------------------------------- | ---------------------------------------------- | ------------------------------ |
| `id`                                      | The unique identifier for the customer.        | `text`                         |
| `display_name`                            | The display name of the customer.              | `text`                         |
| `company_name`                            | The company name of the customer.              | `optional[text]`               |
| `first_name`                              | The first name of the customer contact person. | `optional[text]`               |
| `last_name`                               | The last name of the customer contact person.  | `optional[text]`               |
| `print_on_check_name`                     | The name to print on checks.                   | `optional[text]`               |
| `email`                                   | The primary email address of the customer.     | `optional[text]`               |
| `phone`                                   | The primary phone number of the customer.      | `optional[text]`               |
| `website`                                 | The customer's website URL.                    | `optional[text]`               |
| [`billing_address`](#quickbooks-address)  | The billing address of the customer.           | `optional[quickbooks address]` |
| [`shipping_address`](#quickbooks-address) | The shipping address of the customer.          | `optional[quickbooks address]` |
| `account_number`                          | The customer's account number.                 | `optional[text]`               |
| `balance`                                 | The current balance owed by the customer.      | `optional[number]`             |
| `default_terms`                           | The default payment terms for the customer.    | `optional[text]`               |
| `is_active`                               | Whether the customer is currently active.      | `optional[boolean]`            |

### Quickbooks invoice

A created QuickBooks Invoice.

| Field Name                                  | Description                                         | Type                                                                                          |
| ------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                        | The unique identifier of the invoice in QuickBooks. | `text`                                                                                        |
| `doc_number`                                | The document number of the invoice.                 | `text`                                                                                        |
| `customer_name`                             | The name of the customer.                           | `text`                                                                                        |
| `total_amount`                              | The total amount of the invoice.                    | `number`                                                                                      |
| `balance`                                   | The current balance of the invoice from QuickBooks. | `number`                                                                                      |
| `invoice_date`                              | The invoice date.                                   | `optional[text]`                                                                              |
| `due_date`                                  | The due date.                                       | `optional[text]`                                                                              |
| `terms`                                     | The sales terms name.                               | `optional[text]`                                                                              |
| `items`                                     | List of invoice line items.                         | `optional[list of list of quickbooks sales item line` or `quickbooks description only line?]` |
| [`custom_fields`](#quickbooks-custom-field) | List of custom fields associated with the invoice.  | `optional[list of quickbooks custom field]`                                                   |
| `created_time`                              | When the invoice was created.                       | `optional[text]`                                                                              |
| `last_updated`                              | When the invoice was last updated                   | `optional[text]`                                                                              |

### Quickbooks item

A QuickBooks item (product, service, or category).

| Field Name                                                    | Description                                                         | Type                |
| ------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------- |
| `id`                                                          | The unique identifier for the item                                  | `text`              |
| `name`                                                        | The name of the item                                                | `text`              |
| `type`                                                        | The type of item (Service, Inventory, NonInventory, Category, etc.) | `text`              |
| `sku`                                                         | The SKU code for the item                                           | `optional[text]`    |
| `description`                                                 | Description of the item                                             | `optional[text]`    |
| `unit_price`                                                  | The unit price for sales                                            | `optional[number]`  |
| `purchase_cost`                                               | The cost to purchase the item                                       | `optional[number]`  |
| `qty_on_hand`                                                 | Quantity on hand (for inventory items)                              | `optional[number]`  |
| [`income_account_ref`](#income_account_ref-quickbooks-item)   | Reference to the income account                                     | `optional[json]`    |
| [`expense_account_ref`](#expense_account_ref-quickbooks-item) | Reference to the expense account                                    | `optional[json]`    |
| [`asset_account_ref`](#asset_account_ref-quickbooks-item)     | Reference to the asset account                                      | `optional[json]`    |
| [`parent_ref`](#parent_ref-quickbooks-item)                   | Reference to the parent category (for sub-categories)               | `optional[json]`    |
| `is_active`                                                   | Whether the item is active                                          | `optional[boolean]` |
| `sync_token`                                                  | The sync token for updates                                          | `optional[text]`    |
| `created_time`                                                | The timestamp when the item was created                             | `optional[text]`    |
| `last_updated`                                                | The timestamp when the item was last updated                        | `optional[text]`    |
| `taxable`                                                     | Whether the item is taxable                                         | `optional[boolean]` |
| `fully_qualified_name`                                        | The fully qualified name of the item                                | `optional[text]`    |
| `purchase_desc`                                               | Purchase description of the item                                    | `optional[text]`    |
| `track_qty_on_hand`                                           | Whether to track quantity on hand                                   | `optional[boolean]` |
| `inv_start_date`                                              | The inventory start date (for inventory items)                      | `optional[text]`    |
| `domain`                                                      | The domain of the item                                              | `optional[text]`    |
| `sparse`                                                      | Whether the item is sparse                                          | `optional[boolean]` |

### Quickbooks report

A QuickBooks report with its header, columns, and grouped table sections.This concept represents quickbooks reports, where data is organized into logical groupings.

| Field Name                              | Description                                                      | Type                                                                                        |
| --------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `report_type`                           | The type of report that was generated                            | `enum[account_list_detail, ap_detail, ap_summary, ar_detail, ar_summary, transaction_list]` |
| `header`                                | Header information containing report metadata                    | `json`                                                                                      |
| [`columns`](#columns-quickbooks-report) | Column definitions for the report                                | `list of json`                                                                              |
| [`tables`](#tables-quickbooks-report)   | List of table sections, each representing a grouped data section | `list of json`                                                                              |
| Name   | Type             |
| ------ | ---------------- |
| `id`   | `optional[text]` |
| `name` | `optional[text]` |
| Name   | Type             |
| ------ | ---------------- |
| `id`   | `optional[text]` |
| `name` | `optional[text]` |
| Name   | Type             |
| ------ | ---------------- |
| `id`   | `optional[text]` |
| `name` | `optional[text]` |
| Name   | Type             |
| ------ | ---------------- |
| `id`   | `optional[text]` |
| `name` | `optional[text]` |
| Name   | Type             |
| ------ | ---------------- |
| `id`   | `optional[text]` |
| `name` | `optional[text]` |
| Name   | Type             |
| ------ | ---------------- |
| `id`   | `optional[text]` |
| `name` | `optional[text]` |
| Name   | Type             |
| ------ | ---------------- |
| `id`   | `optional[text]` |
| `name` | `optional[text]` |
| Name   | Type             |
| ------ | ---------------- |
| `id`   | `optional[text]` |
| `name` | `optional[text]` |
| Name        | Type             |
| ----------- | ---------------- |
| `col_type`  | `text`           |
| `col_title` | `text`           |
| `metadata`  | `optional[json]` |
| Name       | Type             |
| ---------- | ---------------- |
| `header`   | `text`           |
| `data`     | `table`          |
| `type`     | `text`           |
| `group`    | `optional[text]` |
| `raw_data` | `optional[json]` |
