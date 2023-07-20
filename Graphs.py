# Each node in a graph is called a vertex. Plural will be vertices. Between the vertices we have a connection and it's called an Edge. 
# A vertex can have multiple edges. For example one node can connect to 3 vertices uses 3 edges.
# The edges can be weighted or non weighted. Directional or Bi-directional. Trees are a form of graphs with limitations. LL is a form of a Tree hence LL is a form of a graph.
# We will implement graphs using adjacency list instead of adjacency matrix as it has much better Big O. Not always but most cases.
class Graph: # First we build the constructor to create the vertex.
    def __init__(self):
        self.adj_list = {} # We are create a empty dictonary as we know the vertex is storted in the dictonary as a key and it's value is a list consisting of it's edges.

    def add_vertex(self, vertex): # Now we are adding the vertex to the list that we created. We will pass in the value tht the vertex will have.
        if vertex not in self.adj_list.keys(): # We are making sure we dont have any duplicates.
            self.adj_list[vertex] = [] # Now we add it as a key, value in the dictonary. Now value is empty as we dont know it's edges yet.
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_edge(self, v1, v2): # Now we are adding edges between vertices. v1 and v2 are the 2 vertices we want to have a edge between.
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): # We can only add if both v1 and v2 exists. Hence we are checking if they are in the dictonary.
            self.adj_list[v1].append(v2) # We are adding v2 into the value of the key v1
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try: # If we try to remove a connection that is not present we get a valueerror. Hence, we use try except method.
                self.adj_list[v1].remove(v2) # We are removing v2 from the value of the key v1
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex): # To remove the vertex we need to remove the connections of that vertex first.
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]: # We are going thru the keys of the vertex we want to remove and then removing all it's connection.
                self.adj_list[other_vertex].remove(vertex) # Now we are removing the vertex as the keys of other vertex it has been connected to.
            del self.adj_list[vertex] # After removing the vertex as a connection key from other vertex we delete the vertex itself.
            return True
        return False
            


    
x = Graph()
x.add_vertex("A")
x.add_vertex('B')
x.add_vertex("C")

x.add_edge("A","B")
x.add_edge("B","C")
x.add_edge("C","A")

x.remove_vertex("C")

x.print_graph()





