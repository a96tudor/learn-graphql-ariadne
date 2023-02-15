from ariadne import convert_kwargs_to_snake_case

from .models import Todo


def resolve_todos(obj, info):
    try:
        todos = [todo.to_dict() for todo in Todo.query.all()]
        payload = {
            'success': True,
            'todos': todos
        }
    except Exception as err:
        payload = {
            'success': False,
            'errors': [str(err)]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_todo(obj, info, todo_id):
    try:
        todo = Todo.query.get(todo_id)
        payload = {
            'success': True,
            'todo': todo.to_dict()
        }
    except Exception as err:
        payload = {
            'success': False,
            'errors': [err]
        }
    return payload
