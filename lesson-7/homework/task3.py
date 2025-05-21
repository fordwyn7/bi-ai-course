import json
import csv
import os
from datetime import datetime
from abc import ABC, abstractmethod


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date 
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            due_date=data.get("due_date"),
            status=data.get("status", "Pending"),
        )

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


# Abstract base class for storage
class StorageInterface(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self, tasks):
        pass


# CSV Storage Implementation
class CSVStorage(StorageInterface):
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def load(self):
        tasks = []
        if not os.path.exists(self.filename):
            return tasks
        with open(self.filename, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task.from_dict(row))
        return tasks

    def save(self, tasks):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["task_id", "title", "description", "due_date", "status"],
            )
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())


# JSON Storage Implementation
class JSONStorage(StorageInterface):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            data = json.load(file)
            return [Task.from_dict(task) for task in data]

    def save(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

class TaskManager:
    def __init__(self, storage: StorageInterface):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        if any(t.task_id == task.task_id for t in self.tasks):
            raise ValueError(f"Task ID {task.task_id} already exists.")
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def update_task(
        self, task_id, title=None, description=None, due_date=None, status=None
    ):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                return
        raise ValueError("Task ID not found.")

    def delete_task(self, task_id):
        original_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        if len(self.tasks) == original_length:
            raise ValueError("Task ID not found.")

    def filter_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status.lower() == status.lower()]

    def save_tasks(self):
        self.storage.save(self.tasks)

    def load_tasks(self):
        self.tasks = self.storage.load()


def main():
    # Choose storage (CSV or JSON)
    storage = JSONStorage()  # or CSVStorage()
    manager = TaskManager(storage)

    menu = """
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
"""

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                task_id = input("Enter Task ID: ").strip()
                title = input("Enter Title: ").strip()
                description = input("Enter Description: ").strip()
                due_date = (
                    input("Enter Due Date (YYYY-MM-DD, optional): ").strip() or None
                )
                status = input("Enter Status (Pending/In Progress/Completed): ").strip()
                manager.add_task(Task(task_id, title, description, due_date, status))
                print("Task added successfully!")

            elif choice == "2":
                tasks = manager.view_tasks()
                if not tasks:
                    print("No tasks available.")
                for task in tasks:
                    print(task)

            elif choice == "3":
                task_id = input("Enter Task ID to update: ").strip()
                title = input("Enter new Title (leave blank to keep current): ").strip()
                description = input(
                    "Enter new Description (leave blank to keep current): "
                ).strip()
                due_date = input(
                    "Enter new Due Date (leave blank to keep current): "
                ).strip()
                status = input(
                    "Enter new Status (leave blank to keep current): "
                ).strip()
                manager.update_task(
                    task_id,
                    title or None,
                    description or None,
                    due_date or None,
                    status or None,
                )
                print("Task updated.")

            elif choice == "4":
                task_id = input("Enter Task ID to delete: ").strip()
                manager.delete_task(task_id)
                print("Task deleted.")

            elif choice == "5":
                status = input("Enter status to filter by: ").strip()
                tasks = manager.filter_tasks_by_status(status)
                if not tasks:
                    print("No tasks with that status.")
                for task in tasks:
                    print(task)

            elif choice == "6":
                manager.save_tasks()
                print("Tasks saved.")

            elif choice == "7":
                manager.load_tasks()
                print("Tasks loaded.")

            elif choice == "8":
                manager.save_tasks()
                print("Exiting.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
