# coding: utf-8
"""Pytextgraphs spark graph."""

BRAILE_2VALUE = [
    ["⠀", "⢀", "⢠", "⢰", "⢸"],
    ["⡀", "⣀", "⣠", "⣰", "⣸"],
    ["⡄", "⣄", "⣤", "⣴", "⣼"],
    ["⡆", "⣆", "⣦", "⣶", "⣾"],
    ["⡇", "⣇", "⣧", "⣷", "⣿"],
]


def spark(nums, characters=' ▁▂▃▄▅▆▇█'):
    """
    Return a vertical spark graph from a list of integers.

    This is provided for backwards compatability and is a wrapper for
    spark_char_per_value.
    """
    return spark_char_per_value(nums, characters)


def spark_char_per_value(nums, characters=' ▁▂▃▄▅▆▇█'):
    """
    Return a vertical spark graph with one character per value from a list of
    integers.

        nums       - list of integers to graph.
        characters - list of characters to use.
    """
    fraction = max(nums) / float(len(characters) - 1)
    # Replace each number with its appropriate part then join
    return ''.join(characters[int(round(x / fraction))] for x in nums)


def _pairwise(iterable):
    """
    Turn an iterable into a pairs.

    Based off <https://stackoverflow.com/a/5389547>
    """
    i = iter(iterable)
    pairs = list(zip(i, i))
    if len(iterable) % 2 != 0:
        # We have an odd list so need to add the last element
        pairs.append((iterable[-1], 0))

    return pairs


def spark_char_per_2_values(nums, characters=None):
    """
    Return a vertical spark graph with one character per two values.

        nums       - list of integers to graph.
        characters - 2d list of characters to use, see BRAILE_2VALUE constant
                     for an example.
    """
    if characters is None:
        characters = BRAILE_2VALUE

    fraction = max(nums) / float(len(characters) - 1)

    output = []
    for pair in _pairwise(nums):
        num_1 = int(round(pair[0] / fraction))
        num_2 = int(round(pair[1] / fraction))
        output += characters[num_1][num_2]
    return ''.join(output)
