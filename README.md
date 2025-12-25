ToDoListUsingPythonStreamlit
A simple task manager application built with Streamlit and Python. This app allows users to manage their tasks, including adding new tasks, marking tasks as completed, deleting tasks, and viewing task analytics. Tasks are stored in a CSV file (tasks.csv) for persistence.

Features

Add Task: Add new tasks with due dates, priority levels, and comments.

View Tasks: View a list of all tasks, with options to mark them as completed or delete them.

Search and Filter Tasks: Search for tasks by name or filter them based on completion status (Completed or Pending).

Analytics: View statistics about your tasks, such as the total number of tasks, completed tasks, and pending tasks.

Clear All Tasks: Clear all tasks from the list in one click.

Tech Stack

Python: The primary programming language used for building the app.

Streamlit: A Python library to create interactive web applications.

Pandas: Used to manage and manipulate task data stored in CSV format.

CSV: Tasks are saved in a tasks.csv file for persistence.

Usage

Once the app is running, you can access the following features from the sidebar:

Add Task: Add new tasks with details like name, due date, priority, and comments.

View Tasks: View and manage your tasks. You can mark tasks as completed or delete them.

Search and Filter Tasks: Search tasks by name or filter them by their completion status (Completed or Pending).

Analytics: View statistics about your tasks: the total number, completed tasks, and pending tasks.

Clear All Tasks: Delete all tasks in the list.

Tasks are saved automatically to a file named tasks.csv in the project directory.

Installation

Install Dependencies To install the necessary libraries, run the following command in your terminal:

pip install streamlit pandas

Run the Application

Once the dependencies are installed, start the app by running this command:

streamlit run app.p# TO-DO-SITE
