import re

line = "auipc s2,-30"

print(list(filter(lambda x: x, re.split(",| ", line))))

print(re.split(",| ", line))


if re.split(",| ", line) == list(filter(lambda x: x, re.split(",| ", line))):
    print("yes")