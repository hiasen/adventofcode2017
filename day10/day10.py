import sys
from functools import reduce
from operator import xor


def repeat_list(l, times):
    for _ in range(times):
        yield from l


def sparse_hash(lengths, rounds=64):
    list_length = 256
    circular_list = bytearray(range(list_length))
    current_position = 0

    for skip_size, length in enumerate(repeat_list(lengths, rounds)):
        end = current_position + length
        if end < list_length:
            circular_list[current_position:end] = reversed(circular_list[current_position:end])
        else:
            end -= list_length
            rev = list(reversed(circular_list[:end])) + list(reversed(circular_list[current_position:])) 
            split = list_length - current_position
            circular_list[current_position:] = rev[:split]
            circular_list[:end] = rev[split:]

        current_position = (current_position + length + skip_size) % list_length
    return circular_list


def knothash(array):
    input = array + bytes([17, 31, 73, 47, 23])
    s = sparse_hash(input)
    return bytearray(
        reduce(xor, s[i:j], 0)
        for i, j in zip(range(0, 256, 16), range(16, 256+16, 16))
    )


if __name__ == "__main__":
    byte_input = sys.stdin.buffer.read().strip()
    lengths = map(int, byte_input.decode().split(","))
    circular_list = sparse_hash(lengths, rounds=1)
    print(circular_list[0]*circular_list[1])
    print(knothash(byte_input).hex())

