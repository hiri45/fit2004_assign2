from heapq import *
class AdjacentList:
    """
    The adjacent list class is used to create an adjacent list to represent the graph of vertices(nodes) connected
    to each other.
    :input:
        value: the value is the vertex(node) in which the adjacent list takes before moving/connecting to the next vertex(node)
    """
    def __init__(self,value, weigth):
        self.vertex = (value, weigth)
        self.next = None
class Graph:
    def __init__(self,num, cafe):
        self.vert = num
        self.graph = [None] * self.vert
        self.cafe = cafe
        self.cafe_list = []
        for i in range(len(self.cafe)):
            self.cafe_list.append(self.cafe[i][0])
    def add_edge(self, head, end_vertex, weight):
        node = AdjacentList(end_vertex, weight)
        node.next = self.graph[head]
        self.graph[head] = node
    def print_graph(self):
        for i in range(self.vert):
            if i not in self.cafe_list:
                print("Adjacency list representation of {}\n head".format(i), end = "")
            else:
                print("Adjacency list representation of \x1B[4m{}\x1B[0m\n head".format(i), end = "")
            temp = self.graph[i]
            while temp:
                print(" - > {}".format(temp.vertex), end = "")
                temp = temp.next
            print("\n")

class RoadGraph:
    """ this class does this"""
    def __init__(self, roads, cafes):
        """ this function does this"""
        # ToDo: Initialize the graph data structure here
        self.roads = roads
        self.cafes = cafes
        max_location_list = []
        for i in range(len(self.roads)):
            max_location_list.append(self.roads[i][0])
            max_location_list.append(self.roads[i][1])
        max_location = max(max_location_list) + 1
        self.create_graph = Graph(max_location, cafes)
        for i in range(len(self.roads)):
            self.create_graph.add_edge(self.roads[i][0], self.roads[i][1],self.roads[i][2])
    def routing(self, start, end):
        """ this function does this"""
        # ToDo: Performs the operation needed to find the optimal route.
def relax(start_vert,end_vert):
    print('wpw')
def dijkstra(graph, start, end):
    print('wpw')
# The roads represented as a list of tuples
roads = [(0, 1, 4), (0, 3, 2), (0, 2, 3), (2, 3, 2), (3, 0, 3)]
# The cafes represented as a list of tuple
cafes = [(0, 5), (3, 2), (1, 3)]
          
myGraph = RoadGraph(roads, cafes)
myGraph.create_graph.print_graph()
""" if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_graph() """