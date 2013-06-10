# coding: utf-8
'''
Text Graphs
'''


def vertical_spark(nums):
    '''
    Returns a vertical spark graph from
    the list of integers num
    '''
    parts = u' ▁▂▃▄▅▆▇▉'
    fraction = max(nums) / float(len(parts) - 1)
    return ''.join(parts[int(round(x / fraction))] for x in nums)


def horizontal_graph(nums, width=79):
    '''
    Returns a horizontal graph from
    the list of integers num of width width
    '''
    parts = ['▉' * i for i in range(0, width)]
    fraction = max(nums) / float(len(parts) - 1)
    return ''.join(parts[int(round(x / fraction))] + "\n" for x in nums)


def vertical_graph(nums, height=10):
    '''
    Returns a vertical graph from
    the list of intergers nums of height height
    '''
    character = '▉'
    fraction = max(nums) / float(height)
    nums = [int(round(n / fraction)) for n in nums]
    print nums

    out = ""
    row_numbers = range(height)
    row_numbers.reverse()
    for i in row_numbers:
        for n in nums:
            if n >= i:
                out = out + character
            else:
                out = out + ' '
        out = out + "\n"
    return out

if __name__ == "__main__":
    example = [12, 34, 45, 5, 16, 20]

    print "Vertical Spark"
    print vertical_spark(example)

    print "Horizontal Graph"
    print horizontal_graph(example)
    print "Horizontal Graph, Width 20"
    print horizontal_graph(example, 20)

    print "Vertical Graph"
    print vertical_graph(example)
    print "Vertical Graph, Height 30"
    print vertical_graph(example, 30)
