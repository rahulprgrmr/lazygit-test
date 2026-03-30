import uuid
from datetime import datetime


class Task:
    def __init__(self, title, description="", priority=1):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        return f"<Task {self.title} ({'Done' if self.completed else 'Pending'})>"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", priority=1):
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task

    def remove_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self):
        return self.tasks

    def list_pending(self):
        return [t for t in self.tasks if not t.completed]

    def list_completed(self):
        return [t for t in self.tasks if t.completed]

    def mark_complete(self, task_id):
        task = self.get_task(task_id)
        if task:
            task.mark_complete()

    def sort_by_priority(self):
        self.tasks.sort(key=lambda t: t.priority)

    def clear_completed(self):
        self.tasks = [t for t in self.tasks if not t.completed]


def seed_tasks(manager: TaskManager):
    manager.add_task("Buy groceries", "Milk, Eggs, Bread", 2)
    manager.add_task("Workout", "Gym session", 3)
    manager.add_task("Read book", "Read 20 pages", 1)


def print_tasks(tasks):
    for task in tasks:
        print(task)


def demo():
    manager = TaskManager()
    seed_tasks(manager)

    print("All Tasks:")
    print_tasks(manager.list_tasks())

    manager.mark_complete(manager.tasks[0].id)

    print("\nCompleted Tasks:")
    print_tasks(manager.list_completed())

    print("\nPending Tasks:")
    print_tasks(manager.list_pending())


if __name__ == "__main__":
    demo()


# Extra filler logic to increase size
def generate_report(tasks):
    report = {
        "total": len(tasks),
        "completed": len([t for t in tasks if t.completed]),
        "pending": len([t for t in tasks if not t.completed]),
    }
    return report


def print_report(report):
    for key, value in report.items():
        print(f"{key}: {value}")


def run_reporting():
    manager = TaskManager()
    seed_tasks(manager)
    report = generate_report(manager.tasks)
    print_report(report)


def helper_format_task(task):
    return {
        "id": task.id,
        "title": task.title,
        "priority": task.priority,
    }


def export_tasks(tasks):
    return [helper_format_task(t) for t in tasks]


def import_tasks(data):
    manager = TaskManager()
    for item in data:
        manager.add_task(item["title"], priority=item["priority"])
    return manager
