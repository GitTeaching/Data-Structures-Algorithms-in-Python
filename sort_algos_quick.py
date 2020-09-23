# -*- coding: utf-8 -*-
"""
QuickSort is a Divide and Conquer algorithm. 
It picks an element as pivot and partitions the given array around the picked pivot. 
There are many different versions of quickSort that pick pivot in different ways : first
element, last element, middle element, etc.

All elements smaller than the pivot are moved to its left. All larger elements are moved 
to its right. Knowing that the pivot is in it's rightful place, we recursively sort the 
values around the pivot until the entire list is sorted.

Quick Sort is very fast (less fast than Tim Sort), nearly twice as fast as Merge Sort and it wouldn't 
need as much space to run.

Worst case time complexity of O(n^2).

With a good pivot, the Quick Sort function would partition the array into halves which 
grows logarithmically with n. Therefore the average time complexity of the Quick Sort 
algorithm is O(nlog(n)).

The space complexity for quicksort is O(log n).
"""

def partition(lst, low, high):
    pivot = lst[high] # pivot as last element of the list
    i = low - 1
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    
    return i+1
        

def quick_sort(lst):
    def _quick_sort(items, low, high):
        if low < high:
            partition_index = partition(items, low, high)
            _quick_sort(items, low, partition_index-1)
            _quick_sort(items, partition_index+1, high)
    _quick_sort(lst, 0, len(lst)-1)
            

# Quick sort algorithm testing
lst = [64, 34, 25, 12, 22, 11, 90, 0]
quick_sort(lst)
print(lst)