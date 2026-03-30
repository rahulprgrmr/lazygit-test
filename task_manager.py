import uuid
from datetime import datetime


class Task:
    def __init__(self, title, description="", level=1):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.level = level
        self.is_done = False
        self.created_at = datetime.utcnow()

    def complete(self):
        self.is_done = True

    def __repr__(self):
        status = "✔" if self.is_done else "✘"
        return f"[{status}] {self.title} (L{self.level})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description="", level=1):
        task = Task(title, description, level)
        self.tasks.append(task)
        return task

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def find_task(self, task_id):
        return next((t for t in self.tasks if t.id == task_id), None)

    def all_tasks(self):
        return list(self.tasks)

    def completed_tasks(self):
        return [t for t in self.tasks if t.is_done]

    def pending_tasks(self):
        return [t for t in self.tasks if not t.is_done]

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            task.complete()

    def sort_tasks(self):
        self.tasks.sort(key=lambda t: (-t.level, t.created_at))

    def purge_completed(self):
        self.tasks = [t for t in self.tasks if not t.is_done]


def seed(manager):
    manager.create_task("Buy groceries", level=2)
    manager.create_task("Workout", level=3)
    manager.create_task("Read book", level=1)


def display(tasks):
    for t in tasks:
        print(t)


def generate_report(tasks):
    return {
        "count": len(tasks),
        "done": sum(1 for t in tasks if t.is_done),
        "not_done": sum(1 for t in tasks if not t.is_done),
    }


def print_report(report):
    print("=== REPORT ===")
    for k, v in report.items():
        print(f"{k.upper()} => {v}")


def demo():
    manager = TaskManager()
    seed(manager)

    manager.complete_task(manager.tasks[0].id)

    display(manager.all_tasks())
    report = generate_report(manager.tasks)
    print_report(report)


# filler for length
def serialize(tasks):
    return [
        {
            "id": t.id,
            "title": t.title,
            "level": t.level,
        }
        for t in tasks
    ]


def deserialize(data):
    manager = TaskManager()
    for item in data:
        manager.create_task(item["title"], level=item["level"])
    return manager


def debug_dump(tasks):
    for t in tasks:
        print(vars(t))


def extra_logic():
    manager = TaskManager()
    seed(manager)
    debug_dump(manager.tasks)
