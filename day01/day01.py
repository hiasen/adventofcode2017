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


def halfway_around_pairs(sequence):
    n = len(sequence)
    half = n//2
    assert 2*half == n, "Sequence should be of even length"
    for x, y in zip(sequence[:half], sequence[half:]):
        if x == y:
            yield x
    



print(sum(map(int, filter_previous(chain(iter(s), s[0])))))
print(sum(map(int, halfway_around_pairs(s)))*2)
