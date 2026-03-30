import uuid
from datetime import datetime
from enum import Enum


class Status(Enum):
    PENDING = "pending"
    DONE = "done"


class Task:
    def __init__(self, title, description="", level=1):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.status = Status.PENDING
        self.created_at = datetime.now()

    def mark_done(self):
        self.status = Status.DONE

    def is_completed(self):
        return self.status == Status.DONE

    def __repr__(self):
        return f"{self.title} [{self.status.value}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, description="", priority=1):
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task

    def remove(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def get(self, task_id):
        return next((t for t in self.tasks if t.id == task_id), None)

    def all(self):
        return self.tasks

    def filter_by_priority(self, min_priority):
        return [t for t in self.tasks if t.priority >= min_priority]

    def mark_done(self, task_id):
        task = self.get(task_id)
        if task:
            task.mark_done()

    def sort(self):
        self.tasks.sort(key=lambda t: t.priority)

    def cleanup(self):
        self.tasks = [t for t in self.tasks if not t.is_completed()]


def seed(manager):
    manager.add("Buy groceries", priority=2)
    manager.add("Workout", priority=3)
    manager.add("Read book", priority=1)


def show(tasks):
    for t in tasks:
        print(t)


def report(tasks):
    return {
        "total_tasks": len(tasks),
        "completed_tasks": len([t for t in tasks if t.is_completed()]),
    }


def print_report(r):
    print("Report Summary")
    for k, v in r.items():
        print(k, ":", v)


def demo():
    manager = TaskManager()
    seed(manager)

    manager.mark_done(manager.tasks[0].id)

    show(manager.all())
    print_report(report(manager.tasks))


# filler
def export(tasks):
    return [{"id": t.id, "title": t.title} for t in tasks]


def import_data(data):
    manager = TaskManager()
    for d in data:
        manager.add(d["title"])
    return manager


def stats(tasks):
    return {
        "high_priority": len([t for t in tasks if t.priority > 2]),
        "low_priority": len([t for t in tasks if t.priority <= 2]),
    }


def debug(tasks):
    for t in tasks:
        print(t.id, t.title)
