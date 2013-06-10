PyTextGraph
===========

Simple text graphs, originally just UTF-8 Spark Graph by @rory.


Example Usage:

```python
import textgraph

example = [12, 34, 45, 5, 16, 20]
labels = ['T', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6']

print "Vertical Spark"
print vertical_spark(example)

print "Horizontal Graph"
print horizontal_graph(example)
print "Horizontal Graph with Labels, Width 20"
print horizontal_graph(example, labels, width=20)

print "Vertical Graph"
print vertical_graph(example)
print "Vertical Graph, Height 30"
print vertical_graph(example, 30)
```

Output:

```bash
$ python textgraph.py
Vertical Spark
▂▆█▁▃▄
Horizontal Graph
█████████████████████
███████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████
█████████
████████████████████████████
███████████████████████████████████

Horizontal Graph with Labels, Width 20
T     █████
Test2 ██████████████
Test3 ███████████████████
Test4 ██
Test5 ███████
Test6 ████████

Vertical Graph
[3, 8, 10, 1, 4, 4]
  ▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉ ▉▉
▉▉▉ ▉▉
▉▉▉ ▉▉
▉▉▉▉▉▉
▉▉▉▉▉▉

Vertical Graph, Height 30
[8, 23, 30, 3, 11, 13]
  ▉   
  ▉   
  ▉   
  ▉   
  ▉   
  ▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉   
 ▉▉  ▉
 ▉▉  ▉
 ▉▉ ▉▉
 ▉▉ ▉▉
 ▉▉ ▉▉
▉▉▉ ▉▉
▉▉▉ ▉▉
▉▉▉ ▉▉
▉▉▉ ▉▉
▉▉▉ ▉▉
▉▉▉▉▉▉
▉▉▉▉▉▉
▉▉▉▉▉▉
▉▉▉▉▉▉
```
