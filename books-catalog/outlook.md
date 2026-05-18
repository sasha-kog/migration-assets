---
title: Microsoft Outlook
description: Overview of the Microsoft Outlook integration.
icon: microsoft
updated: 2026-03-20T14:12
git_hash: 4473aa24be512b2be1dc3790ea383ffedb994984
---

{% hint style="info" %}
The following documentation is for **Microsoft Outlook v2.6.0**.
{% endhint %}

# Overview

Microsoft Outlook provides enterprise email management with calendar, contacts, and task integration capabilities. This integration enables automated email processing, calendar management, and communication workflows. Streamline business communication and enhance productivity through automated email operations.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Microsoft Outlook**
* **Microsoft Office 365**

{% hint style="info" %}
Note: The **Microsoft Outlook** integration depends on **Microsoft Office 365** for core Microsoft capabilities.
{% endhint %}


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

Add a name for the connection. You'll be prompted for [**authentication**](#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Permissions

When using **client credentials** authentication, you need to have the following **application permissions** in Microsoft Graph:

{% hint style="info" %}
Application permissions are used when an app runs without a signed-in user _(such as with a client credentials flow)_.
These permissions give the app organization-wide access and must be granted by an administrator in your Microsoft organization.
For additional details, refer to Microsoft's [**guides**](https://learn.microsoft.com/en-us/graph/security-authorization#grant-permissions-to-an-application).
{% endhint %}

#### User and Directory Access

* `User.Read.All`
* `User.ReadWrite.All`
* `Directory.Read.All`
* `Directory.ReadWrite.All`

#### Mail Operations

* `Mail.Read`
* `Mail.ReadWrite`
* `Mail.ReadBasic`
* `Mail.ReadBasic.All`
* `Mail.ReadWrite.Shared`
* `Mail.Send`

#### Calendar Operations

* `Calendars.ReadBasic`
* `Calendars.Read`
* `Calendars.ReadWrite`

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

The following actions are available in the **Microsoft Outlook** integration:

### 1. Delete some emails

Delete specific emails from an Outlook account.

### 2. Download an attachment

Download an attachment from an event or email.

### 3. Forward an email to a recipient

Forward an email to a specified recipient or group of recipients.

### 4. Get a group's events from outlook

Get all the events from a group's calendar.

### 5. Get a user's event's attachments

Get all the attachments from a user's event.

### 6. Get a user's events from outlook

Get all the events from a user's calendar.

### 7. Get an email folder's subfolders

Get all the subfolders from an email folder.

### 8. Get some email folder's emails

Get emails from an Outlook folder based on specified filters.

### 9. Get the attachments from an email

Get the attachments from an email.

### 10. Mark some emails

Mark specified emails as read or unread.

### 11. Move an email to a target folder

Move emails to a target folder.

### 12. Reply an email

Reply to an email through Outlook with the specified details and attachments.

### 13. Retrieve some email folders from outlook

Get all the email folders from the authenticated user's mailbox.

### 14. Retrieve some user's email folders

Get all the email folders from a user's mailbox.

### 15. Send an email to a recipient

Send an email through Outlook with the specified details and attachments.

### 16. Set an entity's event's body to a text

Update the body of a calendar event.



## Concepts

### Outlook email

An Outlook Email represents an email message in Microsoft Graph.

| Field Name                | Description                                                                                                                             | Type                     |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `id`                      | The unique identifier for the email.                                                                                                    | `optional[text]`         |
| `folder_id`               | The unique identifier for the folder containing the email.                                                                              | `optional[text]`         |
| `subject`                 | The subject of the email.                                                                                                               | `optional[text]`         |
| `body`                    | The body of the email.                                                                                                                  | `optional[text]`         |
| `recipients`              | The recipients of the email.                                                                                                            | `optional[list of text]` |
| `state`                   | The state of the email (e.g., sent, received, draft, deleted, archived, unread).                                                        | `optional[text]`         |
| `sent_date_time`          | The date and time the email was sent.                                                                                                   | `optional[datetime]`     |
| `received_date_time`      | The date and time the email was received.                                                                                               | `optional[datetime]`     |
| `sender`                  | The sender of the email.                                                                                                                | `optional[text]`         |
| `cc_recipients`           | The cc recipients of the email.                                                                                                         | `optional[list of text]` |
| `bcc_recipients`          | The bcc recipients of the email.                                                                                                        | `optional[list of text]` |
| `user_id`                 | The id of the authenticated user making the requests. If it is None, the user is the using the "me" endpoints meaning delegated access. | `optional[text]`         |
| `has_attachments`         | Whether the email has attachments or not.                                                                                               | `optional[boolean]`      |
| `conversation_id`         | The ID of the conversation the email belongs to.                                                                                        | `optional[text]`         |
| `last_modified_date_time` | The date and time the email was last modified.                                                                                          | `optional[datetime]`     |
| `categories`              | The categories associated with the email.                                                                                               | `optional[list of text]` |

### Outlook attachment

An Outlook Attachment represents a file or item attached to a calendar event in Microsoft Graph. It includes the attachment name and content type.

| Field Name      | Description                                              | Type             |
| --------------- | -------------------------------------------------------- | ---------------- |
| `attachment_id` | The unique identifier for the attachment.                | `optional[text]` |
| `odata_type`    | The OData type of the attachment.                        | `optional[text]` |
| `user_id`       | The user ID of the attachment.                           | `optional[text]` |
| `name`          | The name of the attachment.                              | `optional[text]` |
| `event_id`      | The ID of the event to which the attachment is attached. | `optional[text]` |
| `email_id`      | The ID of the email to which the attachment is attached. | `optional[text]` |

### Outlook email folder

OutlookEmailFolder represents a folder within an Outlook mailbox, providing a way to organize and manage emails. It serves as a utility to group emails based on specific criteria, facilitating efficient email management and retrieval.

| Field Name | Description                                           | Type             |
| ---------- | ----------------------------------------------------- | ---------------- |
| `id`       | The unique identifier for the folder.                 | `optional[text]` |
| `name`     | The name of the folder.                               | `optional[text]` |
| `user_id`  | The id of the authenticated user making the requests. | `optional[text]` |

### Office user

An Office User represents a user in the Microsoft Graph. It includes key user details such as display name,email address, and job title.

| Field Name      | Description                                                   | Type             |
| --------------- | ------------------------------------------------------------- | ---------------- |
| `id`            | The unique identifier for the user.                           | `text`           |
| `display_name`  | The name displayed in the address book for the user.          | `optional[text]` |
| `email_address` | The user's email address (usually their user principal name). | `optional[text]` |
| `job_title`     | The user's job title.                                         | `optional[text]` |

### Outlook event

An Outlook Calendar Event is a scheduled occurrence within an Outlook calendar that is managed through theMicrosoft Graph API. The event object includes essential details such as the subject, start and end times, attendees, and location, and supports advanced features like reminders, recurrence patterns, and time zone adjustments.

| Field Name                             | Description                                                                                                                                                                                                                                                                    | Type                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| `id`                                   | The unique identifier for the event. Read-only.                                                                                                                                                                                                                                | `text`                                     |
| `subject`                              | The text of the event's subject line.                                                                                                                                                                                                                                          | `optional[text]`                           |
| `body_preview`                         | The preview of the message associated with the event. It is in text format.                                                                                                                                                                                                    | `optional[text]`                           |
| `start`                                | The start date, time, and time zone of the event. By default, the start time is in UTC.                                                                                                                                                                                        | `optional[datetime]`                       |
| `end`                                  | The date, time, and time zone that the event ends. By default, the end time is in UTC.                                                                                                                                                                                         | `optional[datetime]`                       |
| [`location`](#outlook-event-location)  | The location of the event.                                                                                                                                                                                                                                                     | `optional[outlook event location]`         |
| [`locations`](#outlook-event-location) | The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value. | `optional[list of outlook event location]` |
| [`organizer`](#outlook-email-address)  | The organizer of the event.                                                                                                                                                                                                                                                    | `optional[outlook email address]`          |
| [`attendees`](#outlook-event-attendee) | The collection of attendees for the event.                                                                                                                                                                                                                                     | `optional[list of outlook event attendee]` |

### Outlook event location

An Outlook Event Location represents a specific location associated with a calendar event or meeting inMicrosoft Graph. It includes properties like the display name, address, coordinates, and location type, enabling precise identification and use of locations within calendar-related functionalities.

| Field Name      | Description                                                                                                                                                                                     | Type             |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `display_name`  | The name associated with the location.                                                                                                                                                          | `optional[text]` |
| `email_address` | Optional email address of the location.                                                                                                                                                         | `optional[text]` |
| `type`          | The type of location. The possible values are: default, conferenceRoom, homeAddress, businessAddress,geoCoordinates, streetAddress, hotel, restaurant, localBusiness, postalAddress. Read-only. | `optional[text]` |
| `uri`           | Optional URI representing the location.                                                                                                                                                         | `optional[text]` |

### Outlook email address

Represents an email address associated with a contact or calendar item inMicrosoft Graph. It includes only the name and email address fields.

| Field Name | Description                                         | Type             |
| ---------- | --------------------------------------------------- | ---------------- |
| `name`     | The display name associated with the email address. | `optional[text]` |
| `address`  | The email address.                                  | `optional[text]` |

### Outlook event attendee

An Outlook Event Attendee represents an attendee of a calendar event in Microsoft Graph. It includes the name, email address, attendee type, and response status fields.

| Field Name      | Description                                                                                               | Type                 |
| --------------- | --------------------------------------------------------------------------------------------------------- | -------------------- |
| `name`          | The display name associated with the attendee.                                                            | `optional[text]`     |
| `email_address` | The email address of the attendee.                                                                        | `optional[text]`     |
| `type`          | The type of attendee as a string. Possible values are: required, optional, resource.                      | `optional[text]`     |
| `status`        | The response status of the attendee as a string. Possible values are: accepted, declined, tentative, etc. | `optional[text]`     |
| `response_time` | The datetime when the response was recorded.                                                              | `optional[datetime]` |

### Office group

An Office Group represents a group in the Microsoft Graph. It includes key user details such as display name,and email address.

| Field Name      | Description                                           | Type             |
| --------------- | ----------------------------------------------------- | ---------------- |
| `id`            | The unique identifier for the group.                  | `text`           |
| `display_name`  | The name displayed in the address book for the group. | `optional[text]` |
| `email_address` | The group's email address.                            | `optional[text]` |
