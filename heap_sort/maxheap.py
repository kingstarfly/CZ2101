class MinHeap:
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
        parent = self.get_parent
        while self.has_parent(i) and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            i = parent

    def insert_key(self, key):
        self.heap.append(key)
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

    def heapify_down(self, i):
        while self.has_left_child(i):
            # Get index of bigger child
            min_child_ind = None
            if self.has_left_child(i):
                left = self.get_left_child(i)
                if self.has_right_child(i):
                    right = self.get_right_child(i)
                    min_child_ind = left if self.heap[left] <= self.heap[right] else right
                else:
                    min_child_ind = left
            else:
                # No children
                break

            if self.heap[i] > self.heap[min_child_ind]:
                self.swap(i, min_child_ind)
                i = min_child_ind
            else:
                # Reach correct position
                break

    def array_to_heap(self, arr):
        self.heap = arr
        self.fix_tree(0)

    def fix_tree(self, i):
        if self.has_left_child(i):
            self.fix_tree(self.get_left_child(i))
        if self.has_right_child(i):
            self.fix_tree(self.get_right_child(i))
        self.heapify_down(i)


class MaxHeap:
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
        parent = self.get_parent
        while self.has_parent(i) and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            i = parent

    def insert_key(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)

    def print_heap(self):
        print(self.heap)

    def pop_max(self):
        if len(self.heap) == 0:
            return -1

        self.swap(0, len(self.heap)-1)
        return_val = self.heap.pop()

        # Fix the heap
        self.heapify_down(0)
        return return_val

    def heapify_down(self, i):
        while self.has_left_child(i):
            # Get index of bigger child
            max_child_ind = None
            if self.has_left_child(i):
                left = self.get_left_child(i)
                if self.has_right_child(i):
                    right = self.get_right_child(i)
                    max_child_ind = left if self.heap[left] >= self.heap[right] else right
                else:
                    max_child_ind = left
            else:
                # No children
                break

            if self.heap[i] < self.heap[max_child_ind]:
                self.swap(i, max_child_ind)
                i = max_child_ind
            else:
                # Reach correct position
                break

    def array_to_heap(self, arr):
        self.heap = arr
        self.fix_tree(0)

    def fix_tree(self, i):
        if self.has_left_child(i):
            self.fix_tree(self.get_left_child(i))
        if self.has_right_child(i):
            self.fix_tree(self.get_right_child(i))
        self.heapify_down(i)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    maxh = MaxHeap()
    maxh.array_to_heap(arr)
    maxh.print_heap()

    minh = MinHeap()
    minh.array_to_heap(arr)
    minh.print_heap()
