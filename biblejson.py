import json
import random

# Load verses verses from json file
with open("/app/assets/verses.json", "r") as f:
  data = json.load(f)

# 5202 Verses
verses = data["verses"]

# Retrieve a random verse from dataset
def get_random_sentence():
  random_verse = random.choice(verses)
  return random_verse["text"]