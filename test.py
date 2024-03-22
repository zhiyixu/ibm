import numpy as np


def quick_sort(arr):
    """
    Sorts an array using the quicksort algorithm.

    This function sorts the given array by dividing it into two
    subarrays, one with elements less than the pivot and one with
    elements greater than the pivot. It then recursively sorts the
    subarrays and concatenates them with the pivot in the middle to
    produce the final sorted array.

    Parameters:
    - arr (list): The array to be sorted.

    Returns:
    - list: The sorted array.
    """
    if len(arr) <= 1:
        # Base case: array with 0 or 1 element is already sorted.
        return arr
    pivot = arr[len(arr) // 2]
    # Partition the array into subarrays based on the pivot.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively sort the subarrays and concatenate them with the pivot.
    return quick_sort(left) + middle + quick_sort(right)


def bouble_sort(arr):
    """
    Sorts an array using the bouble sort algorithm.

    This function sorts the given array by comparing adjacent elements
    and swapping them if they are in the wrong order. It then repeats
    the process until the array is sorted.

    Parameters:
    - arr (list): The array to be sorted.

    Returns:
    - list: The sorted array.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
