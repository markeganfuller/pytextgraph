# coding: UTF-8
"""
Python Text Graphing

Creates text based graphs from integer lists.

Example:
    data = [1,2,3]
    print textgraph.spark(data)
    ▂▆█

Graph Types

-Spark
    ▂▆█

-Horizontal
    █████████
    ███████████████████████

-Vertical
     ▉
     ▉
    ▉▉
    ▉▉
    ▉▉
    ▉▉
    ▉▉ ▉▉
"""

from .graphs import spark, horizontal_graph, vertical_graph
