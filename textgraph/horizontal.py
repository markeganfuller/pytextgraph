# coding: utf-8
"""Pytextgraphs."""

import collections
import textgraph


def horizontal(data, width=textgraph.util.terminal_width(),
               character='█'):
    """
    Return a horizontal graph from a list of integers.

    Either labelled or unlabeled, a specific width can be given.

        data   - list of integers to graph
                 list of tuples of label integer to graph
                 collections OrderedDict of label integer to graph
        width  - width of the largest bar (int)
    """
    parts = [character * i for i in range(0, width)]

    if isinstance(data, list):
        # Check if list of tuples (with label) or just numbers
        if isinstance(data[0], tuple):
            labels = [k for k, v in data]
            nums = [v for k, v in data]
        else:
            labels = None
            nums = data
    elif isinstance(data, collections.OrderedDict):
        labels = [k for k in data.keys()]
        nums = [v for v in data.values()]

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
