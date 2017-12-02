#!/usr/bin/env python3
import sys


def parse_line(line):
    return [int(x) for x in line.strip().split()]


def range_(sequence):
    return max(sequence) - min(sequence)


print(sum(map(range_, map(parse_line, sys.stdin))))

