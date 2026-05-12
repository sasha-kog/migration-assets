# Run Capture Template - `process incoming netsuite case`

## Run Metadata
- Run timestamp:  Mar 2, 2026 8:46 PM
- Run ID/link: https://app.kognitos.com/department/d6j8mv1c12a9n3itm7msneli4/processes/6us9lppf3b8qkwhp8u65ozvlz/run/0ij231hychlqcn6bi87czztmo
- Input: email HTML source at email.html
- Email subject (if visible): case# 54133:Get Freighted Pty Ltd:FW:, automation says 'the email subject is "Case Alert: Kognitos Assignation Alert - 1 case"'

## Stage A - Extract Case Numbers from Email
- Extraction method: regex / IDP / string parsing
- Case numbers found: 54133
- Deduplication applied: yes/no
- Final caseNumbers list: 54133

## Stage B - Retrieve Case and Messages (per case number)

### Case: (caseNumber)
- supportCase lookup query:   retrieve some supportCase records from netsuite whose casenumber is the caseNumber
- Record found: yes, support_record.json
- supportRecord.id: 5085191
- msgActivity (= supportRecord.id): 5085191 message_record.json
- Message records retrieved: count = 1
- Pagination needed: not sure

## Stage C - Find Attachment from Messages
- Messages scanned: count = 1
- hasAttachment == "true" found: yes
- If yes:
  - msgRecord.attachments (raw): attachments: 5549575, 5549576, 5549577, 5549578, 5549579, 5549580
  - Split codes (multiCodes): 5549575, 5549576, 5549577 5549578, 5549579, 5549580
  - Selected File id (last code): 5549580
  - File info retrieved: yes
  - File name: Scanned_from_a_Lexmark_Multifunction_Product03-02-2026-201217.pdf
  - Attachment downloaded: yes
  - Input file set to: Scanned_from_a_Lexmark_Multifunction_Product03-02-2026-201217.pdf
- If no attachment found:
  - escalation set to: "Document not found in the email message"

## Stage D - Preprocess Document (CSV Handling)
- File extension: .pdf
- CSV branch taken: NO
- If non-CSV:
  - document set to: (original input file)

## Stage E - Classify Document
- IDP model used: (expected: gemini-2.5-pro)
- Classification result: Sales Order
- Classification confidence/notes: N/A

## Stage F - Route by Classification
- Branch taken: Sales Order
- If Sales Order:
  - Sub-automation invoked: "to create a sales order"
  - Inputs passed: 
    - attachment: Scanned_from_a_Lexmark_Multifunction_Product03-02-2026-201217.pdf
    - caseNumber: 54133
  - Sub-automation result: NOT SHOWN
    - status:
    - escalation: 
    - usecase:
    - usecaseNumber:
  - (If no chaining: outputs captured for manual verification)
- If INDECIPHERABLE:
  - escalation set to: "Could not classify the ticket..."
- If no attachment:
  - escalation set to: "Document not found in the email message"

## Stage G - Update Case on Escalation
- escalation non-empty: NO (if the escalation is not empty then , condition not met)
- If yes:
  - Sub-automation invoked: "Update the Case"
  - Inputs passed:
    - caseNumber:
    - status: "reassign"
    - escalation:
    - usecase: ""
    - usecaseNumber: ""
  - Update result:
  - (If no chaining: escalation value captured for manual verification)

## V1 Parity Check
| Stage | V1 Value | V2 Value | Match |
|-------|----------|----------|-------|
| Case numbers extracted | | | |
| Attachment found | | | |
| File name | | | |
| Classification | | | |
| Sub-automation invoked | | | |
| Final status | | | |
| Final escalation | | | |

## Summary
- Final outcome:
  - success (Sales Order created)
  - escalated (reassign)
  - failed execution
- Cases processed: count
- Primary failure stage (if any):
- Root cause hypothesis:
- Follow-up action:
