import json
import random

# 31103 Verses
books = []

# Load verses isaiah from json file
with open("/app/assets/isaiah.json", "r") as f:
  d = json.load(f)
resultset = d["verses"]
books.append(resultset)

# Load verses philip from json file
with open("/app/assets/philip.json", "r") as f:
  d = json.load(f)
resultset = d["verses"]
books.append(resultset)

# Load verses proverbs from json file
with open("/app/assets/proverbs.json", "r") as f:
  d = json.load(f)
resultset = d["verses"]
books.append(resultset)

# Load verses psalms from json file
with open("/app/assets/psalms.json", "r") as f:
  d = json.load(f)
resultset = d["verses"]
books.append(resultset)

# Load verses romans from json file
with open("/app/assets/romans.json", "r") as f:
  d = json.load(f)
resultset = d["verses"]
books.append(resultset)

for book in books:
  print(len(book))
  
# Retrieve a random verse from dataset
def get_random_sentence():
  random_book = random.choice(books)
  random_verse = random.choice(random_book)
  return random_verse["text"]