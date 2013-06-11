'''
Example Usages of textgraph
'''
EXAMPLE_DATA = [12, 34, 45, 5, 16, 20]
EXAMPLE_LABELS = ['T', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6']
EXAMPLE_WIDTH = 20
EXAMPLE_HEIGHT = 30

# Spark Graph
from textgraph.graphs import spark
print "Spark"
print spark(EXAMPLE_DATA)

# Horizontal Graph
from textgraph.graphs import horizontal_graph
print "Horizontal Graph"
print horizontal_graph(EXAMPLE_DATA)
print "Horizontal Graph with Labels, Width %i" % EXAMPLE_WIDTH
print horizontal_graph(EXAMPLE_DATA, EXAMPLE_LABELS, width=EXAMPLE_WIDTH)

# Vertical Graph
from textgraph.graphs import vertical_graph
print "Vertical Graph"
print vertical_graph(EXAMPLE_DATA)
print "Vertical Graph, Height %i" % EXAMPLE_HEIGHT
print vertical_graph(EXAMPLE_DATA, EXAMPLE_HEIGHT)
