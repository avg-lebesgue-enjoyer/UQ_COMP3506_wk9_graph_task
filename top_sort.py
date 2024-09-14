"""
File:
  top_sort.py

Author:
  YOUR CODE HERE! (your name)
  Gabriel Field (uqgfiel1)

Task to implement!
"""

## SECTION: Imports

from __future__ import annotations
from typing import Dict, List, Set

from graph import *



## SECTION: Implement this pls

def top_sort(graph : Graph) -> Dict[Vertex, int]:
  """
  Produce a topological ordering of the given directed acyclic `graph`.

  Args:
    (graph : Graph): yea sort this one
  Requires:
    `graph` has no (directed) cycles
  Returns:
    (it : Dict[Vertex, int]): A topological ordering of `graph`
  Ensures:
    For all vertices `u`, `v` in `graph` with `v` in `graph.get_adjacents(u)`,
    `it[u] < it[v]`
  Ensures:
    `graph`, and all of its fields, are left unmodified from their initial state
  """
  # YOUR CODE HERE!
  print("\t<!> you haven't implemented `top_sort()` mate")
  raise NotImplementedError
