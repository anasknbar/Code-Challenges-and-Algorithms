from challenge01 import GraphList

#try:
graph = GraphList()
graph.add_vertex('A')
graph.add_vertex('C')
graph.add_vertex('E')
graph.add_vertex('B')
graph.add_vertex('F')
graph.add_vertex('G')
graph.add_vertex('D')
graph.add_vertex('I')
graph.add_vertex('H')

graph.add_vertex('K')


edges = [
    ('A', 'C'),
    ('A', 'E'),
    ('A', 'B'),
    ('C', 'F'),
    ('G', 'E'),
    ('F', 'I'),
    ('H', 'K'),
    ('F', 'H'),
    ('B', 'D'),
    ('E', 'F'),
    ('D', 'E'),
    ('H', 'G'),
    ('I', 'K')
]

for sv, ev in edges:
    graph.add_edge(sv, ev)
    
print(graph)

print(graph.bfs('A'))