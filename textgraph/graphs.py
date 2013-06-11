# coding: utf-8
'''
Graphs
'''


def spark(nums):
    '''
    Returns a vertical spark graph from
    the list of integers num
    '''
    parts = u' ▁▂▃▄▅▆▇█'
    fraction = max(nums) / float(len(parts) - 1)
    # Replace each number with its appropriate part then join
    return ''.join(parts[int(round(x / fraction))] for x in nums)


def horizontal_graph(nums, labels=False, width=79):
    '''
    Returns a horizontal graph from
    the list of integers num of width width
    '''
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

    else:
        return ''.join(parts[int(round(x / fraction))] + "\n" for x in nums)


def vertical_graph(nums, height=10):
    '''
    Returns a vertical graph from
    the list of intergers nums of height height
    '''
    character = '▉'
    fraction = max(nums) / float(height)
    nums = [int(round(n / fraction)) for n in nums]

    out = ""
    row_numbers = range(1, height + 1)
    row_numbers.reverse()
    for i in row_numbers:
        for n in nums:
            if n >= i:
                out = out + character
            else:
                out = out + ' '
        out = out + "\n"
    return out
