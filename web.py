import streamlit as st
from functions import get_todos, write_todos

st.title("My To-do App")

todos = get_todos()
def add_todo():
    new_todo = st.session_state['new']+'\n'
    todos.append(new_todo)
    write_todos(todos)


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='',
              placeholder='Add a new to-do.',
              on_change=add_todo, key='new')