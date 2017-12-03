#!/usr/bin/env python
import math
import sys

number = int(sys.argv[1])

if number == 1:
    result = 0
else:
    n = int(math.ceil((math.sqrt(number) - 1)/2))
    result = n + abs((number - (2*n-1)**2) % (2*n) - n)

print(result)

