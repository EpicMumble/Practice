tasks = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "x" if task["completed"] else "!"
        print(f"{i}. {task['name']} [{status}]")

    print("\nOptions:")
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter new choice: ")

    if choice == "1" :
        new_task = input("Enter new task: ")
        tasks.append({"name": new_task, "completed" : False})
        print("Task added!")

    elif choice == "2" :
            task_num = int(input("Enter task number to amrk as completed:" ))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
    
    elif    choice == "3" :
            task_num = int(input("Enter task numb to remove: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task removed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
            print("Goodbye!")
            break

    else:
        print("Invalid option.")
    