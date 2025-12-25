import streamlit as st
import pandas as pd
import datetime
import os

# ---------- BACKGROUND COLOR ----------
page_bg_style = """
<style>
.stApp {
  background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
  background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_style, unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align: center;'>📋 To-Do List Application</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Manage your tasks easily using To-do App</p>",
    unsafe_allow_html=True
)



# File to store tasks
TASKS_FILE = 'tasks.csv'

# Load tasks from CSV file
def load_tasks():
    if os.path.exists(TASKS_FILE) and os.path.getsize(TASKS_FILE) > 0:
        return pd.read_csv(TASKS_FILE)
    else:
        return pd.DataFrame(columns=['Task', 'Due Date', 'Priority', 'Completed', 'Subtasks', 'Comments', 'Recurrence'])

# Save tasks to CSV file
def save_tasks(tasks):
    tasks.to_csv(TASKS_FILE, index=False)

# Function to add a task
def add_task(task, due_date, priority, comments):
    global tasks
    new_task = pd.DataFrame([{'Task': task, 'Due Date': due_date, 'Priority': priority, 'Completed': False,
                              'Subtasks': '', 'Comments': comments, 'Recurrence': ''}])
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks(tasks)

# Function to mark a task as completed
def complete_task(index):
    global tasks
    tasks.at[index, 'Completed'] = True
    save_tasks(tasks)

# Function to delete a task
def delete_task(index):
    global tasks
    tasks = tasks.drop(index).reset_index(drop=True)
    save_tasks(tasks)

# Function to clear all tasks
def clear_all_tasks():
    global tasks
    tasks = pd.DataFrame(columns=['Task', 'Due Date', 'Priority', 'Completed', 'Subtasks', 'Comments', 'Recurrence'])
    save_tasks(tasks)

# App Layout
def main():
    navigation_page()

def navigation_page():
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Choose an action",
                              ["Add Task", "View Tasks", "Search and Filter Tasks", "Analytics", "Clear All Tasks"])

    if option == "Add Task":
        add_task_page()
    elif option == "View Tasks":
        view_tasks_page()
    elif option == "Search and Filter Tasks":
        search_filter_page()
    elif option == "Analytics":
        analytics_page()
    elif option == "Clear All Tasks":
        clear_all_tasks_page()

def add_task_page():
    st.title("Add New Task")

    with st.form(key='task_form'):
        task = st.text_input("Task")
        due_date = st.date_input("Due Date", datetime.date.today())
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        comments = st.text_area("Comments")
        submit_button = st.form_submit_button(label='Add Task')

        if submit_button and task:
            add_task(task, due_date, priority, comments)
            st.success("Task added successfully!")

def view_tasks_page():
    st.title("Your Tasks")

    if not tasks.empty:
        for i, (index, row) in enumerate(tasks.iterrows(), 1):
            task_str = f"**Task {i}:** {row['Task']} (Due: {row['Due Date']}, Priority: {row['Priority']})"
            if row['Completed']:
                st.markdown(f"~~{task_str}~~")  # Strikethrough for completed tasks
            else:
                st.write(task_str)

                # Add buttons for completing and deleting the task
                col1, col2 = st.columns(2)

                with col1:
                    if st.button(f"Complete Task {i}", key=f"complete_{index}"):
                        complete_task(index)
                        st.success("Task marked as completed!")

                with col2:
                    if st.button(f"Delete Task {i}", key=f"delete_{index}"):
                        delete_task(index)
                        st.success("Task deleted!")

    else:
        st.write("No tasks available.")

def search_filter_page():
    st.title("Search and Filter Tasks")

    search_term = st.text_input("Search Task")
    if search_term:
        filtered_tasks = tasks[tasks['Task'].str.contains(search_term, case=False)]
        if not filtered_tasks.empty:
            st.write(filtered_tasks)
        else:
            st.write("No tasks found.")

    filter_option = st.selectbox("Filter by Completion", ["All", "Completed", "Pending"])
    if filter_option == "Completed":
        filtered_tasks = tasks[tasks['Completed'] == True]
    elif filter_option == "Pending":
        filtered_tasks = tasks[tasks['Completed'] == False]
    else:
        filtered_tasks = tasks

    if not filtered_tasks.empty:
        st.write(filtered_tasks)

def analytics_page():
    st.title("Task Analytics")
    completed_count = tasks['Completed'].sum()
    total_count = len(tasks)

    st.write(f"Total Tasks: {total_count}")
    st.write(f"Completed Tasks: {completed_count}")
    st.write(f"Pending Tasks: {total_count - completed_count}")

def clear_all_tasks_page():
    st.title("Clear All Tasks")
    if st.button("Clear All Tasks"):
        clear_all_tasks()
        st.success("All tasks cleared!")

# Load tasks initially
tasks = load_tasks()

if __name__ == "__main__":
    main()
