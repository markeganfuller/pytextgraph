PyTextGraph
===========

Simple text graphs, originally just UTF-8 Spark Graph by @rory.


Example Usage:

```python
import textgraphs

example = [12, 34, 45, 5, 16, 20]
print "Vertical Spark"
print vertical_spark(example)
print "Horizontal Spark"
print horizontal_graph(example)
print "Horizontal Spark, Width 20"
print horizontal_graph(example, 20)
```

Output:

```bash
$ python textgraph.py 
Vertical Spark
▂▆▉▁▃▄
Horizontal Spark
▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉
▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉
▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉
▉▉▉▉▉▉▉▉▉
▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉
▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉

Horizontal Spark, Width 20
▉▉▉▉▉
▉▉▉▉▉▉▉▉▉▉▉▉▉▉
▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉
▉▉
▉▉▉▉▉▉▉
▉▉▉▉▉▉▉▉
```
