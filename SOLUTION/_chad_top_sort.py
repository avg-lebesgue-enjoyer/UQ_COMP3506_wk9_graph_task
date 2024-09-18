"""
File:
  do.py

Author:
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

  class ImpureMutableInteger:
    """State monad."""
    it : int
    """The integer stored in this sad little box"""
    def __init__(self, it) -> ImpureMutableInteger:
      self.it = it
  
  def dfs_assign_values(
      graph           : Graph, 
      source          : Vertex, 
      seen            : Set[Vertex],
      value           : ImpureMutableInteger, 
      ordering_so_far : Dict[Vertex, int]
  ) -> None:
    """
      Assigns topological ordering values to every vertex downstream of the given `source`.
      Assumes that `source` is yet to be `seen` in the given `graph`.
    """
    seen.add(source)
    for target in graph.get_adjacents(source):
    # invariant: `value.it == len(graph.get_vertices()) - len(seen)`
      if target not in seen:
        dfs_assign_values(graph, target, seen, value, ordering_so_far)
    ordering_so_far[source] = value.it
    value.it = value.it - 1      

  # Setup:
  seen      : Set[Vertex]          = set()                                            # Vertices seen so far
  value     : ImpureMutableInteger = ImpureMutableInteger(len(graph.get_vertices()))  # Value assigned to vertices, counting down
  return_me : Dict[Vertex, int]    = dict()                                           # Mapping to return
  # Topological ordering:
  for vertex in graph.get_vertices():
    if vertex not in seen:
      dfs_assign_values(graph, vertex, seen, value, return_me)
  # Done.
  return return_me
