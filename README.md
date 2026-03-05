![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

# Valgeir Users & Tasks (SQLite + Python)

A command-line application where you can manage users and their tasks using a SQLite database.

This project was created to practice Python + SQL basics (CRUD), input validation, relational data, and working with multiple Python modules.

---

## Features

### Users
- Add user (name + age)
- List all users (ID, name, age, total tasks, pending tasks)
- Update user (by ID)
- Delete user (by ID, with confirmation)
- Search user by name

### Tasks
- Add task to a specific user (by user ID)
- List all tasks (status TODO/DONE, task ID, title, user)
- Show tasks for a specific user
- Update task (change title or move to another user)
- Delete task (by task ID, showing task list first)
- Filter tasks
  - show unfinished tasks
  - show finished tasks
- Toggle task done / undone

### Statistics

**User statistics**
- total users
- adults (18+)
- oldest user
- youngest user
- average age

**Task statistics**
- total tasks
- tasks done
- tasks remaining

---

## Quick Demo

Example output:

Users:

ID: 1 | Valgeir | age=35 | tasks=4 | pending=2  
ID: 2 | Sandra | age=37 | tasks=1 | pending=0  

Tasks:

[TODO] Task ID: 3 | Buy milk | User: Valgeir  
[DONE] Task ID: 4 | Clean room | User: Sandra  

Example workflow:

Add user: Valgeir, 35  
Add task to user ID 1: Buy milk  
Toggle task status → DONE  
Filter tasks → show unfinished tasks  
Search user by name → "Valgeir"

---

## Project Structure


valgeirp_git/
│
├── VP_MANU_APP.py # Main menu (runs the app)
├── VP_DB.py # Database connection + table setup
├── VP_FUNCTIONS.py # Functions (CRUD + validation + helpers)
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

### VP_DB.py
- Creates and connects to the SQLite database
- Creates tables if they do not already exist

### VP_FUNCTIONS.py
Contains all application logic including:

- Input validation (name and positive integers)
- CRUD operations (Create, Read, Update, Delete)
- Task filtering and status toggling
- Statistics queries
- Helper functions for printing users and tasks

### VP_MANU_APP.py
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

- Convert the application into a FastAPI REST API
- Add unit tests
- Add due dates for tasks
- Export users and tasks to CSV
- Add pagination for large datasets

---

## License

MIT (This project was created for learning and practice.)