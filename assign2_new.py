import heapq
# The roads represented as a list of tuple
roads = [(0, 1, 4), (1, 2, 2), (2, 3, 3), (3, 4, 1), (1, 5, 2),
(5, 6, 5), (6, 3, 2), (6, 4, 3), (1, 7, 4), (7, 8, 2),
(8, 7, 2), (7, 3, 2), (8, 0, 11), (4, 3, 1), (4, 8, 10)]
# The cafes represented as a list of tuple
cafes = [(5, 10), (6, 1), (7, 5), (0, 3), (8, 4)]

def relax(u, v, w, dist, pred):
    """function:"""
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        pred[v] = u
    return dist, pred

def dijkstra_impr(graph,start,fin):
    """function:"""
    dist = [9999999] * len(graph)
    pred = [0] * len(graph)
    track_path = []
    dist[start] = 0
    Q = []
    key = 0
    heapq.heappush(Q,(start,key))
    heapq.heapify(Q)    
    while Q != []:
        [u, key] = heapq.heappop(Q)
        if dist[u] == key:
            for i in range(len(graph[u])):
                if dist[graph[u][i][0]] > dist[u] + graph[u][i][1]:
                    dist[graph[u][i][0]] = dist[u] + graph[u][i][1]
                    pred[graph[u][i][0]] = u
                    key = dist[graph[u][i][0]]
                    heapq.heappush(Q,(graph[u][i][0],key))
    currentNode = fin
    while currentNode != start:
        try:
            track_path.insert(0,currentNode)
            currentNode = pred[currentNode]
        except KeyError:
            print("path not reachable")
    track_path.insert(0,start)
    return track_path, dist[fin]  

def index_for_min(list):
    """function:"""
    #get the minimum value in the list
    min_value = min(list)
    #return the index of minimum value 
    for i in range(len(list)):
        if min_value == list[i]:
            return i

class RoadGraph:
    """ this class does this"""
    def __init__(self, roads, cafes):
        """ this function does this"""
        # ToDo: Initialize the graph data structure here
        self.roads = roads
        self.cafes = cafes
        self.max_location_list = []
        for i in range(len(self.roads)):
            self.max_location_list.append(self.roads[i][0])
        for i in range(len(self.roads)):
            self.max_location_list.append(self.roads[i][1])
        max_location = max(self.max_location_list) + 1
        self.list_graph = [[] for i in range(max_location)]
        for i in range(len(self.roads)):
                self.list_graph[self.roads[i][0]].append((self.roads[i][1],self.roads[i][2]))
        print(self.list_graph)

    def routing(self, start, end):
        """function:"""
        # ToDo: Performs the operation needed to find the optimal route
        self.start = start
        self.end = end
        self.total_times = []
        self.all_paths = []
        for i in range(len(self.cafes)):
            self.total_times.append(dijkstra_impr(self.list_graph, self.start, self.cafes[i][0])[1] + dijkstra_impr(self.list_graph, self.cafes[i][0] , self.end)[1] + self.cafes[i][1])
        for i in range(len(self.cafes)):
            self.all_paths.append(dijkstra_impr(self.list_graph, self.start, self.cafes[i][0])[0] + dijkstra_impr(self.list_graph, self.cafes[i][0], self.end)[0][1:])
        best_time_index = index_for_min(self.total_times)
        print(self.all_paths[best_time_index])


mygraph = RoadGraph(roads, cafes)
#print(dijkstra_impr(mygraph.list_graph,6,7))
mygraph.routing(3,4)
#print(dijkstra(mygraph.list_graph,5,8))

