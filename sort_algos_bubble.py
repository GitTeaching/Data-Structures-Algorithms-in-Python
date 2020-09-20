# -*- coding: utf-8 -*-
"""
The bubble sorting algorithm iterates over a list, comparing elements in pairs and 
swapping them until the larger elements "bubble up" to the end of the list, 
and the smaller elements stay at the "bottom".

We begin by comparing the first two elements of the list. 
If the first element is larger than the second element, we swap them. 
If they are already in order we leave them as is. 
We then move to the next pair of elements, compare their values and swap as necessary. 
This process continues to the last pair of items in the list.

Bubble Sort's time complexity is O(n^2).

Bubble Sort is the slowest the worst performer of all the algorithms. 
While it useful as an introduction to sorting and algorithms, it's not fit for practical use.
"""

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def bubble_sort_optimized(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
                
                
# Bubble sort algorithm testing
lst = [64, 34, 25, 12, 22, 11, 90, 0]
bubble_sort(lst)
print(lst)

lst = [64, 34, 25, 12, 22, 11, 90, 0]
bubble_sort_optimized(lst)
print(lst)