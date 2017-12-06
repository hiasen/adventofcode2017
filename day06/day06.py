import sys

l = [int(x) for x in sys.stdin.readline().strip().split()]

visited_at_cycle = {}
configuration = tuple(l)

cycle = 0
while configuration not in visited_at_cycle:
    visited_at_cycle[configuration] = cycle

    value = max(l)
    i = l.index(value)
    l[i] = 0
    for j in range(value):
        l[(i+j+1) % len(l)] += 1

    configuration = tuple(l)
    cycle += 1

print(cycle)
print(cycle - visited_at_cycle[configuration])

