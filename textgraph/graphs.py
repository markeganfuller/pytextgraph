# coding: utf-8
"""Pytextgraphs."""

import math


def spark(nums):
    """
    Return a vertical spark graph from a list of integers.

        nums - list of integers to graph.
    """
    parts = ' ▁▂▃▄▅▆▇█'
    fraction = max(nums) / float(len(parts) - 1)
    # Replace each number with its appropriate part then join
    return ''.join(parts[int(round(x / fraction))] for x in nums)


def horizontal_graph(nums, labels=False, width=79):
    """
    Return a horizontal graph from a list of integers.

    Either labelled or unlabeled, a specific width can be given.

        nums   - list of integers to graph
        labels - list of strings that correspond to the data
        width  - width of the largest bar (int)
    """
    parts = ['█' * i for i in range(0, width)]
    fraction = max(nums) / float(len(parts) - 1)

    if labels:
        # First pad labels
        max_length = len(max(labels, key=len))
        labels = [x + " " * (max_length - len(x)) for x in labels]

        # Create Lines and output
        out = ""
        for i in range(len(nums)):
            out = out + labels[i]
            out = out + " " + parts[int(round(nums[i] / fraction))]
            out = out + "\n"
        return out

    return ''.join(parts[int(round(x / fraction))] + "\n" for x in nums)


def vertical_graph(nums, height=10):
    """
    Return a vertical graph from a list of integers.

    Height of the graph can be specified.

    nums   - list of integers to graph
    height - height of largest bar (int)
    """
    character = '▉'
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
