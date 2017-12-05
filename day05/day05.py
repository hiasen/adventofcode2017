import sys


l = [int(line.strip()) for line in sys.stdin]

def f1(offset):
    return offset + 1

def f2(offset):
    if offset >= 3:
        return offset - 1
    else:
        return offset + 1

def do(l, f):
    l = l[:]
    i = 0
    c = 0
    while i < len(l):
        offset = l[i]
        l[i] = f(offset) 
        i += offset
        c += 1
    return c

print(do(l, f1))
print(do(l, f2))
        
