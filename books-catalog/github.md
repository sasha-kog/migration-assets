---
title: GitHub
updated: 2026-02-06T18:35
git_hash: 96fe46f35e7cfa463a2b9d69b77e09f9e667b129
description: Overview of the GitHub integration.
icon: github
---

# GitHub

{% hint style="info" %}
The following documentation is for **GitHub v2.0.1**.
{% endhint %}

## Overview

GitHub is the world's leading platform for version control and collaborative software development. This integration enables automated repository management, issue tracking, pull request operations, and code deployment workflows. Streamline your development processes and enhance team collaboration on code projects.

## Setup

The following integrations need to be connected to your Kognitos workspace:

* **GitHub**

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

Add a name for the connection. You'll be prompted for [**authentication**](github.md#authentication) details if needed. Then, click on <kbd>**Connect**</kbd>.
{% endstep %}
{% endstepper %}

## Authentication

Use one of the following authentication methods to connect this integration in Kognitos. Each method has its own configuration requirements.

### Connect using API Key

Connect to the GitHub API using an API key.

| Label   | Description                           | Type        |
| ------- | ------------------------------------- | ----------- |
| API Key | The API key to be used for connecting | `sensitive` |

## Actions

The following actions are available in the **GitHub** integration:

### 1. Create a pull request in a repository source

Create a pull request for a specified GitHub repository.

### 2. Create an issue in a repository source

Create an issue for a specified GitHub repository.

### 3. Get the commits from a repository source

Get the commits from a GitHub repository.

### 4. Get the issues from a repository source

Get the issues from a GitHub repository.

### 5. Get the pull request from a repository source

Get a pull request from a GitHub repository.

### 6. Get the pull requests from a repository source

Get the pull requests from a GitHub repository.

### 7. Get the repositories from a source organization

Get the repositories from a GitHub organization.

### 8. Get the team from a source organization

Get a team from a GitHub organization.

### 9. Get the teams from a source organization

Get the teams from a GitHub organization.

### 10. Get the user from a name

Get a user from GitHub.

### 11. Request reviewers for a pull request

Request reviewers for a pull request in a specified GitHub repository.

### 12. Update a pull request in a repository source

Update a pull request for a specified GitHub repository.

### 13. Update an issue in a repository source

Update an issue for a specified GitHub repository.

## Concepts

### Github issue

GitHub Issue Wrapper class.

| Field Name                         | Description                                                                      | Type                             |
| ---------------------------------- | -------------------------------------------------------------------------------- | -------------------------------- |
| `number`                           | The number of the issue. Optional since is None in case of creating an issue.    | `optional[number]`               |
| `title`                            | The title of the issue. Optional since can be None in case of editing an issue.  | `optional[text]`                 |
| `body`                             | The body of the issue. Optional since can be None in case of editing an issue.   | `optional[text]`                 |
| `state`                            | The state of the issue. Optional since is None in case of creating an issue.     | `optional[text]`                 |
| [`labels`](github.md#github-label) | The labels of the issue. Optional since can be None in case of editing an issue. | `optional[list of github label]` |
| [`user`](github.md#github-user)    | The user of the issue. Optional since is None in case of creating an issue.      | `optional[github user]`          |

### Github label

GitHub Label Wrapper class.

| Field Name    | Description                   | Type             |
| ------------- | ----------------------------- | ---------------- |
| `color`       | The color of the label.       | `text`           |
| `description` | The description of the label. | `optional[text]` |
| `name`        | The name of the label.        | `text`           |
| `url`         | The URL of the label.         | `text`           |

### Github user

GitHub User Wrapper class.

| Field Name | Description            | Type               |
| ---------- | ---------------------- | ------------------ |
| `login`    | The login of the user. | `optional[text]`   |
| `id`       | The ID of the user.    | `optional[number]` |
| `type`     | The type of the user.  | `optional[text]`   |

### Github pull request

GitHub Pull Request Wrapper class.

| Field Name | Description                                                                                  | Type                                            |
| ---------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `number`   | The number of the pull request. Optional since is None in case of creating a pull request.   | `optional[number]`                              |
| `head`     | The head of the pull request. Optional since can be None in case of editing a pull request.  | `optional[github pull request part?` or `text]` |
| `title`    | The title of the pull request. Optional since can be None in case of editing a pull request. | `optional[text]`                                |
| `base`     | The base of the pull request. Optional since can be None in case of editing a pull request.  | `optional[github pull request part?` or `text]` |
| `body`     | The body of the pull request. Optional since can be None in case of editing a pull request.  | `optional[text]`                                |
| `state`    | The state of the pull request. Optional since is None in case of creating a pull request.    | `optional[text]`                                |

### Github commit

GitHub Commit Wrapper class.

| Field Name                               | Description            | Type                            |
| ---------------------------------------- | ---------------------- | ------------------------------- |
| [`commit`](github.md#github-git-commit)  | The commit.            | `optional[github git commit]`   |
| `sha`                                    | The SHA of the commit. | `optional[text]`                |
| [`stats`](github.md#github-commit-stats) | The commit stats.      | `optional[github commit stats]` |
| `url`                                    | The URL of the commit. | `optional[text]`                |

### Github git commit

GitHub Git Commit Wrapper class.

| Field Name                                 | Description                  | Type                          |
| ------------------------------------------ | ---------------------------- | ----------------------------- |
| [`author`](github.md#github-git-author)    | The author of the commit.    | `optional[github git author]` |
| [`committer`](github.md#github-git-author) | The committer of the commit. | `optional[github git author]` |
| `message`                                  | The message of the commit.   | `optional[text]`              |
| `sha`                                      | The SHA of the commit.       | `optional[text]`              |

### Github commit stats

GitHub Commit Stats Wrapper class.

| Field Name  | Description                  | Type     |
| ----------- | ---------------------------- | -------- |
| `total`     | The total number of commits. | `number` |
| `deletions` | The number of deletions.     | `number` |
| `additions` | The number of additions.     | `number` |

### Github repository

GitHub Repository Wrapper class.

| Field Name        | Description                        | Type   |
| ----------------- | ---------------------------------- | ------ |
| `branches_url`    | The branches URL.                  | `text` |
| `commits_url`     | The commits URL.                   | `text` |
| `description`     | The description of the repository. | `text` |
| `git_commits_url` | The git commits URL.               | `text` |
| `git_tags_url`    | The git tags URL.                  | `text` |
| `git_url`         | The git URL.                       | `text` |
| `name`            | The name of the repository.        | `text` |

### Github team

GitHub Team Wrapper class.

| Field Name                         | Description                       | Type                            |
| ---------------------------------- | --------------------------------- | ------------------------------- |
| `id`                               | The ID of the team.               | `number`                        |
| `url`                              | The URL of the team.              | `text`                          |
| `name`                             | The name of the team.             | `text`                          |
| `slug`                             | The slug of the team.             | `text`                          |
| `description`                      | The description of the team.      | `text`                          |
| `privacy`                          | The privacy of the team.          | `text`                          |
| `permission`                       | The permission of the team.       | `text`                          |
| [`members`](github.md#github-user) | The members of the team.          | `optional[list of github user]` |
| `members_url`                      | The members URL of the team.      | `optional[text]`                |
| `repositories_url`                 | The repositories URL of the team. | `text`                          |
