"""
In this refactored code, the reg_user, add_task, view_all, view_mine, generate_reports, and display_statistics functions
are implemented according to the provided requirements.
The load_data and save_data functions are used to load and save data respectively.
The main function is responsible for handling the user menu and executing the corresponding functions based on user input.
"""

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

task_list = []
user_list = []

# Function to load data from files

def load_data():
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass

    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    for t_str in task_data:
        curr_t = {}
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False

        task_list.append(curr_t)

    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    for user in user_data:
        username, _ = user.split(';')
        user_list.append(username)

# Function to save data to files

def save_data():
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))

    with open("user.txt", "w") as user_file:
        user_data = []
        for username in user_list:
            user_data.append(f"{username};password")
        user_file.write("\n".join(user_data))

# Function to register a user

def reg_user():
    new_username = input("New Username: ")
    if new_username in user_list:
        print("Username already exists. Please choose a different username.")
        return

    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")
    if new_password == confirm_password:
        user_list.append(new_username)
        save_data()
        print("New user added.")
    else:
        print("Passwords do not match.")

# Function to add a task

def add_task():
    task_username = input("Name of person assigned to task: ")
    if task_username not in user_list:
        print("User does not exist. Please enter a valid username.")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified.")

    curr_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    save_data()
    print("New task added.")

# Function to view all tasks

def view_all():
    print("All Tasks:")
    for i, task in enumerate(task_list, 1):
        print(f"Task {i}:")
        print(f"Assigned to: {task['username']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Assigned Date: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Completed: {'Yes' if task['completed'] else 'No'}")
        print()

# Function to view tasks assigned to the user

def view_mine():
    username = input("Enter your username: ")
    if username not in user_list:
        print("User does not exist. Please enter a valid username.")
        return

    user_tasks = [task for task in task_list if task['username'] == username]
    if len(user_tasks) == 0:
        print("No tasks assigned to you.")
        return

    while True:
        print("Tasks assigned to you:")
        for i, task in enumerate(user_tasks, 1):
            print(f"Task {i}:")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Assigned Date: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Completed: {'Yes' if task['completed'] else 'No'}")
            print()

        print("Select a task number to perform an action or enter '-1' to return to the main menu.")
        task_choice = input("Task number: ")

        if task_choice == "-1":
            break

        try:
            task_choice = int(task_choice)
            if task_choice < 1 or task_choice > len(user_tasks):
                print("Invalid task number. Please choose a valid task.")
                continue

            selected_task = user_tasks[task_choice - 1]
            print("Task Options:")
            print("1. Mark task as complete")
            print("2. Edit task")
            print("3. Return to the task list")

            option_choice = input("Option: ")
            if option_choice == "1":
                if not selected_task['completed']:
                    selected_task['completed'] = True
                    save_data()
                    print("Task marked as complete.")
                else:
                    print("Task is already marked as complete.")
            elif option_choice == "2":
                if not selected_task['completed']:
                    new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                    due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                    selected_task['due_date'] = due_date_time
                    save_data()
                    print("Task due date updated.")
                else:
                    print("Task cannot be edited as it is already complete.")
            elif option_choice == "3":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

# Function to generate reports

def generate_reports():
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task['completed'])
    incomplete_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'] < date.today())
    incomplete_percentage = (incomplete_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / total_tasks) * 100

    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write("Task Overview:\n")
        task_overview_file.write(f"Total Tasks: {total_tasks}\n")
        task_overview_file.write(f"Completed Tasks: {completed_tasks}\n")
        task_overview_file.write(f"Incomplete Tasks: {incomplete_tasks}\n")
        task_overview_file.write(f"Overdue Tasks: {overdue_tasks}\n")
        task_overview_file.write(f"Incomplete Task Percentage: {incomplete_percentage}%\n")
        task_overview_file.write(f"Overdue Task Percentage: {overdue_percentage}%\n")

    total_users = len(user_list)
    assigned_tasks = {}
    for user in user_list:
        assigned_tasks[user] = len([task for task in task_list if task['username'] == user])

    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write("User Overview:\n")
        user_overview_file.write(f"Total Users: {total_users}\n")
        user_overview_file.write(f"Total Tasks: {total_tasks}\n")
        for user in user_list:
            user_tasks = assigned_tasks[user]
            user_task_percentage = (user_tasks / total_tasks) * 100
            completed_user_tasks = sum(1 for task in task_list if task['username'] == user and task['completed'])
            completed_user_task_percentage = (completed_user_tasks / user_tasks) * 100
            incomplete_user_task_percentage = 100 - completed_user_task_percentage
            overdue_user_tasks = sum(1 for task in task_list if task['username'] == user and not task['completed'] and task['due_date'] < date.today())
            overdue_user_task_percentage = (overdue_user_tasks / user_tasks) * 100

            user_overview_file.write(f"\nUsername: {user}\n")
            user_overview_file.write(f"Assigned Tasks: {user_tasks}\n")
            user_overview_file.write(f"Assigned Task Percentage: {user_task_percentage}%\n")
            user_overview_file.write(f"Completed Task Percentage: {completed_user_task_percentage}%\n")
            user_overview_file.write(f"Incomplete Task Percentage: {incomplete_user_task_percentage}%\n")
            user_overview_file.write(f"Overdue Task Percentage: {overdue_user_task_percentage}%\n")

def display_statistics():
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()

    with open("task_overview.txt", "r") as task_overview_file:
        task_overview_data = task_overview_file.read()
        print(task_overview_data)

    with open("user_overview.txt", "r") as user_overview_file:
        user_overview_data = user_overview_file.read()
        print(user_overview_data)

# Main program loop

def main():
    load_data()

    while True:
        print("Task Manager Menu:")
        print("Please select one of the following options:")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("gr - generate reports")
        print("ds - display statistics")
        print("e - exit")

        user_choice = input("Option: ")

        if user_choice == "r":
            reg_user()
        elif user_choice == "a":
            add_task()
        elif user_choice == "va":
            view_all()
        elif user_choice == "vm":
            view_mine()
        elif user_choice == "gr":
            generate_reports()
            print("Reports generated successfully.")
        elif user_choice == "ds":
            display_statistics()
        elif user_choice == "e":
            break
        else:
            print("Invalid option. Please choose a valid option.")

    print("Exiting Task Manager...")
    save_data()

if __name__ == "__main__":
    main()
