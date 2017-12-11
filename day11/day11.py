import sys
from itertools import accumulate

dir_map = {
    "nw": 1,
    "n": 1j,
    "ne": -1+ 1j,
    "se": -1,
    "s":  -1j,
    "sw": 1 -1j,
}

def key(x):
    return max(abs(int(x.imag)), abs(int(x.real)))

directions = sys.stdin.readline().strip().split(",")
distances = list(accumulate(map(dir_map.get, directions)))

print(key(distances[-1]))
print(max(map(key, distances)))
