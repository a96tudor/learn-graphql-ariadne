from main import db, app
from datetime import datetime
from api.models import Todo

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        today = datetime.today().date()
        todo = Todo(description="Run a marathon", due_date=today, completed=False)

        db.session.add(todo)
        db.session.commit()
