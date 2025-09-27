# todo.py
# Console-based To-Do List Application with persistence

TASKS_FILE = "tasks.txt"

# ===== Load tasks from file =====
def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # if file doesn't exist, start with empty list
        tasks = []
    return tasks

# ===== Save tasks to file =====
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ===== Display all tasks =====
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# ===== Main Program =====
def todo_app():
    tasks = load_tasks()
    print("=== Welcome to To-Do List Manager ===")

    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Exiting To-Do List. Goodbye 👋")
            break

        else:
            print("Invalid choice. Please try again.")

# ===== Run Program =====
if __name__ == "__main__":
    todo_app()
