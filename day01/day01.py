#!/usr/bin/env python3
import sys


def filter_equal(it1, it2):
    yield from (x for x, y in zip(it1, it2) if x == y)


def sum_of_equal(it1, it2):
    return sum(map(int, filter_equal(it1, it2)))


def compute(s):
    half = len(s)//2
    assert 2 * half == len(s), "Sequence should be of even length"

    return (
        sum_of_equal(s, s[1:] + s[:1]),
        sum_of_equal(s[half:], s[:half]) * 2
    )


for s in sys.stdin:
    try:
        print(compute(s.strip()))
    except AssertionError as e:
        print(e, file=sys.stderr)

