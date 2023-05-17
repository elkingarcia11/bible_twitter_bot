import json
import random

# 5202 Verses
verses = []

# Load verses isaiah from json file
with open("/app/assets/verses.json", "r") as f:
  d = json.load(f)
verses = d["verses"]

print(len(verses))

# Retrieve a random verse from dataset
def get_random_sentence():
  random_verse = random.choice(verses)
  return random_verse["text"]