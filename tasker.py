from flask import make_response, abort
from config import db
from models import Guard, Todos, GuardSchema, TodosSchema


def auth(hashid):

    person = Guard.query.filter(Guard.hash_id == hashid).one_or_none()

    if person is not None:
        schema = GuardSchema()
        data = schema.dump(person)
        return data

    else:
        abort(
            404,
            "Account not found",
        )

def addaccount(account):
    schema = GuardSchema()
    user_exists = Guard.query.filter(Guard.username == account['username']).one_or_none()

    if user_exists is not None:
        abort( 409 , 'User Already Exists')
    else:
        new_account = Guard(hash_id=account['hashid'], username=account['username'], fullname=account['fullname'])
        db.session.add(new_account)
        db.session.commit()
        data = schema.dump(new_account)
        return data, 201

def read(hashid, status=''):
    if status == 'completed' or status == 'done':
        tasks = Todos.query.filter(Todos.completed == True, Todos.person_hash == hashid).all()
    elif status == 'todo':
        tasks = Todos.query.filter(Todos.completed == False, Todos.person_hash == hashid).all()
    else:
        tasks = Todos.query.filter(Todos.person_hash == hashid).all()
    task_schema = TodosSchema(many=True)
    return task_schema.dump(tasks)

def create(hashid, todo):
    schema = TodosSchema()

    new_task = Todos(task=todo['task'], completed=todo['completed'], person_hash=hashid)

    db.session.add(new_task)
    db.session.commit()

    data = schema.dump(new_task)
    return data, 201


def update(hashid, todo):
    update_task = Todos.query.filter(
        Todos.task_id == todo['task_id']
    ).one_or_none()

    if update_task is None:
        abort( 404, "Task not found" )

    else:
        schema = TodosSchema()

        update_task.task = todo['task']
        update_task.completed = todo['completed']

        db.session.merge(update_task)
        db.session.commit()

        data = schema.dump(update_task)
        return data, 200

def delete(hashid, taskid):

    task = Todos.query.filter(Todos.task_id == taskid).one_or_none()

    if task is not None:
        if task.person_hash != hashid:
            abort ( 401, "Unauthorize Access")
        else:
            db.session.delete(task)
            db.session.commit()
            return make_response(
                "Task Deleted", 200
            )
    else:
        abort( 404, "Task not found",)

