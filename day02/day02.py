#!/usr/bin/env python3
import sys
from itertools import starmap, combinations


def parse_line(line):
    return [int(x) for x in line.strip().split()]


def range_(sequence):
    return max(sequence) - min(sequence)


def even_test(x, y):
    if x < y:
        x, y = y, x
    d, r = divmod(x, y)
    if not r:
        return d
    return None


def part2(sequence):
    return next(filter(None, starmap(even_test, combinations(sequence, 2))))


table = [parse_line(line) for line in sys.stdin]
print(sum(map(range_, table)))
print(sum(map(part2, table))) 

