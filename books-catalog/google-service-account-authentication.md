---
title: Google Service Account Authentication
description: Set up shared Google service account authentication for Google Docs, Google Drive, and Google Sheets.
icon: google
hidden: true
---

# Google Service Account Authentication

Use this guide when you connect a Google integration in Kognitos with <kbd>Client Email</kbd>, <kbd>Token URI</kbd>, and <kbd>Private Key</kbd> instead of <kbd>Continue with Google</kbd>.

You can create one Google service account in Google Cloud and reuse it across these integrations:

* [Google Docs](googledocs.md)
* [Google Drive](googledrive.md)
* [Google Sheets](googlesheets.md)

{% hint style="info" %}
Service account authentication is available for Google Docs, Google Drive, and Google Sheets. Gmail, Google Calendar, and Google Chat use OAuth instead. For OAuth setup, see [Google Authentication](google-authentication.md).
{% endhint %}

## Before You Start

Make sure you have:

* Access to a Google Cloud project, or permission to create one
* Permission to create service accounts and download service account keys
* Access to the Google files, folders, and spreadsheets you want Kognitos to use
* Access to the Kognitos workspace where you want to add the connection

{% hint style="warning" %}
A service account does not automatically inherit access to your Google Workspace content. You must explicitly share the Google Docs documents, Drive folders, or Sheets files with the service account email.
{% endhint %}

## Set Up the Service Account in Google Cloud

{% stepper %}
{% step %}
#### Create or select a Google Cloud project

In [Google Cloud Console](https://console.cloud.google.com/), create a new project or open an existing one that will own the service account.
{% endstep %}

{% step %}
#### Enable the APIs you need

In <kbd>APIs & Services</kbd> → <kbd>Library</kbd>, enable the APIs for the integrations you plan to use:

| Integration | API to enable |
| --- | --- |
| [Google Docs](googledocs.md) | **Google Docs API** and **Google Drive API** |
| [Google Drive](googledrive.md) | **Google Drive API** |
| [Google Sheets](googlesheets.md) | **Google Sheets API** |

If you plan to use several Google integrations, enable all of their APIs in the same project.
{% endstep %}

{% step %}
#### Create the service account

In Google Cloud, go to <kbd>IAM & Admin</kbd> → <kbd>Service Accounts</kbd>, then click <kbd>Create service account</kbd>.

Enter a clear service account name, such as `kognitos-google-integrations`, review the generated service account ID, then click <kbd>Done</kbd> or finish the remaining prompts.
{% endstep %}

{% step %}
#### Create and download a JSON key

From <kbd>IAM & Admin</kbd> → <kbd>Service Accounts</kbd>, locate the service account you just created.

Then use one of these console paths, depending on the Google Cloud UI you see:

* Open the <kbd>Actions</kbd> menu for the service account, click <kbd>Manage keys</kbd>, then click <kbd>Add key</kbd> → <kbd>Create new key</kbd>
* Or click the service account email address, open the <kbd>Keys</kbd> tab, then click <kbd>Add key</kbd> → <kbd>Create new key</kbd>

Select <kbd>JSON</kbd> as the key type, then click <kbd>Create</kbd>. Google downloads the JSON key file to your machine.

{% hint style="info" %}
Google's IAM documentation still describes the <kbd>Keys</kbd> tab flow. In some current console layouts, the same flow appears under the service account's <kbd>Actions</kbd> menu as <kbd>Manage keys</kbd>.
{% endhint %}

{% hint style="warning" %}
Treat the JSON key like a password. Anyone with that file can use the service account until you revoke the key. After Google downloads the key file, you cannot download the same private key again.
{% endhint %}
{% endstep %}
{% endstepper %}

## Get the Values for Kognitos

Open the downloaded JSON key file and copy these values into Kognitos:

| Kognitos field | JSON field |
| --- | --- |
| <kbd>Client Email</kbd> | `client_email` |
| <kbd>Token URI</kbd> | `token_uri` |
| <kbd>Private Key</kbd> | `private_key` |

{% hint style="info" %}
Paste the full private key value exactly as it appears in the JSON, including the `BEGIN PRIVATE KEY` and `END PRIVATE KEY` lines.
{% endhint %}

## Share Google Content with the Service Account

Before you test the connection, share the Google content Kognitos needs to access with the service account email from `client_email`.

For example:

* Share a Google Drive folder with the service account email if your automation will create or read files there
* Share a Google Docs document or its parent folder with the service account email if your automation will edit documents
* Share a Google Sheets file or its parent folder with the service account email if your automation will read or update spreadsheets

Use the same sharing flow you use for any Google account:

1. Open the document, folder, or spreadsheet in Google Workspace.
2. Click <kbd>Share</kbd>.
3. Add the service account email.
4. Grant the level of access your automation needs.

## Use the Credentials in Kognitos

After you create the service account and download its JSON key, connect each supported Google integration in Kognitos with the same credentials.

{% stepper %}
{% step %}
#### Open the integration

In Kognitos, go to <kbd>Integrations</kbd> → <kbd>Explore Integrations</kbd>, then open [Google Docs](googledocs.md), [Google Drive](googledrive.md), or [Google Sheets](googlesheets.md).
{% endstep %}

{% step %}
#### Start a new connection

Click <kbd>Connect</kbd>, add a connection name, and choose the service account authentication option.
{% endstep %}

{% step %}
#### Enter the service account values

Paste the <kbd>Client Email</kbd>, <kbd>Token URI</kbd>, and <kbd>Private Key</kbd> values from the JSON key file.
{% endstep %}

{% step %}
#### Save and test the connection

Click <kbd>Connect</kbd>, then run a simple action to confirm the service account can access the files or folders you shared with it.
{% endstep %}
{% endstepper %}

Repeat this for each supported Google integration you want to connect. You can reuse the same service account across all three integrations.

## Troubleshooting

| Issue | What to check |
| --- | --- |
| Authentication succeeds, but files are missing | Make sure the document, folder, or spreadsheet is shared with the service account email |
| Permission denied | Confirm the service account has the right level of access in Google Workspace |
| Invalid private key | Paste the full `private_key` value exactly as it appears in the JSON key |
| Access blocked by API settings | Verify that the required API is enabled in the Google Cloud project |
| Google Cloud does not let you create a key | Your organization might enforce the `iam.disableServiceAccountKeyCreation` policy. Ask your Google Cloud admin whether service account key creation is blocked for the project. |
| Docs integration cannot create files in a folder | Make sure the service account also has access to Google Drive, not just Google Docs |

## Related Integration Pages

* [Google Authentication](google-authentication.md)
* [Google Docs](googledocs.md)
* [Google Drive](googledrive.md)
* [Google Sheets](googlesheets.md)
