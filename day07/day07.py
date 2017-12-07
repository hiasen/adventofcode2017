import sys
import re


pattern = re.compile("^(?P<name>.*) \((?P<weight>\d*)\)( -> (?P<programs>.*))?\n$")


programs = {}

for line in sys.stdin.readlines():
    m = pattern.match(line)
    name = m.group("name")
    weight = int(m.group("weight"))
    sub_towers = m.group("programs").split(", ") if m.group("programs") else []
    programs[name] = (weight, sub_towers)

root = (set(programs) - set(x for (_, s) in programs.values() for x in s)).pop()
print(root)


def make_tree(root):
    weight, ps = programs[root]
    return Tree(weight, [make_tree(name)  for name in ps])


class Tree(object):
    def __init__(self, weight, children):
        self.weight = weight
        self.children = children
        self.child_weight = sum(x.total_weight() for x in children)

    def total_weight(self):
        return self.weight + self.child_weight

    def get_correct_child_weight(self):
        if not self.children:
            raise ValueError("No children")
        x = self.children[0].total_weight()
        y = self.children[1].total_weight()
        if  x == y: 
            return x 
        if x == self.children[2].total_weight():
            return x
        else:
            return y

    def get_unbalanced_child(self):
        children = self.children
        correct_weight = self.get_correct_child_weight()

        for child in children:
            if child.total_weight() != correct_weight:
                return child


p1 = make_tree(root)


while True:
    n = p1.get_unbalanced_child()
    if not n:
        break
    p1, p2 = n, p1

print(p2.get_correct_child_weight() - p1.child_weight)



