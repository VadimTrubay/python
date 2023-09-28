import json

with open('data.json') as f:
    p = json.load(f)
    print(p)