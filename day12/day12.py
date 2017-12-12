import sys
import re


pattern = re.compile(r"(^\d+) <-> (.*)\n$")

adjacency_list = {}

for line in sys.stdin:
    x, y = pattern.match(line).groups()
    adjacency_list[x] = set(y.split(", "))

groups = set()
for p in adjacency_list:
    found = set()
    stack = [p]
    while stack:
        x = stack.pop()
        found.add(x)
        stack.extend(adjacency_list[x] - found)
    groups.add(frozenset(found))
print(len(next(x for x in groups if "0" in x)))
print(len(groups))

