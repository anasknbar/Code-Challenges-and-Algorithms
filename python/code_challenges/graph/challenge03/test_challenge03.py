# Write your test here

from challenge03 import Graph


def test_strongly_connected_Graph():
  
  graph = Graph()
  for i in range(1, 8):
      graph.add_vertex(i)
  edges1 = [[1, 2],[2, 3],[3, 4],[4, 5],[5, 6],[6, 4],[1, 7],[7, 3]]
  for sv, ev in edges1:
      graph.add_edge(sv, ev)
  
  assert graph.is_strongly_connected() == 'Not strongly connected'
 
 
def test_weakly_connected_Graph():
  
  graph = Graph()
  for i in range(5):
      graph.add_vertex(i)
  edges2 =  [[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]]
  for sv, ev in edges2:
      graph.add_edge(sv, ev)
  assert graph.is_strongly_connected() == 'Strongly connected'