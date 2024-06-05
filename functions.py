def write(file, todo):
    with open(file, "w") as file:
        file.writelines(todo)


def read_todo (file):
    with open(file, "r") as file:
        todo_list = file.readlines()
    return todo_list

if __name__ == "__main__":
    print("Functions program executed")


