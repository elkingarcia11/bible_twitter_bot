import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

from biblejson import verses

# Data is array [string verse]
def add_multiple(data):
    for d in data:
        db.collection('verses').add({"text":d})

# Document is string verse
def insert_into_db(document):
    db.collection('verses').add({"text":document})

# Delete document by string verse
def delete_from_db(text):
    # Note: Use of CollectionRef stream() is prefered to get()
    docs = db.collection('verses').where(filter=FieldFilter('text', '==', text)).stream()
    for doc in docs:
        db.collection('verses').document(doc.id).delete()

# Use a service account.
cred = credentials.Certificate('keys/bible-twitter-bot-firebase-adminsdk-1mnqr-3ea928f05d.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

delete_from_db('testing')
'''
for i in verses:
    insert_into_db(i["text"])

delete_from_db('python insert example')
delete_from_db('verse text')
'''