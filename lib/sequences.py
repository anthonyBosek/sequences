#!/usr/bin/env python3


def print_fibonacci(length):
    """Prints a list of the Fibonacci sequence up to the given length."""
    if length < 0:
        raise ValueError("Length must be a positive integer.")
    if length == 0:
        print([])
        return []
    if length == 1:
        print([0])
        return [0]
    if length == 2:
        print([0, 1])
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, length):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    print(sequence)
    return sequence
