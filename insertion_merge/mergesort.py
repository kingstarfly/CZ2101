def mergesort(arr: list, start: int, end: int):
  # Sorts in place

    if start >= end:
        return

    if end >= start + 2:
        mid = (start+end) // 2
        # print(f"mid is {mid}")
        mergesort(arr, start, mid)
        mergesort(arr, mid+1, end)

    merge(arr, start, end)


def merge(arr: list, start: int, end: int):
    if start >= end:
        return

    mid = start + (end-start) // 2
    start2 = mid + 1

    while start <= mid and start2 <= end:

        # Case 1: if first element is smaller than or equal to right element, i.e correct place
        if arr[start] <= arr[start2]:
            start += 1

        # Case 2: if first element is larger than right element, then shift the right element to before the left element
        else:
            # Right shift all elements from "start" up till element before "start2"
            value = arr[start2]
            for index in range(start2, start, -1):
                arr[index] = arr[index-1]
            # Copy over original start2 value into original start index
            arr[start] = value

            # Update all pointers for next iteration of while loop
            start += 1
            mid += 1
            start2 += 1


if __name__ == "__main__":
    arr = [50, 10, 2, 70, 3, 5]
    print(arr)

    mergesort(arr, 0, len(arr)-1)
    print(arr)

    # mergesort(arr)
    # print(arr)


# 5, 4, 3, 2, 1
# 3, 4, 5, 2, 1
# 3, 4, 5, 2, 1
# 2, 3, 4, 5, 1
