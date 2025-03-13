import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo +'\n')
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""
    print(todo)


st.title("Список фактов")
st.write("*:grey[*Шуня самая красивая девочка у меня!!]*")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "3", placeholder="Введите план", on_change=add_todo, key="new_todo",
              label_visibility = 'collapsed')

col1, col2, col3 = st.columns(3)

st.image("kat_pic.jpg")
