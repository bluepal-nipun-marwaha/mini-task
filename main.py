from task_manager import TaskManager

def run_demo():
    manager = TaskManager()

    manager.add_task("Write documentation")
    manager.add_task("Fix bug #42")

    tasks = manager.list_tasks()
    print("Tasks:", tasks)

    manager.complete_task(0)

    print("Completed tasks:", manager.list_completed())


if __name__ == "__main__":
    run_demo()
