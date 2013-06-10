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


if __name__ == "__main__":
    example = [12, 34, 45, 5, 16, 20]
    print "Vertical Spark"
    print vertical_spark(example)
    print "Horizontal Spark"
    print horizontal_graph(example)
    print "Horizontal Spark, Width 20"
    print horizontal_graph(example, 20)
