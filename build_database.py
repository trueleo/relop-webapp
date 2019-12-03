import os
from config import db
from models import Guard, Todos


# Data to initialize database with
PEOPLE = [
    {'hash_id': '6b21cf3f2043a0c0c7e2b02c792fe18e', 'username': 'rick', 'fullname': 'Rick And Morty'}
]

TASK = [
    {'task': 'Prepare for the workshop', 'completed': False, 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
        {'task': 'Determine date', 'completed': False, 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
        {'task': 'Determine facilitator team and delegate tasks (lead and co-facilitators) ', 'completed': False , 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
        {'task': 'Identify workshop goals ', 'completed': False , 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
        {'task': 'Determine snacks/lunch', 'completed': False , 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
        {'task': 'Look into a guest speaker', 'completed': False , 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
        {'task': 'Note limitations (time, space, money, etc.)', 'completed': False , 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
        {'task': 'Determine methods of promotion (flyer, in-service, etc.)', 'completed': False , 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
        {'task': 'Determine price of workshop (Are you offering food, do you need to pay a facility fee or other fees on top of the 1/$25 or 2/$45 fee)', 'completed': False , 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
        {'task': 'Determine location (note limitations)', 'completed': False , 'person_hash': '6b21cf3f2043a0c0c7e2b02c792fe18e'},
]

# Delete database file if it exists currently
if os.path.exists('taskerdb.db'):
    os.remove('taskerdb.db')


# Create the database
db.create_all()

# Add new data to the database
for person in PEOPLE:
    p = Guard(hash_id=person['hash_id'], username=person['username'], fullname=person['fullname'])
    db.session.add(p)

for t in TASK:
    p = Todos(task=t['task'], completed=t['completed'], person_hash=t['person_hash'])
    db.session.add(p)

db.session.commit()
