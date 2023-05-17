import json
import random

# 31103 Verses
data = []

# Load verses data from json file
with open("t_kjv.json", "r") as f:
  data = json.load(f)
resultset = data["resultset"]
data = resultset["row"]

# Retrieve a random verse from dataset
def get_random_sentence():
  i = random.randint(0, len(data)-1)
  return data[i]["field"][4]