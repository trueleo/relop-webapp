import os
from config import db
from models import Guard, Todos


# Data to initialize database with
PEOPLE = [
    {'hash_id': '2D6G4F', 'username': 'trueleo@pm.me'},
    {'hash_id': '3G6G4F', 'username': 'rick@pm.me'}
]

TASK = [
    {'task': 'Buy 2 Eggs', 'completed': True , 'person_hash': '3G6G4F'}
]


# Delete database file if it exists currently
if os.path.exists('taskerdb.db'):
    os.remove('taskerdb.db')



# Create the database
db.create_all()

# Add new data to the database
for person in PEOPLE:
    p = Guard(hash_id=person['hash_id'], username=person['username'])
    db.session.add(p)

for t in TASK:
    p = Todos(task=t['task'], completed=t['completed'], person_hash=t['person_hash'])
    db.session.add(p)

db.session.commit()
