import json
import csv

json_file = "tasks.json"
csv_file = "tasks.csv"

def load_tasks():
    with open(json_file, 'r') as file:
        return json.load(file)

def display_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def save_tasks(tasks):
    with open(json_file, 'w') as file:
        json.dump(tasks, file, indent=4)

def calculate_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    avg_priority = sum(task["priority"] for task in tasks) / total if total > 0 else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {avg_priority:.2f}")

def convert_to_csv(tasks):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"\nTasks have been successfully written to {csv_file}")

def mark_task_completed(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break

# Run all functions
tasks = load_tasks()
display_tasks(tasks)
calculate_statistics(tasks)

mark_task_completed(tasks, 3)
save_tasks(tasks)  # Save updated tasks

# Convert to CSV
convert_to_csv(tasks)
