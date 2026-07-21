import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks, description):
    tasks.append({"task": description, "done": False})
    save_tasks(tasks)
    print(f"Added: {description}")

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked done: {tasks[index]['task']}")
    else:
        print("Invalid task number.")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['task']}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add task  2. Complete task  3. Show tasks  4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_task(tasks, input("Task: "))
        elif choice == "2":
            show_tasks(tasks)
            complete_task(tasks, int(input("Task number: ")))
        elif choice == "3":
            show_tasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()