"""
File:
  graph.py

Author:
  Gabriel Field (uqgfiel1)

Adjacency list graph implementation. Only bare-bones functionality, but that's exactly what a graph is.
"""

## SECTION: Imports

from __future__ import annotations
from typing import Dict, List



## SECTION: Graph data classes

class Vertex:
  """A vertex in a graph"""

  _data : int
  """Data stored at this vertex"""

  def __init__(self, data : int):
    """
    Construct a vertex with the given data

    Args:
      (data : int): The data to store at this vertex
    """
    self._data = data
  
  def get_data(self) -> int:
    """Return the data stored at this vertex"""
    return self._data
  
class Graph:
  """A DIRECTED graph with no parallel edges, implemented by an adjacency list"""

  # IGNORE ME:
  _vertices : List[Vertex]
  """The vertices stored in this graph"""
  # IGNORE ME:
  _seen_by : Dict[Vertex, List[Vertex]]
  """
  A map from vertices to a adjacency lists.
  For u, v : Vertex, there is an edge u --> v in this graph iff
  v in self._seen_by(u)
  """

  def __init__(self):
    """Construct a new, empty graph"""
    self._vertices = []
    self._seen_by  = {}
  
  # IGNORE ME:
  @classmethod
  def make_from(cls, vertex_data : List[int], adjacency_matrix : List[List[bool]]) -> Graph:
    """
    Construct a graph from adjacency data.

    Args:
      (vertex_data : List[int]): 
        List of data for the vertices
      (adjacency_matrix : List[List[bool]]): 
        Square matrix of non-negative integers. `adjacency_matrix[i][j]` stores 
        True iff there is an edge v_i --> v_j, where v_i and v_j are the vertices 
        constructed for entries i and j of `vertex_data` respectively.
    
    Returns:
      (Graph): yep, the graph
    """
    return_me = Graph()
    the_vertices = [Vertex(datum) for datum in vertex_data]
    return_me._vertices = the_vertices
    for vertex in the_vertices:
      return_me._seen_by[vertex] = []
    for i in range(len(adjacency_matrix)):
      for j in range(len(adjacency_matrix)):
        if adjacency_matrix[i][j]:
          return_me._seen_by[the_vertices[i]].append(the_vertices[j])
    return return_me

  def get_vertices(self) -> List[Vertex]:
    """
    Get a list of all vertices in this Graph.

    Returns:
      (List[Vertex]): A list of all vertices in this Graph
    """
    return self._vertices
  
  def get_adjacents(self, source : Vertex) -> List[Vertex]:
    """
    Get the list of vertices `target` with an edge `source` --> `target`
    in this graph.

    Args:
      (source : Vertex): Vertex at the "source" end of the edges to consider
    
    Returns:
      (List[Vertex]): A list of all vertices `target` with an edge `source`
                      --> `target` in this graph
    """
    return self._seen_by.get(source)
