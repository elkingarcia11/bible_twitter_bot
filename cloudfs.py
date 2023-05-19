import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

# Data is array [string verse]
def add_multiple(data):
    for d in data:
        insert_into_db(d)

# Document is string verse
def insert_into_db(document):
    if type(document) == str:
        db.collection('verses').add({"text":document})

# Delete document by string verse
def delete_from_db(text):
    i = getDocument(text)
    if i != None:
        db.collection('verses').document(i).delete()

def getCollectionLength() -> int:
    c = db.collection('verses').size()
    print(c)

def getDocument(verse) -> str:
    docs = db.collection('verses').where(filter=FieldFilter('text', '==', verse)).stream()
    for doc in docs:
        print(type(doc.id))
        return doc.id
    return None

# Use a service account.
cred = credentials.Certificate('keys/bible-twitter-bot-firebase-adminsdk-1mnqr-3ea928f05d.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

'''

insert_into_db("TESTING")
add_multiple(["2","2",1])
from biblejson import verses

for i in verses:
    insert_into_db(i["text"])
db.collection('verses').document("").delete()
delete_from_db('python delete example')

delete_from_db('TESTING')
'''