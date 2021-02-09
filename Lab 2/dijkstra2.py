"""
Suppose the input graph G = (V, E) is stored in an array of adjacency lists and
we use a minimizing heap for the priority queue. Implement the Dijkstra’s
algorithm using this setting and analyze its time complexity with respect to |V|
and |E| both theoretically and empirically. 
"""


import math
from collections import defaultdict


class Graph_adj_lists:

    # Initialize the lists
    def __init__(self, arr: list = None):
        # Create a default dict with each element being a dict which will hold weights
        self.lists = defaultdict(dict)
        if arr:
            for u, weights in enumerate(arr):
                for v, weight in enumerate(weights):
                    if weight != 0:
                        self.lists[u][v] = weight

    # Add edges

    def add_edge(self, v1, v2, weight):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.lists[v1][v2] = weight

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.lists[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.lists[v1][v2] = 0

    def print_lists(self):
        print(self.lists)

    def __len__(self):
        return len(self.lists)


class PriorityQueue_MinHeap:

    def __init__(self) -> None:
        self.heap = []

    def get_parent(self, i):
        return (i-1)//2

    def get_left_child(self, i):
        return i*2 + 1

    def get_right_child(self, i):
        return i*2 + 2

    def has_parent(self, i):
        return self.get_parent(i) >= 0

    def has_left_child(self, i):
        return self.get_left_child(i) < len(self.heap)

    def has_right_child(self, i):
        return self.get_right_child(i) < len(self.heap)

    def is_leaf(self, i):
        return 2 * i >= len(self.heap) - 1 and i < len(self.heap)

    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def heapify_up(self, i):
        parent = self.get_parent(i)
        while self.has_parent(i) and self.heap[i][1] < self.heap[parent][1]:
            self.swap(i, parent)
            i = parent

    def heapify_down(self, i):
        while self.has_left_child(i):
            # Get index of bigger child
            min_child_ind = None
            if self.has_left_child(i):
                left = self.get_left_child(i)
                if self.has_right_child(i):
                    right = self.get_right_child(i)
                    min_child_ind = left if self.heap[left][1] <= self.heap[right][1] else right
                else:
                    min_child_ind = left
            else:
                # No children
                break

            if self.heap[i][1] > self.heap[min_child_ind][1]:
                self.swap(i, min_child_ind)
                i = min_child_ind
            else:
                # Reach correct position
                break

    def add(self, v, distance):
        self.heap.append((v, distance))
        self.heapify_up(len(self.heap)-1)

    def print_heap(self):
        print(self.heap)

    def pop_min(self):
        if len(self.heap) == 0:
            return -1

        self.swap(0, len(self.heap)-1)
        return_val = self.heap.pop()

        # Fix the heap
        self.heapify_down(0)
        return return_val

    def array_to_heap(self, arr):
        for elt in arr:
            self.heap.append(elt)
        self.fix_tree(0)

    def fix_tree(self, i):
        if self.has_left_child(i):
            self.fix_tree(self.get_left_child(i))
        if self.has_right_child(i):
            self.fix_tree(self.get_right_child(i))
        self.heapify_down(i)

    def edit(self, v, new_distance):
        # Find the vertex, delete it and add a new vertex
        for index, (vertex, distance) in enumerate(self.heap):
            if vertex == v:
                old_distance = self.heap[index][1]
                self.heap[index] = (vertex, new_distance)
                if new_distance > old_distance:
                    self.heapify_down(index)
                else:
                    self.heapify_up(index)

    def pop_min(self):
        smallest_index = 0
        for i in range(1, len(self.heap)):
            if self.heap[i][1] < self.heap[smallest_index][1]:
                smallest_index = i
        return self.heap.pop(smallest_index)

    def is_empty(self):
        return len(self.heap) == 0


def dijkstra_shortest_path(g: Graph_adj_lists, source: int):
    # source is assumed to be the index of the vertex (0 index)
    # Dijkstra's algorithm
    # Use priority queue to keep track of (vertex, dist from source). Purpose is to select the next closest vertex to source.
    pq = PriorityQueue_MinHeap()
    dist = []  # dist[i] tracks distance of i-th vertex from source vertex.
    prev = []  # parent[i] points to parent of i-th vertex in shortest path.
    visited = []  # visited[i] tells if i-th vertex has been visited.
    for v in range(len(g)):
        dist.append(math.inf)
        prev.append(None)
        visited.append(False)

    dist[source] = 0

    for v in range(len(g)):
        # Initially, source node will be the min in pq, and the rest will be behind since their distance is inf.
        pq.add(v, dist[v])  # v[source] is the distance v is from source

    while not pq.is_empty():

        (u, d) = pq.pop_min()
        visited[u] = True

        # For each adjacent vertex of u, check distance and update if needed
        for v, edge in g.lists[u].items():
            if (visited[v] == False and dist[v] > dist[u] + edge):
                new_dist = dist[u] + edge
                dist[v] = new_dist
                prev[v] = u
                pq.edit(v, new_dist)

    return dist, prev, visited


if __name__ == "__main__":

    matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [
        0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    g = Graph_adj_lists(arr=matrix)
    g.print_lists()
    dist, prev, visited = dijkstra_shortest_path(g, 0)
    print(dist)
    print(prev)
    print(visited)

    # Test minheap
    # heap = PriorityQueue_MinHeap()
    # heap.array_to_heap([(1, 5), (2, 4), (3, 22), (4, 10)])
    # heap.print_heap()
