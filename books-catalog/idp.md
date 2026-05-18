---
title: Intelligent Document Processing (IDP)
updated: 2026-03-31T14:46
git_hash: b5b3ee4c39bd614fde610fa6943fd09d76df72c8
description: Overview of the Intelligent Document Processing (IDP) integration.
icon: grid-2
---

# Intelligent Document Processing (IDP)

{% hint style="info" %}
The following documentation is for **Intelligent Document Processing (IDP) v4.15.11**.
{% endhint %}

## Overview

Intelligent Document Processing (IDP) extracts structured data from documents using AI. This integration enables automated document analysis, data extraction, and intelligent processing workflows.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Intelligent Document Processing (IDP)**

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

Add a name for the connection. You'll be prompted for [**authentication**](idp.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Credentials

### 1. Anthropic API Key

Follow these steps to obtain your **Anthropic API key**:

{% stepper %}
{% step %}
#### Log in to the Anthropic Console

Go to the [**Anthropic Console**](https://console.anthropic.com) and log in with your credentials.
{% endstep %}

{% step %}
#### Navigate to API Keys

Go to **Settings** > **API Keys**. Then click **+ Create Key** in the top right.
{% endstep %}

{% step %}
#### Configuration

Select a workspace and give your key a descriptive name (e.g., "Development Key" or "Production App"). Then, click **Add** to generate your API key.
{% endstep %}

{% step %}
#### Copy and Store Your Key

Copy your API key immediately and store it securely. You won't be able to view it again after closing the dialog.
{% endstep %}
{% endstepper %}

### 2. OpenAI API Key

Follow these steps to obtain your **OpenAI API key**:

{% stepper %}
{% step %}
#### Log In to OpenAI

Navigate to the [OpenAI Platform](https://auth.openai.com/log-in) and log in with your credentials.
{% endstep %}

{% step %}
#### API Keys

Open **Account Settings**, then navigate to [**API Keys**](https://platform.openai.com/account/api-keys)**.**&#x20;
{% endstep %}

{% step %}
#### Generate a New API Key

Click **Create new secret key**. Copy the key immediately — it will only be shown once.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using API Key

Connect to Anthropic API for document processing.

| Label   | Description           | Type        |
| ------- | --------------------- | ----------- |
| API Key | The Anthropic API key | `sensitive` |

### Connect using Service Account Credentials and Region

Connect to Google Vertex AI (Gemini) API for document processing.

| Label                       | Description                                           | Type        |
| --------------------------- | ----------------------------------------------------- | ----------- |
| Service Account Credentials | The Google service account credentials JSON as string | `sensitive` |
| Region                      | The Google Cloud region                               | `text`      |

### Connect using API Key

Connect to OpenAI API for document processing.

| Label   | Description        | Type        |
| ------- | ------------------ | ----------- |
| API Key | The OpenAI API key | `sensitive` |

## Actions

The following actions are available in the **Intelligent Document Processing (IDP)** integration:

### 1. Analyze a thing

Analyze a document to extract its structure and content.

### 2. Classify a thing

Classify a document against user-defined topics or rules.

### 3. Extract data from a thing

Extract data from a document using field specifications.

### 4. Extract data from the documents

Extract data from multiple documents in a single LLM call.

### 5. Extract pages from a thing

Extract specified pages from a document.

### 6. Extract subdocument from a thing

Extract a subdocument from a document based on page numbers or markers.

### 7. Extract subdocuments from a thing

Extract subdocuments from a document based on markers or fixed size with overlap.

### 8. Extract table from a thing

Extract table from a document using field specifications.

### 9. Merge pages into a document

Merge multiple page documents into a single consolidated document.

### 10. Merge subdocuments into a document

Merge multiple subdocuments into a single consolidated document.

### 11. Read content from a thing

Read/extract text content from a document.

## Concepts

### Document analysis specification

Input for document analysis (schema-free extraction).All fields are optional.

| Field Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `llm_model`               | \[Optional, default: provider default] LLM model to use. Provider defaults: gemini-2.5-pro, gpt-4o, claude-sonnet-4-5.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `optional[text]`              |
| `analysis_mode`           | \[Optional, default: "single\_pass"] Analysis mode. - "single\_pass": Sequential per-page extraction (simplest) - "parallel": Parallel extraction with smart deduplication - "plan\_based": Plan-based extraction (best for complex docs)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `optional[text]`              |
| `verify`                  | \[Optional, default: False] If True, performs cross-model verification to detect hallucinations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `optional[boolean]`           |
| `verification_strictness` | \[Optional, default: "high"] Strictness level for verification. Options: "high", "moderate", "low".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `optional[text]`              |
| `dpi`                     | \[Optional, default: 150] DPI for image processing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `optional[number?` or `text]` |
| `confidence_threshold`    | \[Optional, default: 0] Minimum confidence score (0-100) for extracted elements. Behavior: - When set to 0 (default): No threshold checking. All elements are returned regardless of confidence. Caller can inspect the `confidence` attribute on individual entities, key\_value\_pairs, and tables to decide how to handle low-confidence data. - When set to 1-100: Acts as a hard limit. If ANY element (entity, key-value pair, or table) has confidence below this threshold, raises AnalysisError. The exception contains: - `analysis`: The full DocumentAnalysis result (still usable) - `low_confidence_elements`: List of elements that failed - `threshold`: The threshold value that was not met Example: Set confidence\_threshold=80 to fail if any element has confidence below 80. Catch AnalysisError to access both the full result and the list of problematic elements. | `optional[number]`            |

### Idp document analysis

Complete analysis of a document.This is the output of schema-free document analysis, containing all detected elements including entities, tables, forms, and structure. All elements have a consistent structure with: - element\_type: For UI discrimination after serialization - page\_number: Page where element was found (1-indexed) - bounding\_box: Optional location on page - confidence: Optional confidence score (0-100)

| Field Name                                                        | Description                                                      | Type                                    |
| ----------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------- |
| `result_type`                                                     | Top-level discriminator for API response type.                   | `optional[text]`                        |
| `document_type`                                                   | The type of document (e.g., invoice, receipt, form).             | `optional[text]`                        |
| `document_title`                                                  | The title of the document if detected.                           | `optional[text]`                        |
| `source`                                                          | The source file name or identifier.                              | `optional[text]`                        |
| [`key_value_pairs`](idp.md#key_value_pairs-idp-document-analysis) | List of key-value pairs extracted from the document.             | `optional[list of json]`                |
| [`tables`](idp.md#idp-extracted-table)                            | List of tables detected in the document.                         | `optional[list of idp extracted table]` |
| [`forms`](idp.md#forms-idp-document-analysis)                     | List of forms detected in the document.                          | `optional[list of json]`                |
| [`entities`](idp.md#entities-idp-document-analysis)               | List of named entities extracted from the document.              | `optional[list of json]`                |
| [`text_blocks`](idp.md#text_blocks-idp-document-analysis)         | List of text blocks/paragraphs in the document.                  | `optional[list of json]`                |
| [`lists`](idp.md#lists-idp-document-analysis)                     | List of bulleted or numbered lists in the document.              | `optional[list of json]`                |
| `full_text`                                                       | Full text content from markdown normalization.                   | `optional[text]`                        |
| `confidence`                                                      | Overall confidence score for the analysis (0-100).               | `optional[number]`                      |
| `verified`                                                        | Whether the analysis has been verified.                          | `optional[boolean]`                     |
| `hallucinations_detected`                                         | Whether hallucinations were detected during verification.        | `optional[boolean]`                     |
| `analysis_mode`                                                   | The analysis mode used (single\_pass, parallel, or plan\_based). | `optional[text]`                        |
| [`metrics`](idp.md#metrics-idp-document-analysis)                 | Document processing metrics (num\_pages, etc.).                  | `optional[json]`                        |

### Idp extracted table

A detected table in the document.This class is returned by both extract\_table\_from\_thing (directly) and analyze\_thing (as part of DocumentAnalysis.tables).

| Field Name                                                | Description                                               | Type                     |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------ |
| `element_type`                                            | Always "table" regardless of which procedure produced it. | `optional[text]`         |
| `page_number`                                             | Page number where table was found (1-indexed).            | `optional[number]`       |
| [`bounding_box`](idp.md#bounding_box-idp-extracted-table) | Location of table on the page.                            | `optional[json]`         |
| `confidence`                                              | Confidence score (0-100).                                 | `optional[number]`       |
| `is_handwritten`                                          | Whether the table appears to be handwritten.              | `optional[boolean]`      |
| `title`                                                   | Table title/caption.                                      | `optional[text]`         |
| `headers`                                                 | Column headers if detected.                               | `optional[list of text]` |
| `rows`                                                    | Table rows (list of cell values).                         | `optional[list of text]` |
| `num_rows`                                                | Number of rows.                                           | `optional[number]`       |
| `num_cols`                                                | Number of columns.                                        | `optional[number]`       |
| `arrow_table`                                             | PyArrow Table representation of the data.                 | `optional[table?]`       |
| [`verification`](idp.md#verification-idp-extracted-table) | Verification result if verify=True was used.              | `optional[json]`         |

### Idp classification input

Input for document classification.All fields are optional. At least one of topics, prompt, or classification\_rules (on procedure) must be provided.

| Field Name                                  | Description                                                                                                                                                                      | Type                                         |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [`topics`](idp.md#idp-classification-topic) | \[Optional, default: None] List of ClassificationTopic objects to classify the document against. Highest priority if provided.                                                   | `optional[list of idp classification topic]` |
| `prompt`                                    | \[Optional, default: None] Classification instructions or context. If no topics provided, topics will be extracted from this prompt. Example: "Is this an invoice or a receipt?" | `optional[text]`                             |
| `llm_model`                                 | \[Optional, default: provider default] LLM model to use. Provider defaults: gemini-2.5-pro, gpt-4o, claude-sonnet-4-5.                                                           | `optional[text]`                             |
| `include_reasoning`                         | \[Optional, default: True] Whether to include reasoning explanation for each classification decision.                                                                            | `optional[boolean]`                          |
| `confidence_threshold`                      | \[Optional, default: 50] Minimum confidence score (0-100) to consider a topic as matched.                                                                                        | `optional[number]`                           |

### Idp classification topic

A topic to classify the document against.Topics define what the classification should look for in a document. They can be simple labels or detailed criteria for the LLM to evaluate.

| Field Name    | Description                                           | Type             |
| ------------- | ----------------------------------------------------- | ---------------- |
| `name`        | The topic name (e.g., "Contains PII", "Is Invoice").  | `optional[text]` |
| `description` | Optional description to help understand the topic.    | `optional[text]` |
| `criteria`    | Optional specific criteria for evaluating this topic. | `optional[text]` |

### Idp classification result

Complete classification result for a document.Contains classification results for all evaluated topics, with an overall summary and confidence score.

| Field Name                                            | Description                                              | Type                                         |
| ----------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------- |
| `result_type`                                         | Top-level API response discriminator.                    | `optional[text]`                             |
| `source`                                              | Source document name or identifier.                      | `optional[text]`                             |
| [`classifications`](idp.md#idp-topic-classification)  | List of classification results for each topic.           | `optional[list of idp topic classification]` |
| `summary`                                             | Overall summary of the classification results.           | `optional[text]`                             |
| `confidence`                                          | Overall confidence score (average across topics, 0-100). | `optional[number]`                           |
| `processing_time_ms`                                  | Time taken to process the classification.                | `optional[number]`                           |
| [`metrics`](idp.md#metrics-idp-classification-result) | Document processing metrics (num\_pages, etc.).          | `optional[json]`                             |

### Idp topic classification

Classification result for a single topic.Represents whether a document matches a specific topic, with confidence scoring and optional reasoning.

| Field Name     | Description                                           | Type                |
| -------------- | ----------------------------------------------------- | ------------------- |
| `element_type` | Discriminator for this element type in API responses. | `optional[text]`    |
| `topic`        | The topic name that was evaluated.                    | `optional[text]`    |
| `matches`      | Whether the document matches this topic.              | `optional[boolean]` |
| `confidence`   | Confidence score (0-100) for this classification.     | `optional[number]`  |
| `reasoning`    | Explanation for why this classification was made.     | `optional[text]`    |

### Field extraction specification

Input for data extraction from documents.Specify extraction requirements using either fields or prompt (not both).

| Field Name                                               | Description                                                                                                                                                                                                         | Type                          |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| [`fields`](idp.md#fields-field-extraction-specification) | \[Required, one of] List of ExtractField objects defining what to extract from the document.                                                                                                                        | `optional[list of json]`      |
| `prompt`                                                 | \[Required, one of] Natural language description of what to extract. The LLM will parse this into fields automatically. Example: "Extract the invoice number, total amount, and vendor"                             | `optional[text]`              |
| `llm_model`                                              | \[Optional, default: provider default] LLM model to use. Provider defaults: gemini-2.5-pro, gpt-4o, claude-sonnet-4-5.                                                                                              | `optional[text]`              |
| `common_default_value`                                   | \[Optional, default: ""] Default value to use for all fields if no specific default is provided.                                                                                                                    | `optional[text]`              |
| `dpi`                                                    | \[Optional, default: 150] DPI for image processing.                                                                                                                                                                 | `optional[number?` or `text]` |
| `confidence_threshold`                                   | \[Optional, default: 90] Minimum confidence score (0-100). Fields below this threshold cause ExtractionError.                                                                                                       | `optional[number]`            |
| `generate_overlay`                                       | \[Optional, default: False] If True, generates an annotated PDF with bounding boxes around extracted fields.                                                                                                        | `optional[boolean]`           |
| `reconcile_locations`                                    | \[Optional, default: True] If True, matches LLM-extracted boxes with precise PDF text locations for digital PDFs. Falls back to LLM locations for scanned documents.                                                | `optional[boolean]`           |
| `verify`                                                 | \[Optional, default: False] If True, performs cross-model verification to detect hallucinations and validate extracted values exist in the source document.                                                         | `optional[boolean]`           |
| `verification_strictness`                                | \[Optional, default: "high"] Strictness level for verification. Options: - "high": Zero tolerance, cell-by-cell exact matching - "moderate": Allows formatting differences - "low": Only flags clear hallucinations | `optional[text]`              |
| `raise_exception`                                        | \[Optional, default: True] If True, raises ExtractionError when fields are missing or have low confidence. If False, returns partial results.                                                                       | `optional[boolean]`           |
| `business_rules`                                         | \[Optional, default: None] File (.txt, .md, .docx) containing extraction guidelines to include in the LLM prompt.                                                                                                   | `optional[file]`              |

### Extraction result

Wrapper for extraction results providing self-describing API response.This class wraps the list of extracted fields to provide a consistent, self-describing response format that matches the pattern used by DocumentAnalysis from analyze\_thing. The UI can use `result_type` to determine how to render the response: - "extraction\_result" -> render as field list - "document\_analysis" -> render as structured analysis

| Field Name                                    | Description                                                 | Type                     |
| --------------------------------------------- | ----------------------------------------------------------- | ------------------------ |
| `result_type`                                 | Type discriminator for UI rendering ("extraction\_result"). | `optional[text]`         |
| [`fields`](idp.md#document-field)             | List of extracted field results.                            | `list of document field` |
| `document`                                    | Primary document filename (for single-doc extraction).      | `optional[text]`         |
| `document_count`                              | Number of documents processed (for multi-doc).              | `optional[number]`       |
| `confidence`                                  | Average confidence across all fields (0-100).               | `optional[number]`       |
| [`metrics`](idp.md#metrics-extraction-result) | Document processing metrics (num\_pages, etc.).             | `optional[json]`         |

### Document field

A dataclass representing an extraction field result.This class defines the structure for field results of data extraction, including the field name, extracted values, confidence, document source, and location. It shares common attributes with KeyValuePair from analysis for consistent API responses. Common attributes with analysis models: - element\_type: Type discriminator for UI rendering - page\_number: 1-indexed page number - bounding\_box: Location on page (BoundingBox format) - confidence: Confidence score (0-100) - verification: Validation result Extraction-specific attributes: - name: Field name (equivalent to 'key' in KeyValuePair) - values: List of extracted values - document: Source document reference - document\_index: For multi-document extraction

| Field Name                                           | Description                                                 | Type                             |
| ---------------------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| `element_type`                                       | Type of element for UI discrimination ("extracted\_field"). | `optional[text]`                 |
| `name`                                               | The name of the extraction field.                           | `optional[text]`                 |
| `values`                                             | List of extracted values for the field.                     | `optional[list of list of any?]` |
| `document`                                           | Full document reference where the value was found.          | `optional[text]`                 |
| `document_index`                                     | 0-based index of the document (multi-document only).        | `optional[number]`               |
| `page_number`                                        | 1-indexed page number where the value was found.            | `optional[number]`               |
| [`bounding_box`](idp.md#bounding_box-document-field) | Location on page using unified BoundingBox format.          | `optional[json]`                 |
| `confidence`                                         | Confidence score (0-100).                                   | `optional[number]`               |
| [`verification`](idp.md#verification-document-field) | Verification result from cross-model validation.            | `optional[json]`                 |

### Page extraction specification

Input for extracting specific pages from a document.All fields are optional.

| Field Name   | Description                                                                                                            | Type                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `start_page` | \[Optional, default: first page] First page to extract (1-based index).                                                | `optional[number]`            |
| `end_page`   | \[Optional, default: last page] Last page to extract (1-based index).                                                  | `optional[number]`            |
| `llm_model`  | \[Optional, default: provider default] LLM model to use. Provider defaults: gemini-2.5-pro, gpt-4o, claude-sonnet-4-5. | `optional[text]`              |
| `dpi`        | \[Optional, default: 150] DPI for image processing.                                                                    | `optional[number?` or `text]` |

### Page extraction result

Result of extracting pages from a document.

| Field Name                                         | Description                                                 | Type             |
| -------------------------------------------------- | ----------------------------------------------------------- | ---------------- |
| `result_type`                                      | Type discriminator for API response handling.               | `optional[text]` |
| [`pages`](idp.md#list-of-file)                     | List of extracted page documents as IO objects.             | `list of file`   |
| `source_document`                                  | Reference to the source document.                           | `optional[text]` |
| [`metrics`](idp.md#metrics-page-extraction-result) | Processing metrics including page count of source document. | `optional[json]` |

### Subdocument extraction specification

Input for extracting a subdocument based on pages or markers.All fields are optional. Use page numbers OR markers, not both.

| Field Name                 | Description                                                                                                            | Type                          |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `llm_model`                | \[Optional, default: provider default] LLM model to use. Provider defaults: gemini-2.5-pro, gpt-4o, claude-sonnet-4-5. | `optional[text]`              |
| `start_page`               | \[Optional, default: first page] First page of the subdocument (1-based index).                                        | `optional[number]`            |
| `end_page`                 | \[Optional, default: last page] Last page of the subdocument (1-based index).                                          | `optional[number]`            |
| `start_page_marker`        | \[Optional, default: None] Text/logic to find the starting page. Example: "Page containing 'Introduction'"             | `optional[text]`              |
| `end_page_marker`          | \[Optional, default: None] Text/logic to find the ending page (inclusive).                                             | `optional[text]`              |
| `excluded_end_page_marker` | \[Optional, default: None] Text/logic to find the ending page (exclusive - page before this marker).                   | `optional[text]`              |
| `subdocument_size`         | \[Optional, default: None] Maximum number of pages in the subdocument. Cannot be used with end markers.                | `optional[number]`            |
| `dpi`                      | \[Optional, default: 150] DPI for image processing.                                                                    | `optional[number?` or `text]` |

### Subdocument extraction result

Result of extracting a subdocument from a document.

| Field Name                                                | Description                                                 | Type               |
| --------------------------------------------------------- | ----------------------------------------------------------- | ------------------ |
| `result_type`                                             | Type discriminator for API response handling.               | `optional[text]`   |
| `subdocument`                                             | The extracted subdocument as an IO object.                  | `file`             |
| `source_document`                                         | Reference to the source document.                           | `optional[text]`   |
| `start_page`                                              | Starting page number (1-based) of the subdocument.          | `optional[number]` |
| `end_page`                                                | Ending page number (1-based) of the subdocument.            | `optional[number]` |
| [`metrics`](idp.md#metrics-subdocument-extraction-result) | Processing metrics including page count of source document. | `optional[json]`   |

### Subdocuments extraction specification

Input for extracting multiple subdocuments using markers or fixed size.All fields are optional. Supports two extraction strategies: 1. Marker-based: Split at pages matching a text pattern 2. Fixed-size: Split into N-page chunks with optional overlap

| Field Name                 | Description                                                                                                            | Type                          |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `llm_model`                | \[Optional, default: provider default] LLM model to use. Provider defaults: gemini-2.5-pro, gpt-4o, claude-sonnet-4-5. | `optional[text]`              |
| `start_page`               | \[Optional, default: first page] First page to process (1-based index).                                                | `optional[number]`            |
| `end_page`                 | \[Optional, default: last page] Last page to process (1-based index).                                                  | `optional[number]`            |
| `start_page_marker`        | \[Optional, default: None] Text/logic to find where each subdocument starts. Example: "INVOICE NUMBER"                 | `optional[text]`              |
| `end_page_marker`          | \[Optional, default: None] Text/logic to find where each subdocument ends (inclusive). Requires start\_page\_marker.   | `optional[text]`              |
| `excluded_end_page_marker` | \[Optional, default: None] Text/logic to find where each subdocument ends (exclusive). Requires start\_page\_marker.   | `optional[text]`              |
| `subdocument_size`         | \[Optional, default: None] Fixed number of pages per subdocument for chunking mode.                                    | `optional[number]`            |
| `subdocument_overlap_size` | \[Optional, default: None] Number of overlapping pages between consecutive chunks. Requires subdocument\_size.         | `optional[number]`            |
| `dpi`                      | \[Optional, default: 150] DPI for image processing.                                                                    | `optional[number?` or `text]` |

### Subdocuments extraction result

Result of extracting multiple subdocuments from a document.

| Field Name                                                 | Description                                                 | Type             |
| ---------------------------------------------------------- | ----------------------------------------------------------- | ---------------- |
| `result_type`                                              | Type discriminator for API response handling.               | `optional[text]` |
| [`subdocuments`](idp.md#list-of-file)                      | List of extracted subdocuments as IO objects.               | `list of file`   |
| `source_document`                                          | Reference to the source document.                           | `optional[text]` |
| [`metrics`](idp.md#metrics-subdocuments-extraction-result) | Processing metrics including page count of source document. | `optional[json]` |

### Table extraction specification

Input for table extraction from documents.

| Field Name                | Description                                                                                                                                                                                                         | Type                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `description`             | \[Required] Description of the table to extract. Example: "Extract the Previous Employment History table"                                                                                                           | `text`                        |
| `llm_model`               | \[Optional, default: provider default] LLM model to use. Provider defaults: gemini-2.5-pro, gpt-4o, claude-sonnet-4-5.                                                                                              | `optional[text]`              |
| `dpi`                     | \[Optional, default: 150] DPI for image processing.                                                                                                                                                                 | `optional[number?` or `text]` |
| `confidence_threshold`    | \[Optional, default: 0] Minimum confidence score (0-100) for the extracted table. If below threshold, raises ExtractionError. Set to 0 to disable threshold checking.                                               | `optional[number]`            |
| `raise_exception`         | \[Optional, default: True] If True, raises ExtractionError when confidence is below threshold. If False, returns the result with low confidence instead of raising.                                                 | `optional[boolean]`           |
| `verify`                  | \[Optional, default: False] If True, performs cross-model verification to detect hallucinations and validate extracted table data exists in the source document.                                                    | `optional[boolean]`           |
| `verification_strictness` | \[Optional, default: "high"] Strictness level for verification. Options: - "high": Zero tolerance, cell-by-cell exact matching - "moderate": Allows formatting differences - "low": Only flags clear hallucinations | `optional[text]`              |

### Idp table extraction result

Wrapper for table extraction results.This provides a consistent API response format for extract\_table\_from\_thing, with a result\_type discriminator for UI rendering.

| Field Name                                              | Description                                     | Type                            |
| ------------------------------------------------------- | ----------------------------------------------- | ------------------------------- |
| `result_type`                                           | Top-level discriminator ("table\_extraction").  | `optional[text]`                |
| [`table`](idp.md#idp-extracted-table)                   | The extracted table.                            | `optional[idp extracted table]` |
| `document`                                              | Source document filename.                       | `optional[text]`                |
| `confidence`                                            | Confidence score (0-100).                       | `optional[number]`              |
| [`metrics`](idp.md#metrics-idp-table-extraction-result) | Document processing metrics (num\_pages, etc.). | `optional[json]`                |

### Merge document result

Result of merging pages or subdocuments into a document.

| Field Name                                        | Description                                                 | Type               |
| ------------------------------------------------- | ----------------------------------------------------------- | ------------------ |
| `result_type`                                     | Type discriminator for API response handling.               | `optional[text]`   |
| `document`                                        | The merged document as an IO object.                        | `file`             |
| `document_name`                                   | Name of the merged document.                                | `optional[text]`   |
| `source_count`                                    | Number of source pages/subdocuments that were merged.       | `optional[number]` |
| [`metrics`](idp.md#metrics-merge-document-result) | Processing metrics including page count of merged document. | `optional[json]`   |

### Read content result

Result of reading/extracting text content from a document.

| Field Name                                      | Description                                                 | Type             |
| ----------------------------------------------- | ----------------------------------------------------------- | ---------------- |
| `result_type`                                   | Type discriminator for API response handling.               | `optional[text]` |
| `content`                                       | The extracted text content.                                 | `optional[text]` |
| `source_document`                               | Reference to the source document.                           | `optional[text]` |
| [`metrics`](idp.md#metrics-read-content-result) | Processing metrics including page count of source document. | `optional[json]` |

#### Concept attribute specifications

**key\_value\_pairs (idp document analysis)**

| Name             | Type                          |
| ---------------- | ----------------------------- |
| `element_type`   | `optional[text]`              |
| `page_number`    | `optional[number]`            |
| `bounding_box`   | `optional[json]`              |
| `confidence`     | `optional[number]`            |
| `is_handwritten` | `optional[boolean]`           |
| `key`            | `optional[text]`              |
| `value`          | `number?]` or `optional[text` |
| `verification`   | `optional[json]`              |

**forms (idp document analysis)**

| Name             | Type                |
| ---------------- | ------------------- |
| `element_type`   | `optional[text]`    |
| `page_number`    | `optional[number]`  |
| `bounding_box`   | `optional[json]`    |
| `confidence`     | `optional[number]`  |
| `is_handwritten` | `optional[boolean]` |
| `title`          | `optional[text]`    |
| `fields`         | `optional[json]`    |

**entities (idp document analysis)**

| Name               | Type                |
| ------------------ | ------------------- |
| `element_type`     | `optional[text]`    |
| `page_number`      | `optional[number]`  |
| `bounding_box`     | `optional[json]`    |
| `confidence`       | `optional[number]`  |
| `is_handwritten`   | `optional[boolean]` |
| `entity_type`      | `optional[text]`    |
| `text`             | `optional[text]`    |
| `normalized_value` | `optional[any?]`    |
| `context`          | `optional[text]`    |
| `verification`     | `optional[json]`    |

**text\_blocks (idp document analysis)**

| Name             | Type                |
| ---------------- | ------------------- |
| `element_type`   | `optional[text]`    |
| `page_number`    | `optional[number]`  |
| `bounding_box`   | `optional[json]`    |
| `confidence`     | `optional[number]`  |
| `is_handwritten` | `optional[boolean]` |
| `content`        | `optional[text]`    |
| `style`          | `optional[text]`    |
| `level`          | `optional[number]`  |
| `items`          | `optional[text]`    |
| `list_type`      | `optional[text]`    |

**lists (idp document analysis)**

| Name             | Type                |
| ---------------- | ------------------- |
| `element_type`   | `optional[text]`    |
| `page_number`    | `optional[number]`  |
| `bounding_box`   | `optional[json]`    |
| `confidence`     | `optional[number]`  |
| `is_handwritten` | `optional[boolean]` |
| `list_type`      | `optional[text]`    |
| `items`          | `optional[text]`    |

**metrics (idp document analysis)**

| Name        | Type               |
| ----------- | ------------------ |
| `num_pages` | `optional[number]` |

**bounding\_box (idp extracted table)**

| Name     | Type               |
| -------- | ------------------ |
| `x`      | `optional[number]` |
| `y`      | `optional[number]` |
| `width`  | `optional[number]` |
| `height` | `optional[number]` |

**verification (idp extracted table)**

| Name                      | Type                |
| ------------------------- | ------------------- |
| `is_valid`                | `optional[boolean]` |
| `adjusted_confidence`     | `optional[number]`  |
| `value_found_in_document` | `optional[boolean]` |
| `issues`                  | `optional[text]`    |
| `suggested_correction`    | `optional[text]`    |

**metrics (idp classification result)**

| Name        | Type               |
| ----------- | ------------------ |
| `num_pages` | `optional[number]` |

**fields (field extraction specification)**

| Name            | Type             |
| --------------- | ---------------- |
| `name`          | `text`           |
| `format`        | `optional[text]` |
| `rule`          | `optional[text]` |
| `default_value` | `optional[any?]` |

**metrics (extraction result)**

| Name        | Type               |
| ----------- | ------------------ |
| `num_pages` | `optional[number]` |

**bounding\_box (document field)**

| Name     | Type               |
| -------- | ------------------ |
| `x`      | `optional[number]` |
| `y`      | `optional[number]` |
| `width`  | `optional[number]` |
| `height` | `optional[number]` |

**verification (document field)**

| Name                      | Type                |
| ------------------------- | ------------------- |
| `is_valid`                | `optional[boolean]` |
| `adjusted_confidence`     | `optional[number]`  |
| `value_found_in_document` | `optional[boolean]` |
| `issues`                  | `optional[text]`    |
| `suggested_correction`    | `optional[text]`    |

**metrics (page extraction result)**

| Name        | Type               |
| ----------- | ------------------ |
| `num_pages` | `optional[number]` |

**metrics (subdocument extraction result)**

| Name        | Type               |
| ----------- | ------------------ |
| `num_pages` | `optional[number]` |

**metrics (subdocuments extraction result)**

| Name        | Type               |
| ----------- | ------------------ |
| `num_pages` | `optional[number]` |

**metrics (idp table extraction result)**

| Name        | Type               |
| ----------- | ------------------ |
| `num_pages` | `optional[number]` |

**metrics (merge document result)**

| Name        | Type               |
| ----------- | ------------------ |
| `num_pages` | `optional[number]` |

**metrics (read content result)**

| Name        | Type               |
| ----------- | ------------------ |
| `num_pages` | `optional[number]` |
