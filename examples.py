#!/usr/bin/env python3
"""Example Usages of textgraph."""

import textgraph

EXAMPLE_DATA = [12, 34, 45, 5, 16, 20]
EXAMPLE_DATA_LABELLED = [
    ('T1', 12),
    ('Test2', 34),
    ('Test3', 45),
    ('Test4', 5),
    ('Test5', 16),
    ('Test6', 20)
]
EXAMPLE_WIDTH = 20
EXAMPLE_HEIGHT = 30


# Spark Graph
print("Spark")
print(textgraph.spark(EXAMPLE_DATA))

# Horizontal Graph
print("Horizontal Graph")
print(textgraph.horizontal(EXAMPLE_DATA))
print("Horizontal Graph with Labels, Width {}".format(EXAMPLE_WIDTH))
print(
    textgraph.horizontal(
        EXAMPLE_DATA_LABELLED,
        width=EXAMPLE_WIDTH
    )
)

# Vertical Graph
print("Vertical Graph")
print(textgraph.vertical(EXAMPLE_DATA))
print("Vertical Graph, Height {}".format(EXAMPLE_HEIGHT))
print(textgraph.vertical(EXAMPLE_DATA, height=EXAMPLE_HEIGHT))
