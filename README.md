* Valgeir Users & Tasks (SQLite + Python)
* A simple console app where you can manage users and tasks using a SQLite database.
  This project is made to practice Python + SQL basics (CRUD), input validation, and working with files/modules.

*Features

Users
Add a user (name + age)
List users (sorted by age and name)
Update a user
Delete a user (and automatically delete their tasks)
Tasks
Add a task to a specific user (by user )
Show tasks for a specific user
Update a task (title + move to another user)
Delete a task

*Stats
Total users
Adults (18+)
Oldest user
Youngest user
Average age

Project structure
valgeirp_git/
│
├── VP_MANU_APP.py       # Main menu (runs the app)
├── VP_DB.py             # Database connection + table setup
├── VP_FUNCTIONS.py      # All functions (CRUD + validation)
└── Valgeir_Palsson.db   # SQLite database (created automatically)

*Requirements
Python 3.x
SQLite is included with Python (no extra install needed)

*How to run
Open terminal / CMD in the project folder

*Run the app:
python VP_MANU_APP.py
(or python3 VP_MANU_APP.py depending on your setup)

*When you run the app, the database file will be created automatically if it doesn’t exist:
Valgeir_Palsson.db

*How it works (short explanation)
VP_DB.py creates/opens the database using sqlite3.connect()
setup_tables() creates the tables if they don’t exist
VP_FUNCTIONS.py contains all logic for:
input validation (name, positive integers)
CRUD actions (Create, Read, Update, Delete)
VP_MANU_APP.py shows the menu and calls the correct function based on your choice

**Database tables
*users
id (PRIMARY KEY)
name (TEXT, required)
age (INTEGER, required)

*tasks
id (PRIMARY KEY)
title (TEXT, required)
user_id (FOREIGN KEY → users.id)
done (INTEGER, default 0)

*The tasks table uses a foreign key with ON DELETE CASCADE, meaning:
If a user is deleted, all their tasks are deleted automatically.
Example usage
Add user: Valgeir, 33
Add task to user ID 1: Buy milk
Show tasks for user ID 1
Update task title or move it to another user
Delete a user and tasks will be removed automatically
Known improvements / next steps (ideas/in progress)
Add “Mark task as done/undone” (in progress)
Show tasks with ✅ / ❌ status (in progress)
Add “List all tasks” option (in progress)
Add search (find user by name) (in progress)
Add unit tests

*The database file is ignored in Git (.gitignore).
*It will be created automatically when the application runs.

*License
*This project is for learning/practice.
