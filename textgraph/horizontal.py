# coding: utf-8
"""Pytextgraphs."""

import textgraph


def horizontal(nums, labels=False, width=textgraph.util.terminal_width(),
               character='█'):
    """
    Return a horizontal graph from a list of integers.

    Either labelled or unlabeled, a specific width can be given.

        nums   - list of integers to graph
        labels - list of strings that correspond to the data
        width  - width of the largest bar (int)
    """
    parts = [character * i for i in range(0, width)]
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
