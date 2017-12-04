#!/usr/bin/env python
import sys

part1 = 0
part2 = 0
passphrases = (line.strip().split() for line in sys.stdin)
for words in passphrases:
    part1 += int(len(words) == len(set(words)))
    part2 += int(len(words) == len(set("".join(sorted(word)) for word in words)))

print(part1)
print(part2)
    
