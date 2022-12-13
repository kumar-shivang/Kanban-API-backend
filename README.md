<!--- This file creates a README.md file for the project. -->
<!--- This file is part of the project. -->
# Kanban App

A simple Kanban app built with Python Flask backend and VueJS frontend.

## Requirements

Requirements for the project are listed in the requirements.txt file.

## Installation

-1 Clone the repository

```bash
git clone https://github.com/kumar-shivang/Kanban

```

-2 Create a virtual environment

```bash
python3 -m venv venv
```

-3 Install the requirements
  
  ```bash
  pip install -r requirements.txt
  ```

-4 Create the database
  
  ```python
  from app import app, db
  with app.app_context():
      db.create_all()
  ```

-4 Run the app
  
  ```bash
  flask run
  ```

## Usage

To use the Kanban App, simply run the app and go to the url <http://localhost:5000/> or <http://127.0.0.1/5000/>
