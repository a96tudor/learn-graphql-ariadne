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
