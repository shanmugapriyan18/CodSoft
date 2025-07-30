#Task 1: To-Do List 

# To-Do List Application

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nTasks:")
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. {task}")
    elif choice == '2':
        task = input("Enter task to add: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == '3':
        task_no = int(input("Enter task number to update: ")) - 1
        if 0 <= task_no < len(todo_list):
            new_task = input("Enter new task: ")
            todo_list[task_no] = new_task
            print("Task updated.")
        else:
            print("Invalid task number.")
    elif choice == '4':
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(todo_list):
            removed = todo_list.pop(task_no)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    elif choice == '5':
        print("Exiting To-Do List App.")
        break
    else:
        print("Invalid choice.")

