# TextGraph

[![Build Status](https://travis-ci.org/markeganfuller/pytextgraph.svg?branch=master)](https://travis-ci.org/markeganfuller/pytextgraph)

Library for generating text graphs.

Based on code by Rory McCann <https://github.com/rory>

## Install

```bash
pip install textgraph
```

See `examples.py` for usage examples.

Example Output (from `examples.py`):

```bash
$ python examples.py
Spark
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
  ▉
  ▉
 ▉▉
 ▉▉
 ▉▉
 ▉▉
 ▉▉ ▉▉
▉▉▉ ▉▉
▉▉▉ ▉▉
▉▉▉▉▉▉

Vertical Graph, Height 30
  ▉
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
```
