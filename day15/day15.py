from itertools import islice, starmap

def generator(start, factor, divisor=2147483647):
    value = start
    while True:
        value = (value * factor) % divisor
        yield value


def is_match(a, b):
    return (a & (2**16-1)) == (b & (2**16-1))

a_initial, b_initial = 277, 349
a_factor = 16807
b_factor = 48271

def part1(a, b):
    pairs = zip(generator(a_initial, a_factor), generator(b_initial, b_factor))
    first_40million = islice(pairs, 40*10**6)
    return sum(starmap(is_match, first_40million))

def divides(d):
    def func(x):
        return x % d == 0
    return func


def part2(a, b):
    pairs = zip(
        filter(divides(4), generator(a_initial, a_factor)),
        filter(divides(8), generator(b_initial, b_factor))
    )
    first_5million = islice(pairs, 5*10**6)
    return sum(starmap(is_match, first_5million))

print(part1(a_initial, b_initial))
print(part2(a_initial, b_initial))
