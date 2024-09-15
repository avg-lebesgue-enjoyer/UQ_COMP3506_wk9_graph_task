"""
File:
  test_top_sort.py

Author:
  Gabriel Field (uqgfiel1)

Test harness!
NOTE: Run this test harness with `python test_top_sort.py` in the terminal.
"""

## SECTION: Imports

from __future__ import annotations
from typing import Dict, List, Set

from graph import *
from top_sort import top_sort



## TEST: Answer verifier

# IGNORE ME:
def verify(graph : Graph, candidate_topological_ordering : Dict[Vertex, int]) -> bool:
  """
  Does what the parameter list suggests.

  Args:
    (graph : Graph):
      yep, one of them
    (candidate_topological_ordering : Dict[Vertex, int]):
      A mapping from vertices of the graph to integers
  
  Returns:
    (bool): `True` iff 
              for all `u` in `graph`,
                `candidate_topological_ordering[u] is not None`
              and for all `u`, `v` in `graph` with `u != v`,
                `candidate_topological_ordering[u] != candidate_topological_ordering[v]`
              and for all `u --> v` in `graph`, 
                `candidate_topological_ordering[u] <  candidate_topological_ordering[v]`
  """
  print("\t<?> Checking candidate topological ordering...")
  print("\t\t<?> Checking that all vertices are assigned some value in candidate_topological_ordering...")
  for vertex in graph.get_vertices():
    if candidate_topological_ordering.get(vertex) is None:
      print(f"\t\t\t<!> Vertex {vertex} with data {vertex.get_data()} was not assigned any value :(")
      return False
  print("\t\t<?> Checking that no vertices are assigned duplicate values in candidate_topological_ordering...")
  values_used : Dict[int, Vertex] = dict() # value |--> first vertex seen using it
  for vertex in graph.get_vertices():
    value = candidate_topological_ordering.get(vertex)
    if value in values_used.keys():
      print(f"\t\t\t<!> The vertices")
      print(f"\t\t\t<!>\t{vertex} with data {vertex.get_data()}")
      print(f"\t\t\t<!>\t{values_used.get(value)} with data {values_used.get(value).get_data()}")
      print(f"\t\t\t<!> were assigned the same value {value} in the candidate topological ordering :(")
      return False
    values_used[value] = vertex
  print("\t\t<?> Checking that the candidate ordering has the topological ordering property...")
  for source in graph.get_vertices():
    for target in graph.get_adjacents(source):
      if not (candidate_topological_ordering.get(source) < candidate_topological_ordering.get(target)):
        print(f"\t\t\t<!> The given graph has an edge s --> t where:")
        print(f"\t\t\t<!>\t s = {source} with data {source.get_data()}")
        print(f"\t\t\t<!>\t t = {target} with data {target.get_data()}")
        print(f"\t\t\t<!> but `candidate_topological_ordering.get(s)` was not less than `candidate_topological_ordering.get(t)` :(")
        return False
  print("\t<?> lgtm :)")
  return True


## TEST: Test data

# IGNORE ME:
class TestData:
  def __init__(self):
    self.vertices_0 = []
    self.matrix_0 = []
    self.vertices_1 = [10]
    self.matrix_1 = [[False]]
    self.vertices_2 = [10, 20]
    self.matrix_2 = [
      [False, True ], 
      [False, False]
    ]
    self.vertices_3 = [10, 20, 30]
    self.matrix_3 = [
      [False, True , True ],
      [False, False, False],
      [False, False, False]
    ]
    self.vertices_4 = [10, 20]
    self.matrix_4 = [
      [False, False],
      [False, False]
    ]
    self.vertices_5 = [10, 20, 30]
    self.matrix_5 = [
      [False, False, True ],
      [False, False, True ],
      [False, False, False]
    ]
    self.verticess = [self.vertices_0, self.vertices_1, self.vertices_2, self.vertices_3, self.vertices_4, self.vertices_5]
    self.matrices =  [self.matrix_0,   self.matrix_1,   self.matrix_2,   self.matrix_3,   self.matrix_4,   self.matrix_5  ]



## TEST: Test harness

def run_tests():
  test_data = TestData()
  for i in range(len(test_data.verticess)):
    gamer = Graph.make_from(test_data.verticess[i], test_data.matrices[i]) 
    test_graph(
      i,
      gamer,
      gamer
    )
  print("<?> ALL TESTS PASSED :)")
  return

def test_graph(test_number : int, overlord_graph : Graph, sacrificial_graph : Graph) -> bool:
  """
  Test with a given graph.
  Ensure that `overlord_graph` and `sacrificial_graph` are DISTINCT REFERENCES, but EQUAL UNDERLYING GRAPHS
  (whose vertex references match).
  """
  print(f"<?> Testing graph number {test_number}...")
  candidate_topological_ordering = top_sort(sacrificial_graph)
  if not verify(overlord_graph, candidate_topological_ordering):
    fail_out()

def fail_out():
  """
  Print debug info and immediately halt execution.
  """
  print("<!> FAILED.")
  print("<!> you get no more debug info, sorry; I only get paid so many hours in the week")
  assert False



## LAUNCH:

if __name__ == "__main__":
  run_tests()
