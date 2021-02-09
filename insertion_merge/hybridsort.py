import time
import numpy as np
import math


def hybrid_mergesort(arr: list, start: int, end: int, thresh: int):
  # Sorts in place

    if start >= end:
        return

    if end-start+1 <= thresh:
        insertionsort(arr, start, end)
        return

    if end >= start + 2:
        mid = (start+end) // 2
        # print(f"mid is {mid}")
        hybrid_mergesort(arr, start, mid, thresh)
        hybrid_mergesort(arr, mid+1, end, thresh)

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


def time_hybridsort(arr: list, thresh: int):

    # start = time.process_time_ns()
    start = time.perf_counter_ns()
    hybrid_mergesort(arr, 0, len(arr)-1, thresh)
    # end = time.process_time_ns()
    end = time.perf_counter_ns()
    return end - start


def run_average_case():
    np.random.seed(27)

    for pow in range(2, 6):
        MIN_NUM = 0
        MAX_NUM = 999
        N = 10**pow
        ITERS = 1
        MAX_THRESH = 20

        matrix = np.zeros(MAX_THRESH)

        for i in range(ITERS):
            ori_arr = np.random.randint(low=MIN_NUM, high=MAX_NUM, size=N)
            for thresh in range(1, MAX_THRESH+1):
                arr = ori_arr.copy().tolist()
                # print(arr, end="")
                matrix[thresh-1] = time_hybridsort(arr, thresh)
                # print(f" --> {arr}")

        # Calculate average execution time across iterations for each threshold
        threshold_timings = np.mean(matrix, axis=0)

        # Save timings
        np.save(f"./timings/avr_pow{pow}.npy", threshold_timings)

        # print(threshold_timings)
        low = np.argmin(threshold_timings)
        print(f"N = {N}")
        print(
            f"Size=10^{pow}. Fastest at thresh={low+1} with speed {threshold_timings[low] / 1e9} seconds")


def run_best_case():
    for pow in range(2, 5):
        N = 10**pow
        ITERS = 3
        MAX_THRESH = 20

        matrix = np.zeros([ITERS, MAX_THRESH])

        for i in range(ITERS):
            ori_arr = [x for x in range(N)]
            for thresh in range(1, MAX_THRESH+1):
                arr = ori_arr[:]  # make a copy
                # print(arr, end="")
                matrix[i][thresh-1] = time_hybridsort(arr, thresh)
                # print(f" --> {arr}")

        # Calculate average execution time for each threshold
        threshold_timings = np.mean(matrix, axis=0)

        # Save timings
        np.save(f"./timings/best_pow{pow}.npy", threshold_timings)

        print(threshold_timings)
        low = np.argmin(threshold_timings)
        print(
            f"Size=10^{pow}. Fastest at thresh={low+1} with speed {threshold_timings[low] / 1e9} seconds")


def run_worst_case():
    for pow in range(2, 5):
        N = 10**pow
        ITERS = 3
        MAX_THRESH = 20

        matrix = np.zeros([ITERS, MAX_THRESH])

        for i in range(ITERS):
            ori_arr = worstCaseArrayOfSize(N)
            for thresh in range(1, MAX_THRESH+1):
                arr = ori_arr[:]  # make a copy
                # print(arr, end="")
                matrix[i][thresh-1] = time_hybridsort(arr, thresh)
                # print(f" --> {arr}")

        # Calculate average execution time for each threshold
        if ITERS > 1:
            threshold_timings = np.mean(matrix, axis=0)
        else:
            threshold_timings = matrix

        # Save timings
        np.save(f"./timings/worst_pow{pow}.npy", threshold_timings)

        print(threshold_timings)
        low = np.argmin(threshold_timings)
        print(
            f"Size=10^{pow}. Fastest at thresh={low+1} with speed {threshold_timings[low] / 1e9} seconds")


def worstCaseArrayOfSize(n):
    if n == 1:
        return [1]
    else:
        top = worstCaseArrayOfSize(int(math.floor(float(n) / 2)))
        bottom = worstCaseArrayOfSize(int(math.ceil(float(n) / 2)))
        return list(map(lambda x: x * 2, top)) + list(map(lambda x: x * 2 - 1, bottom))


if __name__ == "__main__":
    run_average_case()
