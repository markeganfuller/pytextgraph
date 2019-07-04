#!/usr/bin/env python3
"""Example Usages of textgraph."""

import textgraph

EXAMPLE_DATA = [12, 34, 45, 5, 16, 20]
EXAMPLE_DATA_LABELLED = [
    ('T1', 12),
    ('Test2', 12),
    ('Test3', 12),
    ('Test4', 12),
    ('Test5', 12),
    ('Test6', 12)
]
EXAMPLE_WIDTH = 20
EXAMPLE_HEIGHT = 30


# Spark Graph
print("Spark")
print(textgraph.spark(EXAMPLE_DATA))

# Horizontal Graph
print("Horizontal Graph")
print(textgraph.horizontal(EXAMPLE_DATA))
print(f"Horizontal Graph with Labels, Width {EXAMPLE_WIDTH}")
print(
    textgraph.horizontal(
        EXAMPLE_DATA_LABELLED,
        width=EXAMPLE_WIDTH
    )
)

# Vertical Graph
print("Vertical Graph")
print(textgraph.vertical(EXAMPLE_DATA))
print(f"Vertical Graph, Height {EXAMPLE_HEIGHT}")
print(textgraph.vertical(EXAMPLE_DATA, height=EXAMPLE_HEIGHT))
