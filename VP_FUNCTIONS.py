def input_valid_name(prompt="Enter your name: "): # Insert name
    while True:
        name= input(prompt).strip()
        if name =="":
            print("That isn´t your name!")
            continue
        if name.replace(" ", "").isalpha():
            return name
        print("Only letters and spaces! Please")
        
def input_valid_positive_int(prompt): # Numbers for age
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if val <= 0:
                print("You need to put in positive number!")
                continue
            return val
        except ValueError:
            print("Put in a number! please")
            
def list_users(cursor): # Users in ORDER BY aga ASC
    cursor.execute("SELECT id, name, age FROM users ORDER BY age ASC, name ASC")
    users = cursor.fetchall()
    if not users:
        print("No users in database.")
        return[]
    print("\nUsers:")
    for user_id, name, age in users:
        print (f"ID: {user_id} | {name} | age={age}")
    print()
    return users

def add_user(cursor, conn): # Add user (name,age)
    name = input_valid_name()
    age = input_valid_positive_int("Enter age: ")

    cursor.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("User added\n")

def add_task(cursor, conn): # Add task by ID
    users = list_users(cursor)
    if not users:
        return
    
    user_id = input_valid_positive_int("Enter user ID: ")

    cursor.execute("SELECT name FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user is None:
        print("User not found.\n")
        return
    
    while True: # Ask for task
        title = input(f"Enter task for {user[0]}: ").strip()
        if title == "":
            print("Task can´t be empty!")
        else:
            break

    cursor.execute(
        "INSERT INTO tasks (title, user_id) VALUES (?, ?)", (title, user_id))
    conn.commit()
    print(f"Task added for {user[0]}!\n")
    
def show_tasks_for_user(cursor): #Showing task/s for user
    users = list_users(cursor)
    if not users:
        return
    user_id = input_valid_positive_int("Enter user ID to show tasks for: ")

    cursor.execute("SELECT name FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user is None:
        print("User not found.\n")
        return   

    cursor.execute("""
        SELECT id, title, done
        FROM tasks
        WHERE user_id = ?
        ORDER BY id
    """, (user_id,))
    tasks = cursor.fetchall()
    
    print(f"\nTasks for {user[0]}:")

    if not tasks:
        print("No tasks found for this user.\n")
    else:
        for task_id, title, done in tasks:
            status = "✅" if done == 1 else "❌"
            print(f"{status} Task ID: {task_id} | Title: {title}")
        print()
        
def show_stats(cursor): #Show users age status (count, 18+, max(age), min(age), avg(age))
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users WHERE age >= 18")
    adults = cursor.fetchone()[0]

    cursor.execute("SELECT MAX(age) FROM users")
    max_age = cursor.fetchone()[0]
    
    cursor.execute("SELECT MIN(age) FROM users")
    min_age = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(age) FROM users")
    avg_age = cursor.fetchone()[0]

    print("\n--- Stats ---")
    print(f"Total users: {total_users}")
    print(f"Adults (18+): {adults}")
    print(f"Oldest User: {max_age if max_age is not None else 'N/A'}")
    print(f"Youngest User: {min_age if min_age is not None else 'N/A'}")
    print(f"Average age: {avg_age:.2f}" if avg_age is not None else "Average age: N/A")
    print()
    
def update_user(cursor, conn): # Update user (name & age)
    users = list_users(cursor)
    if not users:
        return

    user_id = input_valid_positive_int("Enter user ID to update: ")

    cursor.execute("SELECT id, name, age FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if user is None:
        print("User not found.\n")
        return

    old_id, old_name, old_age = user
    print(f"Current: ID={old_id} | {old_name} | age={old_age}")

# New name
    new_name_input = input("Enter new name (leave blank to keep current): ").strip()

    if new_name_input == "":
        new_name = old_name
    else:
        while True:
            if new_name_input.replace(" ", "").isalpha():
                new_name = new_name_input
                break
            print("Name must contain only letters and spaces!")
            new_name_input = input("Enter new name: ").strip()

# New age
    new_age_raw = input("Enter new age (leave blank to keep current): ").strip()

    if new_age_raw == "":
        new_age = old_age
    else:
        try:
            new_age = int(new_age_raw)
            if new_age <= 0:
                print("Age must be positive.\n")
                return
        except ValueError:
            print("Age must be a number.\n")
            return

    cursor.execute(
        "UPDATE users SET name = ?, age = ? WHERE id = ?",
        (new_name, new_age, user_id))
    conn.commit()

    print("User updated successfully!\n")
    
def get_user_by_id(cursor, user_id): # Get user by id
    cursor.execute(
        "SELECT id, name, age FROM users WHERE id = ?",
        (user_id,))
    return cursor.fetchone()

def get_task_by_id(cursor, task_id): # Get task by id
    cursor.execute(
        "SELECT id, title, user_id FROM tasks WHERE id = ?",
        (task_id,))
    return cursor.fetchone()

def update_task(cursor, conn): # Update task
    cursor.execute("""
        SELECT tasks.id, tasks.title, users.name
        FROM tasks
        JOIN users ON tasks.user_id = users.id
        ORDER BY tasks.id
    """)
    rows = cursor.fetchall()

    if not rows:
        print("\nNo tasks in database.\n")
        return

    print("\nTasks:")
    for task_id, title, user_name in rows:
        print(f"Task ID: {task_id} | {title} | user={user_name}")
    print()

    task_id = input_valid_positive_int("Enter task ID to update: ")

    task = get_task_by_id(cursor, task_id)
    if task is None:
        print("Task not found.\n")
        return

    old_task_id, old_title, old_user_id = task
    print(f"Current: Task ID={old_task_id} | title='{old_title}' | user_id={old_user_id}")

# New title
    new_title = input("Enter new task or Enter to keep current: ").strip()
    if new_title == "":
        new_title = old_title


    new_user_raw = input("Enter Another user ID or Enter to keep current: ").strip()
    if new_user_raw != "":
        try:
            new_user_id = int(new_user_raw)
            if new_user_id <= 0:
                print("User ID must be positive.\n")
                return
        except ValueError:
            print("User ID must be a number.\n")
            return

        if get_user_by_id(cursor, new_user_id) is None:
            print("No user with that ID.\n")
            return
    else:
        new_user_id = old_user_id

    cursor.execute(
        "UPDATE tasks SET title = ?, user_id = ? WHERE id = ?",
        (new_title, new_user_id, task_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("No changes made.\n")
    else:
        print("Task updated successfully!\n")
    

def delete_user_by_id(cursor, conn): # Delete user by ID
    users = list_users(cursor)
    if not users:
        return

    user_id = input_valid_positive_int("Enter user ID to delete: ")

    cursor.execute("SELECT name FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user is None:
        print("User not found.\n")
        return

    confirm = input(f"Are you sure you want to delete {user[0]}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.\n")
        return

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("No user deleted.\n")
    else:
        print("User deleted.\n")


def delete_task_by_id(cursor, conn): # Delete task by ID
    task_id = input_valid_positive_int("Enter task ID to delete: ")

    task = get_task_by_id(cursor, task_id)
    if task is None:
        print("Task not found.\n")
        return

    _, title, user_id = task
    confirm = input(f"Delete task '{title}' (task_id={task_id})? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.\n")
        return

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("No task deleted.\n")
    else:
        print("Task deleted.\n")