# Books Reference — V1→V2 Migration Capability Map

**Purpose:** quick-reference for the migration agent's Phase B preflight (Book Capability Check). When walking captured V1 KLang, use this to classify a line that needs a book and propose candidate books to verify against the workspace's installed set.

**Source of truth for procedure details:** `/Users/sashajh2/Kognitos/docs-gitbook/guides-v2/platform/integrations/<book>.md`. This file is a digest, not a replacement.

---

## How to use this file

1. Walk the KLang line-by-line for each stage.
2. **Skip lines that don't need a book** — pure control flow (`if … then`, loops, comparisons, arithmetic, string operations) does not enter the inventory.
3. For lines that need a book, classify the intent and pick candidate books from the table below.
4. Confirm with `kognitos_books(list)` whether each candidate is installed in the target workspace; then `kognitos_books(search_procedures, book=<X>, query=<intent>)` to verify a procedure matches.

---

## KLang patterns → candidate books

### Document / file content extraction (top suspects: IDP)

| KLang pattern | Candidate book(s) | Notes |
|---|---|---|
| `extract data from <doc>`, `extract <fields> from <doc>` with or without a prompt | **IDP** (`Extract data from a thing`) | IDP accepts a free-text `prompt` parameter, so Koncierge-style "extract X by asking the LLM" is satisfied here. |
| `extract tables from <doc>`, `extract the <named> table from <doc>` | **IDP** (`Extract table from a thing`) | IDP table extraction takes a description; supports cross-model verification. |
| `classify <doc>`, `determine the type of <doc>`, `is this an invoice or a receipt` | **IDP** (`Classify a thing`) | IDP classification accepts a prompt OR explicit topics. |
| `analyze <doc>`, `understand the structure of <doc>` | **IDP** (`Analyze a thing`) | Schema-free extraction. |
| `read the content of <doc>`, `get the text of <doc>` | **IDP** (`Read content from a thing`) | Plain text from a document. |
| `extract pages <a>–<b> from <doc>`, `split <doc> into subdocuments` | **IDP** (`Extract pages`, `Extract subdocument(s)`) | Pages/subdocument splitting. |
| `merge <docs> into a single document` | **IDP** (`Merge pages/subdocuments into a document`) | |

### Document format readers (when IDP isn't the right tool)

| KLang pattern | Candidate book(s) |
|---|---|
| Working with `.pdf` shape/text without LLM extraction | **PDF** |
| Working with `.docx` content | **DOCX** |
| Working with `.xlsx`, `.xls` (cells/sheets/formulas) | **Microsoft Excel** *or* **Excel** (standalone). Both exist; check which is installed. |
| Working with `.csv` rows/columns | **CSV** |
| Working with `.eml` email messages on disk | **EML** |
| Working with `.msg` (Outlook saved messages) | **MSG** |
| Working with `.zip` archives | **ZIP** |
| Generic file-system operations | **File** |

### UI automation (no API)

| KLang pattern | Candidate book(s) |
|---|---|
| `open a browser to <url>`, `click on <element>`, `type <X> into the <field>` | **Browser** or **Browser Use** |
| Anything that visibly walks a webpage UI when no SaaS book exists for that service | **Browser** / **Browser Use** |

### Direct LLM access (no document attached)

| KLang pattern | Candidate book(s) | Decision |
|---|---|---|
| `ask the LLM <question>`, free-form Koncierge block over plain values (no document) | **Anthropic**, **OpenAI**, or **Gemini**, OR pure SPy with inline Koncierge | Both options are valid. List both in the inventory and surface to the user as `needs_confirmation`. Don't auto-pick. |

### SaaS integrations — record/finance/operations

| KLang pattern | Candidate book |
|---|---|
| `from netsuite`, `in netsuite`, NetSuite IDs/records | **NetSuite** |
| `from quickbooks`, `in quickbooks` | **QuickBooks** |
| `from sap`, `in sap` | **SAP** |
| `from salesforce`, `in salesforce` | **Salesforce** |
| `from oracle fusion`, `in oracle fusion` | **Oracle Fusion** |
| `from epicor`, `in epicor` | **Epicor** |
| `from aspire` | **Aspire** |
| `from katana` | **Katana** |
| `from servicenow`, `in servicenow` | **ServiceNow** |
| `from zendesk`, `in zendesk` (tickets) | **Zendesk** |

### SaaS — productivity / project / docs

| KLang pattern | Candidate book |
|---|---|
| Mentions Google Docs files/content | **Google Docs** |
| Mentions Google Sheets cells/rows | **Google Sheets** |
| Mentions Google Drive files | **Google Drive** |
| Mentions Google Calendar events | **Google Calendar** |
| Mentions SharePoint | **Microsoft SharePoint** |
| Mentions Office 365 / Outlook calendar etc. | **Microsoft Office 365** |
| Mentions Confluence pages | **Confluence** |
| Mentions Jira issues | **Jira** |
| Mentions Asana tasks | **Asana** |
| Mentions Linear issues | **Linear** |
| Mentions Smartsheet rows | **Smartsheet** |
| Mentions Airtable rows | **Airtable** |
| Mentions GitHub PRs/issues/repos | **GitHub** |

### SaaS — communication

| KLang pattern | Candidate book |
|---|---|
| `send an email`, `from gmail`, `in gmail` | **Gmail** |
| `from outlook`, `in outlook` | **Microsoft Outlook** |
| `post to slack`, `from slack`, `in slack` | **Slack** |
| `post to teams`, `from teams` | **Microsoft Teams** |
| `post to google chat`, `from google chat` | **Google Chat** |
| `send an sms`, `make a call` (Twilio) | **Twilio** |
| Zoom meetings/recordings | **Zoom** |

### Databases / search

| KLang pattern | Candidate book |
|---|---|
| SQL against Postgres | **Postgres** |
| SQL against MSSQL | **MSSQL** |
| SQL against Snowflake | **Snowflake** |
| Spark/data against Databricks | **Databricks** |
| Search over an OpenSearch index | **OpenSearch** |

### Cloud infrastructure

| KLang pattern | Candidate book |
|---|---|
| S3 object read/write | **S3** (or **Amazon Selling Partner** only for the marketplace, not files) |
| Azure blob read/write | **Azure Blob Storage** |
| AWS EC2 actions | **EC2** |
| AWS SNS publish | **SNS** |
| AWS SQS enqueue/dequeue | **SQS** |
| AWS Secrets Manager fetch | **Secrets Manager** |
| Azure Key Vault fetch | **Azure Key Vault** |
| Azure Service Bus | **Azure Service Bus** |
| Azure Translator | **Azure Translator** |

### Generic protocols / utilities

| KLang pattern | Candidate book |
|---|---|
| Raw HTTP request/response | **HTTP** |
| SFTP put/get | **SFTP** |
| FileMaker / Claris records | **FileMaker** / **Claris** |
| Weather lookup | **Open Weather** |
| Amazon marketplace operations | **Amazon Selling Partner** |

---

## Full installed-book reference (64 books)

Canonical names as they appear in the workspace's `kognitos_books(list)`:

Airtable, Amazon Selling Partner, Anthropic, Asana, Aspire, Azure Blob Storage, Azure Key Vault, Azure Service Bus, Azure Translator, Browser, Browser Use, Confluence, CSV, Databricks, DOCX, EC2, EML, Epicor, Excel, File, FileMaker, Gemini, GitHub, Gmail, Google Calendar, Google Chat, Google Docs, Google Drive, Google Sheets, HTTP, Intelligent Document Processing (IDP), Jira, Katana, Linear, Microsoft Excel, Microsoft Office 365, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, MSG, MSSQL, NetSuite, OpenAI, OpenSearch, Open Weather, Oracle Fusion, PDF, Postgres, QuickBooks, S3, Salesforce, SAP, ServiceNow, Secrets Manager, SFTP, Slack, Smartsheet, Snowflake, SNS, SQS, Twilio, Zendesk, ZIP, Zoom

**Watch:** Excel and Microsoft Excel are separate entries in the docs (`/integrations/excel-standalone` vs `/integrations/excel`). When uncertain, mark as `needs_confirmation`; don't auto-select.

---

## What this file is NOT

- Not authoritative for procedure signatures — always query `kognitos_books(search_procedures)` against the live workspace before declaring a procedure missing or matching.
- Not a static classifier — the agent's KLang classification must look at the line in context (a `from gmail` in a comment is not a Gmail action).
- Not a substitute for `needs_confirmation` — when multiple candidates plausibly fit (e.g. Excel vs Microsoft Excel), don't pick. Surface to the user.
