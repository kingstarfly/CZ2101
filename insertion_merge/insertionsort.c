#include <stdio.h>
#include <stdlib.h>

int compare(int, int);
void insertionsort(int *, int, int);
void swap(int *, int, int);
void printlist(int *, int);

int main()
{
  int arr[] = {50, 10, 2, 70, 3, 5};
  // int arr[] = {9, 10, 11, 70, 3, 5};
  // int arr[] = {9, 8, 7, 6, 5, 4};
  // int arr[] = {4, 5, 6, 7, 8, 9};

  int length = 6;
  printlist(arr, length);
  insertionsort(arr, 0, length - 1);
  printlist(arr, length);

  return 0;
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
      while (counter > start)
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

void printlist(int *arr, int length)
{
  for (int i = 0; i < length; i++)
  {
    printf("%d ", arr[i]);
  }
  printf("\n");
}
