<!--- This file creates a README.md file for the project. -->
<!--- This file is part of the project. -->
# Kanban App

A simple Kanban app built with Python Flask backend and VueJS frontend.

## Requirements
<--!- This section lists the requirements for the project. -->
- Python 3.11
- VueJS 3.0.11
- Flask 2.0.1
- sqlite3 3.35.5
- sqlalchemy 1.4.22

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
