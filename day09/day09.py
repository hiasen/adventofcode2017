import sys

def char_iterator(file):
    c = sys.stdin.read(1)
    while c:
        yield c
        c = sys.stdin.read(1)


negated = False
garbage = False
garbage_characters = 0
current_score = 0
total_score = 0

for c in char_iterator(sys.stdin):
    if negated:
        negated = False
    elif c == "!":
        negated = True
    elif garbage:
        if c == ">":
            garbage = False
        else:
            garbage_characters += 1
    elif c == "<":
        garbage = True
    elif c == "{":
        current_score += 1
        total_score += current_score
    elif c == "}":
        current_score -= 1

print(total_score)
print(garbage_characters)
