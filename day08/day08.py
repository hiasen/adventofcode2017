import sys
import re
import operator
from collections import defaultdict

pattern = re.compile("^([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) (>=|<=|<|>|==|!=) (-?\d+)\n$")


ops = {
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}


def condition(name, op_symbol, operand):
    op = ops[op_symbol]
    return op(registers[name], int(operand))


registers = defaultdict(int)
maximum = -100000000000000000000


for line in sys.stdin:
    name, op, operand, *condition_args = pattern.match(line).groups()

    if condition(*condition_args):
        increment = int(operand)
        if op == "dec":
            increment *= -1
        registers[name] += increment
        maximum = max(registers[name], maximum)

print(max(registers.values()))
print(maximum)

