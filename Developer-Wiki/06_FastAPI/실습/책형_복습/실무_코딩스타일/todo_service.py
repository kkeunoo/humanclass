todos = [{'id': 1, 'item': '공부'}]

def find_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return None

def rename_todo(todo_id, item):
    todo = find_todo(todo_id)
    if todo is None:
        return False
    todo['item'] = item
    return True
