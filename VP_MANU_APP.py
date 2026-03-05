#Connect to functions and database
from VP_DB import get_connection, setup_tables
from VP_FUNCTIONS import (
    add_user, list_users, add_task, show_tasks_for_user, show_stats,
    update_user, update_task, delete_user_by_id, delete_task_by_id, search_user, list_all_tasks, filter_tasks, toggle_task_done)
def main():
    conn, cursor = get_connection()
    setup_tables(cursor, conn)

    # Drive Menu
    while True:
        print("==== MENU ====")
        print("1) Add user")
        print("2) Add task")
        print("3) List all users")
        print("4) List all tasks")
        print("5) Stats")
        print("6) Update user")
        print("7) Update task")
        print("8) Delete user")
        print("9) Delete task")
        print("10) Exit")
        print("11) Search user by name")
        print("12) Show tasks for user")
        print("13) Filter tasks")
        print("14) Toggle task done/undone")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_user(cursor, conn)
        elif choice == "2":
            add_task(cursor, conn)
        elif choice == "3":
            list_users(cursor)
        elif choice == "4":
            list_all_tasks(cursor)
        elif choice == "5":
            show_stats(cursor)
        elif choice == "6":
            update_user(cursor, conn)
        elif choice == "7":
            update_task(cursor, conn)
        elif choice == "8":
            delete_user_by_id(cursor, conn)
        elif choice == "9":
            delete_task_by_id(cursor, conn)
        elif choice == "10":
            break
        elif choice == "11":
            search_user(cursor)
        elif choice == "12":
            show_tasks_for_user(cursor)
        elif choice == "13":
            filter_tasks(cursor)
        elif choice == "14":
            toggle_task_done(cursor, conn)
        else:
            print("Invalid choice.\n")
            
#close DB
    conn.close()
    print("Thank you for trying me! ;)")

 # Main Menu 
if __name__ == "__main__":
    main()