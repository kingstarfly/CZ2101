def heapsort(arr):
    # 1. Construct heap from array

    # 2. Iterate through each elt in arr and delete maximum node, and insert the node into last position of array.

    # 3. Done
    pass


def heapify(arr, size, i):
    # i is the current index of arr
    # if i is not a leaf, then heapify left tree and right tree.
    # Fixheap by pretending to insert itself back into the heap
    if 2*i < size-1:
        left_child_index = 2*i + 1
        right_child_index = 2*i + 2
        # todo the size of subtree is ambiguous?
        heapify(arr, size-2, left_child_index)
        heapify(arr, size-2, right_child_index)
        fixHeap(arr, size, i, arr[i])


def fixHeap(arr, size, i, k):
    # Current node is arr[i].
    # Size of heap is size.
    # Adds k to heap at the current node, and maintains heap property

    if i >= size:
        print("Index larger than size of heap")
        return

    # If H is a leaf, then insert k into root of H
    if 2*i >= size-1:
        arr[i] = k
    else:
        # Compare left child with right child
        left_child_index = 2*i + 1
        right_child_index = 2*i + 2
        bigger_child_index = None
        if arr[left_child_index] >= arr[right_child_index]:
            bigger_child_index = left_child_index
        else:
            bigger_child_index = right_child_index

        if k >= arr[bigger_child_index]:
            arr[i] = k
        else:
            arr[i] = arr[bigger_child_index]
            fixHeap(arr, size, bigger_child_index, k)


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5]
    heapify(arr, len(arr), 0)
    print(arr)

# Rules for 0-index implementation

# Entry i in array is a tree node if 0 <= i <= n - 1

# Parent: return ceiling of i/2 and minus 1

# Left Subtree: return 2i + 1

# Right Subtree: return 2i + 2

# arr[i] is a leaf only if 2i >= n-1


def deleteMax(arr, size):
    biggest = H[-1]


# Heap can be represented by arr and size of heap

# Node in a heap can be presented by Heap and index.
