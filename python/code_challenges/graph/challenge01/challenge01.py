# Write here the code challenge solution


class GraphList:
    ''' initializing a grapg class '''
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        '''method for adding a vertex to the graph instance class'''
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, sv, ev):
      ''' method for adding an edge for the graph'''
      if sv in self.adj_list.keys() and ev in self.adj_list.keys():
        self.adj_list[sv].append(ev)
        self.adj_list[ev].append(sv)
        
      else:
        raise KeyError('one or both Vertexes Not Found')
        


    def bfs(self,start):
      '''breadth first search algorithm for printing all the vertex in the class'''
      if start not in self.adj_list:
        return
      
      visited = [start]
      queue = [start]
      
      while len(queue):
        s = queue.pop(0)
        
        for i in self.adj_list[s]:
          if i not in visited:
            visited.append(i)
            queue.append(i)
      return(visited)
    def __str__(self):
        display = '\n'
        for key, value in self.adj_list.items():
            display += f"{key}: {value}\n"
        return display
      



