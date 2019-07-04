# coding: utf-8
"""Pytextgraphs vertical."""

import math


def vertical(nums, height=10, character='▉'):
    """
    Return a vertical graph from a list of integers.

    Height of the graph can be specified.

    nums   - list of integers to graph
    height - height of largest bar (int)
    """
    fraction = max(nums) / float(height)
    nums = [int(math.ceil(n / fraction)) for n in nums]

    out = ""
    row_numbers = list(range(1, height + 1))
    row_numbers.reverse()
    for i in row_numbers:
        for j in nums:
            if j >= i:
                out = out + character
            else:
                out = out + ' '
        out = out + "\n"
    return out
