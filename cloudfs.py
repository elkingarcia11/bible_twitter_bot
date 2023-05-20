import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

# Use a service account.
cred = credentials.Certificate('keys/bible-twitter-bot-firebase-adminsdk-1mnqr-3ea928f05d.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
collection = db.collection('verses')

# Data is array [string verse]
def insert_multiple(data):
    for d in data:
        insert_into_db(d)

# Document is string verse
def insert_into_db(document):
    if type(document) == str:
        collection.add({"text":document})

# Delete document by string verse
def delete_from_db(text):
    i = get_document_id(text)
    if i != None:
        collection.document(i).delete()

def get_collection_length() -> int:
    c = collection.size()
    print(c)

def get_document_id(verse) -> str:
    docs = collection.where(filter=FieldFilter('text', '==', verse)).stream()
    for doc in docs:
        return doc.id
    return None

def get_random_document():
    # Generate a random number.
    collOb = collection.count().get()

    # Generate a random number between 0 and 10.
    random_number = random.randint(0, int(collOb[0][0].value) - 1)

    docs = collection.where(filter=FieldFilter('index', '==', random_number)).stream()
    for doc in docs:
        print(doc.get("text"))
    
def update_all_docs():
    counter = 0
    for doc in collection.get():
        doc.reference.set({"index":counter,"text":doc.get("text")})
        print(counter)
        counter += 1

get_random_document()
'''

doc = collection.document("00FpyITgqio5JZAMVxiT")
doc.set({"index":3, "text": doc.get().to_dict()["text"]})


insert_into_db("TESTING")
add_multiple(["2","2",1])
from biblejson import verses

for i in verses:
    insert_into_db(i["text"])
collection.document("").delete()
delete_from_db('python delete example')

delete_from_db('TESTING')
'''