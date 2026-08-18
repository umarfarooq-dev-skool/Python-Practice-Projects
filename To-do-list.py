FILE_NAME = "tasks.txt"


def add_task():
    task = input("Enter task: ")

    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")

    print("Task added!")


def view_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

            for number, task in enumerate(tasks, 1):
                print(number, "-", task.strip())

    except FileNotFoundError:
        print("No tasks found.")


while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        break

    else:
        print("Invalid choice!")