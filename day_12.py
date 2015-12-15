import json

with open('day_12.txt', 'r') as f:
    input = json.loads(f.read())

def flatten(prev, cur):
    if isinstance(cur, list):
        prev.extend(cur)
    elif isinstance(cur, dict):
        prev.extend(cur.values())
    elif isinstance(cur, int):
        prev.append(cur)
    return prev

def flatten_no_red(prev, cur):
    if isinstance(cur, list):
        prev.extend(cur)
    elif isinstance(cur, dict):
        if "red" in cur.keys() + cur.values():
            pass
        else:
            prev.extend(cur.values())
    elif isinstance(cur, int):
        prev.append(cur)
    return prev


start = reduce(flatten, input, [])

while not all(isinstance(i, int) for i in start):
    start = reduce(flatten, start, [])

print sum(start)

start = reduce(flatten_no_red, input, [])

while not all(isinstance(i, int) for i in start):
    start = reduce(flatten_no_red, start, [])

print sum(start)


