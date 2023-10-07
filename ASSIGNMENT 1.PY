def bubble_sort(arr):
    """
    Sorts the input array using Bubble Sort algorithm.

    Parameters:
    arr (list): The unsorted list of integers.

    Returns:
    list: The sorted list of integers.
    """
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

unsorted_array = [5, 2, 9, 1, 5, 6]
print("Unsorted Array:", unsorted_array)
bubble_sort(unsorted_array)
print("Sorted Array:", unsorted_array)

"""
Time Complexity Analysis:

Bubble Sort has a time complexity of O(n^2) in the worst and average cases, where n is the number of elements in the array. 
This is due to the nested loops iterating through the array.

Stability:

Bubble Sort is a stable sorting algorithm, meaning it preserves the relative order of equal elements.
Performance on Different Input Data:

Bubble Sort performs well on small datasets or nearly sorted data. However, it is highly inefficient for large datasets due to 
its quadratic time complexity.
"""

# QUICK SORT

def quick_sort(arr):
    """
    Sorts the input array using Quick Sort algorithm.

    Parameters:
    arr (list): The unsorted list of integers.

    Returns:
    list: The sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

unsorted_array = [5, 2, 9, 1, 5, 6]
print("Unsorted Array:", unsorted_array)
sorted_array_quick = quick_sort(unsorted_array)
print("Sorted Array using Quick Sort:", sorted_array_quick)

"""
Time Complexity Analysis:

Quick Sort has an average and best-case time complexity of O(n log n), making it significantly faster than Bubble Sort for most 
inputs. However, in the worst case, it can degrade to O(n^2) time complexity.
"""

"""
Differences and Scenarios:


Quick Sort is generally faster than Bubble Sort for a large number of elements due to its average time complexity being 
O(n log n), which is more efficient than Bubble Sort's O(n^2) complexity.

Bubble Sort is easy to implement and understand but is inefficient for large datasets.

Quick Sort is preferred for large datasets and is widely used in practice due to its average-case efficiency, making it 
suitable for general-purpose sorting.

Bubble Sort might be preferred only for educational purposes or when dealing with very small datasets where its 
simplicity might outweigh its inefficiency.
"""
