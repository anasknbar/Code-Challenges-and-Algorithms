# Write here the code challenge solution

class Graph:
    def __init__(self):
        ''' Initializing a graph class '''
        self.adj_list = {}

    def add_vertex(self, vertex):
        ''' Method for adding a vertex to the graph instance class '''
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, sv, ev):
        ''' Method for adding an edge for the graph (Directed Graph) '''
        if sv in self.adj_list.keys() and ev in self.adj_list.keys():
            self.adj_list[sv].append(ev)
        else:
            raise Exception('One or both vertices not found')
    
    
    def _DFS(self, v, visited):
        ''' Utility method to perform DFS '''
        visited[v] = True
        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self._DFS(neighbor, visited)

    def _transpose(self):
        ''' Method to return the transpose of the graph '''
        transposed_graph = Graph()
        for vertex in self.adj_list:
            transposed_graph.add_vertex(vertex)
        for vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                transposed_graph.add_edge(neighbor, vertex)
        return transposed_graph

    def is_strongly_connected(self):
        ''' Method to check if the graph is strongly connected '''
        visited = {v: False for v in self.adj_list}

        # Step 1: Do DFS from any vertex
        start_vertex = next(iter(self.adj_list))  # Get an arbitrary starting vertex
        self._DFS(start_vertex, visited)

        # If DFS traversal doesn’t visit all vertices, the graph isn’t strongly connected
        if any(not visited[v] for v in visited):
            return "Not strongly connected"

        # Step 2: Get the transposed graph
        transposed_graph = self._transpose()

        # Step 3: Do DFS on the transposed graph
        visited = {v: False for v in transposed_graph.adj_list}
        transposed_graph._DFS(start_vertex, visited)

        # If DFS on the transposed graph doesn’t visit all vertices, the graph isn’t strongly connected
        if any(not visited[v] for v in visited):
            return "Not strongly connected"

        return "Strongly connected"

    def __str__(self):
        ''' Method to display the adjacency list '''
        display = '\n'
        for key, value in self.adj_list.items():
            display += f"{key}: {value}\n"
        return display



