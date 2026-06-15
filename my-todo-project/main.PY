import json

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def saveTasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def addtask():
    task = input("enter your task: ")
    tasks.append(task)
    saveTasks()
    print("Added!")

def listtask():
    if not tasks:
        print("No tasks")
        return
    for i, task in enumerate(tasks):
        print(f"{i}. {task}")

def deletetask():
    listtask()
    try:
        i = int(input("task number to delete: "))
        if 0 <= i < len(tasks):
            print("Deleted:", tasks.pop(i))
            saveTasks()
        else:
            print("Invalid index")
    except ValueError:
        print("Invalid input")

while True:
    try:
        option = int(input("""
1. Add task
2. List tasks
3. Delete task
4. Exit
"""))
    except ValueError:
        print("Enter a number")
        continue

    if option == 1:
        addtask()
    elif option == 2:
        listtask()
    elif option == 3:
        deletetask()
    elif option == 4:
        break
    else:
        print("Invalid option")
