def insertionsort(arr: list, start: int, end: int):
    for i in range(start+1, end+1):
        for j in range(i, start, -1):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)
            else:
                break


def swap(arr: list, i: int, j: int):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp
    return


if __name__ == "__main__":
    arr = [50, 10, 2, 70, 3, 5]
    print(arr)

    insertionsort(arr, 1, 3)
    print(arr)
