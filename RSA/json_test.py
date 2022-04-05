import json

with open('test.json', 'w') as f:
    f.write(json.dumps({'1': 1}))

with open('test.json', 'r') as f:
    f = json.load(f)

