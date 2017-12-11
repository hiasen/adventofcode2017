import sys
from itertools import accumulate

direction_strings = ["n", "ne", "se", "s", "sw", "nw"]
dir_map = dict(zip(direction_strings, [1, 1j, -1+1j, -1, -1j, 1-1j]))

def distance(x):
    return max(abs(x.imag), abs(x.real), abs(x.real+x.imag))

directions = sys.stdin.readline().strip().split(",")
positions = list(accumulate(map(dir_map.get, directions)))

print(distance(positions[-1]))
print(max(map(distance, positions)))
