#!/usr/bin/env python3
import math
import sys
from itertools import count

number = int(sys.argv[1])

if number == 1:
    result = 0
else:
    n = int(math.ceil((math.sqrt(number) - 1)/2))
    result = n + abs((number - (2*n-1)**2) % (2*n) - n)

print(result)



border = [1]*8
while True:
    next_border = [0] * (len(border)+8)

    sl = len(border)//4
    nsl = sl + 2

    border[-1] += border[0]
    border[-2] += border[0]

    for s in range(4):
        for i in range(sl):
            j = i + sl * s
            value = border[j]
            if value >= number:
                print(value)
                exit(0)

            if j+1 < len(border):
                border[j+1] += value

            next_border[i+nsl*s] += value
            next_border[i+nsl*s+1] += value
            next_border[i+nsl*s+2] += value

        if s < 3:
            border[sl*(s+1)] += border[sl*(s+1) - 2]
            next_border[nsl*(s+1)] += border[sl*(s+1) - 1]
            next_border[nsl*(s+1)+1] += border[sl*(s+1) - 1]

    next_border[0] += border[-1]
    next_border[1] += border[-1]


    border = next_border
