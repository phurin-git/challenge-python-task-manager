# Python Task Manager

Python Task Manager is a python cli task management, I practice python and git skill by do the challenge in Practical Software Engineering Final Project at WeStride. The application allows users to run in cli mode in the system console, add task, view all tasks, complete task, load and save task, and find task with word filtering.

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/phurin-git/westride-challenge-python-task-manager.git
```

2. Start the project

```bash
python runme.py
```

## Features

- Add New Task: Users can add tasks with a title, description, and a due date. Each task should be assigned a unique ID.
- View All Tasks: Display all tasks in a structured format. Separate tasks into pending and completed categories.
- Mark Task as Complete: Provide a feature that allows users to mark tasks as completed by referencing the task's unique ID.
- Delete Task: Users can delete tasks by their unique ID.
- Save and Load Tasks: All tasks should be saved to a JSON file and loaded when the program starts.
- Search Tasks: Add a function to search tasks by keywords or due date.
- CLI Mode: For user interaction. The CLI include:
  - A menu that displays available options (e.g., add task, view tasks, mark as complete, delete task, search tasks, exit).
  - Input validation to ensure proper task entry (e.g., no empty titles or invalid dates).
