from datetime import datetime
from config import db, ma


class Guard(db.Model):
    __tablename__ = 'guard'
    hash_id = db.Column(db.String(120), primary_key=True, autoincrement=False)
    username = db.Column(db.String(40))
    fullname = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    relationship_to_todos = db.relationship('Todos', lazy=True)

class Todos(db.Model):
    __tablename__ = 'todos'
    task_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    completed = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    person_hash = db.Column(db.Integer, db.ForeignKey('guard.hash_id'), nullable=False)

class GuardSchema(ma.ModelSchema):
    class Meta:
        fields = ("hash_id", "username", "fullname")
        model = Guard
        sqla_session = db.session

class TodosSchema(ma.ModelSchema):
    class Meta:
        model = Todos
        sqla_session = db.session