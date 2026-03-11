from storage import TaskStorage
from utils import generate_task_id


class TaskManager:

    def __init__(self):
        self.storage = TaskStorage()

    def add_task(self, title: str):
        task = {
            "id": generate_task_id(),
            "title": title,
            "completed": False
        }
        self.storage.save_task(task)

    def complete_task(self, task_index: int):
        tasks = self.storage.get_tasks()
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            self.storage.save_all(tasks)

    def list_tasks(self):
        return self.storage.get_tasks()

    def list_completed(self):
        tasks = self.storage.get_tasks()
        return [t for t in tasks if t["completed"]]

    def search_tasks(self, keyword: str):
        tasks = self.storage.get_tasks()
        return [t for t in tasks if keyword.lower() in t["title"].lower()]
