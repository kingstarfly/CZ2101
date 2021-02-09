#include <stdio.h>
#include <stdlib.h>

int compare(int, int);
void mergesort(int *, int, int);
void merge(int *, int, int);
void printlist(int *, int);

int main()
{
  int arr[] = {50, 10, 2, 70, 3, 5};
  // int arr[] = {9, 10, 11, 70, 3, 5};
  // int arr[] = {9, 8, 7, 6, 5, 4};
  // int arr[] = {4, 5, 6, 7, 8, 9};

  int length = 6;
  printlist(arr, length);
  mergesort(arr, 0, length - 1);
  printlist(arr, length);

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
void mergesort(int *arr, int start, int end)
{
  if (start >= end)
  {
    return;
  }

  if (start <= end - 2)
  {
    int mid = start + (end - start) / 2;
    printf("mid is %d\n", mid);
    mergesort(arr, start, mid);
    mergesort(arr, mid + 1, end);
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
