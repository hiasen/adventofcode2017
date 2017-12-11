import sys
from collections import Counter

c = Counter(sys.stdin.readline().strip().split(","))
n = c["n"] - c["s"]
ne = c["ne"] - c["sw"]
nw = c["nw"] - c["se"]
print(max(abs(nw+n), abs(n+ne)))

