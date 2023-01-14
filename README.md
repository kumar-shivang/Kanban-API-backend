# Kanban API

Welcome to KanbanAPI - a simple Kanban board API built with Flask and SQLAlchemy. This API is used by the Kanban App which can be found [here](https://www.github.com/kumar-shivang/Kanban). The Kanban App is a simple Kanban board built with Vue 3 and Vite.

## Features

* Create, edit, and delete tasks
* Create, edit, and delete task lists
* Mark tasks as complete and incomplete
* export tasks as a CSV file
* daily task reminders
* monthly user summary
* user authentication
* caching

## Project Structure

```sh
.
├── api
│   ├── authAPI.py
│   ├── cardAPI.py
│   ├── exportAPI.py
│   ├── __init__.py
│   ├── listAPI.py
│   └── userAPI.py
├── app.py
├── cache
│   └── __init__.py
├── config
│   └── __init__.py
├── database
│   └── __init__.py
├── file_structure.txt
├── jobs
│   ├── export.py
│   └── __init__.py
├── mail
│   ├── daily_reminder.py
│   ├── __init__.py
│   └── monthly_summary.py
├── OpenAPI.yml
├── README.md
├── requirements.txt
├── run.sh
└── worker
    └── task.py

8 directories, 21 files
```

## Requirements

Requirements for the project are listed in the requirements.txt file.

## Installation

* Clone the repository

    ```bash
  git clone https://github.com/kumar-shivang/Kanban-API-backend.git
  cd Kanban-API-backend
  ```

* Build and run the app
  
    ```bash
      sh run.sh
    ```

* Run the redis server

    ```bash
    sh redis-server.sh
    ```

* Run the celery worker and beat

    ```bash
    sh run_worker.sh
    ```

## Usage

To use the Kanban App, simply run the app and go to the frontend. The frontend can be found [here](https://www.github.com/kumar-shivang/Kanban).
