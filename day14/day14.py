import sys
from day10.day10 import knothash

s = sys.argv[1]

result = sum(sum(sum(map(int, bin(x)[2:])) for x in knothash(f"{s}-{i}".encode()))
for i in range(128))
print(result)
