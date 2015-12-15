import re


def get_output(input):
    output = ""
    for i in re.finditer(r'(\d)\1*', input):
        output += "%s%s" % (len(i.group()), i.group()[0])
    return output

x = get_output("1113122113")

for i in range(39):
    x = get_output(x)

print len(x)

for i in range(10):
    x = get_output(x)

print len(x)
