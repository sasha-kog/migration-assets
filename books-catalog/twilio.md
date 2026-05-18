---
title: Twilio
updated: 2026-03-20T14:12
git_hash: b64f6c1400d977555ceae120fd37967a0138b13c
description: Overview of the Twilio integration.
icon: phone
---

# Twilio

{% hint style="info" %}
The following documentation is for **Twilio v2.1.0**.
{% endhint %}

## Overview

Enables interacting with and managing SMS communications via the Twilio API. Twilio provides a comprehensive communication platform, offering features such as SMS, voice calls, video, and chat. Ideal for businesses and developers seeking reliable and scalable communication solutions. This integration ensures secure and seamless access to these services.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **Twilio**

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

Add a name for the connection. You'll be prompted for [**authentication**](twilio.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using Account SID and Auth Token

Connect to the Twilio API using account credentials.

| Label       | Description                               | Type        |
| ----------- | ----------------------------------------- | ----------- |
| Account SID | The Account SID from your Twilio account. | `text`      |
| Auth Token  | The Auth Token from your Twilio account.  | `sensitive` |

## Actions

The following actions are available in the **Twilio** integration:

### 1. Read some SMS messages

Get SMS messages from the Twilio API.

### 2. Send an SMS message

Send an SMS message using the Twilio API.

## Concepts

### Twilio sms message

SMS message data model.An SMS (Short Message Service) message. Represents a text communication sent over a cellular network, typically between mobile phones.

| Field Name              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Type                 |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| `sid`                   | The unique, Twilio-provided string that identifies the Message resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `optional[text]`     |
| `body`                  | The text content of the message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `optional[text]`     |
| `num_segments`          | The number of segments that make up the complete message. SMS message bodies that exceed the [character limit](https://www.twilio.com/docs/glossary/what-sms-character-limit) are segmented and charged as multiple messages. Note: For messages sent via a Messaging Service, `num_segments` is initially `0`, since a sender hasn't yet been assigned                                                                                                                                                                                                                                                                                                                                        | `optional[text]`     |
| `sender_number`         | The sender's phone number (in [E.164](https://en.wikipedia.org/wiki/E.164) format), [alphanumeric sender ID](https://www.twilio.com/docs/sms/quickstart), [Wireless SIM](https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands), [short code](https://www.twilio.com/en-us/messaging/channels/sms/short-codes), or [channel address](https://www.twilio.com/docs/messaging/channels) (e.g., `whatsapp:+15554449999`). For incoming messages, this is the number or channel address of the sender. For outgoing messages, this value is a Twilio phone number, alphanumeric sender ID, short code, or channel address from which the message is sent | `optional[text]`     |
| `recipient_number`      | The recipient's phone number (in [E.164](https://en.wikipedia.org/wiki/E.164) format) or [channel address](https://www.twilio.com/docs/messaging/channels) (e.g. `whatsapp:+15552229999`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `optional[text]`     |
| `price`                 | The amount billed for the message in the currency specified by `price_unit`. The `price` is populated after the message has been sent/received, and may not be immediately available. View the [Pricing page](https://www.twilio.com/en-us/pricing) for more details.                                                                                                                                                                                                                                                                                                                                                                                                                          | `optional[number]`   |
| `account_sid`           | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `text`               |
| `num_media`             | The number of media files associated with the Message resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `number`             |
| `status`                | The status of the message, for more information about possible statuses see [Message Status](https://www.twilio.com/docs/messaging/api/message-resource#message-status-values)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `optional[text]`     |
| `messaging_service_sid` | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) associated with the Message resource. A unique default value is assigned if a Messaging Service is not used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `text`               |
| `date_sent`             | The [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) timestamp (in GMT) of when the Message was sent. For an outgoing message, this is when Twilio sent the message. For an incoming message, this is when Twilio sent the HTTP request to your incoming message webhook URL.                                                                                                                                                                                                                                                                                                                                                                                             | `optional[datetime]` |
| `date_created`          | The [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) timestamp (in GMT) of when the Message resource was created                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `optional[datetime]` |
| `date_updated`          | The [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) timestamp (in GMT) of when the Message resource was last updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `optional[datetime]` |
| `price_unit`            | The currency in which `price` is measured, in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. `usd`, `eur`, `jpy`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `text`               |
| `error_code`            | The [error code](https://www.twilio.com/docs/api/errors) returned if the Message `status` is `failed` or `undelivered`. If no error was encountered, the value is `null`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `optional[number]`   |
| `error_message`         | The description of the `error_code` if the Message `status` is `failed` or `undelivered`. If no error was encountered, the value is `null`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `optional[text]`     |
