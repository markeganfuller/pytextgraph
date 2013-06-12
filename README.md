TextGraph
=========

Library for generating text graphs.

Based on code by Rory McCann https://github.com/rory

Install
```
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

Versions
--------
* 0.2 - Improved Docstrings
* 0.1 - Initial Release
