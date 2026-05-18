---
title: Google Authentication
description: Set up shared Google OAuth authentication for Gmail, Google Calendar, Google Chat, Google Docs, Google Drive, and Google Sheets.
icon: google
hidden: true
---

# Google Authentication

Use this guide when you connect a Google integration in Kognitos with <kbd>Continue with Google</kbd>.

You can create one Google OAuth app in Google Cloud and reuse the same **Client ID** and **Client Secret** across these integrations:

* [Gmail](gmail.md)
* [Google Calendar](googlecalendar.md)
* [Google Chat](chat.md)
* [Google Docs](googledocs.md)
* [Google Drive](googledrive.md)
* [Google Sheets](googlesheets.md)

{% hint style="info" %}
Google Docs, Google Drive, and Google Sheets also support service account authentication. This page covers the shared OAuth setup that works across all six Google integrations. For service account setup, see [Google Service Account Authentication](google-service-account-authentication.md).
{% endhint %}

## Before You Start

Make sure you have:

* Access to a Google Cloud project, or permission to create one
* Permission to configure the Google Auth Platform and create OAuth clients
* Access to the Kognitos workspace where you want to add the connection

If your organization wants to avoid Google's unverified app warning, create the OAuth app as an **Internal** app in your Google Workspace organization.

## Set Up the OAuth App in Google Cloud

{% stepper %}
{% step %}
#### Create or select a Google Cloud project

In [Google Cloud Console](https://console.cloud.google.com/), create a new project or open an existing one that will own the OAuth app.

<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-create-project.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
#### Configure the consent screen

In **Google Auth Platform**, set up the consent screen for the project:

1. Enter an app name.
2. Select a user support email.
3. Choose **Internal** as the audience if the app should only be used by people in your Google Workspace organization.
4. Add a contact email.
5. Accept Google's user data policy and save the configuration.

<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-app-information.png" alt=""><figcaption></figcaption></figure></div>
<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-audience.png" alt=""><figcaption></figcaption></figure></div>
<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-contact-information.png" alt=""><figcaption></figcaption></figure></div>
<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-finish.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
#### Create the OAuth client

Create a new client with these settings:

* **Application type:** Web application
* **Authorized redirect URI:** `https://app.us-1.kognitos.com/oauth/connections/callback`

<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-create-client.png" alt=""><figcaption></figcaption></figure></div>

Copy the **Client ID** and **Client Secret** after you create the client. Store the secret somewhere secure in case Google only shows it once.

{% hint style="warning" %}
Use the production redirect URI exactly as shown. Do not use the dev URL or a legacy callback URL.
{% endhint %}

<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-redirect-uri.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
#### Enable the APIs you need

In <kbd>APIs & Services</kbd> → <kbd>Library</kbd>, enable the APIs for the Google integrations you plan to use:

| Integration | API to enable |
| --- | --- |
| [Gmail](gmail.md) | **Gmail API** |
| [Google Calendar](googlecalendar.md) | **Google Calendar API** |
| [Google Chat](chat.md) | **Google Chat API** |
| [Google Docs](googledocs.md) | **Google Docs API** and **Google Drive API** |
| [Google Drive](googledrive.md) | **Google Drive API** |
| [Google Sheets](googlesheets.md) | **Google Sheets API** |

<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-api-library.png" alt=""><figcaption></figcaption></figure></div>
<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-enable-apis.png" alt=""><figcaption></figcaption></figure></div>

If you plan to use several Google integrations, enable all of their APIs in the same project.

{% hint style="info" %}
If you use [Google Chat](chat.md), open the Google Chat API configuration after you enable the API and complete the app details before you connect it in Kognitos:

* **App name:** for example, `Kognitos`
* **Avatar URL:** `https://www.kognitos.com/img/favicon.svg`
* **Description:** for example, `Google Chat integration with Kognitos`
* Enable **Build this Chat app as a Workspace add-on**
* Disable **Interactive features**
{% endhint %}

<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-chat-config.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

## Use the Credentials in Kognitos

After you create the OAuth client in Google Cloud, connect each Google integration in Kognitos with the same credentials.

{% stepper %}
{% step %}
#### Open the integration

In Kognitos, go to <kbd>Integrations</kbd> → <kbd>Explore Integrations</kbd>, then open the Google integration you want to connect.
{% endstep %}

{% step %}
#### Start a new connection

Click <kbd>Connect</kbd>, add a connection name, and choose the OAuth option if Kognitos asks you to select an authentication method.

<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-kognitos-connection.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
#### Enter your OAuth client details

Paste the **Client ID** and **Client Secret** from Google Cloud.

<div data-with-frame="true"><figure><img src="../../.gitbook/assets/google-auth-kognitos-oauth-fields.png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
#### Authorize with Google

Click <kbd>Continue with Google</kbd>, sign in to Google, grant access, and return to Kognitos.
{% endstep %}
{% endstepper %}

Repeat this for each Google integration you want to connect. You can reuse the same OAuth app across all six integrations.

## Troubleshooting

| Issue | What to check |
| --- | --- |
| Redirect URI mismatch | Confirm the redirect URI is exactly `https://app.us-1.kognitos.com/oauth/connections/callback` |
| Unverified app warning | Make sure the OAuth app audience is set to **Internal**, and the user belongs to the same Google Workspace organization |
| Access blocked | Verify that the API for the integration is enabled in the Google Cloud project |
| Missing client secret | Create a new client secret in Google Cloud, then update the connection in Kognitos |

## Related Integration Pages

* [Gmail](gmail.md)
* [Google Calendar](googlecalendar.md)
* [Google Chat](chat.md)
* [Google Docs](googledocs.md)
* [Google Drive](googledrive.md)
* [Google Sheets](googlesheets.md)
