'''
Example Usages of textgraph
'''
EXAMPLE_DATA = [12, 34, 45, 5, 16, 20]
EXAMPLE_LABELS = ['T', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6']
EXAMPLE_WIDTH = 20
EXAMPLE_HEIGHT = 30

import textgraph

# Spark Graph
print "Spark"
print textgraph.spark(EXAMPLE_DATA)

# Horizontal Graph
print "Horizontal Graph"
print textgraph.horizontal_graph(EXAMPLE_DATA)
print "Horizontal Graph with Labels, Width %i" % EXAMPLE_WIDTH
print textgraph.horizontal_graph(EXAMPLE_DATA, labels=EXAMPLE_LABELS,
                                 width=EXAMPLE_WIDTH)

# Vertical Graph
print "Vertical Graph"
print textgraph.vertical_graph(EXAMPLE_DATA)
print "Vertical Graph, Height %i" % EXAMPLE_HEIGHT
print textgraph.vertical_graph(EXAMPLE_DATA, height=EXAMPLE_HEIGHT)
