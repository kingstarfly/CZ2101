"""
Suppose the input graphG = (V, E)is stored inanadjacency matrixand we use an arrayforthe priority queue. Implement the Dijkstra’salgorithmusing this settingand  analyze  its time complexity with  respect  to|V|and |E|both theoreticallyand empirically
"""


import math


class Graph_adj_matrix:

    # Initialize the matrix
    def __init__(self, size: int = None, arr: list = None):
        if size is None and arr is None:
            print("Either size or arr is required.")
            return
        self.matrix = []
        if arr:
            self.matrix = arr
            self.size = len(arr)
        else:
            for i in range(size):
                self.adjMatrix.append([0 for j in range(size)])
            self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.matrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0

    def print_matrix(self):
        print(self.matrix)

    def __len__(self):
        return self.size


class PriorityQueue_array:

    def __init__(self) -> None:
        self.queue = []

    def add(self, v, distance):
        self.queue.append((v, distance))

    def edit(self, v, new_distance):
        for index, (vertex, distance) in enumerate(self.queue):
            if vertex == v:
                self.queue[index] = (vertex, new_distance)

    def pop_min(self):
        smallest_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][1] < self.queue[smallest_index][1]:
                smallest_index = i
        return self.queue.pop(smallest_index)

    def is_empty(self):
        return len(self.queue) == 0


def dijkstra_shortest_path(g: Graph_adj_matrix, source: int):
    # source is assumed to be the index of the vertex (0 index)
    # Dijkstra's algorithm
    # Use priority queue to keep track of (vertex, dist from source). Purpose is to select the next closest vertex to source.
    pq = PriorityQueue_array()
    dist = []  # dist[i] tracks distance of i-th vertex from source vertex.
    prev = []  # parent[i] points to parent of i-th vertex in shortest path.
    visited = []  # visited[i] tells if i-th vertex has been visited.
    for v in range(g.size):
        dist.append(math.inf)
        prev.append(None)
        visited.append(False)

    dist[source] = 0

    for v in range(g.size):
        # Initially, source node will be the min in pq, and the rest will be behind since their distance is inf.
        pq.add(v, dist[v])  # v[source] is the distance v is from source

    while not pq.is_empty():

        (u, d) = pq.pop_min()
        visited[u] = True

        # For each adjacent vertex of u, check distance and update if needed
        for v, edge in enumerate(g.matrix[u]):
            if (edge != 0 and visited[v] == False and dist[v] > dist[u] + edge):
                new_dist = dist[u] + edge
                dist[v] = new_dist
                prev[v] = u
                pq.edit(v, new_dist)

    return dist, prev, visited


if __name__ == "__main__":

    matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [
        0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    g = Graph_adj_matrix(arr=matrix)
    g.print_matrix()
    dist, prev, visited = dijkstra_shortest_path(g, 0)
    print(dist)
    print(prev)
    print(visited)
