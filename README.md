# Mini Task Manager

Mini Task Manager is a lightweight Python task management utility designed for learning and experimentation.  
It demonstrates a simple architecture for managing tasks, persisting them to disk, and interacting with them through a small API-like interface.

This repository is intentionally small and structured to demonstrate how code and documentation should stay synchronized as features evolve.

The system consists of three core modules:

- `task_manager.py` — main task management logic
- `storage.py` — persistence layer for saving and loading tasks
- `utils.py` — helper utilities for IDs and timestamps
- `main.py` — example usage

---

# Table of Contents

- Overview
- Architecture
- Installation
- Usage
- TaskManager API
- Storage Layer
- Utilities
- Data Format
- Example Workflow

---

# Overview

The Mini Task Manager provides basic functionality for creating and managing tasks.

Each task contains:

- a unique identifier
- a title
- a completion status

Tasks are stored locally in a JSON file so that data persists between program executions.

The application is intentionally minimal so that the code structure is easy to understand and extend.

---

# Architecture

The system is composed of three main layers.

## Task Manager Layer

The `TaskManager` class provides the public interface for interacting with tasks.

Responsibilities include:

- creating tasks
- marking tasks as completed
- retrieving task lists

The task manager does not directly interact with files.  
Instead it delegates persistence responsibilities to the storage layer.

---

## Storage Layer

The `TaskStorage` class manages reading and writing task data.

Responsibilities include:

- writing task data to disk
- loading tasks from disk
- maintaining the JSON file

Separating storage from business logic allows the application to easily switch to other storage systems in the future.

---

## Utility Layer

Utility functions provide reusable helpers such as:

- generating unique IDs
- creating timestamps

---

# Installation

Clone the repository:

```bash
git clone https://github.com/example/mini-task-manager.git
cd mini-task-manager
```

No external dependencies are required.

The project runs on **Python 3.8+**.

---

# Usage

Run the demo program:

```bash
python main.py
```

Example output:

```text
Tasks: [{'id': '...', 'title': 'Write documentation', 'completed': False}]
Completed tasks: [{'id': '...', 'title': 'Write documentation', 'completed': True}]
```

---

# TaskManager API

The `TaskManager` class provides the primary interface for interacting with tasks.

## Constructor

### `TaskManager()`

Creates a new task manager instance.

Internally this initializes a `TaskStorage` instance responsible for persistence.

---

## Methods

### `add_task(title)`

Creates a new task and stores it.

Parameters:

- **title (str)** — the task description

Behavior:

1. Generates a unique task ID
2. Creates a task object
3. Stores the task using the storage layer

Example:

```python
manager.add_task("Write documentation")
```

---

### `complete_task(task_index)`

Marks a task as completed.

Parameters:

- **task_index (int)** — index of the task in the list

If the index is valid, the task's `completed` flag will be updated.

Example:

```python
manager.complete_task(0)
```

---

### `list_tasks()`

Returns a list containing all stored tasks.

Example:

```python
tasks = manager.list_tasks()
```

Return value:

```json
[
  {
    "id": "...",
    "title": "Write documentation",
    "completed": false
  }
]
```

---

### `list_completed()`

Returns a filtered list containing only completed tasks.

Example:

```python
completed = manager.list_completed()
```

---

# Storage Layer

The `TaskStorage` class is responsible for persisting tasks to disk.

Tasks are stored in a JSON file named:

```
tasks.json
```

---

## Constructor

### `TaskStorage(file_path="tasks.json")`

Creates a storage manager.

Parameters:

- **file_path (str)** — location of the task file

---

## Methods

### `save_task(task)`

Adds a new task to the storage file.

Steps performed:

1. Loads existing tasks
2. Appends the new task
3. Writes updated data back to disk

Example:

```python
storage.save_task(task)
```

---

### `save_all(tasks)`

Writes an entire task list to disk.

This is typically used after updating task states.

Example:

```python
storage.save_all(tasks)
```

---

### `get_tasks()`

Loads all tasks from storage.

If the storage file does not exist, an empty list is returned.

Example:

```python
tasks = storage.get_tasks()
```

---

# Utilities

Utility functions are located in `utils.py`.

---

## `generate_task_id()`

Generates a unique identifier for tasks using UUID.

Example output:

```text
3f1c2a8e-bb8a-4f9d-9c8e-8df3b1e4c5b9
```

---

## `get_timestamp()`

Returns the current UTC timestamp in ISO format.

Example:

```text
2025-01-01T12:00:00Z
```

---

# Data Format

Tasks are stored in JSON format.

Example `tasks.json` file:

```json
[
  {
    "id": "a8c21e",
    "title": "Write documentation",
    "completed": false
  }
]
```

---

# Example Workflow

A typical workflow might look like:

1. Create a task manager instance

```python
manager = TaskManager()
```

2. Add tasks

```python
manager.add_task("Write documentation")
manager.add_task("Fix bug")
```

3. List tasks

```python
tasks = manager.list_tasks()
```

4. Complete a task

```python
manager.complete_task(0)
```

5. View completed tasks

```python
completed = manager.list_completed()
```

---

# Future Improvements

Potential improvements include:

- persistent database storage
- task deadlines
- task priorities
- tagging and filtering
- REST API interface
