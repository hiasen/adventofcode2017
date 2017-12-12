import sys
import re


def main():
    adjacency_list = parse_adjacency_list()
    print(len(do_search("0", adjacency_list)))
    print(len(get_groups(adjacency_list)))


def parse_adjacency_list():
    pattern = re.compile(r"(^\d+) <-> (.*)\n$")
    return {
        x: set(y.split(", "))
        for x, y in (
            pattern.match(line).groups() 
            for line in sys.stdin
        )
    }


def do_search(p, adjacency_list):
    found = set()
    stack = [p]
    while stack:
        x = stack.pop()
        found.add(x)
        stack.extend(adjacency_list[x] - found)
    return frozenset(found)


def get_groups(adjacency_list):
    groups = set()
    not_found = set(adjacency_list)
    while not_found:
        found = do_search(not_found.pop(), adjacency_list)
        groups.add(found)
        not_found -= found
    return groups


if __name__ == "__main__":
    main()
