---
title: PDF
updated: 2026-03-20T14:12
git_hash: 8d0b968d0ff046933ab602124b2a6dd8f4c11066
description: Overview of the PDF integration.
icon: file-pdf
---

# PDF

{% hint style="info" %}
The following documentation is for **PDF v1.8.0**.
{% endhint %}

## Overview

Enables converting PDF files to other formats.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **PDF**

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

Add a name for the connection. You'll be prompted for [**authentication**](pdf.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Actions

The following actions are available in the **PDF** integration:

### 1. Convert a pdf file to docx

Convert a PDF file to DOCX format.

### 2. Extract pages from a pdf

Extracts specific pages from a PDF file to create a new PDF.

### 3. Get a pdf's fields

Gets all form fields from a PDF file.

### 4. Get a pdf's labels

Gets all text labels (text spans) from a PDF file.

### 5. Get a pdf's lines

Gets all text lines from a PDF file.

### 6. Get a pdf's page count

Gets the total number of pages in a PDF file.

### 7. Read a pdf file

Read text from a PDF file, optionally by page.

### 8. Remove duplicates from a pdf

Removes duplicate pages from a PDF based on text similarity.

### 9. Set a pdf field's value

Sets the value of a form field in a PDF.

## Concepts

### Pdf

Configuration for PDF to DOCX conversion.All fields have optimal defaults. Override specific values as needed.

| Field Name                       | Description                                         | Type                |
| -------------------------------- | --------------------------------------------------- | ------------------- |
| `debug`                          | Set to True for debugging layout issues             | `optional[boolean]` |
| `ignore_page_error`              | Continue conversion even if a page fails            | `optional[boolean]` |
| `parse_lattice_table`            | Parse tables with visible borders                   | `optional[boolean]` |
| `parse_stream_table`             | Parse tables without visible borders                | `optional[boolean]` |
| `extract_stream_table`           | Extract stream tables separately                    | `optional[boolean]` |
| `clip_image_res_ratio`           | Resolution ratio (4x = 288dpi from 72dpi base)      | `optional[number]`  |
| `min_section_height`             | Minimum height for a valid section                  | `optional[number]`  |
| `max_line_spacing_ratio`         | Maximum line spacing ratio                          | `optional[number]`  |
| `line_overlap_threshold`         | Delete overlapping lines (higher = less aggressive) | `optional[number]`  |
| `line_break_width_ratio`         | Break line if too narrow                            | `optional[number]`  |
| `line_break_free_space_ratio`    | Break line if too much free space                   | `optional[number]`  |
| `line_separate_threshold`        | Distance threshold for separate lines               | `optional[number]`  |
| `new_paragraph_free_space_ratio` | New paragraph threshold                             | `optional[number]`  |
| `lines_left_aligned_threshold`   | Left alignment threshold (points)                   | `optional[number]`  |
| `lines_right_aligned_threshold`  | Right alignment threshold (points)                  | `optional[number]`  |
| `lines_center_aligned_threshold` | Center alignment threshold (points)                 | `optional[number]`  |
| `connected_border_tolerance`     | Border connection tolerance                         | `optional[number]`  |
| `max_border_width`               | Maximum border width                                | `optional[number]`  |
| `min_border_clearance`           | Minimum clearance between borders                   | `optional[number]`  |
| `page_margin_factor_top`         | Top margin reduction factor [0,1]                   | `optional[number]`  |
| `page_margin_factor_bottom`      | Bottom margin reduction factor [0,1]                | `optional[number]`  |
| `shape_min_dimension`            | Ignore shapes smaller than this                     | `optional[number]`  |
| `float_image_ignorable_gap`      | Float image gap threshold                           | `optional[number]`  |
| `min_svg_gap_dx`                 | Merge vector graphics horizontal gap                | `optional[number]`  |
| `min_svg_gap_dy`                 | Merge vector graphics vertical gap                  | `optional[number]`  |
| `min_svg_w`                      | Minimum SVG width                                   | `optional[number]`  |
| `min_svg_h`                      | Minimum SVG height                                  | `optional[number]`  |
| `delete_end_line_hyphen`         | Keep hyphens at line ends                           | `optional[boolean]` |
| `multi_processing`               | Enable for faster conversion of large files         | `optional[boolean]` |
| `cpu_count`                      | 0 = use all CPUs, or specify number                 | `optional[number]`  |

### Pdf field

Represents a form field extracted from a PDF.

| Field Name | Description                                     | Type             |
| ---------- | ----------------------------------------------- | ---------------- |
| `name`     | The field name                                  | `text`           |
| `value`    | The current field value                         | `optional[text]` |
| `type`     | The field type (text, checkbox, combobox, etc.) | `text`           |
| `page`     | Page number (0-indexed)                         | `number`         |
| `bbox`     | Bounding box coordinates                        | `json`           |

### Pdf bounding box

Represents the bounding box coordinates for a PDF element.

| Field Name | Description         | Type     |
| ---------- | ------------------- | -------- |
| `x0`       | Left x-coordinate   | `number` |
| `y0`       | Top y-coordinate    | `number` |
| `x1`       | Right x-coordinate  | `number` |
| `y1`       | Bottom y-coordinate | `number` |

### Pdf label

Represents a text label (text span) extracted from a PDF.

| Field Name | Description              | Type     |
| ---------- | ------------------------ | -------- |
| `text`     | The label text content   | `text`   |
| `page`     | Page number (0-indexed)  | `number` |
| `bbox`     | Bounding box coordinates | `json`   |

### Pdf line

Represents a text line extracted from a PDF.

| Field Name | Description              | Type     |
| ---------- | ------------------------ | -------- |
| `text`     | The complete line text   | `text`   |
| `page`     | Page number (0-indexed)  | `number` |
| `bbox`     | Bounding box coordinates | `json`   |
