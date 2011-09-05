Python implementation of Tarjan's algorithm
===========================================

Tarjan's algorithm takes as input a directed (possibly cyclic!) graph and
returns as output its strongly connected components in a topological order.

Example
-------
![](http://github.com/bwesterb/py-tarjan/raw/master/doc/example.png)
```python
>>> tarjan({1:[2],2:[1,5],3:[4],4:[3,5],5:[6],6:[7],7:[8,9],8:[6],9:[]})
[[9], [8, 7, 6], [5], [2, 1], [4, 3]]
```

Installation
------------
Simply execute

    easy_install tarjan

or from this source distribution, run

    python setup.py install
