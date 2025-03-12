FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r', encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(values, filepath=FILEPATH):
    with open(filepath, "w", encoding="utf-8") as file_local:
        file_local.writelines(values)