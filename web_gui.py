import streamlit as st
import functions
import os


if not os.path.exists("todo_list.txt"):
    with open("todo_list.txt", "w") as file:
        pass

todo_list = functions.read_todo("todo_list.txt")


def add_todo():
    todo = st.session_state["add_todo"]
    if todo !="":
        todo_list.append(todo+"\n")
        functions.write("todo_list.txt", todo_list)


def delete_todo():
    index_list =[]

    for index, todo in enumerate(todo_list):
        index_list.append(index)
    for index in reversed(index_list):
        if st.session_state[f"{index}-todo"]:
            todo_list.pop(index)
    functions.write("todo_list.txt", todo_list)


st.title("My todo app")
st.subheader("This is Lucas and Laurine Todo App")

button_add = st.button("Add", on_click=add_todo)
st.columns([1,1])

st.text_input(label="Add_todo", on_change=add_todo, key="add_todo")

for index_todos, todos in enumerate(todo_list):
    st.checkbox(todos, key=f"{index_todos}-todo" )

button_complete = st.button("Delete", on_click=delete_todo)