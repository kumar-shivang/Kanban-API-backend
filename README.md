<!--- This file creates a README.md file for the project. -->
<!--- This file is part of the project. -->
# Kanban App

Welcome to KanbanApp, a simple Kanban-style task management application built using the Flask web framework for backend API and VueJS framework. With KanbanApp, you can easily organize and manage your tasks in a flexible and intuitive way.

## Features

* Create, edit, and delete tasks
* Create, edit, and delete task lists
* Drag and drop tasks to move them between lists
* Mark tasks as complete and incomplete
* Filter tasks by list and completion status
* Search for tasks by name
* Responsive design

## Requirements

Requirements for the project are listed in the requirements.txt file.

## Installation

* Clone the repository

```bash
git clone https://github.com/kumar-shivang/Kanban

```

1. Create a virtual environment

```bash
python3 -m venv venv
```

2. Install the requirements
  
  ```bash
  pip install -r requirements.txt
  ```

3. Create the database
  
  ```python
  from app import app, db
  with app.app_context():
      db.create_all()
  ```

4. Run the app
  
  ```bash
  flask run
  ```

## Usage

To use the Kanban App, simply run the app and go to the url <http://localhost:5000/> or <http://127.0.0.1/5000/>
