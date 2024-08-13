from challenge03 import Graph

# try this
graph1 = Graph()
for i in range(1, 8):
    graph1.add_vertex(i)
edges1 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 4), (1, 7), (7, 3)]
for sv, ev in edges1:
    graph1.add_edge(sv, ev)
print(graph1.is_strongly_connected()) 

graph2 = Graph()
for i in range(5):
    graph2.add_vertex(i)
edges2 = [(1, 2), (1, 0), (0, 4), (4, 3), (3, 2), (3, 1), (2, 1), (2, 4)]
for sv, ev in edges2:
    graph2.add_edge(sv, ev)
print(graph2.is_strongly_connected())  

