![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
# Valgeir Users & Tasks (SQLite + Python)

A simple command-line application where you can manage users and their tasks using a SQLite database.

This project was created to practice Python + SQL basics (CRUD), input validation, and working with multiple Python modules.

---

## Features

### Users
- Add a user (name + age)
- List users (sorted by age and name)
- Update a user
- Delete a user (automatically deletes their tasks)

### Tasks
- Add a task to a specific user
- Show tasks for a specific user
- Update a task (change title or move to another user)
- Delete a task

### Statistics
- Total users
- Adults (18+)
- Oldest user
- Youngest user
- Average age

---

## Quick Demo


==== MENU ====

Add user

List users

Add task

Show tasks for user

Stats

Update user

Update task

Delete user

Delete task

Exit


Example workflow:


Add user: Valgeir, 33
Add task to user ID 1: Buy milk
Show tasks for user ID 1
Update task title or move it to another user
Delete a user (their tasks are deleted automatically)


---

## Project Structure


valgeirp_git/
│
├── VP_MANU_APP.py # Main menu (runs the app)
├── VP_DB.py # Database connection + table setup
├── VP_FUNCTIONS.py # All functions (CRUD + validation)
└── Valgeir_Palsson.db # SQLite database (created automatically)


---

## Requirements

- Python 3.x
- SQLite (included with Python, no installation required)

---

## How to Run

Open terminal / CMD in the project folder and run:


python VP_MANU_APP.py


(or `python3 VP_MANU_APP.py` depending on your system)

When the application starts, the database file will be created automatically if it does not exist:


Valgeir_Palsson.db


---

## How It Works

**VP_DB.py**
- Creates and connects to the SQLite database
- Creates tables if they do not already exist

**VP_FUNCTIONS.py**
Contains all application logic including:
- Input validation (name and positive integers)
- CRUD operations (Create, Read, Update, Delete)

**VP_MANU_APP.py**
- Displays the menu
- Calls the appropriate function based on user input

---

## Database Schema

### users

| column | type |
|------|------|
| id | INTEGER PRIMARY KEY |
| name | TEXT |
| age | INTEGER |

### tasks

| column | type |
|------|------|
| id | INTEGER PRIMARY KEY |
| title | TEXT |
| user_id | INTEGER |
| done | INTEGER (default 0) |

`user_id` references `users.id`.

The tasks table uses **ON DELETE CASCADE**, meaning:

If a user is deleted, all their tasks are deleted automatically.

---

## Planned Improvements

- Mark task as done / undone
- Show task status (✅ / ❌)
- Add "List all tasks" option
- Search users by name
- Add unit tests
- Convert the application into a FastAPI REST API

---

## License

This project was created for learning and practice.
