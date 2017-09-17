import json

file = 'b.out'
with open(file) as f:
    data = f.read().strip().split('\n')
data = [json.loads(d) for d in data]

for d in data:
    print(d)
