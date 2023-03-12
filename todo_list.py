from tabulate import tabulate

table_header = ["ID", "Name", "Status"]


class Todo:
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status


class TodosTable:
    def __init__(self):
        self.todos = []

    def find_todo(self, id):
        for index, todo in enumerate(self.todos):
            if id == todo.id:
                return {"todo": todo, "index": index}
        return None

    def add_todo(self, title, status):
        id = 0
        if len(self.todos) > 0:
            id = self.todos[-1].id + 1
        self.todos.append(Todo(id, title, status or False))

    def read_todo(self):
        print(
            tabulate(
                map(lambda todo: [todo.id, todo.title, todo.status], self.todos),
                table_header,
                rowalign="center",
                tablefmt="fancy_grid",
            )
        )

    def update_todo(self, id, target, new_val):
        found = self.find_todo(id)
        if found is None:
            return

        if target == "title":
            found["todo"].title = new_val
        elif target == "status":
            found["todo"].status = new_val

    def delete_todo(self, index):
        del self.todos[index]


my_todo_table = TodosTable()

while True:
    print(
        """----------------------
Input your Action Choice:
[a]: Add a todo
[r]: Read todo list
[u]: Update a todo
[d]: Delete a todo
[0]: Exit"""
    )
    match (input()):
        case "a":
            print("----------------------\n")
            title = input("Input the title of todo to add: ")
            my_todo_table.add_todo(title=title, status=False)
            print("Add Todo Success.")

        case "r":
            my_todo_table.read_todo()

        case "u":
            print("----------------------\n")
            id = int(input("The ID of todo to update? "))
            found = my_todo_table.find_todo(id)
            if found is None:
                print('[Error]: Todo with id "{}" no found.'.format(id))
                continue

            target = input("What to update (title/status)? ")
            if target != "title" and target != "status":
                print('[Error]: Unknown target "{}"'.format(target))
                continue

            new_val = input("New Value of {}? ".format(target))
            my_todo_table.update_todo(id, target, new_val)
            print("Update Todo Success.")

            my_todo_table.read_todo()

        case "d":
            print("----------------------\n")
            id = int(input("The ID of todo to delete? "))
            found = my_todo_table.find_todo(id)
            if found is None:
                print('[Error]: Todo with id "{}" no found.'.format(id))
                continue
            my_todo_table.delete_todo(found["index"])
            print("Delete Todo Success.")

        case "0":
            print("----------------------\nExit.")
            break

        case _:
            print("Invalid Option")
    # break
