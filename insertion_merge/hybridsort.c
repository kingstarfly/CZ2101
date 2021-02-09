#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// #define THRESHOLD 20
#define N (int)1e5
#define MIN_NUM 0
#define MAX_NUM 999

void hybridsort(int *, int, int, int);
int compare(int, int);
void mergesort(int *, int, int);
void merge(int *, int, int);
void insertionsort(int *, int, int);
void swap(int *, int, int);
void printlist(int *, int);

int main()
{
  int best_threshold = -1;
  double best_cpu_time = 10000.00;

  clock_t start, end;
  double cpu_time_used;

  // int arr[] = {50, 10, 2, 70, 3, 5};
  // int arr[] = {9, 10, 11, 70, 3, 5};
  // int arr[] = {9, 8, 7, 6, 5, 4};
  // int arr[] = {4, 5, 6, 7, 8, 9};
  int original_arr[N];
  int variable_arr[N];
  srand(27);
  int range = MAX_NUM - MIN_NUM + 1;
  for (int i = 0; i < N; i++)
  {
    original_arr[i] = rand() % range + MIN_NUM; //assign random number to index in the array;
  }

  // printlist(arr, N);
  for (int threshold = 1; threshold < 50; threshold += 1)
  {
    // Reset the variable array
    for (int i = 0; i < N; i++)
    {
      variable_arr[i] = original_arr[i];
    }

    // Start the clock timer
    start = clock();
    hybridsort(variable_arr, 0, N - 1, threshold);
    end = clock();

    cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;
    if (cpu_time_used < best_cpu_time)
    {
      best_cpu_time = cpu_time_used;
      best_threshold = threshold;
    }
    // printlist(arr, N);
    printf("Threshold: %d, CPU time used: %.8f\n", threshold, cpu_time_used);
  }

  printf("Best threshold is %d with time of %.8f\n", best_threshold, best_cpu_time);

  return 0;
}

void printlist(int *arr, int length)
{
  for (int i = 0; i < length; i++)
  {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// start and end are indexes
void hybridsort(int *arr, int start, int end, int threshold)
{
  if (start >= end)
  {
    return;
  }

  // If below or equal to a certain threshold length, use Insertion Sort. Or else, use Merge Sort.
  int length = end - start + 1;
  if (length <= threshold)
  {
    insertionsort(arr, start, end);
    return; // do not proceed with mergesort code
  }

  if (start <= end - 2)
  {
    int mid = start + (end - start) / 2;
    // printf("mid is %d\n", mid);

    hybridsort(arr, start, mid, threshold);
    hybridsort(arr, mid + 1, end, threshold);
  }

  merge(arr, start, end);
}

void merge(int *arr, int start, int end)
{
  if (start >= end)
    return;

  // Merges arr from index n to index m
  int mid = start + (end - start) / 2;
  int a = start;
  int b = mid + 1;

  while (a <= mid && b <= end)
  {
    int cmp = compare(arr[a], arr[b]);

    // Case 1 : Right is greater than Left. Shift Right element to just before Left element.
    if (cmp > 0)
    {
      int tmp = arr[b]; // Save the value to be shifted
      for (int i = b; i > a; i--)
      {
        // Within the sorted portion, shift all values to the right. Leftmost value is unchanged.
        arr[i] = arr[i - 1];
      }
      arr[a] = tmp; // Save the tmp value into leftmost in sorted portion.

      // Increment all 3 pointers
      a++;
      b++;
      mid++;
    }
    else if (cmp < 0)
    {
      a++; // This value is in the right place. Just increment a by 1.
    }
    else
    {
      if (a == mid && b == end)
        break; // No movement needed if they are the last elements

      a++;              // Move a up by 1 because we want to insert the right side value only after this.
      int tmp = arr[b]; // Save the value to be shifted and move b forward by 1
      for (int i = b; i > a; i--)
      {
        // Within the sorted portion, shift all values to the right. Leftmost value is unchanged.
        arr[i] = arr[i - 1];
      }
      arr[a] = tmp;

      // Increment the 2 other pointers
      b++;
      mid++;
    }
  }
}

void insertionsort(int *arr, int start, int end)
{
  for (int i = start + 1; i <= end; i++)
  {
    // Check i-th element with left neighbour.

    // Case 1: i-th element is smaller than left neighbour
    if (arr[i] < arr[i - 1])
    {
      int counter = i;
      // Continuously swap the chosen element leftwards whenever possible. Stops when at correct position.
      while (counter > 0)
      {
        if (arr[counter] < arr[counter - 1])
        {
          swap(arr, counter, counter - 1);
        }
        else
        {
          break;
        }
        counter--;
      }
    }

    // Case 2: i-th element is greater than or equal to left neighobur
    // Nothing to be done
  }
}

void swap(int *arr, int i, int j)
{
  int tmp = arr[j];
  arr[j] = arr[i];
  arr[i] = tmp;
}

int compare(int val1, int val2)
{
  if (val1 > val2)
  {
    return 1;
  }
  else if (val1 == val2)
  {
    return 0;
  }
  else
  {
    return -1;
  }
}
