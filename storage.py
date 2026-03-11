import json


class TaskStorage:

    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path

    def save_task(self, task: dict):
        tasks = self.get_tasks()
        tasks.append(task)
        self.save_all(tasks)

    def save_all(self, tasks: list):
        with open(self.file_path, "w") as f:
            json.dump(tasks, f, indent=2)

    def get_tasks(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def export_tasks_json(self):
        return json.dumps(self.get_tasks(), indent=2)
