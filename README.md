# TODO List Backend

The backend interface for managing todo lists, complementing the [frontend](https://voitixler.com/course/coding/todo-frontend/), [available on GitHub](https://github.com/Luckykarter/todo-frontend).

## Table of Contents

- [Introduction](#introduction)
- [Code Structure](#code-structure)
  - [resources.py](#resourcespy)
  - [web_server.py](#web_serverpy)
- [RESTful API](#restful-api)
- [Getting Started](#getting-started)

## Introduction

This backend interface is designed to provide comprehensive todo list management. It allows for hierarchical organization of tasks with JSON serialization, along with RESTful API endpoints.

## Code Structure

### resources.py

Defines the main classes and functions for handling entries:

- `print_with_indent`: Function for indenting prints.
- `Entry`: Class for handling individual entries.
- `EntryManager`: Class for managing all entries.

### web_server.py

Code for running the Flask web server, including:

- Route handling
- CORS headers
- Application entry point

## RESTful API

Endpoints for managing the todo list:

- **`GET /api/entries/`**: Fetch all entries.
- **`POST /api/save_entries/`**: Save entries.

Each endpoint leverages the `Entry` and `EntryManager` classes to perform operations and return results.

## Getting Started

To run the server, you will first need to modify the `FOLDER` variable in `web_server.py`. This folder will act as a file-based local database where the entries will be saved.

```bash
FOLDER = 'Path\\to\\your\\local\\folder'
```

After setting up the folder, you can run the server with:

```bash
python web_server.py
```

The server will be running on 0.0.0.0:8000. You can access it through your browser or by using a tool like curl or Postman to interact with the RESTful API.
