import streamlit as st
import pandas as pd
import os

st.title("✅ TO-DO-LIST")

TASK_FILE = 'tasks.csv'

# Load existing tasks
def load_tasks():
    if os.path.exists(TASK_FILE):
        return pd.read_csv(TASK_FILE).to_dict(orient='records')
    return []

# Save tasks to CSV
def save_tasks(tasks):
    df = pd.DataFrame(tasks)
    df.to_csv(TASK_FILE, index=False)

# Load tasks into session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = load_tasks()

# Input box to add new task
new_task = st.text_input("➕ Add a new task")

if st.button("Add Task"):
    if new_task.strip():
        # Add new task to session state
        st.session_state.tasks.append({"task": new_task.strip(), "completed": False})
        save_tasks(st.session_state.tasks)
        st.experimental_rerun()  # Refresh the app state

# Display tasks
st.subheader("📋 Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        # Add a checkbox for each task
        completed = st.checkbox(task['task'], task['completed'], key=i)
        
        if completed != task['completed']:
            # Update task completion status
            st.session_state.tasks[i]['completed'] = completed
            save_tasks(st.session_state.tasks)
else:
    st.write("No tasks available. Start adding some! 😎")
