import re

with open('day_8.txt', 'r') as f:
    strings = f.read().splitlines()

total_characters = sum(map(len, strings))
characters_in_memory = sum(map(lambda x: len(eval(x)), strings))

print total_characters - characters_in_memory


# Find the difference if you were to escape the strings
# Add 2 since there's always quotes around it
# Then count how many quotes or slashes there are
count = 0
for x in strings:
    temp = x.strip()
    print x, 2 + temp.count('"') + temp.count('\\')
    count += 2 + temp.count('"') + temp.count('\\')
print count
