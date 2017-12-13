import sys
from itertools import count

recording = [
    tuple(map(int, line.split(":")))
    for line in sys.stdin
]

def caught(depth, rang, delay=0):
    return not bool((depth+delay) % ((rang - 1) *2)) 

severity = sum(depth*rang for depth, rang in recording if caught(depth, rang))

for delay in count():
    if not any(caught(depth, rang, delay) for depth, rang in recording):
        break

print(severity)
print(delay)
