def quicksort(arr, l=None, r=None):
    # Sorts arr in place
    if l is None or r is None:
        l = 0
        r = len(arr) - 1
    if (l >= r): return
    pivot_pos = partition(arr, l, r)

    # run quicksort on left array (smaller than pivot)
    quicksort(arr, l, pivot_pos-1)
    
    # run quicksort on right array (larger than pivot)
    quicksort(arr, pivot_pos+1, r)
    

    
def partition(arr, l, r) -> int:
    # pivot_ind = (l+r)//2  # Choose midpoint as pivot
    mid = (l+r)//2
    pivot_ind = median_of_three(arr, l, mid, r) # choose median of three
    print(f"{arr[pivot_ind]} was pivot")
    pivot = arr[pivot_ind] 

    swap(arr, pivot_ind, l)  # Swap pivot with left element

    last_small = l
    
    for ind in range(l+1, r+1):
        # Case 1: elt is larger than pivot
        # Do nothing
        
        # Case 2: elt is smaller than pivot
        if (arr[ind] < pivot):
            last_small += 1 # move last_small pointer by 1
            swap(arr, ind, last_small)
    
    # Once done with for loop, sub array should be arranged in {pivot}{smaller than pivot}{larger than pivot}
    # Place pivot back in correct spot
    swap(arr, l, last_small)
    print(arr)
    return last_small


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def median_of_three(L, low, mid, high):
    a = L[low]
    b = L[mid]
    c = L[high]
    if a <= b <= c:
        return mid
    if c <= b <= a:
        return mid
    if a <= c <= b:
        return high
    if b <= c <= a:
        return high
    return low


        


if __name__ == "__main__":
    # arr = [5, 2, 3, 12, 1]
    arr = [10,20,30,40,50,60,70,80,0]
    print(arr)
    quicksort(arr)
    print(arr)


# 5, 4, 3, 2, 1
# 3, 4, 5, 2, 1
# 3, 4, 5, 2, 1
# 2, 3, 4, 5, 1
