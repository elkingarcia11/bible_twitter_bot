import json

# 31103 Verses
data = []

with open("t_kjv.json", "r") as f:
  data = json.load(f)
resultset = data["resultset"]
data = resultset["row"]

def get_random_sentence(random_number):
  if random_number < 31103:
    return data[random_number]["field"][4]
  return None