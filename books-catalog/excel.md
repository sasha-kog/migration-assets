---
title: Excel (online)
updated: 2026-03-20T14:12
git_hash: 80bbd59dcfc250966dba4d99ada0fef612c9191a
description: Overview of the Excel (online) integration.
icon: microsoft
---

# Excel (online)

{% hint style="info" %}
The following documentation is for **Excel (online) v2.6.0**.
{% endhint %}

## Overview

Enables interacting with and managing Excel Online files and spreadsheets via the Microsoft Graph API. Excel offers powerful capabilities for data analysis, visualization, and automation, making it ideal for teams that need reliable, high-volume spreadsheet operations. This integration gives agents seamless access to worksheet management, bulk range and table updates, formulas, formatting, sorting, filtering, protection, pivot refresh, and recalculation for accurate, real-time data handling.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Excel (online)**

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

Add a name for the connection. You'll be prompted for [**authentication**](excel.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Client ID, Client Secret and Tenant ID

Connect to the Microsoft Graph API using the provided client credentials.

| Label         | Description                                                  | Type        |
| ------------- | ------------------------------------------------------------ | ----------- |
| Client ID     | The client ID of the application registered in Azure AD.     | `text`      |
| Client Secret | The client secret of the application registered in Azure AD. | `sensitive` |
| Tenant ID     | The tenant ID of the Azure AD directory.                     | `text`      |

### Connect using Client ID, Certificate and Tenant ID

Connect to the Microsoft Graph API using certificate credentials.

| Label       | Description                                                                           | Type        |
| ----------- | ------------------------------------------------------------------------------------- | ----------- |
| Client ID   | The client ID of the application registered in Azure AD.                              | `text`      |
| Certificate | PEM-encoded X.509 certificate string containing both the certificate and private key. | `sensitive` |
| Tenant ID   | The tenant ID of the Azure AD directory.                                              | `text`      |

### Connect using Client ID, Certificate, Private Key and Tenant ID

Connect to the Microsoft Graph API using certificate and private key.

| Label       | Description                                              | Type        |
| ----------- | -------------------------------------------------------- | ----------- |
| Client ID   | The client ID of the application registered in Azure AD. | `text`      |
| Certificate | PEM-encoded certificate string.                          | `sensitive` |
| Private Key | PEM-encoded private key string.                          | `sensitive` |
| Tenant ID   | The tenant ID of the Azure AD directory.                 | `text`      |

## Actions

The following actions are available in the **Excel (online)** integration:

### 1. Clear all filters on the table

Clear all filters on a table.

### 2. Clear the filter on the table's column

Clear the filter on a specific table column.

### 3. Clear the worksheet range

Delete the contents of a range of cells in an Excel worksheet.

### 4. Copy the sheet with a name

Copy a worksheet's content to a new sheet in the same workbook.

### 5. Create a new sheet in the file

Create a new worksheet in an Excel workbook.

### 6. Create a table on a worksheet range

Create a table from a specified range of cells in an Excel worksheet.

### 7. Create a worksheet range in a sheet

Create a range reference for a set of cells in an Excel worksheet, defined by start and end cell addresses. This does not modify the spreadsheet; it creates a local reference that can be used with other procedures to read, write, or clear data.

### 8. Create a workbook in a folder

Create a new empty Excel workbook in a SharePoint or OneDrive folder.

### 9. Delete a column from the table

Delete a column from a table in an Excel worksheet.

### 10. Delete a row from the table

Delete a row from a table in an Excel worksheet.

### 11. Delete the sheet

Delete a worksheet from an Excel workbook.

### 12. Filter the table's column by a filter value

Apply a value-based filter to a table column.

### 13. Get the cell's color

Get the background color of a cell in an Excel worksheet.

### 14. Get the cell's formula

Get the formula of a cell in an Excel worksheet.

### 15. Get the cell's number format

Get the number format string of a cell in an Excel worksheet.

### 16. Get the cell's value

Get the value of a cell in an Excel worksheet.

### 17. Get the column count in a table

Get the number of columns in a table in an Excel worksheet.

### 18. Get the column count in a worksheet range

Get the number of columns in an Excel worksheet range.

### 19. Get the column's cells from the table

Get the cells from a column in a table in an Excel worksheet.

### 20. Get the file's sheets

Get the worksheets of an Excel file.

### 21. Get the following row range in a worksheet range

Get a range representing the row immediately below the given range, spanning the same columns. Useful for appending data below an existing range or table.

### 22. Get the row count in a table

Get the number of rows in a table in an Excel worksheet.

### 23. Get the row count in a worksheet range

Get the number of rows in an Excel worksheet range.

### 24. Get the row's cells from the table

Get the cells from a row in a table in an Excel worksheet.

### 25. Get the row's cells from the worksheet range

Get the cells from a row in an Excel worksheet range.

### 26. Get the sheet's pivot tables

Get the pivot tables from an Excel worksheet.

### 27. Get the sheet's protection status

Get the protection status of a worksheet.

### 28. Get the sheet's tables

Get the tables from an Excel worksheet.

### 29. Get the sheet's used range

Get the used range of an Excel worksheet.

### 30. Get the worksheet range's rows

Get the rows from a range in an Excel worksheet.

### 31. Get the worksheet range from the table

Get the range of a table in an Excel worksheet.

### 32. Insert a new column in the table

Insert a new column within a table in an Excel worksheet.

### 33. Insert a new row in the table

Insert a new row in a table in an Excel worksheet.

### 34. Open a workbook at a url

Open an Excel workbook by its SharePoint or OneDrive URL, returning its sheets.

### 35. Protect the sheet

Protect a worksheet from editing.

### 36. Read the content from a table

Read the contents of a table in an Excel worksheet.

### 37. Read the content from a worksheet range

Read the contents of a range in an Excel worksheet.

### 38. Recalculate the workbook

Force a full recalculation of all formulas in the workbook.

### 39. Refresh all pivot tables in the sheet

Refresh all pivot tables in a worksheet.

### 40. Refresh the pivot table

Refresh a specific pivot table.

### 41. Rename the sheet to a new name

Rename a worksheet in an Excel workbook.

### 42. Retrieve the columns from the table

Get the columns from a table in an Excel worksheet.

### 43. Retrieve the rows from the table

Get the rows from a table in an Excel worksheet.

### 44. Set the cell's content to a value

Update the value of a cell in an Excel worksheet.

### 45. Set the cell's formula to a formula value

Update the formula of a cell in an Excel worksheet.

### 46. Set the cell's number format to a format string

Set the number format of a cell in an Excel worksheet.

### 47. Set the worksheet range's number format to a format string

Set a uniform number format on all cells in a range.

### 48. Sort the table by a column index

Sort a table by a specified column.

### 49. Sort the worksheet range by a column index

Sort a range by a specified column.

### 50. Unprotect the sheet

Remove protection from a worksheet.

### 51. Write the content in a table

Update the contents of an Excel table with new data.

### 52. Write the content in a worksheet range

Update the contents of a range in an Excel worksheet.

## Concepts

### Excel table reference

ExcelTableRef represents a reference to a table within an Excel worksheet, providing essential details to uniquely identify and interact with specific tables. This utility is used to facilitate data management, structured data handling, and integration within larger workflows.

| Field Name | Description                                                  | Type   |
| ---------- | ------------------------------------------------------------ | ------ |
| `id`       | The unique identifier for the worksheet.                     | `text` |
| `name`     | The name of the worksheet.                                   | `text` |
| `drive_id` | The unique identifier for the drive containing the workbook. | `text` |
| `file_id`  | The unique identifier for the workbook.                      | `text` |
| `sheet_id` | The unique identifier for the worksheet.                     | `text` |

### Excel column reference

ExcelColumnRef represents a reference to a specific column within an Excel worksheet. It serves as a utility to uniquely identify and interact with data in a column, providing essential metadata that allows for efficient data manipulation and retrieval.

| Field Name | Description                           | Type     |
| ---------- | ------------------------------------- | -------- |
| `id`       | The unique identifier for the column. | `text`   |
| `index`    | The index of the column.              | `number` |

### Excel range reference

ExcelRangeRef represents a reference to a range of cells within an Excel worksheet. It provides detailed information about a contiguous set of cells and is designed for use in applications that require precise range-based operations, such as data extraction, modification, and analysis within spreadsheets.

| Field Name      | Description                                                  | Type                |
| --------------- | ------------------------------------------------------------ | ------------------- |
| `drive_id`      | The unique identifier for the drive containing the workbook. | `text`              |
| `file_id`       | The unique identifier for the workbook.                      | `text`              |
| `sheet_id`      | The unique identifier for the worksheet.                     | `text`              |
| `address`       | The address of the range.                                    | `text`              |
| `address_local` | The local address of the range.                              | `optional[text]`    |
| `cell_count`    | The number of cells in the range.                            | `optional[number]`  |
| `column_count`  | The number of columns in the range.                          | `optional[number]`  |
| `column_hidden` | Whether the columns in the range are hidden.                 | `optional[boolean]` |
| `column_index`  | The index of the first column in the range.                  | `optional[number]`  |
| `hidden`        | Whether the range is hidden.                                 | `optional[boolean]` |
| `row_count`     | The number of rows in the range.                             | `optional[number]`  |
| `row_hidden`    | Whether the rows in the range are hidden.                    | `optional[boolean]` |
| `row_index`     | The index of the first row in the range.                     | `optional[number]`  |

### Excel sheet reference

ExcelSheetRef represents a reference to a worksheet within an Excel workbook, providing details to uniquely identify and interact with a specific sheet. It facilitates precise data manipulation and integration, useful for data processing, automated workflows, and integration across multiple files.

| Field Name | Description                                                  | Type   |
| ---------- | ------------------------------------------------------------ | ------ |
| `id`       | The unique identifier for the worksheet.                     | `text` |
| `name`     | The name of the worksheet.                                   | `text` |
| `drive_id` | The unique identifier for the drive containing the workbook. | `text` |
| `file_id`  | The unique identifier for the workbook.                      | `text` |

### Sharepoint file reference

A Sharepoint File Reference is a reference to a file in a SharePoint document library.

| Field Name                                                        | Description                                                                                                                          | Type                |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| `id`                                                              | The unique identifier for the document library.                                                                                      | `optional[text]`    |
| `name`                                                            | The name of the document library.                                                                                                    | `optional[text]`    |
| `web_url`                                                         | URL that either displays the resource in the browser (for Office file formats), or is a direct link to the file (for other formats). | `optional[text]`    |
| [`parent_reference`](#parent_reference-sharepoint-file-reference) | Parent information, if the item has a parent.                                                                                        | `optional[json]`    |
| `is_folder`                                                       | Boolean flag indicating whenever this item is a folder or not.                                                                       | `optional[boolean]` |
| `file_name`                                                       | The name of the file. Same as name.                                                                                                  | `optional[text]`    |

### Sharepoint folder reference

A Sharepoint Folder Reference is a reference to a folder in a SharePoint document library.

| Field Name                                                          | Description                                                                                                                          | Type                |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| `id`                                                                | The unique identifier for the document library.                                                                                      | `optional[text]`    |
| `name`                                                              | The name of the document library.                                                                                                    | `optional[text]`    |
| `web_url`                                                           | URL that either displays the resource in the browser (for Office file formats), or is a direct link to the file (for other formats). | `optional[text]`    |
| [`parent_reference`](#parent_reference-sharepoint-folder-reference) | Parent information, if the item has a parent.                                                                                        | `optional[json]`    |
| `is_folder`                                                         | Boolean flag indicating whenever this item is a folder or not.                                                                       | `optional[boolean]` |
| `folder_name`                                                       | The name of the folder. Same as name.                                                                                                | `optional[text]`    |

### Excel row reference

ExcelRowRef represents a reference to a specific row within an Excel worksheet. This utility enables efficient access, manipulation, and reference of data within rows, providing essential information to uniquely identify and interact with a row's content.

| Field Name | Description                        | Type     |
| ---------- | ---------------------------------- | -------- |
| `id`       | The unique identifier for the row. | `text`   |
| `index`    | The index of the row.              | `number` |

### Excel pivot table reference

ExcelPivotTableRef represents a reference to a pivot table within an Excel worksheet.Graph API is read-only for pivot tables: list and refresh only. Cannot create, modify, or delete pivot tables via the API.

| Field Name | Description                                                  | Type   |
| ---------- | ------------------------------------------------------------ | ------ |
| `id`       | The unique identifier for the pivot table.                   | `text` |
| `name`     | The name of the pivot table.                                 | `text` |
| `drive_id` | The unique identifier for the drive containing the workbook. | `text` |
| `file_id`  | The unique identifier for the workbook.                      | `text` |
| `sheet_id` | The unique identifier for the worksheet.                     | `text` |

### Excel cell reference

ExcelCellRef represents a reference to a specific cell within an Excel worksheet, serving as a utility to uniquely identify and manipulate data within the cell. It provides essential details to locate the cell precisely.

| Field Name     | Description                                       | Type             |
| -------------- | ------------------------------------------------- | ---------------- |
| `drive_id`     | The unique identifier for the drive.              | `text`           |
| `file_id`      | The unique identifier for the file.               | `text`           |
| `sheet_id`     | The unique identifier for the sheet.              | `text`           |
| `row_index`    | The row of the cell.                              | `number`         |
| `column_index` | The column of the cell.                           | `number`         |
| `id`           | The unique identifier for the cell.               | `optional[text]` |
| `row_id`       | The unique identifier for the row of the cell.    | `optional[text]` |
| `column_id`    | The unique identifier for the column of the cell. | `optional[text]` |
| `address`      | The address of the cell.                          | `optional[text]` |
| `table_id`     | The unique identifier for the table.              | `optional[text]` |
| Name       | Type             |
| ---------- | ---------------- |
| `id`       | `optional[text]` |
| `drive_id` | `optional[text]` |
| Name       | Type             |
| ---------- | ---------------- |
| `id`       | `optional[text]` |
| `drive_id` | `optional[text]` |
