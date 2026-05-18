---
title: Excel
updated: 2026-03-20T14:12
git_hash: 950017423423f62a68f154b4ee1e5e2c86977910
description: Overview of the Excel integration.
icon: file-excel
---

# Excel

{% hint style="info" %}
The following documentation is for **Excel v1.3.3**.
{% endhint %}

## Overview

Enables reading, creating, and modifying offline Excel files (xlsx, xlsm, xls, xlsb) without requiring a network connection or Microsoft account. This integration provides file-based spreadsheet operations for agents that need to work with Excel files directly. It supports creating new spreadsheets, reading worksheet data, extracting structured tables, managing worksheets (add, remove, copy, rename), cell-level reads and writes, row and column insertion, bulk cell updates, and formula insertion across row ranges. Read support covers all major Excel formats (.xlsx, .xlsm, .xls, .xlsb). Write and modification operations are supported for .xlsx and .xlsm formats only.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Excel**

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

Add a name for the connection. You'll be prompted for [**authentication**](excel-standalone.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Actions

The following actions are available in the **Excel** integration:

### 1. Add a filter to a worksheet

Add auto-filter to a worksheet.

### 2. Add a worksheet to an excel

Add an empty worksheet to an Excel file.

### 3. Add data validation to a worksheet

Add data validation to a range of cells.

### 4. Append data to a range

Append data from a table at a specific cell position.

### 5. Append data to a worksheet

Append rows from a table to the end of a worksheet.

### 6. Autofill a range in a worksheet

Auto-fill a target range based on the pattern in the source range.

### 7. Copy a worksheet in the excel

Copy a worksheet within an Excel file.

### 8. Create an excel

Create a new Excel file with one or more worksheets.

### 9. Delete columns from a worksheet

Delete one or more columns from a worksheet.

### 10. Delete rows from a worksheet

Delete one or more rows from a worksheet.

### 11. Export a worksheet to csv

Export a worksheet to CSV or TSV format.

### 12. Extract a table from a worksheet

Extract a structured table from a worksheet.

### 13. Format cells in a worksheet

Format cells in a worksheet with background color, font color, weight, and size.

### 14. Get a cell's value from a worksheet

Get the value of a specific cell from a worksheet.

### 15. Get a range from a worksheet

Get cell values from a range in a worksheet.

### 16. Get a worksheet's cell's formula

Get the formula from a specific cell in a worksheet.

### 17. Get an excel's worksheet

Get a single worksheet from an Excel file by name.

### 18. Get an excel's worksheet names

Get the list of worksheet names from an Excel file.

### 19. Get an excel's worksheets

Get all worksheets from an Excel file at once.

### 20. Insert a formula into an excel

Insert formulas into a column across a range of rows.

### 21. Insert a table into a worksheet

Insert a table into a worksheet at a specified location.

### 22. Insert a vlookup formula into a worksheet

Insert a VLOOKUP formula into a cell.

### 23. Insert columns into a worksheet

Insert one or more columns into a worksheet.

### 24. Insert rows into a worksheet

Insert one or more rows into a worksheet.

### 25. Merge cells in a worksheet

Merge cells in a worksheet.

### 26. Protect a worksheet

Protect a worksheet from editing.

### 27. Read content from an excel

Read the content of an Excel, CSV, or TSV file as a markdown string.

### 28. Remove a worksheet

Remove a worksheet from an Excel file.

### 29. Rename a worksheet in the excel

Rename a worksheet in an Excel file.

### 30. Replace values in a worksheet

Find and replace text values in a worksheet.

### 31. Set a worksheet's cell to a string

Set the value of a cell in a worksheet.

### 32. Sort a worksheet

Sort rows in a worksheet by a specified column.

### 33. Split a column in a worksheet

Split text in a column into multiple columns by a delimiter.

### 34. Unmerge cells in a worksheet

Unmerge previously merged cells in a worksheet.

### 35. Unprotect a worksheet

Remove protection from a worksheet.

### 36. Update an excel's cell values

Update multiple cell values in a worksheet at once.

## Concepts

### Excel table

A structured data table extracted from an Excel worksheet, with named columns and typed rows.This class represents a table that was extracted from a worksheet. It contains the table data and extraction context.

| Field Name          | Description                                                 | Type             |
| ------------------- | ----------------------------------------------------------- | ---------------- |
| `data`              | PyArrow table containing the extracted table data           | `table`          |
| `source_worksheet`  | Name of the worksheet this table was extracted from         | `optional[text]` |
| `location`          | Cell range where table was found (e.g., "A1:D10")           | `optional[text]` |
| `extraction_method` | How the table was extracted ("location", "headers", "full") | `optional[text]` |

### Excel worksheet

A single sheet within an Excel workbook containing rows and columns of cell data.This class contains the worksheet data and basic identifying information. Metadata (row_count, column_count) is computed from data, not stored separately.

| Field Name        | Description                                                  | Type               |
| ----------------- | ------------------------------------------------------------ | ------------------ |
| `name`            | Name of the worksheet                                        | `text`             |
| `data`            | PyArrow table containing the worksheet data                  | `table`            |
| `excel_file_name` | Name of the parent Excel file (string reference, not object) | `text`             |
| `_row_count`      | Cached row count (computed from data)                        | `optional[number]` |
| `_column_count`   | Cached column count (computed from data)                     | `optional[number]` |
