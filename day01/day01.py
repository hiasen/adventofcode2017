#!/usr/bin/env python3
import sys
from itertools import chain

s = sys.stdin.read().strip() 

def filter_previous(it):
    previous = next(it)
    for x in it:
        if x == previous:
            yield x
        previous = x

print(sum(map(int, filter_previous(chain(iter(s), s[0])))))
