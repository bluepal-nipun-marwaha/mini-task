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
- `export_tasks_json`: Export tasks to a JSON formatted string
- `save_task`: Save a single task to storage

Separating storage from business logic allows the application to easily switch to other storage systems in the future.

---

## Utility Layer

Utility functions provide reusable helpers such as:

- generating unique IDs
- creating timestamps

---

# Installation

Clone the repository:


