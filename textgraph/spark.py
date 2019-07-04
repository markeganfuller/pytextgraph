# coding: utf-8
"""Pytextgraphs spark graph."""


def spark(nums, characters=' ▁▂▃▄▅▆▇█'):
    """
    Return a vertical spark graph from a list of integers.

        nums - list of integers to graph.
    """
    fraction = max(nums) / float(len(characters) - 1)
    # Replace each number with its appropriate part then join
    return ''.join(characters[int(round(x / fraction))] for x in nums)
