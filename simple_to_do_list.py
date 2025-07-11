import os
import json

TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Show all tasks with numbering"""
    print("\n📋 Your To-Do List:")
    if not tasks:
        print("No tasks yet! Add some tasks to get started.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print()

def add_task(tasks):
    """Add a new task"""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Added: {task}")
    else:
        print("⚠️ Task cannot be empty!")

def remove_task(tasks):
    """Remove a task by number"""
    display_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"❌ Removed: {removed}")
        else:
            print(f"⚠️ Please enter a number between 1-{len(tasks)}")
    except ValueError:
        print("⚠️ Please enter a valid number!")

def main():
    """Main application loop"""
    tasks = load_tasks()
    
    print("\n" + "="*40)
    print("✨ Command-Line To-Do List Manager")
    print("="*40)
    
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("\n💾 Saving your tasks...")
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter 1-4")

if __name__ == "__main__":
    main()